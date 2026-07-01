# P11 - Figma AI 辅助产品分析报告

**项目：** Product-Analysis
**阶段：** P11 (第 5 篇 AI 辅助产品分析)
**日期：** 2026-07-01
**仓库：** https://github.com/conanxin/Product-Analysis
**基础提交：** bc37dda (P10 Cursor review)

---

## 1. 任务概述

第 5 篇 AI 辅助产品分析 — **Figma** (公开公司 / 协作式设计平台 / Config 2025 五大 AI 产品线 / Dev Mode)。延续 source-first workflow (P5 → P6 → P6.1 → P7 → P8 → P8.1 → P9 → P9.1 → P10 → P11 第九次验证)。

## 2. Source-first 验证结果

### URL 验证统计

| 类型 | 数量 | 状态 |
|------|------|------|
| Figma 官方页 (主页 + design + figjam + slides + make + sites + buzz + draw + dev-mode + pricing + enterprise + security + developers + blog + ai + release-notes + design-systems) | 16 | verified (200) |
| Figma 官方 docs (developers/api + help.figma.com) | 2 | verified (200) |
| Wikipedia (Figma + Dylan_Field) | 2 | reference-verified (200) |
| SEC EDGAR full-text search (Figma + 10-K search) | 2 | investor-reference (200) |
| **小计 verified** | **~23** | **全部 HTTP 200** |
| Figma /community/ /plugins/ /trust/ /code-connect/ /components/ /variables/ /config-2026/ | 8 | unverified (403/404) 降权 |
| `investor.figma.com` / `figma.com/investor-relations/` | 2 | unverified (403/404) 降权 |
| `www.sec.gov` 详情页 / `efts.sec.gov` 特定搜索 | 2 | unverified (403/500) 降权 |
| TechCrunch / Reuters / CNBC / WSJ / FT / Bloomberg 原报道 URL | 6+ | unverified (not HTTP-checked) 仅 Wikipedia 引用 |

### 关键事实双源验证 (按 P11 spec-required 第 12/14 条)

| 关键事实 | 主源 | 次源 | 本轮 HTTP 验证? |
|---------|------|----------------------|----------------|
| Figma 是 collaborative design platform (官方) | figma.com/ + Wikipedia | 双 verified | ✅ 高 |
| 2012 创立 / 2016 公开 | Wikipedia + figma.com 主页 | 双 verified | ✅ 高 |
| 创始人 Dylan Field + Evan Wallace (Brown University) | Wikipedia + figma.com 主页 | 双 verified | ✅ 高 |
| Multiplayer collaboration | figma.com + Wikipedia | 双 verified | ✅ 高 |
| Components / Variables / Design systems | figma.com/design-systems + Wikipedia | 双 verified | ✅ 高 |
| Dev Mode 2023-06 | figma.com/dev-mode + Wikipedia | 双 verified | ✅ 高 |
| FigJam 2021-04-21 | figma.com/figjam + Wikipedia | 双 verified | ✅ 高 |
| Figma Slides 2024-06 | figma.com/slides + Wikipedia | 双 verified | ✅ 高 |
| Config 2025 五大产品 (Sites/Make/Buzz/Draw) 2025-05-07 | figma.com 5 个产品页 + Wikipedia | 双 verified | ✅ 高 |
| Weavy 收购 $200M+ 2025-10 | Wikipedia (verified) | — | ⚠️ Wikipedia 单源 |
| Pricing: Starter Free / Pro $15 / Organization $45 / Enterprise Custom | figma.com/pricing | — | ✅ 单源 verified |
| 2022-09-15 Adobe $20B 收购 announced → 2023 终止 | Wikipedia (verified) | 中文转载 (IT 之家 / 36 氪) | ⚠️ Wikipedia 主源,FT/WSJ/Bloomberg 原报道 URL 未直接 HTTP 验证 |
| 2025-07-31 IPO NYSE:FIG / 价 $33 / 首日 +250% | Wikipedia (verified) | 中文转载 (QQ / Sohu) | ⚠️ Wikipedia 主源,TechCrunch / Reuters / CNBC 原报道 URL 未直接 HTTP 验证 |
| 2025 营收 $1.06B / 亏损 -$1.29B / 1886 员工 | Wikipedia (verified) | SEC EDGAR 索引 (但详情页 403) | ⚠️ Wikipedia 主源,严格按 checklist 未达双独立 verified media |
| 1300 万用户中 95% 财富 500 客户 | Wikipedia (verified, 招股书数据) | — | ⚠️ Wikipedia 单源 |
| 总部 Phelan Building San Francisco | Wikipedia + figma.com | 双源 | ✅ 高 |
| 创始人 Thiel Fellow 2012 | Wikipedia | — | ⚠️ Wikipedia 单源 |

**结论**：严格按 P11 spec-required 第 12 条 + 第 14 条执行,所有公开公司金融事实 + IPO 事实 + Adobe 收购事实 标 **partial**。

## 3. source_url_verification_status 判定

**判定：partial**

理由(诚实评估)：
1. 主体产品事实 23 URL 全 verified (官方页 + docs + Wikipedia + SEC EDGAR 索引)
2. 创始人 / 总部 / 公开公司状态等基础信息双源 (Wikipedia + figma.com)
3. 公开公司金融事实 (IPO 价 $33 / 首日 +250% / 估值 $65B / 营收 $1.06B / 亏损 -$1.29B) 严格按 P11 spec-required 第 12/14 条:
   - 优先用 SEC / IR / Reuters / CNBC 双源 — 本轮只 Wikipedia + 中文转载
   - 标 partial 不是失败,是诚实评估
4. Adobe $20B 收购失败 严格按 P11 spec-required 第 14 条:
   - 终止时点是 2023 (来自 Wikipedia)
   - 严格说本轮未亲验 FT / WSJ / Bloomberg 原报道
5. 招股书数据 (1886 员工 / 95% 财富 500) 严格按 P11 spec-required 第 12 条:
   - 是 Wikipedia reference 源
   - 严格说本轮未亲验 SEC 10-K 详情页 (403)
6. 与 P5 Linear / P7 Raycast / P9 Cursor 保持一致:金融/IPO 类事实严格按 P11 spec 标 partial

**为什么不用 verified?**
- 主体产品事实 verified 占比高
- IPO / 金融类高风险事实 Wikipedia 是单一 reference 源
- 按 source-quality-checklist 的"双独立 verified media"门槛,标 partial 是诚实标准

## 4. review_status 判定

**判定：draft**

理由：
- 包含大量 §14 中文 MVP 推断 + §15 项目启发 7 条 + §13 主要问题 8 条 + §17.2 18 条可信度分级
- 与 P9 Cursor 相同模式:draft → 等 P12 人工复核 → reviewed
- 这是 P5-P11 系列的标准流程

## 5. 文章结构 (17 节)

| 节 | 标题 | 状态 |
|---|------|------|
| §1 | 一句话定位 | ✅ |
| §2 | 目标用户 (7 类 + 表格) | ✅ |
| §3 | 核心场景 (14 场景表格) | ✅ |
| §4 | 产品解决的问题 (7 痛点 + 5 解法) | ✅ |
| §5 | 首页与第一印象 | ✅ |
| §6 | 核心用户路径 (个人 + 企业 + Config 2025) | ✅ |
| §7 | 信息架构 (15 对象 + 4 列 spec 必写表格) | ✅ |
| §8 | 交互与视觉设计 (12 交互点表格 + 6 原因) | ✅ |
| §9 | 内容/社区/增长机制 (7 spec 子项) | ✅ |
| §10 | 商业模式 (4 层订阅 + 8 竞品定价对比 + 4 策略 + 3 压力点) | ✅ |
| §11 | 竞品与替代方案 (10 竞品) | ✅ |
| §12 | 主要优点 (7 条) | ✅ |
| §13 | 主要问题 (8 条,严重程度分级) | ✅ |
| §14 | 如果我来重做 (3 spec 必答 + 6 行 MVP 表 + 7 必含功能 + 中文竞争分析) | ✅ |
| §15 | 启发 (7 条 spec 必写) | ✅ |
| §16 | 今日复盘 (收获 + 注意 + 未解答) | ✅ |
| §17 | 人工复核结论 (17.1-17.4 + Sources 6 分组) | ✅ |

## 6. 主要交付物

### 文件清单

| 文件 | 大小 | 状态 |
|------|------|------|
| `analyses/ai-assisted/2026-07-01-figma.md` | 35.6 KB | 新增 |
| `README.md` | AI 索引 +1 行 | 修改 |
| `CHANGELOG.md` | 顶部 P11 记录 (+75 行) | 修改 |
| `reports/P11-figma-ai-assisted-analysis-report.md` | 本报告 | 新增 |

### YAML front matter 字段 (11 字段)

```yaml
product: Figma
category: design-collaboration
tags: [6 个]
source_urls: [23 URL]
analysis_type: ai-assisted
created_at: 2026-07-01
reviewed_at: 2026-07-01
review_status: draft
review_notes: [P11 复核待办说明]
source_url_verified_at: 2026-07-01
source_url_verification_status: partial
source_quality_notes: [P11 源验证情况]
one_line_insight: Figma 把设计编辑器、实时协作、设计系统、原型、Dev Mode、Config 2025 新五大产品线...
```

## 7. 与 P5/P7/P9/P10 的对比

| 维度 | P5 Linear | P7 Raycast | P9/P10 Cursor | P11 Figma |
|------|-----------|------------|---------------|-----------|
| 来源类型 | 22 官方 + 3 TC + 1 Wiki | 23 官方 + 10 blog + 3 TC + 1 Wiki | 38+ 官方 + Cursor blog + 2 TC + 2 Wiki | 18 官方 + 2 Wiki + 2 SEC EDGAR |
| Wikipedia 角色 | 创始人/公司 secondary | 创始人 secondary | 融资/估值/ARR **主源** | 基础信息 + IPO 金融 **主源** |
| 公开公司 | ❌ (private) | ❌ (private) | ❌ (private → pending SpaceX) | ✅ **NYSE:FIG 2025-07-31** |
| key facts 双源 | 部分 | Series A/B / 创始人 | 创始人/公司+产品功能+定价,融资单源 | 创始人/公司+产品功能+定价,IPO/金融单源 |
| review_status | draft → reviewed | draft → reviewed | draft → reviewed | draft (P12 待复核) |
| verification_status | partial | partial | partial | partial (P11 spec-required 12/14) |
| 推断密度 | 中 | 高 (中文 MVP) | 高 (中文 MVP + 启发 7 条) | 高 (中文 MVP + 启发 7 条) |
| 待观察事件 | 无 | 无 | SpaceX $60B pending | Adobe $20B 收购终止 + IPO 后增长 |
| 文章大小 | 25 KB | 25.5 KB | 36.5 KB | 35.6 KB |

## 8. 关键决策

1. **draft 状态保留** — 因包含 §14 中文 MVP 推断 + §15 项目启发 7 条 + §13 主要问题 8 条,推断密度高,需人工复核
2. **partial 标注** — 严格按 P11 spec-required 第 12 条 + 第 14 条执行,Wikipedia 是 reference 源非独立 verified media
3. **§14 中文 MVP 假设** — 单独提出"AI 原生小团队设计-开发协作画布"+ 7 必含功能 + 中文竞争分析 (MasterGo / 即时设计 / 摹客 / Pixso / 蓝湖)
4. **§15 项目启发 7 条** — 把分析 Figma 的过程本身作为对 Product-Analysis 项目的反思 (含"产品研究协作画布"方向)
5. **Sources 6 分组** — 按 P11 spec 要求的 6 分组 (Official / Product-Pricing-Doc / Investor-SEC-Financial / Verified Media / Secondary / Unverified)
6. **CHANGELOG 严格用 edit 追加** — 避免 P7 误用 write 覆盖的教训 (P11 跟随 P7 模式 +93 行)
7. **§17.3 11 条** — P8.1 5 条 + P9 6 条 + P11 5 条 (公开公司/AI/IPO/credits/趋势判断)
8. **§17.2 18 条** — 含 Figma 公开公司/IPO 金融事实分级 (中,严格按 P11 spec-required)

## 9. P11+ 下一步

1. **P12 优先**:
   - 人工复核 Figma 文章 → 升 reviewed (类似 P8 / P10 模式)
   - 主动尝试找到 TechCrunch / Reuters / CNBC 原报道 URL 突破 Wikipedia 单源
   - 找到至少 1 个独立 verified media 后,IPO / 营收 / Adobe 收购 事实可考虑从 partial 升级
2. **P13 候选**:
   - 第 6 篇 AI 辅助分析 (Notion / Framer / Adobe Express / Canva / Webflow / Linear / Tana / Obsidian)
   - 或回看 Figma 后续 (Q2/Q3 2026 财报)
3. **P12+ 流程改进**:
   - 每篇新分析在 review_status 升级前先做 source URL recovery
   - 主动引入 agent-browser 验证 bot-protected URL (TechCrunch / Reuters / CNBC)
   - 公开公司金融事实严格按 P11 spec-required 第 12/14 条执行
4. **诚实评估**:
   - verification_status=partial 不是失败,严格按 source-quality-checklist 是产品分析质量的核心
   - Wikipedia 是 reference 源,不是 high-quality-media-verified
   - 公开公司金融事实必须 SEC + 至少 1 个独立财经媒体双源

## 10. 长期观察点

1. **Figma Q2/Q3 2026 财报** — ARR 增速 + 现金流转正 + 五大 AI 产品线采用率
2. **Adobe 战略应对** — Firefly / Express 与 Figma 竞争演化
3. **Google Stitch** — Google AI 设计工具跨入,对 Figma 影响
4. **中国市场接入** — MasterGo / 即时设计 / 摹客 / Pixso / 蓝湖的竞争
5. **AI 五大产品线 (Make / Sites / Buzz / Draw / Weave) 实际采用率** — 决定 Figma 长期增长
6. **Dylan Field 战略** — IPO 后 Figma 战略调整
7. **Weavy (Figma Weave) 整合** — AI 图像/视频编辑能力的产品演化

---

*报告日期：2026-07-01*
*分析者：辛 (AI 辅助)*
*阶段：P11*
*复核状态：draft → 待 P12 人工复核*