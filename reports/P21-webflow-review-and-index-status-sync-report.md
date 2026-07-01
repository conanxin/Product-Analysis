# P21 - Webflow Review and Index Status Sync Report

**项目：** Product-Analysis
**阶段：** P21 (Webflow 人工复核与索引状态同步)
**日期：** 2026-07-01
**仓库：** https://github.com/conanxin/Product-Analysis
**基础提交：** 302a061 (P20 Webflow draft)

---

## 1. 任务概述

对 P20 新增的 Webflow AI 辅助分析进行人工复核，将 review_status 从 draft 升为 reviewed，同步所有索引文件。

**P21 重点：**
- 修正 Wikipedia reference vs direct verified media 边界
- 收购事实和收购金额拆开验证
- 新增 4 个 verified 来源 (3 Webflow blog posts + 1 W3Techs)
- 尝试但未成功验证 4 个底层媒体 URL (404/403/429)
- §14 中文 MVP 推断标注 [判断] / [推断]

## 2. 提交链路

```
git log --oneline -10:
302a061 P20: add Webflow AI-assisted product analysis
1136646 P19.1: fix Canva index status drift
8db1079 P19: review Canva analysis and sync index status
0e0a2fa P18: add Canva AI-assisted product analysis
3c0f385 P17: review Notion analysis and sync index status
c682263 P16: add Notion AI-assisted product analysis
c4bb23d P15: enrich analyses/index.yml and analyses/README.md with real article metadata
ba56d48 P15: add AI analysis index and quality dashboard
74fda7a P14: review Framer analysis and normalize YAML/Sources format
7b72404 P13: add Framer AI-assisted product analysis
```

**任务链:** P20 Webflow draft → P21 Webflow review (本轮) → P22 候选 (第 10 篇 AI 辅助分析)

## 3. Source-Hardening 执行

### 3.1 新增 Verified 来源 (4 个)

| URL | type | status | used_for | note |
|-----|------|--------|----------|------|
| `webflow.com/blog/webflow-acquires-gsap` | primary-official-blog | verified (200) | GSAP 收购事实 | 标题: "Webflow acquires the GreenSock business, the company behind GSAP" |
| `webflow.com/blog/webflow-acquires-vidoso` | primary-official-blog | verified (200) | Vidoso.ai 收购事实 | 标题: "Webflow acquires Vidoso.ai to deploy AI agents that work within your brand" |
| `webflow.com/blog/ai-site-builder` | primary-official-blog | verified (200) | AI site builder 功能 | 标题: "Build sites that scale with Webflow's AI site builder" |
| `w3techs.com/technologies/details/cm-webflow` | high-quality-data | verified (200) | Webflow usage statistics | W3Techs 独立数据源 |

### 3.2 尝试但未成功的媒体 URL (4 个)

| URL | HTTP 状态 | 备注 |
|-----|----------|------|
| `techcrunch.com/2026/03/12/webflow-buys-vidoso-ai` | 404 | Wikipedia reference cites TechCrunch；Vidoso.ai 收购事实由 Webflow official blog verified 200 支撑 |
| `axios.com/2024/10/15/webflow-acquires-gsap` | 403 | Wikipedia reference cites Axios；GSAP 收购事实由 Webflow official blog verified 200 支撑 |
| `venturebeat.com/2021/01/13/webflow-140m-2-1b-valuation` | 429 | Wikipedia reference cites VentureBeat；Series B 融资事实仍 partial |
| `forbes.com/webflow-series-a-72m` | 404 | Wikipedia reference cites Forbes；Series A 融资事实仍 partial |

### 3.3 URL Verification 统计

| 分类 | P20 | P21 |
|------|-----|-----|
| Official / Primary (webflow.com/*) | 39 | 39 |
| Official Blog Posts (webflow.com/blog/*) | 0 | 3 (+3) |
| High-Quality Data (w3techs.com) | 0 | 1 (+1) |
| Reference / Encyclopedia (Wikipedia) | 1 | 1 |
| **Total Verified** | **40** | **44 (+4)** |
| Unverified / Needs Follow-up | 13 | 13 (4 个从 "未尝试" 变为 "P21 尝试 404/403/429") |

## 4. review_status + source_url_verification_status

### Before / After

| 字段 | BEFORE (P20) | AFTER (P21) |
|------|-------------|-------------|
| review_status | draft | reviewed |
| reviewed_at | null | 2026-07-01 |
| review_notes | null | P21 人工复核完成... |
| source_url_verification_status | partial | partial (保持) |
| source_urls count | 40 | 44 (+4) |

### partial 保持原因

1. **主体产品机制 → verified** (42 个 Webflow 官方 URL + W3Techs = 43 verified)
2. **融资/估值 → partial**: Wikipedia reference cites Forbes / VentureBeat，底层媒体 URL P21 尝试验证 404/429
3. **收购金额 → 低**: 均未披露 / undisclosed
4. **员工数 / Y Combinator → 中**: Wikipedia reference 源

## 5. 收购事实和收购金额拆开验证

| 收购 | 事实可信度 | 金额 | 备注 |
|------|----------|------|------|
| GSAP (2024-10) | **中-高** | **未披露 / undisclosed** | Webflow official blog verified 200 + Wikipedia reference cites Axios (403) |
| Vidoso.ai (2026-03) | **中-高** | **未披露 / undisclosed** | Webflow official blog verified 200 + Wikipedia reference cites TechCrunch (404) |

## 6. Wikipedia Reference vs Direct Verified Media 边界修正

### P20 问题 (已修正)

P20 文章中写了 "Forbes / VentureBeat / Axios / TechCrunch verified 引用"，但实际只是 Wikipedia 引用底层媒体，P21 修正为：
- "Wikipedia reference cites Forbes / VentureBeat / Axios / TechCrunch"
- "底层媒体原文 URL P21 尝试验证但 404/403/429，未直接 HTTP verified"
- Wikipedia 是 reference source，不是 high-quality-media-verified

### 修正位置

- §1 一句话定位: Wikipedia 引用修正
- source_quality_notes: 全面重写
- §17.2 可信度分级: Series A/B 降为低-中
- §17.3 后续改进: 新增 Wikipedia reference 教训
- §17.4 Sources: 新增 P21 尝试结果
- Sources 区: Unverified 更新

## 7. 推测性声明标注

### §14 中文 MVP 推断

P20 已标注部分 [判断]，P21 补充标注：
- "核心判断" → "[推断]"
- "中文网站建设痛点" → "[推断]"
- "应该先做完整 Webflow 吗" → "[判断]"
- "MVP 建议" → "[判断/推断]"
- "核心功能" → "[推断]"
- "如何避免成为'又一个模板建站工具'" → "[判断]"

## 8. Pricing 最终措辞

所有 pricing 来自 webflow.com/pricing (verified 200)，无第三方引用：
- Starter: Free
- Basic: $15/mo (年付)
- Premium: $25/mo (年付)
- Business: $29/mo
- Ecommerce Standard: $29/mo
- Ecommerce Plus: $74/mo
- Workspace / Enterprise: Custom

## 9. 融资 / 估值最终措辞

- Series A $72M: "Wikipedia reference cites Forbes；Forbes 原文 URL P21 尝试验证 404" → 低-中
- Series B $140M / $2.1B valuation: "Wikipedia reference cites VentureBeat 2021-01-13；VentureBeat 原文 URL P21 尝试验证 429" → 低-中
- 1.2% top 10M websites: "W3Techs 页面 P21 verified 200" → 中-高 (P21 升级)

## 10. 索引状态同步

### README.md

| 字段 | BEFORE (P20) | AFTER (P21) |
|------|-------------|-------------|
| Webflow 行 | draft / partial | reviewed / partial |
| AI 辅助分析 | 9 (8 reviewed + 1 draft) | 9 (9 reviewed) |
| reviewed | 8 | 9 |
| draft | 1 | 0 |
| P21 计划 | — | [x] |
| 最后更新 | P20 | P21 |

### analyses/README.md

| 字段 | BEFORE (P20) | AFTER (P21) |
|------|-------------|-------------|
| Webflow 行 | draft / partial | reviewed / partial |
| AI 辅助分析 | 9 (8 reviewed + 1 draft) | 9 (全部 reviewed) |
| reviewed | 8 | 9 |
| draft | 1 | 0 |
| P 报告累计 | 13 | 14 |

### analyses/index.yml

| 字段 | BEFORE (P20) | AFTER (P21) |
|------|-------------|-------------|
| Webflow review_status | draft | reviewed |
| Webflow reviewed_at | null | 2026-07-01 |
| Webflow quality_notes.reason | P20 source-hardening... | P21 复核后... |
| summary.reviewed | 8 | 9 |
| summary.draft | 1 | 0 |
| summary.p_reports_total | 13 | 14 |
| yaml.safe_load | ✅ | ✅ |

## 11. 验证清单

- ✅ 起始 HEAD = origin/master clean (302a061 = P20)
- ✅ YAML review_status = reviewed
- ✅ YAML reviewed_at = 2026-07-01
- ✅ YAML review_notes 存在且语义正确
- ✅ YAML source_urls 44 个纯 URL 字符串 (P20 的 40 + P21 新增 4)
- ✅ YAML source_url_verification_status = partial
- ✅ §17.1 已从 draft 改为人工复核完成状态
- ✅ §17.2 可信度分级已同步更新 (收购事实/收购金额拆开; Series A/B 降为低-中)
- ✅ §17.3 包含 Wikipedia reference vs direct verified media 教训
- ✅ §17.4 Sources 新增 4 个 P21 verified 来源
- ✅ Sources 区新增 High-Quality Data Sources 分组
- ✅ 正文不得写 Webflow 是公开公司或已 IPO
- ✅ 正文已修正 Wikipedia reference 和媒体 direct verified 的边界
- ✅ §14 中文 MVP 推断标注 [判断] / [推断]
- ✅ README AI 索引中 Webflow 状态已从 draft 改为 reviewed
- ✅ README 当前质量状态中 reviewed=9、draft=0
- ✅ analyses/README.md 中 Webflow 状态已从 draft 改为 reviewed
- ✅ analyses/README.md 当前质量状态中 reviewed=9、draft=0
- ✅ analyses/index.yml 中 Webflow review_status=reviewed
- ✅ analyses/index.yml summary reviewed=9、draft=0
- ✅ analyses/index.yml 可被 yaml.safe_load 解析
- ✅ CHANGELOG.md 顶部有 P21 记录，且没有覆盖历史记录
- ✅ reports/P21-webflow-review-and-index-status-sync-report.md 存在
- ✅ Perplexity / Linear / Raycast / Cursor / Figma / Framer / Notion / Canva 文章未改
- ✅ 旧人工分析文章未改
- ✅ pic/ 目录未动
- ✅ git diff 无无关文件
- ✅ working tree clean post-push

## 12. Remaining Issues

1. **Series A $72M / Series B $140M / $2.1B valuation** 仍 partial — 底层媒体 URL 404/429，可能需要 archive.org / cached versions
2. **收购金额** 均未披露 / undisclosed — 官方 blog + Wikipedia 均未披露
3. **501-1000 employees** 来自 Wikipedia reference，可能过时
4. **AI site builder 真实可用性 / 采用率** 没有独立数据
5. **中文 MVP 推断** 完全是产品假设，无市场调研支撑

## 13. P21 Lessons

1. **Wikipedia reference 里的媒体引用不能直接写成媒体 verified** — P20 错误已修正
2. **Webflow official blog 是收购事实的 best source** — 比 Wikipedia reference 更直接
3. **收购事实和收购金额要拆开** — 事实可以中-高，金额可能低
4. **W3Techs 是独立数据源** — 不依赖 Wikipedia reference
5. **底层媒体 URL 可能 404/403/429** — 不当 verified，标 "P21 尝试 404/403/429"
6. **4 文件同步更新** — P19.1 教训持续落地

---

*报告日期：2026-07-01*
*分析者：辛 (AI 辅助)*
*阶段：P21*
*复核状态：reviewed | partial*
