#!/usr/bin/env python3
"""
Product-Analysis AI 分析索引与 YAML 一致性自动校验脚本 (P24)

检查:
  1. AI 分析文章 YAML front matter 可解析
  2. YAML 不存在重复 key
  3. source_urls 是纯 URL 字符串
  4. analyses/index.yml 与每篇文章 YAML 一致
  5. README.md / analyses/README.md / analyses/index.yml 计数一致
  6. README.md / analyses/README.md 产品行状态一致

运行:
  cd <repo-root>
  python3 scripts/verify_ai_analysis_index.py

退出码:
  0 = PASS
  1 = FAIL
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


# ---------- 文件路径 ----------
REPO_ROOT = Path(__file__).resolve().parent.parent
ANALYSES_DIR = REPO_ROOT / "analyses" / "ai-assisted"
INDEX_YML = REPO_ROOT / "analyses" / "index.yml"
ANALYSES_README = REPO_ROOT / "analyses" / "README.md"
README_MD = REPO_ROOT / "README.md"

# ---------- 字段配置 ----------
REQUIRED_FM_FIELDS = [
    "product", "category", "tags", "source_urls", "analysis_type",
    "created_at", "review_status", "source_url_verified_at",
    "source_url_verification_status", "source_quality_notes", "one_line_insight",
]

REQUIRED_INDEX_ENTRY_FIELDS = [
    "product", "file", "category", "analysis_type", "created_at",
    "review_status", "source_url_verification_status", "tags",
    "one_line_insight", "quality_notes",
]

REQUIRED_INDEX_TOP_KEYS = ["version", "analyses", "summary", "by_category", "reading_paths"]

CONSISTENCY_FIELDS = [
    "product", "category", "analysis_type", "review_status",
    "source_url_verification_status", "one_line_insight",
]

ALLOWED_REVIEW_STATUS = {"draft", "reviewed"}
ALLOWED_VERIFICATION_STATUS = {"partial", "verified"}
ALLOWED_ANALYSIS_TYPE = {"ai-assisted"}


# ---------- 自定义 YAML Loader (检测重复 key) ----------
class DuplicateKeyError(Exception):
    pass


def _construct_mapping(loader: yaml.Loader, node: yaml.MappingNode, deep: bool = False) -> dict:
    """覆盖 construct_mapping,遇到重复 key 直接抛错。"""
    if not isinstance(node, yaml.MappingNode):
        raise yaml.constructor.ConstructorError(
            None, None, f"expected a mapping node, but found {node.id}", node.start_mark,
        )
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise DuplicateKeyError(f"duplicate key: {key!r}")
        value = loader.construct_object(value_node, deep=deep)
        mapping[key] = value
    return mapping


def _make_strict_loader() -> type[yaml.SafeLoader]:
    """返回注入了 duplicate-key 严格检测的 SafeLoader。"""
    loader_cls = type("StrictSafeLoader", (yaml.SafeLoader,), {})
    loader_cls.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping,
    )
    return loader_cls


# ---------- 工具函数 ----------
def list_analysis_files() -> list[Path]:
    if not ANALYSES_DIR.exists():
        return []
    pat = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
    return sorted(p for p in ANALYSES_DIR.glob("*.md") if p.is_file() and pat.match(p.name))


def extract_front_matter(text: str) -> str | None:
    stripped = text.lstrip()
    if not stripped.startswith("---"):
        return None
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def detect_inline_annotations(url: str) -> list[str]:
    """检测 source_urls 是否包含 inline annotation (verified / partial / primary / secondary / note / type: / status:)。"""
    bad_tokens = [
        r"\|\s*verified", r"\|\s*partial", r"\|\s*primary", r"\|\s*secondary",
        r"\|\s*note", r"\|\s*type", r"\|\s*status",
        r"\(\s*verified", r"\(\s*partial",
        r"\bverified\s*$", r"\bpartial\s*$",
        r"type:", r"status:", r"note:",
        r"\s{2,}verified", r"\s{2,}partial",
    ]
    issues: list[str] = []
    for pat in bad_tokens:
        if re.search(pat, url, re.IGNORECASE):
            issues.append(pat)
    return issues


def check_source_urls(urls: Any) -> list[str]:
    if not isinstance(urls, list):
        return ["source_urls 不是 list"]
    issues: list[str] = []
    for i, u in enumerate(urls):
        if not isinstance(u, str):
            issues.append(f"[{i}] 不是 string")
            continue
        if not u.startswith(("http://", "https://")):
            issues.append(f"[{i}] 不以 http(s):// 开头: {u[:80]}")
        # inline annotation
        for pat in detect_inline_annotations(u):
            issues.append(f"[{i}] 包含 inline annotation (pattern: {pat}): {u[:80]}")
        # markdown 表格分隔符
        if "|" in u:
            issues.append(f"[{i}] 包含 markdown 分隔符 '|': {u[:80]}")
    return issues


def extract_section(text: str, heading: str) -> str:
    pattern = rf"^##\s*(?:\d+\.\s+)?{re.escape(heading)}\s*$"
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start = i
            break
    if start is None:
        return ""
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            return "\n".join(lines[start:j])
    return "\n".join(lines[start:])


def parse_quality_status_numbers(section: str) -> dict[str, int]:
    mapping: dict[str, int] = {}
    for m in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|", section, re.MULTILINE):
        label = m.group(1).strip().lstrip("- ").strip()
        try:
            mapping[label] = int(m.group(2))
        except ValueError:
            pass
    return mapping


# ---------- 主校验逻辑 ----------
class Validator:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.articles: list[Path] = []
        self.entries: list[dict] = []
        self.total = 0
        self.reviewed = 0
        self.draft = 0
        self.partial = 0
        self.verified = 0

    def add(self, msg: str) -> None:
        self.errors.append(msg)

    @property
    def passed(self) -> bool:
        return not self.errors

    def print_result(self) -> None:
        if self.passed:
            print("PASS: AI analysis index consistency verified")
            print(f"- analyses found: {self.total}")
            print(f"- reviewed: {self.reviewed}")
            print(f"- draft: {self.draft}")
            print(f"- partial: {self.partial}")
            print(f"- verified: {self.verified}")
        else:
            print("FAIL: AI analysis index consistency errors")
            for i, err in enumerate(self.errors, 1):
                print(f"{i}. {err}")
            print()
            print(f"- analyses found: {self.total}")
            print(f"- reviewed: {self.reviewed}")
            print(f"- draft: {self.draft}")
            print(f"- partial: {self.partial}")
            print(f"- verified: {self.verified}")


def run_validation(v: Validator) -> None:
    if not HAS_YAML:
        v.add("PyYAML 未安装 — 请 pip install pyyaml")
        return

    # --- 1. 逐篇 article 检查 ---
    v.articles = list_analysis_files()
    if not v.articles:
        v.add(f"{ANALYSES_DIR} 下没有 YYYY-MM-DD-*.md 文件")
        return

    parsed_articles: dict[str, dict[str, Any]] = {}
    strict_loader = _make_strict_loader()

    for path in v.articles:
        fname = path.name
        content = path.read_text(encoding="utf-8")
        fm_text = extract_front_matter(content)
        if fm_text is None:
            v.add(f"{fname} 无 --- 包裹的 YAML front matter")
            continue

        # strict parse (检测重复 key)
        try:
            fm = yaml.load(fm_text, Loader=strict_loader)  # noqa: S506 - intentional strict loader
        except DuplicateKeyError as e:
            v.add(f"{fname} duplicate YAML key: {e}")
            continue
        except yaml.YAMLError as e:
            v.add(f"{fname} yaml.safe_load 失败: {e}")
            continue
        if not isinstance(fm, dict):
            v.add(f"{fname} front matter 不是 mapping")
            continue
        parsed_articles[fname] = fm

        # 必备字段
        missing = [f for f in REQUIRED_FM_FIELDS if f not in fm]
        if missing:
            v.add(f"{fname} 缺失字段: {', '.join(missing)}")

        # review_status
        rs = fm.get("review_status")
        if rs not in ALLOWED_REVIEW_STATUS:
            v.add(f"{fname} review_status 非法: {rs!r} (允许: {sorted(ALLOWED_REVIEW_STATUS)})")
        elif rs == "reviewed":
            if not fm.get("reviewed_at"):
                v.add(f"{fname} review_status=reviewed 但 reviewed_at 为空")
            if not fm.get("review_notes"):
                v.add(f"{fname} review_status=reviewed 但 review_notes 为空")

        # source_url_verification_status
        sv = fm.get("source_url_verification_status")
        if sv not in ALLOWED_VERIFICATION_STATUS:
            v.add(f"{fname} source_url_verification_status 非法: {sv!r}")

        # analysis_type
        at = fm.get("analysis_type")
        if at not in ALLOWED_ANALYSIS_TYPE:
            v.add(f"{fname} analysis_type 非法: {at!r} (允许: {sorted(ALLOWED_ANALYSIS_TYPE)})")

        # source_urls 格式
        url_issues = check_source_urls(fm.get("source_urls"))
        if url_issues:
            v.add(f"{fname} source_urls 格式问题: {'; '.join(url_issues)}")

    # --- 2. 计数 (从 article YAML 实际计算) ---
    # total 计数所有 .md 文件(即使 YAML parse 失败),因为它们都在 index.yml 中
    v.total = len(v.articles)
    v.reviewed = sum(1 for fm in parsed_articles.values() if fm.get("review_status") == "reviewed")
    v.draft = sum(1 for fm in parsed_articles.values() if fm.get("review_status") == "draft")
    v.partial = sum(
        1 for fm in parsed_articles.values()
        if fm.get("source_url_verification_status") == "partial"
    )
    v.verified = sum(
        1 for fm in parsed_articles.values()
        if fm.get("source_url_verification_status") == "verified"
    )

    # --- 3. index.yml 检查 ---
    if not INDEX_YML.exists():
        v.add(f"{INDEX_YML} 不存在")
        return
    try:
        idx = yaml.safe_load(INDEX_YML.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        v.add(f"analyses/index.yml 解析失败: {e}")
        return

    for key in REQUIRED_INDEX_TOP_KEYS:
        if key not in idx:
            v.add(f"analyses/index.yml 缺失顶层 key: {key}")

    if "analyses" not in idx or not isinstance(idx.get("analyses"), list):
        v.add("analyses/index.yml analyses 不是 list")
        return

    v.entries = idx["analyses"]

    # entry 字段完整性
    for e in v.entries:
        product = e.get("product", "<unknown>")
        missing = [f for f in REQUIRED_INDEX_ENTRY_FIELDS if f not in e]
        if missing:
            v.add(f"index.yml entry {product} 缺失字段: {', '.join(missing)}")
        # quality_notes 子字段
        qn = e.get("quality_notes")
        if isinstance(qn, dict):
            for qk in ("product_mechanism", "high_risk_facts", "reason"):
                if qk not in qn:
                    v.add(f"index.yml {product}.quality_notes 缺失: {qk}")

    # summary 一致性
    summary = idx.get("summary", {})
    expected_summary = {
        "total": v.total,
        "reviewed": v.reviewed,
        "draft": v.draft,
        "partial": v.partial,
        "verified": v.verified,
    }
    for k, exp_v in expected_summary.items():
        actual_v = summary.get(k)
        if actual_v != exp_v:
            v.add(f"index.yml summary.{k} expected {exp_v}, got {actual_v}")

    # --- 4. article ↔ index 一致性 ---
    entries_by_file = {e.get("file"): e for e in v.entries}
    for fname, fm in parsed_articles.items():
        rel_path = f"analyses/ai-assisted/{fname}"
        entry = entries_by_file.get(rel_path)
        if entry is None:
            v.add(f"{fname} 在 index.yml 中找不到 file={rel_path}")
            continue
        for field in CONSISTENCY_FIELDS:
            v_art = fm.get(field)
            v_idx = entry.get(field)
            if v_art != v_idx:
                v.add(
                    f"{fname} field '{field}': article={v_art!r} != index={v_idx!r}",
                )
        # tags
        art_tags = sorted(fm.get("tags") or [])
        idx_tags = sorted(entry.get("tags") or [])
        if art_tags != idx_tags:
            v.add(f"{fname} tags: article={art_tags} != index={idx_tags}")
        # reviewed_at
        art_rev = str(fm.get("reviewed_at")) if fm.get("reviewed_at") else None
        idx_rev = str(entry.get("reviewed_at")) if entry.get("reviewed_at") else None
        if art_rev != idx_rev:
            v.add(f"{fname} reviewed_at: article={art_rev!r} != index={idx_rev!r}")

    # --- 5. README.md / analyses/README.md 质量状态检查 ---
    _check_quality_status(v, README_MD, "README.md", expected_summary)
    _check_quality_status(v, ANALYSES_README, "analyses/README.md", expected_summary)

    # --- 6. 产品行状态 ---
    _check_product_rows(v, README_MD, "README.md", v.entries)
    _check_product_rows(v, ANALYSES_README, "analyses/README.md", v.entries)


def _check_quality_status(v: Validator, path: Path, label: str, expected: dict[str, int]) -> None:
    if not path.exists():
        v.add(f"{label} 不存在")
        return
    text = path.read_text(encoding="utf-8")
    section = extract_section(text, "当前质量状态")
    if not section:
        v.add(f"{label} 未找到 '当前质量状态' 小节")
        return
    parsed = parse_quality_status_numbers(section)
    # README 表格用 'AI 辅助分析' 而非 'total'
    readme_expected = {
        "AI 辅助分析": expected["total"],
        "reviewed": expected["reviewed"],
        "draft": expected["draft"],
        "verified": expected["verified"],
        "partial": expected["partial"],
    }
    for key, exp_v in readme_expected.items():
        actual_v = parsed.get(key)
        if actual_v is None:
            v.add(f"{label} 质量状态表 缺少 '{key}' 行")
        elif actual_v != exp_v:
            v.add(f"{label} 质量状态表 {key} expected {exp_v}, got {actual_v}")


def _check_product_rows(v: Validator, path: Path, label: str, entries: list[dict]) -> None:
    if not path.exists() or not entries:
        return
    text = path.read_text(encoding="utf-8")
    for entry in entries:
        product = entry.get("product", "")
        if not product:
            continue
        exp_rs = entry.get("review_status", "")
        exp_ss = entry.get("source_url_verification_status", "")
        product_lines = [line for line in text.splitlines() if product in line and "|" in line]
        if not product_lines:
            v.add(f"{label} 找不到产品 '{product}' 的行")
            continue
        line = product_lines[0]
        if exp_rs and exp_rs not in line:
            v.add(f"{label} {product}: expected review_status '{exp_rs}' not in row: {line[:80]}")
        if exp_ss and exp_ss not in line:
            v.add(f"{label} {product}: expected source_url_verification_status '{exp_ss}' not in row: {line[:80]}")


def main() -> int:
    v = Validator()
    run_validation(v)
    v.print_result()
    return 0 if v.passed else 1


if __name__ == "__main__":
    sys.exit(main())