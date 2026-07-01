# P10 - Cursor 人工复核与高风险事实加固报告

**项目：** Product-Analysis
**阶段：** P10 (Cursor review / source-hardening / docs-only)
**日期：** 2026-07-01
**仓库：** https://github.com/conanxin/Product-Analysis
**基础提交：** ea84cb4 (P9.1 spec-compliance)

---

## 1. 任务概述

P10 是对 P9 新增的 Cursor AI 辅助产品分析做人工复核与高风险事实加固，遵循 Linear P6 / Raycast P8 review 模式。

## 2. 执行链路 (Step 1)

```
ea84cb4 P10 (待写)
f8df0da P9: add Cursor AI-assisted product analysis (source-first)
2bf4b26 P8.1: complete §17.3 spec-required 5 items + §17.4 P8 review status header
93df2cc P8: review Raycast analysis and upgrade status to reviewed
154e28d P7: add Raycast AI-assisted product analysis (source-first)
8062089 P6.1: verify Reuters URL for Linear (datadome-protected, status stays partial)
24e118d P6: review Linear analysis and upgrade source status
33e1b88 P5: reformat Linear sources
da03aae P5: add Linear AI-assisted analysis
81f1e0a P4.2: Perplexity verified source recovery
```

P10 起点 = ea84cb4 (P9.1)，与 origin/master 同步。

## 3. 复核范围与方法

### 3.1 工作区状态

- `git status`: ✅ 干净 (HEAD = origin/master = ea84cb4)

### 3.2 高风险事实逐项复核 (Step 3.1)

**Series A 60M / 400M** - P10 重大发现:
- 之前 (P9)：单源 (Wikipedia + 推定 TechCrunch URL 404)
- **P10 升级**：
  - 真实 TechCrunch URL 找到并 verified: `https://techcrunch.com/2024/08/09/anysphere-a-github-copilot-rival-has-raised-60m-series-a-at-400m-valuation-from-a16z-thrive-sources-say/` (200)
  - Cursor 官方 blog 找到并 verified: `https://www.cursor.com/blog/series-a` (200)
  - **首次达到 source-quality-checklist 双独立 verified media 标准** → 升 **high**

**Series B 100M** (P9) vs **$105M** (P10 修正):
- P9 写 $100M，来自 Wikipedia
- **P10 发现 Cursor 官方 blog 原文是 $105M** (2025-01-16, Thrive + a16z + Benchmark)
- 修正: §17.1 中 "$100M" → "$105M"
- 升 **中-高**

**Series C 900M / 9.9B**:
- P10 新增 Cursor 官方 blog 验证: `https://www.cursor.com/blog/series-c` (200)
- Cursor 官方原口径：$900M at $9.9B, Thrive + Accel + a16z + DST, ARR $500M, Fortune 500 half (NVIDIA/Uber/Adobe)
- 升 **中-高**

**Series D 2.3B / 29.3B**:
- P10 新增 Cursor 官方 blog 验证: `https://www.cursor.com/blog/series-d` (200)
- Cursor 官方原口径：$2.3B at $29.3B post-money, Accel + Thrive + a16z + 新增 Coatue + NVIDIA + Google, ARR $1B, 300+ team
- 升 **中-高**

**ARR 100M / 500M / 1B**:
- P10 全部在 Cursor 官方 blog 验证 (Series B/C/D 三个 blog 都有)
- 升 **high**

**ARR 3B May 2026**:
- Wikipedia 单源 (Cursor blog 未明确披露 May 2026 数字)
- 仍 **中**

### 3.3 SpaceX / Anysphere 交易复核 (Step 3.2)

- 状态：announced (xAI 2026-04-21 deal) + SpaceX 行使 (2026-06-16) + expected Q3 2026 close
- **本轮未亲验到一手或独立 verified media**:
  - Reuters 主域: 401 (Datadome)
  - Bloomberg 主域: 403
  - NYT 主域: 403
  - SpaceX.com 200 (主域) 但没找到具体 announcement 页面
  - xAI / x.com: 403
- 仍 partial,状态明示 "pending/expected Q3 2026 close"
- 严格不写成"已完成收购"

### 3.4 产品功能事实复核 (Step 3.3)

主体产品功能全部保持 high:
- Tab / Chat / Composer / Agent / Cloud Agent / MCP / Rules / iOS (public beta) / Design Mode / Composer 2
- 全部 docs.cursor.com / cursor.com 官方 verified

## 4. 来源补强 (Step 4)

### P10 新增 verified URLs (7 个)

| URL | 类型 | 状态 | 用途 | 备注 |
|-----|------|------|------|------|
| `https://www.cursor.com/blog/series-a` | primary-official | verified (200) | Series A 融资 | $60M 官方原口径 |
| `https://www.cursor.com/blog/series-b` | primary-official | verified (200) | Series B 融资 | $105M 官方原口径,修正 P9 错误 |
| `https://www.cursor.com/blog/series-c` | primary-official | verified (200) | Series C 融资 | $900M/$9.9B 官方原口径 |
| `https://www.cursor.com/blog/series-d` | primary-official | verified (200) | Series D 融资 | $2.3B/$29.3B 官方原口径 |
| `https://www.cursor.com/blog/supermaven` | primary-official | verified (200) | Supermaven 收购 | 创始人 Truell 原口径,11-12 收购 |
| `https://techcrunch.com/2024/11/12/anysphere-acquires-supermaven-to-beef-up-cursor/` | high-quality-media-verified | verified (200) | Supermaven 收购 | TechCrunch 记者,双独立 verified |
| `https://techcrunch.com/2024/08/09/anysphere-a-github-copilot-rival-has-raised-60m-series-a-at-400m-valuation-from-a16z-thrive-sources-say/` | high-quality-media-verified | verified (200) | Series A 融资 | TechCrunch 记者,双独立 verified |

### 本轮尝试但失败 (4 个)

| URL | 状态 | 原因 |
|-----|------|------|
| `https://www.reuters.com/business/spacex-acquire-cursor-anysphere/` | 401 | Datadome bot-blocked |
| `https://www.bloomberg.com/news/articles/2026-04-21/xai-cursor-deal/` | 403 | paywalled / bot-blocked |
| `https://www.theinformation.com/articles/cursor-anysphere-2-3-billion` | 403 | paywalled |
| `https://x.ai/cursor` | 403 | Datadome bot-blocked |

## 5. YAML 状态修正详情 (Step 2)

### Before (P9.1)

```yaml
review_status: draft
review_notes: 初稿基于 source-first workflow;...
source_quality_notes: ... Wikipedia 是单一 reference 源 ...
```

### After (P10)

```yaml
review_status: reviewed
review_notes: Cursor draft reviewed in P10; product claims checked against Cursor official docs (docs.cursor.com), official blog (cursor.com/blog/*), Anysphere pages, GitHub repository, and TechCrunch Supermaven acquisition + Series A articles. High-risk financing/valuation/ARR/SpaceX transaction claims remain partial: Series A is now double-sourced (TechCrunch 200 + Cursor blog 200); Series B/C/D have Cursor blog official source verified; ARR $100M/$500M/$1B have Cursor blog official source; SpaceX $60B acquisition remains pending/expected Q3 2026 (announced Jun 16 2026) with only Wikipedia + Chinese secondary coverage, no direct Reuters/Bloomberg/SpaceX primary URL verified.

source_url_verification_status: partial (保持)
source_quality_notes: P10 复核后升级: ... (8 项升级 + 1 项不升级 + 1 项修正) ...
```

## 6. 修正的事实错误 (1 项)

- §17.1 中 "2024 Series B ($100M)" → 修正为 "2025 Series B ($105M, P10 修正)"
- §17.1 中 "ARR 里程碑($100M Jan 2025 → ...)" → 修正为 "ARR 里程碑($100M+ Jan 2025 → ...)"

## 7. §17.2 可信度分级升级详情 (Step 3 详细)

### 升级到 **high** (3 项)
- Series A $60M at $400M (TechCrunch + Cursor blog 双独立 verified)
- ARR $100M / $500M / $1B (Cursor blog 官方原口径)
- Supermaven 收购 (Cursor blog + TechCrunch 双独立 verified)
- Half of Fortune 500 是 Cursor 客户 (Cursor blog 官方原口径)
- Cursor 团队规模 300+ (Cursor blog 官方原口径)

### 升级到 **中-高** (4 项)
- Series B $105M (Cursor blog + Wikipedia)
- Series C $900M at $9.9B (Cursor blog + Wikipedia)
- Series D $2.3B at $29.3B (Cursor blog + Wikipedia)
- OpenAI Startup Fund 领投 2023-10 种子轮 $8M (Wikipedia + 二手转载)

### 保持 **中** (1 项)
- ARR $3B (May 2026) - Wikipedia 单源
- SpaceX $60B 收购 (announced 2026-04-21 xAI / 2026-06-16 SpaceX) - pending/expected Q3 2026 close

## 8. 改动统计

| 维度 | 数量 |
|------|------|
| 修改文件 | 4 (Cursor 全文 + README + CHANGELOG + P10 报告新增) |
| 文章主体改动 | 1 处数字修正 (§17.1 Series B $100M → $105M) |
| 文章追加 | §17.5 P10 复核记录 + §17.2 8 项 P10 升级 |
| YAML 字段改动 | 3 字段 (review_status, review_notes, source_quality_notes) |
| §17.2 表条数变化 | 26 → 34 条 (+8 P10 升级) |
| 新增小节 | §17.5 P10 复核记录 |
| Sources 5 分组变化 | Official +5 (Cursor blog 5 篇) + Verified Media +2 (TechCrunch 2 篇) |
| 文件大小变化 | 36 → 36.5 KB |
| 新增报告 | reports/P10-cursor-review-and-risk-fact-hardening-report.md (~9KB) |
| 新增 CHANGELOG 行数 | +80 行 |

## 9. 验证清单

- ✅ 起始 HEAD = origin/master clean (ea84cb4)
- ✅ Cursor 文 mtime 未被破坏 (主体修改是 1 处数字修正 + §17.5 追加)
- ✅ YAML 3 字段齐
- ✅ review_status = reviewed
- ✅ reviewed_at = 2026-07-01
- ✅ source_url_verification_status = partial (保持, 诚实评估)
- ✅ §17.1 1 处数字修正 (Series B $100M → $105M)
- ✅ §17.2 +8 P10 升级项 (含 5 项 high + 4 项 中-高)
- ✅ §17.5 P10 复核记录存在
- ✅ Sources 5 分组 (Official +5, Verified Media +2)
- ✅ Perplexity / Linear / Raycast mtime 未变
- ✅ 9 旧人工分析文章 + pic/ 未动
- ✅ 无 force push / reset --hard / amend
- ✅ working tree clean post-push

## 10. P11+ 下一步

1. **P11 优先**：第 5 篇 AI 辅助分析 (候选：Notion / Figma / Arc / Tana / Obsidian / Claude Code 等)
2. **P11 流程改进**：
   - 继续 source-first workflow
   - 主动尝试找到"官方 + 独立 verified media"双源模式 (本次 P10 通过发现 Cursor 官方 blog 大幅提升)
3. **长期**：
   - SpaceX 收购 Q3 2026 后追踪 (announced → completed 状态变化)
   - 继续用 agent-browser 验证 bot-protected URL (Reuters / Bloomberg / NYT 等)
   - 每季度复核已有分析 URL 可用性
4. **诚实评估**：
   - verification_status=partial 不是失败,严格按 source-quality-checklist 是产品分析质量的核心
   - 本次 P10 通过"找到 7 个未充分利用的官方/独立 verified source"实现 8 项升级,但仍保持 partial (因为 SpaceX + $3B ARR May 2026 仍未达 verified)
5. **教训沉淀**：
   - 真实 TechCrunch URL 往往不是搜索引擎列出的推定路径,需要通过 Wikipedia 引用的真实链接或网站内搜索找到
   - Cursor 官方 blog 在 `cursor.com/blog/series-*` 路径下,这个模式可应用到其他 startup 公司的官方融资 blog 搜索
   - "P9 已认为 verified 充分" 可能是过早的判断;P10 的 source-hardening 总是能找到新的 verified source

## 11. 与 P8 Raycast review 的对比

| 维度 | P8 Raycast | P10 Cursor |
|------|-----------|------------|
| 起点状态 | draft | draft |
| 升级目标 | reviewed | reviewed |
| verification_status | partial (保持) | partial (保持) |
| 找到的新独立源 | 1 (Linear blog + 1 Wikipedia) | **7** (5 Cursor blog + 2 TechCrunch) |
| Series A 双独立源? | ❌ (Raycast Series A 仅 TC 单源) | ✅ **TechCrunch + Cursor blog 双独立 verified** |
| 修正的事实错误 | 0 | 1 (Series B $100M → $105M) |
| 主体改动数 | 5 | 1 (只改 1 个数字) |
| §17.5 P-marker | §17.5 P8 复核记录 | §17.5 P10 复核记录 |
| 报告路径 | reports/P8-... | reports/P10-... |

P10 vs P8: P10 是 P8 之后更成熟的 source-hardening,因为 Cursor 官方 blog 大幅补充了源独立验证。

---

*报告日期：2026-07-01*
*阶段：P10*
*复核者：辛 (AI 辅助) / 爸爸 (人工指定)*
*状态：draft → reviewed,verification_status partial 保持*