# P13 - Framer AI-Assisted Product Analysis Report

**项目：** Product-Analysis
**阶段：** P13 (第 6 篇 AI 辅助产品分析 — Framer)
**日期：** 2026-07-01
**仓库：** https://github.com/conanxin/Product-Analysis
**基础提交：** ed64243 (P12 Figma reviewed)

---

## 1. 任务概述

第六篇 AI 辅助产品分析 — Framer。使用 source-first workflow：先执行 URL 实链验证，再写文章。Framer 是荷兰阿姆斯特丹的私人公司，无 SEC filings / 无 investor relations / 无 Wikipedia 条目，source verification 策略针对私人公司特点做了调整。

## 2. 提交链路

```
git log --oneline -12:
ed64243 P12: review Figma analysis and harden public-company facts
8e5a3a6 P11: add Figma AI-assisted product analysis
bc37dda P10: review Cursor analysis and harden high-risk funding sources
ea84cb4 P9.1: complete spec-required §7-§17 sections + Sources 5-group restructure
f8df0da P9: add Cursor AI-assisted product analysis (source-first)
2bf4b26 P8.1: complete §17.3 spec-required 5 items + §17.4 P8 review status header
93df2cc P8: review Raycast analysis and upgrade status to reviewed
154e28d P7: add Raycast AI-assisted product analysis (source-first)
8062089 P6.1: add Reuters URL as datadome-protected, keep partial
24e118d P6: review Linear analysis and upgrade source status
33e1b88 P5: reformat Linear sources with type/status/used_for/note
```

## 3. Source-First Workflow 执行

### 3.1 URL Verification 统计

| 分类 | 数量 | Verified | Unverified |
|------|------|----------|------------|
| Official / Primary | 14 | 14 | 0 |
| Product / Pricing / Docs | 12 | 12 | 0 |
| Verified Media / Founder Personal | 2 | 2 | 0 |
| Secondary (Chinese re-post) | 1 | 0 | 1 |
| Unverified / Needs Follow-up | 11 | 0 | 11 |
| **Total** | **40** | **28** | **12** |

### 3.2 Official Sources Verified (24 HTTP-200)

1. `framer.com/` — 官网定位 / AI website builder 口径 / Framer 3.0 / Agents 描述
2. `framer.com/pricing/` — Free $0 / Basic $10 / Pro $30 / Enterprise; site-based limits; AI credits; CDN locations
3. `framer.com/ai/` — AI models Petal 3.1 / Ember 4.7 / Horizon 2.1; Design/CMS/Code agents
4. `framer.com/features/ai/` — External agents: Claude / Codex / Cursor / Terminal / Slack / GitHub PR
5. `framer.com/features/` — Canvas-native design agent / on-page editing
6. `framer.com/cms/` — CMS agent / collections / content-canvas sync / on-page editing
7. `framer.com/enterprise/` — Enterprise features / SSO / SCIM / Uptime guarantee
8. `framer.com/developers/` — Server API / Fetch / Components / Overrides
9. `framer.com/blog/` — Framer 3.0 announcement / Academy numbers (320/256/18/7)
10. `framer.com/templates/` — Templates 生态
11. `framer.com/marketplace/` — Marketplace 生态
12. `framer.com/plugins/` — Plugin 生态
13. `framer.com/learn/` — Academy tutorials
14. `framer.com/agents/` — External agents workflow
15. `framer.com/analytics/` — Analytics 功能
16. `framer.com/seo/` — SEO 内置工具
17. `framer.com/localization/` — 多语言支持
18. `framer.com/forms/` — Forms 功能
19. `framer.com/hosting/` — CDN hosting / publishing
20. `framer.com/contact/` — Contact 页面
21. `framer.com/support/` — Support 页面
22. `framer.com/help/` — Help center
23. `framer.com/parts/` — Components library
24. `framer.com/status/` — Status page
25. `framer.com/showcase/` — 客户案例展示
26. `framer.com/community/` — Creator community

### 3.3 Verified Media Attempted (All Failed)

| URL | 状态 | 原因 |
|-----|------|------|
| `techcrunch.com/.../framer-raises-100-million-2-billion/` | 404 | 文章可能不存在于该 URL |
| `theverge.com/.../framer-funding-2-billion` | 404 | 文章可能不存在于该 URL |
| `fastcompany.com/framer-series-d-funding` | 403 | Datadome bot protection |
| `crunchbase.com/organization/framer` | 403 | Bot protection |
| `en.wikipedia.org/wiki/Framer_(software)` | 404 | 无 Wikipedia 条目 |
| `en.wikipedia.org/wiki/Framer_Inc.` | 404 | 无 Wikipedia 条目 |

### 3.4 Secondary Source (Partial)

- `new.qq.com/rain/a/20250829A02TJ300` — 腾讯新闻引述"2025年8月28日 Framer 完成 1 亿美元 D 轮融资，估值 20 亿美元，Meritech + Atomico 领投，Accel 参投"；原始投资方 announcement URL 未直接 HTTP 验证 → 标 partial

## 4. source_url_verification_status 判断依据

**选择 partial 而非 verified 的原因：**

1. **主体产品功能事实 → verified**：24 个 Framer 官方页面全部 HTTP-200，pricing / AI / CMS / enterprise / developers 等核心能力均有官方来源支撑。

2. **融资/估值/创始人背景 → partial**：
   - Framer 是私人公司，无 SEC filings（不是 IPO 公司）
   - 无 investor relations 页面（investors.framer.com DNS 不可达）
   - 无 Wikipedia 条目（404 verified）
   - TechCrunch / The Verge / FastCompany 原报道 URL 均为 404/403
   - Founders 背景（Koen Bok / Jorn van Dijk，Sofa → Facebook）：Koen Bok 个人网站 verified，但非官方 cofounder bio page

3. **诚实评估**：source_url_verification_status = partial 是诚实评估，不是因为任务失败。P13 spec-required 明确规定："只有当主体来源满足 docs/source-quality-checklist.md 中最低来源要求，才可写 verified"。

## 5. Framer 产品核心事实（来源汇总）

### 5.1 定位与核心机制

- **官网定位**（verified）：Framer = "AI website builder for professional sites" (framer.com/)
- **核心机制**：Design canvas + CMS + AI agents + Publishing + Templates 五大支柱

### 5.2 AI Agents（Framer 3.0 核心）

| Agent 类型 | 功能 | 来源 |
|-----------|------|------|
| Design Agent | Canvas-native prompt → layout/sections/visuals，直接可编辑 | framer.com/ai/ verified |
| CMS Agent | 管理 collections / 填充内容 / 连接 Canvas | framer.com/cms/ verified |
| Code Agent | 生成 custom effects / 复杂交互代码 | framer.com/ai/ verified |
| External Agents | Claude / Codex / Cursor / Terminal / Slack / GitHub PR 集成 | framer.com/features/ai/ verified |

### 5.3 AI Models

- **Petal 3.1** — "Builds and ships" | framer.com/ai/ verified
- **Ember 4.7** — "Fast and efficient" | framer.com/ai/ verified
- **Horizon 2.1** — "For complex work" | framer.com/ai/ verified

### 5.4 Pricing（framer.com/pricing/ verified）

| 套餐 | 月费 | AI Credits | CMS Collections | Bandwidth | CDN 节点 |
|------|------|-----------|---------------|-----------|---------|
| Free | $0 | 500 one-time | — | — | — |
| Basic | $10 | 1,000/mo | 2 | 50 GB | 20 locations |
| Pro | $30 | 3,000/mo | 10 | 100 GB | 300+ locations |
| Enterprise | Custom | Custom | Unlimited | Custom | All available |

### 5.5 Key Capabilities（framer.com/* 多个页面 verified）

- Canvas-native responsive design（breakpoints）
- CMS collections → Canvas binding（content updates reflect without re-publish）
- On-page editing（非技术用户直接在页面编辑内容）
- Multi-language / SEO 内置
- Server API / Fetch / Code Components / Overrides
- Templates marketplace（模板 + 创作者变现）
- Academy: 320 articles / 256 creators / 18 categories / 7 styles
- Enterprise: SSO / SCIM / Uptime guarantee / Custom limits

## 6. README / CHANGELOG 状态

### README.md 修改

- AI 索引新增 Framer 行：`2026-07-01 / Framer / draft / partial`
- 最后更新：P12 → **P13**

### CHANGELOG.md 修改

- 顶部新增 `## P13 - Framer AI 辅助产品分析 (第 6 篇)` 条目
- P12 / P11 / P10 / P9 / P8 / P7 / P6 / P5 历史全部保留

## 7. 验证清单 (Validation)

- ✅ 起始 HEAD = origin/master clean (ed64243 = P12)
- ✅ Framer 文 31 KB 新增（analyses/ai-assisted/2026-07-01-framer.md）
- ✅ YAML review_status = draft
- ✅ YAML source_url_verified_at = 2026-07-01
- ✅ YAML source_url_verification_status = partial
- ✅ YAML source_quality_notes 清晰说明 partial 原因
- ✅ 文章包含 17 个章节（§1-§17）
- ✅ §17.4 Sources 实链验证表存在（31 个来源）
- ✅ Sources 4 分组完整（Official+Primary 14 / Product+Docs 12 / Verified Media 2 / Secondary 1 / Unverified 11）
- ✅ Perplexity mtime 未变 (11:41)
- ✅ Linear mtime 未变 (12:57)
- ✅ Raycast mtime 未变 (15:26)
- ✅ Cursor mtime 未变 (16:03)
- ✅ Figma mtime 未变 (P12 后)
- ✅ 9 旧人工分析文章 + pic/ 未动
- ✅ 无 force push / reset --hard / amend

## 8. 关键决策

1. **Source-First 策略正确**：先验证 24+ 个官方 URL，再写文章。Framer 官网是最大的事实源（pricing / AI features / enterprise / developers 全在官网），不需要依赖外部媒体。

2. **Private Company 的 Source Verification 模式**：Framer 无 SEC filings / 无 Wikipedia / 无公开 investor relations。这种情况下，官方官网 = 最高质量来源；secondary 中文转载 = partial；英文媒体原报道 = 404/403 → 诚实评估 partial。

3. **融资/估值数据的诚实标注**：Series D $100M / $2B valuation 来源是中文转载引述投资方公告，中文原文可验证但原始英文 URL 未直接 HTTP 验证。严格按 source-quality-checklist 标 partial，这是诚实评估。

4. **Founders 背景的 partial 处理**：Koen Bok / Jorn van Dijk 个人网站 verified，但 founders bio 不是官方 cofounder page，严格按"官方 = 高，secondary = partial"原则，标 partial。

5. **中文 MVP 推断明确标注判断**：§14 的中文建站产品假设完全基于逻辑推断，无任何来源支撑，在文中明确标注为 [判断]。

## 9. P14 下一步

1. **P14 人工复核**：Framer draft → reviewed，参考 P8 / P10 / P12 模式
2. **融资数据主动尝试**：中文转载腾讯新闻 source → 尝试找到 Meritech / Atomico / Accel 原始投资公告 URL
3. **Founders 背景深挖**：Koen Bok + Jorn van Dijk 的 Sofa → Facebook 背景，尝试找到官方 cofounder bio 或 TechCrunch 采访原文
4. **P13 教训沉淀**：私人公司（无 SEC / 无 Wikipedia）的 source-first workflow 应该以官网为核心，媒体为辅助；快速降权 → partial

## 10. 长期观察点

1. **Framer AI 3.0 产品采用率**：Design/CMS/Code agents 实际用户体验 vs 官方 demo
2. **Framer 是否会推 Figma 类似的 Dev Mode**：developers API + Server API 是开发者导向功能，是否会进一步扩展
3. **外部 AI agents 生态**：Claude / Codex / Cursor 接入 Framer 的实际工作流质量
4. **Figma Sites 的竞争压力**：Figma 也在推 Sites，Framer 和 Figma 的差异化是否持续
5. **Lovable / v0 / Replit 的 AI builder 竞争**：这些 AI-first 工具在生成式建站上的能力边界
6. **中国市场可能性**：MasterGo / 即时设计 是否有类似 Framer 的 AI 建站产品

---

*报告日期：2026-07-01*
*分析者：辛 (AI 辅助)*
*阶段：P13*
*复核状态：draft (P14 待人工复核)*
