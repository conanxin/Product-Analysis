#!/usr/bin/env python3
"""
Product-Analysis AI 辅助分析索引一致性 + YAML 质量检查脚本 (P24)

P24 工具:verify_ai_analysis_index.py
用途:
  1. 提取 analyses/ai-assisted/*.md 的 YAML front matter
  2. 检测 YAML 重复 key (PyYAML safe_load 静默覆盖 — P22.1 教训)
  3. 验证 YAML 必备字段
  4. 检查 source_urls 是否纯 URL 字符串
  5. 解析 analyses/index.yml
  6. 检查 article YAML 与 index.yml 一致性
  7. 校验 index.yml summary count
  8. 校验 README.md 当前质量状态
  9. 校验 analyses/README.md 当前质量状态
 10. 校验 README / analyses/README 产品状态行

退出码:
  0 = PASS (所有检查通过)
  1 = FAIL (有失败项)

运行:
  cd <repo-root>
  python3 scripts/verify_ai_analysis_index.py
"""

from __future__ import annotations

import os
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

# ---------- 可选依赖:PyYAML ----------
try:
    import yaml  # type: ignore
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


# ---------- ANSI 颜色 ----------
class C:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


# ---------- 报告收集器 ----------
class Report:
    def __init__(self) -> None:
        self.checks: list[tuple[str, bool, str]] = []  # (name, passed, detail)

    def add(self, name: str, passed: bool, detail: str = "") -> None:
        self.checks.append((name, passed, detail))

    @property
    def fails(self) -> list[tuple[str, bool, str]]:
        return [c for c in self.checks if not c[1]]

    @property
    def passed(self) -> bool:
        return all(c[1] for c in self.checks)

    def print_summary(self) -> None:
        total = len(self.checks)
        fail_count = len(self.fails)
        pass_count = total - fail_count
        print()
        print(f"{C.BOLD}{'=' * 60}{C.RESET}")
        print(f"{C.BOLD}检查总数:{total}  通过:{C.GREEN}{pass_count}{C.RESET}  失败:{C.RED}{fail_count}{C.RESET}{C.RESET}")
        print(f"{C.BOLD}{'=' * 60}{C.RESET}")
        if fail_count:
            print(f"\n{C.RED}{C.BOLD}失败项:{C.RESET}")
            for name, _, detail in self.fails:
                print(f"  {C.RED}✗ {name}{C.RESET}")
                if detail:
                    for line in detail.splitlines():
                        print(f"      {line}")
        print()
        if self.passed:
            print(f"{C.GREEN}{C.BOLD}OVERALL: PASS ✓{C.RESET}")
        else:
            print(f"{C.RED}{C.BOLD}OVERALL: FAIL ✗{C.RESET}")


# ---------- 文件路径 ----------
REPO_ROOT = Path(__file__).resolve().parent.parent
ANALYSES_DIR = REPO_ROOT / "analyses" / "ai-assisted"
INDEX_YML = REPO_ROOT / "analyses" / "index.yml"
ANALYSES_README = REPO_ROOT / "analyses" / "README.md"
README_MD = REPO_ROOT / "README.md"


# ---------- 工具函数:重复 key 检测 ----------
def detect_duplicate_top_level_keys(yaml_text: str) -> list[str]:
    """
    检测 top-level YAML mapping 中的重复 key。
    PyYAML safe_load 会静默覆盖重复 key,这里用 regex + 缩进检测。
    简化实现:仅检测 root level (无 indent) 的 key 重复。
    """
    keys: list[str] = []
    seen = Counter()
    in_front_matter = False
    for raw_line in yaml_text.splitlines():
        # 简单判断:以 --- 包裹 front matter
        if raw_line.strip() == "---":
            in_front_matter = not in_front_matter
            continue
        if not in_front_matter:
            continue
        # top-level key 格式:`key:` (无前导空格)
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:", raw_line)
        if m:
            key = m.group(1)
            keys.append(key)
            seen[key] += 1
    return [k for k, n in seen.items() if n > 1]


# ---------- 工具函数:source_urls 格式检查 ----------
# 来源 item 不得包含的字符 / token (这些是明确不合法 inline annotation marker)
SOURCE_URL_FORBIDDEN_TOKENS = ["|"]  # 表格分隔符,不允许出现在 source_urls 中
SOURCE_URL_ALLOWED_SCHEMES = ("http://", "https://")
# 这些关键词 / token 出现在 URL 中代表有 inline annotation
SOURCE_URL_INLINE_NOTE_TOKENS = [
    "verified",
    "partial",
    "primary",
    "secondary",
    "official",
    "paywalled",
    "datadome",
    "note:",
    "type:",
    "status:",
]


def check_source_urls(urls: Any) -> list[str]:
    """返回每个违规项的描述;空 list = 通过。"""
    issues: list[str] = []
    if not isinstance(urls, list):
        return ["source_urls 不是 list"]
    for i, u in enumerate(urls):
        if not isinstance(u, str):
            issues.append(f"  [{i}] 不是 string")
            continue
        if not u.startswith(SOURCE_URL_ALLOWED_SCHEMES):
            issues.append(f"  [{i}] 不以 http(s):// 开头: {u[:60]}")
        # 检查 markdown 表格分隔符
        for tok in SOURCE_URL_FORBIDDEN_TOKENS:
            if tok in u:
                issues.append(f"  [{i}] 包含 markdown 分隔符 '{tok}': {u[:60]}")
        # 检查是否包含明显的 inline annotation token (用空格隔开避免误伤)
        # 这些词出现在 URL 后面/中间用空格分隔表示 inline note
        if "  " in u:  # 双空格表明后面可能有空格分隔的 token
            for tok in SOURCE_URL_INLINE_NOTE_TOKENS:
                # 检查形如 "url verified" / "url (verified" 这样的 inline note
                if re.search(rf"[\s(]+{re.escape(tok)}[\s)]*$", u, re.IGNORECASE):
                    issues.append(f"  [{i}] 包含 inline annotation '{tok}': {u[:60]}")
                    break
    return issues


# ---------- 工具函数:质量状态表格解析 ----------
def parse_quality_status_table(text: str) -> dict[str, int]:
    """
    解析当前质量状态小节中的 markdown 表格,返回 {key: count}。
    支持两种行格式:
      - `| AI 辅助分析 | 10 | 全部 reviewed |`
      - `| - reviewed | 10 | 人工复核完成 |`
      - `| reviewed | 10 | 人工复核完成 |`
    """
    mapping: dict[str, int] = {}
    # 匹配 `| <label> | <number> |` 形式
    for m in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|", text, re.MULTILINE):
        label = m.group(1).strip()
        try:
            count = int(m.group(2))
        except ValueError:
            continue
        # 统一处理:'- reviewed' → 'reviewed'
        normalized = label.lstrip("- ").strip()
        mapping[normalized] = count
    return mapping


def extract_section(text: str, heading: str) -> str:
    """提取从 `## [<number>.] {heading}` 开始到下一个 `## ` 之前的内容。

    支持两种格式:
      - `## 当前质量状态`  (README.md)
      - `## 3. 当前质量状态`  (analyses/README.md)
    """
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


# ---------- 工具函数:产品行状态提取 ----------
# README.md 索引行格式:
# | 2026-07-01 | Perplexity | `analyses/ai-assisted/...` | AI 辅助 | tags | one-liner | reviewed | partial |
# analyses/README.md 索引行格式:
# | Perplexity | ai-search | [file](...) | reviewed | partial | one-liner |
PRODUCT_ROW_RE_README = re.compile(
    r"^\|\s*[\d-]+\s*\|\s*([^|]+?)\s*\|\s*`[^`]+`\s*\|[^|]*\|\s*[^|]+\s*\|\s*[^|]+\s*\|\s*(draft|reviewed|partial|verified|unverified)\s*\|\s*(draft|partial|verified|unverified|reviewed)\s*\|",
    re.MULTILINE,
)
PRODUCT_ROW_AREADME = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*[a-z-][a-z0-9-]*\s*\|\s*\[[^\]]+\]\([^)]+\)\s*\|\s*(draft|reviewed|partial|verified|unverified)\s*\|\s*(draft|partial|verified|unverified|reviewed)\s*\|",
    re.MULTILINE,
)


def extract_product_rows_readme(text: str) -> dict[str, tuple[str, str]]:
    """从 README.md 提取产品状态: {product: (review_status, source_url_status)}"""
    out: dict[str, tuple[str, str]] = {}
    for m in PRODUCT_ROW_RE_README.finditer(text):
        product = m.group(1).strip()
        rs = m.group(2).strip()
        ss = m.group(3).strip()
        out[product] = (rs, ss)
    return out


def extract_product_rows_areadme(text: str) -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    for m in PRODUCT_ROW_AREADME.finditer(text):
        product = m.group(1).strip()
        rs = m.group(2).strip()
        ss = m.group(3).strip()
        out[product] = (rs, ss)
    return out


# ============================================================
# 检查函数
# ============================================================

def check_yaml_dependencies(report: Report) -> None:
    if not HAS_YAML:
        report.add(
            "yaml 依赖",
            False,
            "PyYAML 未安装 — 请 pip install pyyaml;脚本需要 PyYAML 解析 YAML。",
        )
        return
    report.add("yaml 依赖", True, f"PyYAML {yaml.__version__}")


def list_analysis_files() -> list[Path]:
    """只匹配 YYYY-MM-DD-<product>.md 格式的 AI 分析文件,排除 README.md 等其他说明文件。"""
    if not ANALYSES_DIR.exists():
        return []
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
    return sorted(p for p in ANALYSES_DIR.glob("*.md") if p.is_file() and pattern.match(p.name))


def extract_front_matter(text: str) -> tuple[str | None, str]:
    """返回 (front_matter_text, body)。如果没有 --- 包裹,返回 (None, full_text)。"""
    stripped = text.lstrip()
    if not stripped.startswith("---"):
        return None, text
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None, text
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, text
    fm_text = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1 :])
    return fm_text, body


def check_each_analysis_file(report: Report) -> dict[str, dict[str, Any]]:
    """对每篇 analyses/ai-assisted/*.md 做检查,返回 {filename: parsed_fm}。"""
    parsed: dict[str, dict[str, Any]] = {}
    files = list_analysis_files()
    if not files:
        report.add("AI 分析文件存在", False, f"{ANALYSES_DIR} 下没有 .md 文件")
        return parsed
    report.add(f"AI 分析文件 ({len(files)})", True, ", ".join(p.name for p in files))

    for path in files:
        label = f"  {path.name}"
        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            report.add(label, False, f"读取失败: {e}")
            continue

        # 1. front matter 提取
        fm_text, body = extract_front_matter(content)
        if fm_text is None:
            report.add(f"{label} front-matter", False, "无 --- 包裹的 YAML front matter")
            continue
        report.add(f"{label} front-matter", True, f"{len(fm_text)} chars")

        # 2. 重复 key 检测 (PyYAML 静默覆盖 — P22.1 教训)
        dup_keys = detect_duplicate_top_level_keys(fm_text)
        if dup_keys:
            report.add(
                f"{label} 重复 key 检测",
                False,
                f"发现重复 top-level key: {', '.join(dup_keys)} (PyYAML safe_load 会静默覆盖)",
            )
        else:
            report.add(f"{label} 重复 key 检测", True, "无重复 top-level key")

        # 3. YAML 解析
        if not HAS_YAML:
            continue
        try:
            fm = yaml.safe_load(fm_text)
        except yaml.YAMLError as e:
            report.add(f"{label} YAML 解析", False, f"yaml.safe_load 失败: {e}")
            continue
        if not isinstance(fm, dict):
            report.add(f"{label} YAML 解析", False, f"front matter 不是 mapping,得到 {type(fm).__name__}")
            continue
        report.add(f"{label} YAML 解析", True, f"{len(fm)} fields")
        parsed[path.name] = fm

        # 4. 必备字段
        required_fields = [
            "product",
            "category",
            "tags",
            "source_urls",
            "analysis_type",
            "created_at",
            "review_status",
            "source_url_verified_at",
            "source_url_verification_status",
            "source_quality_notes",
            "one_line_insight",
        ]
        missing = [f for f in required_fields if f not in fm]
        if missing:
            report.add(f"{label} 必备字段", False, f"缺失: {', '.join(missing)}")
        else:
            report.add(f"{label} 必备字段", True, "全部 11 字段存在")

        # 5. review_status 条件字段
        rs = fm.get("review_status")
        if rs == "reviewed":
            if not fm.get("reviewed_at"):
                report.add(f"{label} reviewed_at", False, "review_status=reviewed 但 reviewed_at 为空")
            if not fm.get("review_notes"):
                report.add(f"{label} review_notes", False, "review_status=reviewed 但 review_notes 为空")
            else:
                report.add(f"{label} reviewed_at + review_notes", True, "完整")
        elif rs == "draft":
            report.add(f"{label} reviewed 条件字段", True, "draft 模式,允许 reviewed_at 缺失")
        else:
            report.add(f"{label} review_status 值", False, f"未识别的 review_status: {rs}")

        # 6. source_urls 检查
        urls_issues = check_source_urls(fm.get("source_urls"))
        if urls_issues:
            report.add(f"{label} source_urls 格式", False, "\n".join(urls_issues))
        else:
            url_count = len(fm.get("source_urls", []))
            report.add(f"{label} source_urls 格式", True, f"{url_count} 纯 URL")

    return parsed


def check_index_yml(report: Report, parsed_articles: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    """解析 analyses/index.yml,检查 summary + analyses list 完整性。"""
    if not HAS_YAML:
        return None
    if not INDEX_YML.exists():
        report.add("analyses/index.yml 存在", False, f"{INDEX_YML} 不存在")
        return None
    try:
        idx = yaml.safe_load(INDEX_YML.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        report.add("analyses/index.yml 解析", False, f"yaml.safe_load 失败: {e}")
        return None
    report.add("analyses/index.yml 解析", True, f"{len(idx)} top-level keys")

    for key in ("analyses", "summary"):
        if key not in idx:
            report.add(f"analyses/index.yml.{key}", False, f"缺失 top-level '{key}'")
            return None
    report.add("analyses/index.yml.analyses & summary", True, "存在")

    entries = idx["analyses"]
    if not isinstance(entries, list):
        report.add("analyses/index.yml.analyses 类型", False, f"不是 list,得到 {type(entries).__name__}")
        return None
    report.add("analyses/index.yml.analyses 类型", True, f"{len(entries)} entries")

    # entry 字段完整性
    required_entry_fields = [
        "product",
        "file",
        "category",
        "analysis_type",
        "created_at",
        "review_status",
        "source_url_verification_status",
        "tags",
        "one_line_insight",
        "quality_notes",
    ]
    for e in entries:
        product = e.get("product", "<unknown>")
        label = f"  index entry: {product}"
        missing = [f for f in required_entry_fields if f not in e]
        if missing:
            report.add(label, False, f"缺失字段: {', '.join(missing)}")
        else:
            report.add(label, True, f"{len(required_entry_fields)} 字段齐全")

    # summary 校验
    summary = idx["summary"]
    expected = {
        "total": len(entries),
        "reviewed": sum(1 for e in entries if e.get("review_status") == "reviewed"),
        "draft": sum(1 for e in entries if e.get("review_status") == "draft"),
        "verified": sum(
            1 for e in entries if e.get("source_url_verification_status") == "verified"
        ),
        "partial": sum(
            1 for e in entries if e.get("source_url_verification_status") == "partial"
        ),
    }
    for k, expected_v in expected.items():
        actual_v = summary.get(k)
        if actual_v != expected_v:
            report.add(
                f"summary.{k}",
                False,
                f"期望 {expected_v},实际 {actual_v}",
            )
        else:
            report.add(f"summary.{k}", True, f"{actual_v}")
    return idx


def check_article_vs_index_consistency(
    report: Report,
    parsed_articles: dict[str, dict[str, Any]],
    idx: dict[str, Any] | None,
) -> None:
    if idx is None:
        return
    entries_by_file = {e.get("file"): e for e in idx["analyses"]}

    for filename, fm in parsed_articles.items():
        rel_path = f"analyses/ai-assisted/{filename}"
        entry = entries_by_file.get(rel_path)
        if entry is None:
            report.add(
                f"  article→index 一致性 ({filename})",
                False,
                f"index.yml 中找不到 file={rel_path}",
            )
            continue
        label = f"  article→index 一致性 ({fm.get('product')})"
        inconsistent = []
        for field in (
            "product",
            "category",
            "analysis_type",
            "review_status",
            "source_url_verification_status",
            "one_line_insight",
        ):
            v_art = fm.get(field)
            v_idx = entry.get(field)
            if v_art != v_idx:
                inconsistent.append(f"    - {field}: article={v_art!r} ≠ index={v_idx!r}")
        # tags 比较 (list vs list)
        art_tags = sorted(fm.get("tags") or [])
        idx_tags = sorted(entry.get("tags") or [])
        if art_tags != idx_tags:
            inconsistent.append(f"    - tags: article={art_tags} ≠ index={idx_tags}")
        # reviewed_at 比较
        art_rev = str(fm.get("reviewed_at")) if fm.get("reviewed_at") else None
        idx_rev = str(entry.get("reviewed_at")) if entry.get("reviewed_at") else None
        if art_rev != idx_rev:
            inconsistent.append(f"    - reviewed_at: article={art_rev!r} ≠ index={idx_rev!r}")
        if inconsistent:
            report.add(label, False, "\n".join(inconsistent))
        else:
            report.add(label, True, "8 字段一致")


def check_readme_quality_status(
    report: Report,
    path: Path,
    label: str,
    expected: dict[str, int],
) -> None:
    if not path.exists():
        report.add(f"{label} 存在", False, f"{path} 不存在")
        return
    text = path.read_text(encoding="utf-8")
    section = extract_section(text, "当前质量状态")
    if not section:
        report.add(f"{label} 当前质量状态 小节", False, "未找到 ## 当前质量状态 小节")
        return
    parsed = parse_quality_status_table(section)
    # 动态比较:实际值应与 expected 一致
    bad = []
    for key, expected_v in expected.items():
        actual_v = parsed.get(key)
        if actual_v is None:
            bad.append(f"    - 缺少 '{key}' 行")
        elif actual_v != expected_v:
            bad.append(f"    - {key}: README={actual_v} ≠ index.yml summary={expected_v}")
    if bad:
        report.add(f"{label} 当前质量状态 一致性", False, "\n".join(bad))
    else:
        report.add(f"{label} 当前质量状态 一致性", True, f"与 index.yml summary 一致: {expected}")


def check_product_rows_in_readme(
    report: Report,
    path: Path,
    label: str,
    idx: dict[str, Any] | None,
    extract_fn,
) -> None:
    if idx is None or not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    rows = extract_fn(text)
    if not rows:
        report.add(f"{label} 产品行提取", False, "未提取到任何产品行 — 表格格式可能变化")
        return
    report.add(f"{label} 产品行提取", True, f"{len(rows)} 产品")
    index_entries = {e["product"]: e for e in idx["analyses"]}
    bad = []
    for product, (rs, ss) in rows.items():
        entry = index_entries.get(product)
        if entry is None:
            bad.append(f"    - {product}: 不在 index.yml 中")
            continue
        idx_rs = entry.get("review_status")
        idx_ss = entry.get("source_url_verification_status")
        if rs != idx_rs or ss != idx_ss:
            bad.append(
                f"    - {product}: README=({rs},{ss}) ≠ index=({idx_rs},{idx_ss})"
            )
    if bad:
        report.add(f"{label} 产品状态行一致性", False, "\n".join(bad))
    else:
        report.add(f"{label} 产品状态行一致性", True, f"{len(rows)} 产品状态与 index.yml 一致")


# ============================================================
# 主入口
# ============================================================

def main() -> int:
    if not HAS_YAML:
        print(f"{C.RED}错误:未安装 PyYAML。请 pip install pyyaml。{C.RESET}")
        return 1

    print(f"{C.BOLD}Product-Analysis 索引一致性 + YAML 质量检查 (P24){C.RESET}")
    print(f"仓库根:{REPO_ROOT}")
    print()

    report = Report()

    # 1. PyYAML 依赖
    check_yaml_dependencies(report)

    # 2. 逐篇 article 检查
    parsed_articles = check_each_analysis_file(report)

    # 3. index.yml 解析 + summary 校验
    idx = check_index_yml(report, parsed_articles)

    # 4. article vs index 一致性
    check_article_vs_index_consistency(report, parsed_articles, idx)

    # 5. README.md 当前质量状态
    if idx is not None:
        entries = idx["analyses"]
        expected_summary = {
            "AI 辅助分析": len(entries),
            "reviewed": sum(1 for e in entries if e.get("review_status") == "reviewed"),
            "draft": sum(1 for e in entries if e.get("review_status") == "draft"),
            "verified": sum(
                1 for e in entries
                if e.get("source_url_verification_status") == "verified"
            ),
            "partial": sum(
                1 for e in entries
                if e.get("source_url_verification_status") == "partial"
            ),
        }
        check_readme_quality_status(report, README_MD, "README.md", expected_summary)
        check_readme_quality_status(
            report, ANALYSES_README, "analyses/README.md", expected_summary
        )

    # 6. 产品状态行一致性
    check_product_rows_in_readme(
        report, README_MD, "README.md AI 索引", idx, extract_product_rows_readme
    )
    check_product_rows_in_readme(
        report,
        ANALYSES_README,
        "analyses/README.md AI 总览",
        idx,
        extract_product_rows_areadme,
    )

    # 输出报告
    report.print_summary()
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main())