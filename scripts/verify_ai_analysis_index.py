#!/usr/bin/env python3
"""
Product-Analysis AI 辅助分析索引一致性 + YAML 质量检查脚本 (P24)

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
from collections import Counter
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

CONSISTENCY_FIELDS = [
    "product", "category", "analysis_type", "review_status",
    "source_url_verification_status", "one_line_insight",
]


# ---------- 错误收集 ----------
class Validator:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.articles_checked = 0
        self.index_entries = 0
        self.reviewed = 0
        self.draft = 0
        self.partial = 0
        self.verified = 0

    def fail(self, code: str, msg: str) -> None:
        self.errors.append(f"[{code}] {msg}")

    @property
    def passed(self) -> bool:
        return not self.errors


# ---------- YAML 工具 ----------
def detect_duplicate_top_level_keys(yaml_text: str) -> list[str]:
    """检测 front matter 中 top-level 重复 key (PyYAML safe_load 静默覆盖 — P22.1 教训)。"""
    seen: Counter[str] = Counter()
    in_fm = False
    for line in yaml_text.splitlines():
        if line.strip() == "---":
            in_fm = not in_fm
            continue
        if not in_fm:
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:", line)
        if m:
            seen[m.group(1)] += 1
    return [k for k, n in seen.items() if n > 1]


def extract_front_matter(text: str) -> str | None:
    """提取 --- ... --- 之间的 YAML 文本。"""
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


def list_analysis_files() -> list[Path]:
    """只匹配 YYYY-MM-DD-*.md，排除 README.md。"""
    if not ANALYSES_DIR.exists():
        return []
    pat = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
    return sorted(p for p in ANALYSES_DIR.glob("*.md") if p.is_file() and pat.match(p.name))


def check_source_urls(urls: Any) -> list[str]:
    """检查 source_urls 是否纯 URL 字符串。"""
    issues: list[str] = []
    if not isinstance(urls, list):
        return ["source_urls 不是 list"]
    for i, u in enumerate(urls):
        if not isinstance(u, str):
            issues.append(f"  [{i}] 不是 string")
            continue
        if not u.startswith(("http://", "https://")):
            issues.append(f"  [{i}] 不以 http(s):// 开头: {u[:80]}")
        if "|" in u:
            issues.append(f"  [{i}] 包含 markdown 分隔符 '|': {u[:80]}")
    return issues


# ---------- 表格/段落提取 ----------
def extract_section(text: str, heading: str) -> str:
    """提取 ## [<num>.] {heading} 到下一个 ## 之间的内容。"""
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
    """从质量状态表格中提取数字。"""
    mapping: dict[str, int] = {}
    for m in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|", section, re.MULTILINE):
        label = m.group(1).strip().lstrip("- ").strip()
        try:
            mapping[label] = int(m.group(2))
        except ValueError:
            pass
    return mapping


# ---------- 主检查逻辑 ----------
def run_validation(v: Validator) -> None:
    if not HAS_YAML:
        v.fail("YAML_DEP", "PyYAML 未安装 — 请 pip install pyyaml")
        return

    # --- 1. 逐篇 article 检查 ---
    files = list_analysis_files()
    if not files:
        v.fail("NO_ARTICLES", f"{ANALYSES_DIR} 下没有 YYYY-MM-DD-*.md 文件")
        return

    v.articles_checked = len(files)
    parsed_articles: dict[str, dict[str, Any]] = {}

    for path in files:
        fname = path.name
        content = path.read_text(encoding="utf-8")

        # front matter 提取
        fm_text = extract_front_matter(content)
        if fm_text is None:
            v.fail("NO_FRONT_MATTER", f"{fname} 无 --- 包裹的 YAML front matter")
            continue

        # 重复 key 检测
        dup_keys = detect_duplicate_top_level_keys(fm_text)
        if dup_keys:
            v.fail("YAML_DUPLICATE_KEY", f"{fname} duplicate key: {', '.join(dup_keys)}")

        # YAML 解析
        try:
            fm = yaml.safe_load(fm_text)
        except yaml.YAMLError as e:
            v.fail("YAML_PARSE_ERROR", f"{fname} yaml.safe_load 失败: {e}")
            continue

        if not isinstance(fm, dict):
            v.fail("YAML_NOT_MAPPING", f"{fname} front matter 不是 mapping")
            continue

        parsed_articles[fname] = fm

        # 必备字段
        missing = [f for f in REQUIRED_FM_FIELDS if f not in fm]
        if missing:
            v.fail("MISSING_FIELDS", f"{fname} 缺失字段: {', '.join(missing)}")

        # review_status 条件字段
        rs = fm.get("review_status")
        if rs == "reviewed":
            if not fm.get("reviewed_at"):
                v.fail("MISSING_REVIEWED_AT", f"{fname} review_status=reviewed 但 reviewed_at 为空")
            if not fm.get("review_notes"):
                v.fail("MISSING_REVIEW_NOTES", f"{fname} review_status=reviewed 但 review_notes 为空")
        elif rs not in ("reviewed", "draft"):
            v.fail("INVALID_REVIEW_STATUS", f"{fname} 未识别的 review_status: {rs}")

        # source_urls 格式
        url_issues = check_source_urls(fm.get("source_urls"))
        if url_issues:
            v.fail("SOURCE_URLS_FORMAT", f"{fname} " + "; ".join(url_issues))

    # --- 2. index.yml 解析 ---
    if not INDEX_YML.exists():
        v.fail("NO_INDEX_YML", f"{INDEX_YML} 不存在")
        return

    try:
        idx = yaml.safe_load(INDEX_YML.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        v.fail("INDEX_YAML_PARSE_ERROR", f"analyses/index.yml 解析失败: {e}")
        return

    if "analyses" not in idx or "summary" not in idx:
        v.fail("INDEX_MISSING_KEYS", "analyses/index.yml 缺失 analyses 或 summary")
        return

    entries = idx["analyses"]
    if not isinstance(entries, list):
        v.fail("INDEX_ANALYSES_NOT_LIST", "analyses/index.yml analyses 不是 list")
        return

    v.index_entries = len(entries)

    # entry 字段完整性
    for e in entries:
        product = e.get("product", "<unknown>")
        missing = [f for f in REQUIRED_INDEX_ENTRY_FIELDS if f not in e]
        if missing:
            v.fail("INDEX_ENTRY_MISSING_FIELDS", f"{product} 缺失字段: {', '.join(missing)}")

    # summary count 计算
    v.reviewed = sum(1 for e in entries if e.get("review_status") == "reviewed")
    v.draft = sum(1 for e in entries if e.get("review_status") == "draft")
    v.verified = sum(1 for e in entries if e.get("source_url_verification_status") == "verified")
    v.partial = sum(1 for e in entries if e.get("source_url_verification_status") == "partial")

    summary = idx["summary"]
    expected_summary = {
        "total": len(entries),
        "reviewed": v.reviewed,
        "draft": v.draft,
        "verified": v.verified,
        "partial": v.partial,
    }
    for k, exp_v in expected_summary.items():
        actual_v = summary.get(k)
        if actual_v != exp_v:
            v.fail("SUMMARY_MISMATCH", f"index.yml summary.{k} expected {exp_v}, got {actual_v}")

    # --- 3. article ↔ index 一致性 ---
    entries_by_file = {e.get("file"): e for e in entries}
    for fname, fm in parsed_articles.items():
        rel_path = f"analyses/ai-assisted/{fname}"
        entry = entries_by_file.get(rel_path)
        if entry is None:
            v.fail("ARTICLE_NOT_IN_INDEX", f"{fname} 在 index.yml 中找不到 file={rel_path}")
            continue
        for field in CONSISTENCY_FIELDS:
            v_art = fm.get(field)
            v_idx = entry.get(field)
            if v_art != v_idx:
                v.fail(
                    "FIELD_MISMATCH",
                    f"{fname} field '{field}': article={v_art!r} ≠ index={v_idx!r}",
                )
        # tags
        art_tags = sorted(fm.get("tags") or [])
        idx_tags = sorted(entry.get("tags") or [])
        if art_tags != idx_tags:
            v.fail("TAGS_MISMATCH", f"{fname} tags: article={art_tags} ≠ index={idx_tags}")
        # reviewed_at
        art_rev = str(fm.get("reviewed_at")) if fm.get("reviewed_at") else None
        idx_rev = str(entry.get("reviewed_at")) if entry.get("reviewed_at") else None
        if art_rev != idx_rev:
            v.fail("REVIEWED_AT_MISMATCH", f"{fname} reviewed_at: article={art_rev!r} ≠ index={idx_rev!r}")

    # --- 4. README.md 质量状态检查 ---
    _check_quality_status(v, README_MD, "README.md", expected_summary)
    _check_quality_status(v, ANALYSES_README, "analyses/README.md", expected_summary)

    # --- 5. 产品状态行检查 (简化字符串匹配) ---
    _check_product_rows(v, README_MD, "README.md", entries)
    _check_product_rows(v, ANALYSES_README, "analyses/README.md", entries)


def _check_quality_status(v: Validator, path: Path, label: str, expected: dict[str, int]) -> None:
    """检查 README/analyses README 的当前质量状态表格。"""
    if not path.exists():
        v.fail("FILE_NOT_FOUND", f"{label} 不存在")
        return
    text = path.read_text(encoding="utf-8")
    section = extract_section(text, "当前质量状态")
    if not section:
        v.fail("SECTION_NOT_FOUND", f"{label} 未找到 '当前质量状态' 小节")
        return
    parsed = parse_quality_status_numbers(section)
    # README 表格用 'AI 辅助分析' 而非 'total'
    readme_expected = {k: v for k, v in expected.items() if k != "total"}
    readme_expected["AI 辅助分析"] = expected["total"]
    for key, exp_v in readme_expected.items():
        actual_v = parsed.get(key)
        if actual_v is None:
            v.fail("README_SUMMARY_MISMATCH", f"{label} 缺少 '{key}' 行")
        elif actual_v != exp_v:
            v.fail("README_SUMMARY_MISMATCH", f"{label} {key} count expected {exp_v}, got {actual_v}")


def _check_product_rows(v: Validator, path: Path, label: str, entries: list[dict]) -> None:
    """简化字符串匹配:每个产品名存在 + 行含 expected status。"""
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for entry in entries:
        product = entry.get("product", "")
        if not product:
            continue
        exp_rs = entry.get("review_status", "")
        exp_ss = entry.get("source_url_verification_status", "")
        # 找包含产品名的行
        product_lines = [line for line in text.splitlines() if product in line and "|" in line]
        if not product_lines:
            v.fail("PRODUCT_ROW_MISSING", f"{label} 找不到产品 '{product}' 的行")
            continue
        # 取第一个匹配行检查 status
        line = product_lines[0]
        if exp_rs and exp_rs not in line:
            v.fail("PRODUCT_STATUS_MISMATCH", f"{label} {product}: expected review_status '{exp_rs}' not found in row")
        if exp_ss and exp_ss not in line:
            v.fail("PRODUCT_STATUS_MISMATCH", f"{label} {product}: expected source_url_verification_status '{exp_ss}' not found in row")


# ---------- 主入口 ----------
def main() -> int:
    if not HAS_YAML:
        print("FAIL: AI analysis index validation failed")
        print("[YAML_DEP] PyYAML 未安装 — 请 pip install pyyaml")
        return 1

    v = Validator()
    run_validation(v)

    if v.passed:
        print("PASS: AI analysis index validation passed")
        print(f"- articles_checked: {v.articles_checked}")
        print(f"- index_entries: {v.index_entries}")
        print(f"- reviewed: {v.reviewed}")
        print(f"- draft: {v.draft}")
        print(f"- partial: {v.partial}")
        print(f"- verified: {v.verified}")
        return 0
    else:
        print("FAIL: AI analysis index validation failed")
        for err in v.errors:
            print(err)
        print()
        print(f"- articles_checked: {v.articles_checked}")
        print(f"- index_entries: {v.index_entries}")
        print(f"- reviewed: {v.reviewed}")
        print(f"- draft: {v.draft}")
        print(f"- partial: {v.partial}")
        print(f"- verified: {v.verified}")
        return 1


if __name__ == "__main__":
    sys.exit(main())