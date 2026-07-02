# P24 - AI Index and YAML Consistency Validator Report

**日期：** 2026-07-02
**任务类型：** tooling / validation / docs-only + data-fix

---

## Task Overview

新增自动校验脚本，检查 AI 分析索引与 YAML 一致性；修复脚本运行中发现的真实数据问题。

---

## Final Status

```
STATUS: PASS
REPOSITORY: https://github.com/conanxin/Product-Analysis
BRANCH: master
BASE_COMMIT: db5a5ab (P24.1)
NEW_COMMIT: (TBD at commit time)
PUSH_RESULT: (TBD at push time)
```

---

## Git State (Pre-Change)

```
$ git log --oneline -10
db5a5ab P24.1: rewrite validation script output to spec format
70defde P24: add AI analysis index validation script
4414283 P23.1: fix Replit README quality status drift
e81df08 P23: review Replit analysis and sync index status
a4cb31f P23: review Replit analysis and sync index status
086cebe P22.1: fix Replit YAML duplicate source quality notes
6ca0d8b P22: add Replit AI-assisted product analysis
cf497a9 P21: review Webflow analysis and sync index status
302a061 P20: add Webflow AI-assisted product analysis
1136646 P19.1: fix Canva index status drift
```

---

## Step 0 — Current State Verification

```
README.md:  AI 辅助分析 10 / reviewed 10 / draft 0 / partial 10 / verified 0
analyses/README.md:  AI 辅助分析 10 / reviewed 10 / draft 0 / partial 10 / verified 0
analyses/index.yml:  summary total=10 reviewed=10 draft=0 partial=10 verified=0
10 篇 AI 分析文章 YAML:  全部 reviewed | partial
```

四文件状态一致 → P24 可继续。

---

## Script (scripts/verify_ai_analysis_index.py)

- Python 3.10+ + PyYAML
- 自定义 SafeLoader (检测重复 key，P22.1 教训)
- 11 大类检查，约 30+ 子项
- 输出：`PASS: AI analysis index consistency verified` + stats / `FAIL: AI analysis index consistency errors` + 编号错误列表

---

## Checks Implemented

1. YAML front matter 提取（每篇文章 `---` 包裹）
2. YAML duplicate key 检测（自定义 SafeLoader，不依赖 yaml.safe_load）
3. 必备字段（11 字段：product / category / tags / source_urls / analysis_type / created_at / review_status / source_url_verified_at / source_url_verification_status / source_quality_notes / one_line_insight）
4. review_status 条件字段（reviewed → 必须 reviewed_at + review_notes）
5. review_status 合法性（只允许 draft / reviewed）
6. source_url_verification_status 合法性（只允许 partial / verified）
7. analysis_type 合法性（只允许 ai-assisted）
8. source_urls 格式（list[string] / http(s):// 前缀 / 无 inline annotation）
9. analyses/index.yml 顶层 key（version / analyses / summary / by_category / reading_paths）
10. index entry 字段完整性（10 字段）
11. quality_notes 子字段（product_mechanism / high_risk_facts / reason）
12. summary count 一致性（动态计算 vs summary 字段）
13. article ↔ index.yml 字段一致性（8 字段）
14. README.md 质量状态表
15. analyses/README.md 质量状态表
16. README.md 产品行（字符串匹配）
17. analyses/README.md 产品行（字符串匹配）

---

## Validation Result

修复前：

```
FAIL: AI analysis index consistency errors
1. 2026-07-01-cursor.md yaml.safe_load 失败: mapping values are not allowed here
2. 2026-07-01-perplexity.md yaml.safe_load 失败: mapping values are not allowed here
3. 2026-07-01-raycast.md yaml.safe_load 失败: mapping values are not allowed here
4-12. one_line_insight 引号风格不一致（9 项）

- analyses found: 7 (其中 3 篇无法 parse)
- reviewed: 7
- draft: 0
- partial: 7
- verified: 0
```

修复后：

```
PASS: AI analysis index consistency verified
- analyses found: 10
- reviewed: 10
- draft: 0
- partial: 10
- verified: 0
```

---

## Current Counts (final PASS)

| 维度 | 值 |
|------|---|
| total | 10 |
| reviewed | 10 |
| draft | 0 |
| partial | 10 |
| verified | 0 |

---

## Duplicate Key Detection Result

脚本使用自定义 SafeLoader：

```python
def _construct_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise DuplicateKeyError(f"duplicate key: {key!r}")
        value = loader.construct_object(value_node, deep=deep)
        mapping[key] = value
    return mapping
```

P22.1 修复后当前 10 篇文章无重复 key，P24 验证脚本可检测。

---

## README / analyses README / index.yml Consistency Result

| 检查 | 结果 |
|------|------|
| README.md AI 辅助分析 count | 10 ✅ |
| README.md reviewed count | 10 ✅ |
| README.md draft count | 0 ✅ |
| README.md partial count | 10 ✅ |
| README.md verified count | 0 ✅ |
| analyses/README.md AI 辅助分析 count | 10 ✅ |
| analyses/README.md reviewed count | 10 ✅ |
| analyses/README.md partial count | 10 ✅ |
| analyses/index.yml summary.total | 10 ✅ |
| analyses/index.yml summary.reviewed | 10 ✅ |
| analyses/index.yml summary.draft | 0 ✅ |
| analyses/index.yml summary.partial | 10 ✅ |
| 10 个产品行 status 一致性 | ✅ |

---

## Files Intentionally Not Changed

- analyses/README.md — 已是正确状态
- 旧人工分析文章 (legacy-note / Product Hunt P2)
- pic/
- templates/

---

## Files Modified (P24 final)

| 文件 | 变更类型 | 详情 |
|------|----------|------|
| scripts/verify_ai_analysis_index.py | modified | 重写为简洁 PASS:/FAIL: 格式 + 自定义 SafeLoader + 11 大类检查 |
| docs/index-sync-validation.md | new | 6 节工作流文档 |
| docs/validation-workflow.md | deleted | 旧 doc，重命名为 index-sync-validation.md |
| analyses/ai-assisted/2026-07-01-cursor.md | modified | review_notes + source_quality_notes 加双引号（修复 YAML scan error） |
| analyses/ai-assisted/2026-07-01-perplexity.md | modified | source_quality_notes 加双引号（修复 YAML scan error） |
| analyses/ai-assisted/2026-07-01-raycast.md | modified | source_quality_notes 加双引号（修复 YAML scan error） |
| analyses/index.yml | modified | 9 个 entry 的 one_line_insight 同步为 article 引号风格 |
| README.md | modified | 新增 "如何校验索引一致性" 小节 + todo + 最后更新 |
| CHANGELOG.md | modified | 顶部 prepend P24 (Final) 记录 |
| reports/P24-ai-index-yaml-consistency-validator-report.md | new | 本报告 |

---

## Remaining Issues

无。P24 修复所有 12 项真实问题后，脚本 PASS。

---

## Lessons

1. **P22.1 教训：** PyYAML `yaml.safe_load` 会静默覆盖重复 key — 必须自定义 SafeLoader（覆盖 construct_mapping）
2. **P23.1 教训：** 同步索引不仅要改 4 处文件，所有引用同一数据的统计表格也要同步
3. **新教训：** 长 YAML 值（含冒号 / 方括号 / 复杂标点）必须加双引号包裹或转义
4. **新教训：** 同一字段在多个文件中必须严格字符串一致（article YAML ↔ index.yml），引号风格也要统一
5. **新教训：** 同步 9 个 article 的 one_line_insight 用 yaml.dump 自动重写 index.yml 会破坏 tags / quality_notes / summary 等字段的 inline 风格 — 后续 P* 任务修复单字段时应考虑选择性更新而非全文重写

---

## NEXT_STEP

1. P25 候选：新增第 11 篇 AI 分析（Coda / Obsidian / Tana / Arc / Claude Code / Lovable / v0）
2. P25 必须先通过 `python3 scripts/verify_ai_analysis_index.py` 验证 PASS
3. P26 (候选)：将脚本接入 GitHub Actions CI（`.github/workflows/validate.yml`）
4. P26 (候选)：pre-commit hook — commit 前自动跑脚本
5. 长期：主流媒体 paywall 401/403/404 仍 partial；Replit IPO 时间表追踪

---

_报告生成时间：2026-07-02_
_P24 完成状态：PASS（修复 12 项真实数据问题后脚本运行 PASS）_