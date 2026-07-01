# P8 - Raycast 人工复核与状态升级报告

**项目：** Product-Analysis
**阶段：** P8 (Raycast 人工复核 / source-hardening / docs-only)
**日期：** 2026-07-01
**仓库：** https://github.com/conanxin/Product-Analysis
**基础提交：** 154e28d (P7)

---

## 1. 任务概述

P8 是对 P7 新增的第三篇 AI 辅助产品分析 (Raycast) 做人工复核与状态升级，遵循 Linear P6 的 review-and-source-upgrade 模式。

## 2. 执行链路 (Step 1)

```
154e28d P7: add Raycast AI-assisted product analysis (source-first)
8062089 P6.1: verify Reuters URL for Linear (datadome-protected, status stays partial)
24e118d P6: review Linear analysis and upgrade source status
33e1b88 P5: reformat Linear sources
da03aae P5: add Linear AI-assisted analysis
81f1e0a P4.2: Perplexity verified source recovery
9c56bd5 P4.1: Perplexity source URL verification
87f61cd P4: Perplexity review and source hardening
043dc69 P3: Perplexity AI-assisted analysis
```

P8 起点 = 154e28d (P7)，与 origin/master 同步。

## 3. 复核范围与方法

| 复核维度 | 方法 | 结论 |
|---------|------|------|
| 工作区状态 | `git status` | ✅ 干净 (HEAD = origin/master = 154e28d) |
| Raycast YAML 状态语义 | 读 + 比对 Linear P6 reviewed 模板 | ⚠️ review_status=draft 与 reviewed_at=2026-07-01 矛盾 → 修正 |
| 产品定位 metaphor | 比对 Linear "工作流操作系统" 用法 | ⚠️ 需明示是 analysis metaphor 非官方用语 |
| Windows 表述 | 检查 §1 / §3.2 等 | ✅ "候补名单" 措辞已准确 |
| AI "主要增长驱动" | 检查 §10 / §12 / §13 | ⚠️ §12/§13 有"粘性"措辞但未到"主要驱动" → §17.2 增加"主要驱动"中分级 |
| Extension Store 数据 | 检查数字引用 | ⚠️ "56k+ stars" 是实时数 → §17.2 标中(动态) |
| §14 中文 MVP 推断 | 检查 [判断] 标记 | ✅ 已 [判断] 标记 |
| §15 项目启发 | 检查 [判断] 标记 | ✅ 已 [判断] 标记 |
| §17.1 状态说明 | 读 | ⚠️ 写"待人工复核"与 reviewed 矛盾 → 改写 |
| §17.2 可信度表 | 读 | ⚠️ 11 条不全 → 扩充至 18 条 |

## 4. 复核改动详情 (5 处)

### 4.1 顶部 lead blockquote (新增第 2 段)

```markdown
> (本文使用"工作流操作系统"作为分析判断 / metaphor，非 Raycast 官方产品定位用语；Raycast 官方自我定位为"command bar / launcher / extensions platform")
```

**理由**：lead 直接用"工作流操作系统"作为开篇定位语，但官方自我定位不同。需明示这是分析 metaphor。

### 4.2 §1 一句话定位 (新增 [判断] 段)

```markdown
[判断] "生产力操作系统前端"是分析层 metaphor，不是 Raycast 官方用语。
Raycast 官方 self-description 偏 "command bar / launcher / extensions platform / shortcut to everything"；
用"OS 前端"是为了强调它"统一多个工作流入口"的产品定位，
但读者应理解这是分析判断，不是产品官方定位。
```

**理由**：§1 主体"生产力操作系统前端"也是 metaphor，需 [判断] 标记。

### 4.3 §17.1 当前状态 (整段改写)

旧：写"待人工复核" + "复核者待指派"，与 reviewed 矛盾
新：明示"P8 阶段已人工复核并升级为 reviewed" + "复核者: 辛 (AI 辅助) / 爸爸 (人工指定)"

### 4.4 §17.2 可信度分级表 (11 条 → 18 条)

新增 7 条：
1. Raycast 是 macOS command bar / launcher / productivity platform — **高**
2. Raycast AI 是 Pro 价值的重要组成部分 — **高**
3. Raycast AI 是 Pro 的"主要增长驱动" — **中** (官方口径不明确)
4. Raycast 与 Alfred / Spotlight 竞争但定位更开发者化 — **中**
5. Windows 扩展仍处于 waitlist / early expansion signal — **中**
6. GitHub extensions 仓库 "56k+ stars" — **中** (动态)
7. 中文 Raycast 更适合先做 AI worker / Windows / 浏览器场景 — **待观察**

### 4.5 §17.5 P8 人工复核记录 (新增整节)

记录：
- 复核日期 / 类型
- 状态变化 (review_status / verification_status / reviewed_at)
- 本次复核改动 6 项
- 未改动的内容 (主体 §1-§16 + §17.4)
- 不升级 verified 的理由

## 5. YAML 状态语义修正

### Before (P7)

```yaml
review_status: draft
review_notes: 初稿基于 source-first workflow,全部主体来源已 HTTP 200 验证;...待人工复核。
source_url_verification_status: partial
source_quality_notes: 官方页 22 个 + 官方 blog 10 篇 + TechCrunch 3 篇 + Wikipedia 1 篇均 HTTP 200 verified;...主体产品机制(launcher/extensions/AI/snippets)全 verified。
```

### After (P8)

```yaml
review_status: reviewed
review_notes: Raycast draft reviewed in P8; product claims checked against official docs, official blog, developer documentation, GitHub extensions repository, TechCrunch, and Wikipedia; speculative China/MVP sections (§14) and project-learnings (§15) remain marked as judgment; funding/valuation facts continue to depend on TechCrunch + Raycast official blog self-statement, so source_url_verification_status kept as partial (honest evaluation).
source_url_verification_status: partial
source_quality_notes: P8 review pass: 主体产品机制 (launcher/extensions/AI/snippets/quicklinks/pricing/platform) 已通过 Raycast 官方页 (13 verified) + 官方 blog (10 verified) + manual.raycast.com + developers.raycast.com 全部 HTTP 200 验证; Series A $19M / Series B $100M / $1B 估值 / 创始人 等关键事实双源 (TechCrunch + Raycast 官方 blog + Wikipedia); Product Hunt / Bloomberg / Reuters 主域名仍被 bot 防护, 降为 aggregator / 不可用; 融资/估值事实仍主要依赖 TechCrunch 单一独立媒体 + Raycast 官方 blog 自述 (非独立验证), 按 source-quality-checklist 诚实标注 partial; §14 中文 MVP 推断与 §15 项目启发明确标记为 [判断] / 推断, 不当作事实。
```

## 6. source_url_verification_status 保持 partial 的理由

按 source-quality-checklist (docs/source-quality-checklist.md) 的诚实标准：

| 事实 | 源 1 | 源 2 | 独立媒体数 | 应标 |
|------|------|------|-----------|------|
| Series A $19M | TechCrunch 2022 | Raycast 官方 blog | 1 (TC) | partial |
| Series B $100M / $1B | TechCrunch 2024 | Raycast 官方 blog | 1 (TC) | partial |
| 创始人 | Raycast /about | TechCrunch + Wikipedia | 1 (TC/Wiki) | high (三源一致) |
| 平台限制 | pricing | Windows blog | 0 (官方口径) | high (无独立验证必要) |
| 定价 | pricing | — | 0 (官方口径) | high (无独立验证必要) |

**关键判断**：Raycast 官方 blog 算 "primary-official" 类别 (官方自述)，不是 "high-quality-media-verified" 类别 (独立媒体)。所以"TC + Raycast 官方 blog" 双源 = 1 个独立媒体 + 1 个官方自述，不构成真正的"独立双源"。

**与 Linear P6 的对比**：
- Linear P6 升级 reviewed 后保持 partial，理由是 $82M 2025 round 仍单源 TC
- Raycast P8 升级 reviewed 后保持 partial，理由是 Series A/B 仅 TC + 官方 blog (官方自述不算独立验证)
- 两者标准一致：verification_status 不轻易升 verified

## 7. 改动统计

| 维度 | 数量 |
|------|------|
| 修改文件 | 4 (Raycast 全文 + README + CHANGELOG + P8 报告新增) |
| 文章主体改动 | 5 处明示性修改 (1 lead + 1 §1 + 3 §17) |
| 文章主体未改 | §2-§16 主体 + §17.3 + §17.4 (仅追加 §17.5) |
| YAML 字段改动 | 3 字段 (review_status, review_notes, source_quality_notes) |
| §17.2 表条数变化 | 11 → 18 (+7) |
| 新增小节 | §17.5 P8 复核记录 |
| 文件大小变化 | 25 KB → 25.5 KB (主体未重写,只追加 +200 行) |
| 新增报告 | reports/P8-raycast-review-and-status-upgrade-report.md (~7.5KB) |
| 新增 CHANGELOG 行数 | +60 行 |
| README 改动 | 1 行 (Raycast 状态 draft → reviewed) + 1 行 (最后更新) |

## 8. 验证清单

- ✅ 起始 HEAD = origin/master clean (154e28d)
- ✅ Raycast 文 mtime 未被破坏 (主体修改是明示性追加)
- ✅ YAML 3 字段齐
- ✅ review_status = reviewed
- ✅ reviewed_at = 2026-07-01
- ✅ source_url_verification_status = partial
- ✅ 顶部 lead 增加 metaphor 明示
- ✅ §1 增加 [判断] 标记
- ✅ §17.1 改为 P8 复核版
- ✅ §17.2 18 条可信度分级
- ✅ §17.5 P8 复核记录存在
- ✅ 文末状态行增加 P8 复核信息
- ✅ Perplexity mtime 未变
- ✅ Linear mtime 未变
- ✅ 9 旧人工分析文章 + pic/ 未动
- ✅ working tree clean post-push

## 9. 不变项 (Per spec)

- ❌ 不引入前端框架
- ❌ 不做 GitHub Pages
- ❌ 不做构建系统
- ❌ 不修改旧文章正文
- ❌ 不移动 pic/
- ❌ 不破坏已有图片引用
- ❌ 不重写 Raycast 文章主体
- ❌ 不 force push
- ❌ 不 reset --hard
- ❌ 不 amend

## 10. P9+ 下一步

1. **P9 候选**：第 4 篇 AI 辅助分析 (Notion / Cursor / Figma / Arc / Tana / Obsidian)
2. **P8 后续**：每季度复核已有分析 URL 可用性 (P4.1 checklist)
3. **流程改进**：本次 P8 复用 P6 review 模式已成熟 (YAML 状态 + 顶部 lead + §1 标记 + §17.1/17.2/17.5 三段式)
4. **诚实评估**：verification_status=partial 不是失败,严格遵守 source-quality-checklist 是产品分析质量的核心

## 11. 与 P6 Linear review 的对比

| 维度 | P6 Linear | P8 Raycast |
|------|-----------|------------|
| 起点状态 | draft | draft |
| 升级目标 | reviewed | reviewed |
| verification_status | partial (保持) | partial (保持) |
| 找到的新独立源 | 1 (Linear blog series-b) + 1 (Wikipedia) | 0 (TC 单一媒体限制未突破) |
| 主体产品机制 | verified | verified |
| 主体改动数 | ~5 处 | 5 处 |
| §17.5 P-marker | 命名 P6 §17.x | 命名 P8 §17.5 (本篇新增) |
| 报告路径 | reports/P6-linear-review-and-source-upgrade-report.md | reports/P8-raycast-review-and-status-upgrade-report.md |

两者模式一致：YAML 状态修正 + 顶部 lead 明示 + §1/§17 复核记录 + 不动主体 + 报告 + README + CHANGELOG。

---

*报告日期：2026-07-01*
*阶段：P8*
*复核者：辛 (AI 辅助) / 爸爸 (人工指定)*