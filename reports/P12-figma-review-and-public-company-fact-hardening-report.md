# P12 - Figma 人工复核与公开公司事实加固报告

**项目：** Product-Analysis
**阶段：** P12 (第 5 篇 AI 辅助产品分析 — Figma 复核)
**日期：** 2026-07-01
**仓库：** https://github.com/conanxin/Product-Analysis
**基础提交：** 8e5a3a6 (P11 Figma AI 辅助分析)

---

## 1. 任务概述

对第五篇 AI 辅助产品分析 — Figma 进行人工复核与公开公司高风险事实加固。
延续 P8 (Raycast) / P10 (Cursor) 的人工复核 + source-hardening 模式 (P12 是 P8 / P10 之后的第三次该模式应用)。

## 2. 提交链路

```
git log --oneline -10:
8e5a3a6 P11: add Figma AI-assisted product analysis (source-first)
bc37dda P10: review Cursor analysis and harden high-risk funding sources
ea84cb4 P9.1: complete spec-required §7-§17 sections + Sources group restructure
f8df0da P9: add Cursor AI-assisted product analysis (source-first)
2bf4b26 P8.1: complete §17.3 spec-required 5 items + §17.4 P8 review status header
93df2cc P8: review Raycast analysis and upgrade status to reviewed
154e28d P7: add Raycast AI-assisted product analysis (source-first)
8062089 P6.1: add Reuters URL as datadome-protected, keep partial
24e118d P6: review Linear analysis and upgrade source status
33e1b88 P5: reformat Linear sources with type/status/used_for/note
```

**任务链:** P11 Figma draft → P12 Figma review (本轮) → P13 候选 (Notion / Framer / Adobe Express / Canva / Webflow / Tana / Obsidian / Arc)

## 3. review_status 与 source_url_verification_status 修订

### 3.1 修改前 vs 修改后

| 维度 | 修改前 (P11) | 修改后 (P12) |
|------|-------------|-------------|
| review_status | draft | **reviewed** |
| reviewed_at | 2026-07-01 | 2026-07-01 (不变) |
| source_url_verification_status | partial | partial (不变) |
| source_url_verified_at | 2026-07-01 | 2026-07-01 (不变) |
| review_notes | 初稿,P11 source-first workflow 描述 | **P12 人工复核完整描述 + 6 新源 + 2 重大事实修订** |
| source_quality_notes | P11 23 URL + 1,886 员工 + 4 款 Config 2025 | **P12 30 URL + 1,600+ 员工 + 5 款 Config 2025 + Config 2026 五项 + Weave 官方** |

### 3.2 review_status 升级原因

- ✅ **主体产品功能事实全部与 verified Figma 官方源一致** (Config 2025 五款 / Config 2026 五项 / Weave 收购 / Dev Mode / FigJam / Slides / Pricing)
- ✅ **P12 source-hardening +7 verified URLs**, 大量中-高风险事实升级 high
- ⚠️ **个人判断部分**(§14 中文 MVP / §15 项目启发 7 条 / §13 主要问题 8 条)保留为 [判断], 不影响事实部分
- ✅ **诚实评估 IPO/Adobe 终止金融事实**: Reuters Datadome 401 + Wikipedia 单源 → 标 partial, 不为状态好看而升级

### 3.3 source_url_verification_status 保持 partial 原因

- **Reuters/Bloomberg/CNBC 原报道 URL 全部 Datadome-protected (401/403)**, 与 P9 Cursor 模式一致
- IPO 定价 $33 / 首日 +250% / 估值 $65B / 2025 营收 $1.06B / Adobe $20B 终止 严格按 source-quality-checklist 未达"双独立 verified media"门槛
- **诚实评估**, 不是失败

## 4. P12 source-hardening 新增 URL (7 verified)

| URL | type | status | used_for | note |
|-----|------|--------|----------|------|
| `figma.com/newsroom/` | primary-official newsroom | verified (200) | §17.2 员工/用户/营收分布 | **Q1 2025 Figma at a glance** |
| `figma.com/blog/config-2025-recap/` | primary-official blog | verified (200) | §3 §17.2 Config 2025 五款 | Dylan Field 2025-05-07 |
| `figma.com/blog/config-2026-recap/` | primary-official blog | verified (200) | §3 §17.2 Config 2026 五项 | 官方 2026-06-24 |
| `figma.com/blog/connecting-figma-and-weave/` | primary-official blog | verified (200) | §3 §17.2 Weave 收购 | Itay Schiff 2026-06-24 |
| `config.figma.com/` | primary-official site | verified (200) | §9 §17.2 Config conference | Config conference 官方主页 |
| `weave.figma.com/` | primary-official product | verified (200) | §3 §17.2 Weave 产品 | Weave 产品独立站 |
| `efts.sec.gov/LATEST/search-index?q=%22Figma%22&forms=S-1` | investor-reference | verified (200) | §17.2 S-1 搜索 | P11 之前 500 错误, P12 重试成功 |

## 5. P12 source-verification 主动尝试 + 失败 (4 URLs)

| URL | 类型 | 状态 |
|-----|------|------|
| `reuters.com/business/figma-jumps-ai-push-boosts-software-design-spending-2026-02-19/` | Reuters Datadome | 401 |
| `reuters.com/business/figma-shares-jump-ai-push/` | Reuters Datadome | 401 |
| `reuters.com/markets/figma-ipo-2025-07-31` | Reuters Datadome | 401 |
| `fastcompany.com/91329127/figma-config-2025-dylan-field` | Fast Company | 403 |

**结论**: Reuters/Bloomberg/CNBC/Fast Company 原报道 URL 全部 Datadome-protected 或 bot-blocked;
**与 P9 Cursor Reuters 401 + P5 Linear Reuters Datadome 模式一致**, 是公开公司金融类事实的标准处境;
按 P12 spec-required 第 17 条: 快速降权 → 明确标 partial, 不浪费 30 分钟重复验证。

## 6. 重大事实修订 (4 项)

### 6.1 Config 2025 产品数量 4 → 5

**P11 误漏**: P11 文 §3 + §17.2 写 "Sites/Make/Buzz/Draw" 4 款
**P12 修正**: figma.com/blog/config-2025-recap/ 官方原文明确 5 款 — Make / Sites / Grid / Draw / Buzz (P11 漏 Grid)
**P12 修订位置**: §3 表格 + §17.2 第 6 条 + §17.1 状态描述
**修订理由**: 官方 blog 是 announcement source, 本身就是事实源

### 6.2 员工数 1886 → 1,600+

**P11 误信**: P11 文 §17.2 标 "员工 1886", 来源 Wikipedia
**P12 修正**: figma.com/newsroom/ Q1 2025 官方原文 "Figma has over 1,600 employees globally"
**P12 修订位置**: §17.1 状态描述 + §17.2 第 13 条 + §16 第 2 条 (今日复盘)
**修订理由**: Wikipedia 招股书数据可能引用旧版;严格按 source-quality-checklist 应优先官方 newsroom/blog;**Wikipedia 与官方 newsroom 冲突时, 优先官方**

### 6.3 Figma Weave 收购 date 2025-10 → 2026-06-24 Config 公告

**P11 误传**: P11 文 §3 + §17.2 写 "Weavy 收购 2025-10", 来源 Wikipedia
**P12 修正**: figma.com/blog/connecting-figma-and-weave/ 官方 announcement 2026-06-24 (Config 2026)
**P12 修订位置**: §3 表格 (Weave 行) + §17.2 第 8 条
**修订理由**: 官方 blog 原文 "Figma has acquired Weavy" 是 announcement source
**未升级**: 收购具体日期与金额 ($200M+ 估值) Wikipedia 单源, 仍 partial

### 6.4 新增 Config 2026 五项 canvas 升级

**P11 遗漏**: P11 文完全未提 Config 2026
**P12 修正**: figma.com/blog/config-2026-recap/ + figma.com/newsroom/ + weave.figma.com 全部 200 verified:
- **Code Layers** (Figma Design 内探索代码方向)
- **Figma Motion** (画布内 timeline 动画)
- **Shaders** (Canvas 内着色器 / 动态视觉效果)
- **Generative Plugins** (Plugin 生态 + AI 生成)
- **Weave tools in Figma** (Weave → Figma integration)
**P12 修订位置**: §3 表格 (新增 5 行) + §17.1 + §17.2 + §16 第 3 条

## 7. 高风险事实最终措辞 (Wording)

### 7.1 IPO / NYSE:FIG (P12 最终)

> "Figma IPO / public company status (NYSE: FIG 2025-07-31)" — **可信度: 中**
> 依据: Wikipedia (verified);Figma 官方未找到 IPO blog;Reuters/CNBC 原报道 URL Datadome 401;
> 未升级 high,因为 Figma 官方原文 + 双独立 verified media 双源未达成。

### 7.2 Adobe $20B 收购终止 (P12 最终)

> "Adobe $20B 收购失败 (2022 announced → 2023 terminated)" — **可信度: 中**
> 依据: Wikipedia (verified);Figma 官方未找到 Adobe 终止 blog;FT/WSJ/NYT 原报道 URL 未 HTTP 验证;
> 与 P11 一致,未升级。

### 7.3 AI monetization / AI credits (P12 最终)

> "Figma AI products 是新增长方向" — **可信度: 高 (升级)**
> 依据: figma.com/blog/config-2025-recap/ (Make/Sites/Grid/Draw/Buzz) + figma.com 5 个产品页 + Wikipedia;
> Config 2025 五款 + Config 2026 五项都是官方 announcement,本身是事实源。

> "AI credit 定价模式 / AI 营收占比" — **保持 partial**
> 依据: figma.com/pricing/ 提及 AI credits 但未详细;Q1 2026 earnings call transcript 未公开;
> 严格按 P12 spec-required 第 21 条, 必须 figma.com/pricing + Q-财报 + earnings call 三件套, 暂只 1/3。

## 8. CLAIM_CONFIDENCE_CHANGES (可信度变化)

### UPGRADED → 高

| 事实 | 修改前 | 修改后 | 升级依据 |
|------|--------|--------|----------|
| Config 2025 五款产品 (Make/Sites/Grid/Draw/Buzz) | 中 (P11 4 款 + Wikipedia) | **高** | figma.com/blog/config-2025-recap/ 官方 announcement |
| Config 2026 五项 canvas 升级 | 未提 (P11 遗漏) | **高 (新增)** | figma.com/blog/config-2026-recap/ + connecting-figma-and-weave/ |
| Figma 收购 Weavy → Figma Weave | 中 (Wikipedia) | **高** | figma.com/blog/connecting-figma-and-weave/ 官方 announcement |
| 员工数 1,600+ as of Q1 2025 | 中 (P11 1,886 Wikipedia) | **高** | figma.com/newsroom/ 官方原文 |
| 月活 2/3 非设计师 + 85% 非美国 + 50%+ 营收非美国 | 未提 (P11 遗漏) | **高 (新增)** | figma.com/newsroom/ 官方原文 |
| Config conference 多年增长节点 | 中 | **高** | config.figma.com + 多个 Config blog 双源 |

### UNCHANGED → 中 (诚实评估)

| 事实 | 状态 | 原因 |
|------|------|------|
| Figma IPO / NYSE:FIG 2025-07-31 | 中 | Reuters Datadome 401;Figma 无 IPO blog |
| IPO 定价 $33 / 首日 +250% / 估值 $65B | 中 | Reuters Datadome 401;中文转载为 secondary |
| S-1 提交 (2025-04-15) | 中 (新增) | 中文转载 (sohu/网易);Figma 无官方 S-1 blog |
| Adobe $20B 收购失败 | 中 | FT/WSJ/NYT 原报道 URL 未 HTTP 验证;Figma 无 Adobe blog |
| 2025 营收 $1.06B / 亏损 -$1.29B | 中 | 招股书数据;Reuters/CNBC 原报道 URL 未 HTTP 验证 |
| 1300 万用户 / 95% Fortune 500 | 中 | Wikipedia 招股书数据;Figma 官方未独立 verify |
| Weavy 收购金额 $200M+ | 中 | Wikipedia 单源 |

### DEPRECATED (P12 弃用)

| 事实 | P11 标 | P12 弃用 | 弃用依据 |
|------|--------|---------|----------|
| 员工数 1,886 | 中 (Wikipedia) | **弃用** | figma.com/newsroom/ 官方 1,600+ as of Q1 2025 优先 |

## 9. README / CHANGELOG 状态

### README.md 修改

- AI 索引 Figma 行: `状态 draft | partial` → **`状态 reviewed | partial`**
- 最后更新: P11 → **P12 (人工复核 + source-hardening)**

### CHANGELOG.md 修改

- 顶部新增 `## P12 - Figma 人工复核与公开公司事实加固` 条目 (~110 行)
- P11 条目保留未动
- 历史 P10/P9/P8/P7/P6/P5 全部保留

## 10. 验证清单 (Validation)

- ✅ 起始 HEAD = origin/master clean (8e5a3a6 = P11)
- ✅ Figma 文 49.8 → **59.4 KB** (+9.6 KB source-hardening)
- ✅ analyses/ai-assisted/2026-07-01-figma.md 存在
- ✅ YAML review_status = **reviewed**
- ✅ YAML reviewed_at = 2026-07-01
- ✅ YAML review_notes = **P12 复核完整版** (明示 source-hardening 范围)
- ✅ source_url_verification_status = partial (原因清晰)
- ✅ §3 表格新增 Grid / Config 2026 五项
- ✅ §17.1 改写为 P12 复核版 (明示 source-hardening 增量)
- ✅ §17.2 18 → **24 条** 可信度分级
- ✅ §17.3 11 → **16 条** (P12 spec-required 5 条)
- ✅ §17.4 Sources 实链验证表 新增 **7 verified URL** + 4 unverified URL 主动尝试
- ✅ Sources 6 分组 同步更新 (Official +6 / Investor-SEC +1 verified + 4 unverified)
- ✅ Perplexity mtime 未变 (11:41)
- ✅ Linear mtime 未变 (12:57)
- ✅ Raycast mtime 未变 (15:26)
- ✅ Cursor mtime 未变 (16:03)
- ✅ Figma mtime 改 (P12 source-hardening 必然)
- ✅ 9 旧人工分析文章 + pic/ 未动
- ✅ 无 force push / reset --hard / amend

## 11. 关键决策 (P12 Lessons)

### 11.1 决策模式

1. **review_status 升级 reviewed (非 draft)** — 主体产品事实全部与 verified 官方源一致, 主动 source-hardening +7 verified URL, 大量事实升级 high;**诚实评估 IPO/Adobe 终止金融事实 partial**
2. **不重写主体 §1-§16** — P12 遵循 P8/P10 模式, 只做局部修订 (lead + §3 + §17);P11 主体 §1-§16 描述准确, 不重写
3. **Figma Newsroom 优先于 Wikipedia** — Wikipedia 招股书数据可能与官方不一致, 优先官方原文
4. **官方 blog = announcement source = 高可信度** — Config blog 本身就是 announcement source, 不需要 Reuters/TechCrunch 独立确认
5. **Reuters Datadome 401 快速降权** — 与 P9 Cursor / P5 Linear 一致, 快速标 partial, 不浪费 30 分钟

### 11.2 P12 spec-required 5 条沉淀 (已写入 §17.3 第 17-21 条)

17. 公开公司事实要优先使用 SEC / IR / Reuters / CNBC — Datadome 401 快速降权
18. 官方 newsroom / blog 是 IPO 之外的事实金矿 — newsroom + Config blog 全部 200 verified
19. Wikipedia 招股书数据 vs 官方 newsroom 优先用官方 — 员工数 P11 1886 vs P12 Newsroom 1,600+ 冲突
20. Config / 产品发布会事实 = 公司级官方 announcement — 官方 blog 本身就是事实源
21. AI monetization / AI credits 是 partial 但不能高 — 必须 pricing + 财报 + earnings call 三件套

### 11.3 P12 通用教训 (跨产品分析沉淀)

1. **公开公司 / IPO 公司的事实金矿**: figma.com/newsroom + figma.com/blog/config-*-recap + figma.com/blog/connecting-* 远比 Reuters/CNBC 更易 verified
2. **Wikipedia 招股书数据不可信作为唯一源** — 1886 vs 1,600+ 冲突证明 Wikipedia 数据可能有滞后或不一致
3. **官方 announcement (blog) = 事实源** — 不需要二手媒体独立 confirm; 官方 blog 本身就是 announcement source
4. **Reuters Datadome 401 是公开公司金融事实标准处境** — 快速降权 → partial, 不浪费时间
5. **AI monetization 是新公开公司 partial 标准原因** — AI credit 定价 + AI ARR 是公开公司核心财务, 严格按 source-quality-checklist 通常 partial

## 12. P13 下一步

1. **P12 同会话 P13 不建议** — 本轮 Figma P12 source-hardening 已经做了充分 work, P13 应在下一会话启动
2. **P13 候选**: 第 6 篇 AI 辅助分析 — **Notion / Framer / Adobe Express / Canva / Webflow / Tana / Obsidian / Arc / Claude Code**
3. **优先选**: Notion (与 Figma 同属 "AI-native productivity canvas" 品类, 增长趋势明显) 或 Framer (与 Figma 设计 + AI 矩阵重叠)
4. **避免**: Adobe Express (与 Figma 竞争, 数据敏感) / Canva (海外数据不友好, 与 P7 Raycast 模式不同)
5. **优先**: 公开公司类 (有 newsroom/IR) > 私人公司类 (只能用 Wikipedia + 媒体)

## 13. 长期观察点

1. **Figma Q1 / Q2 / Q3 2026 财报** (等 figma.com/newsroom 或 investor.figma.com 解封)
2. **Figma AI 五大产品线采用率** (Make/Sites/Grid/Draw/Buzz 用户数)
3. **Adobe Firefly / Express 战略应对** (Adobe 收购失败后)
4. **Google Stitch 跨入 AI 设计** (Google 跨入, 对 Figma 影响)
5. **中国市场接入策略** (MasterGo / 即时设计 / 摹客 / Pixso / 蓝湖 竞争)
6. **Dylan Field 在 IPO 后的战略** (Config 2026 Weave 收购是大动作)
7. **§14 中文 MVP 推断的现实可行性** (MasterGo / 即时设计 是否已占领"AI 原生小团队"市场)

---

*报告日期：2026-07-01*
*分析者：辛 (AI 辅助)*
*阶段：P12*
*复核状态：reviewed (P12 人工复核完成)*