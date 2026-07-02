# Product Analysis / 产品分析档案

## 项目定位

这是一个从早期人工产品观察发展而来的 **AI 辅助产品分析档案库**。第一阶段已完成 13 篇 reviewed AI 产品分析，覆盖 AI 搜索、编程、设计、建站、知识工作台、云端开发、local-first 知识库和 agentic meeting workflow 等方向。项目采用 **source-first** 工作流：每篇分析保留 YAML metadata、来源验证、`review_status` 和 `source_url_verification_status`。

当前质量状态：**13 篇 AI 辅助分析 · 全部 reviewed · source URL 验证状态全部 partial**。`partial` 不是失败，而是严格 source-first 标准下的诚实状态——主体产品机制通常可由官方源 verified，但融资 / 估值 / ARR / 用户数 / 客户数等高风险事实需要 ≥ 2 个独立高质量媒体才能 verified，在私人公司为主的状态下诚实地说"主体 verified 高风险 partial"是正确状态机结果。

> "因为想要做一些东西，但是不知道如何下手。最近想清楚了，可以先快速学习一下原型的制作。"——早期动机

**Phase 1 状态：** 已完成第一阶段发布收口。当前版本可作为公开产品研究作品集阅读；建议从 [Release Notes](docs/phase-1-release-notes.md)、[Product Map Navigation](docs/product-map-navigation.md) 和 [Visual Product Map](docs/visual-product-map.md) 开始。如果 GitHub Pages 尚未启用，请以 README / Release Notes 为主；Pages workflow 已准备好。

---

## 快速入口

- [Phase 1 Release Notes](docs/phase-1-release-notes.md) — 第一阶段发布说明、范围、质量状态和已知限制
- [GitHub Pages Showcase](https://conanxin.github.io/Product-Analysis/) — 静态展示页，适合公开阅读（HTML + CSS + 原生 JS + JSON，无框架 / 无构建系统）
- [AI Product Analysis Phase 1 Synthesis](docs/ai-product-analysis-phase-1-synthesis.md) — 13 篇综合、14 条 AI 产品设计规律、source-first 方法论
- [Visual Product Map](docs/visual-product-map.md) — Mermaid 产品图谱 + ASCII fallback
- [Product Map Navigation](docs/product-map-navigation.md) — 按类型、问题、阅读路径导航 13 篇 AI 产品分析
- [AI 辅助分析索引](analyses/README.md) — 13 篇产品分析的目录、状态、阅读路径
- [机器可读索引](analyses/index.yml) — 程序可解析的 YAML 索引（含 reading_paths）
- [Source-first 质量标准](docs/review-status-guide.md) — `review_status` / `source_url_verification_status` 状态机
- [索引一致性校验](docs/index-sync-validation.md) — validator 工作原理

## 项目目标

1. **训练产品观察能力** — 通过持续分析，建立对产品设计的敏感度
2. **总结优秀产品的设计机制** — 信息架构、交互设计、社区机制、内容组织方式
3. **建立可复用的产品分析框架** — 从旧框架（特点/问题/设想）升级为更完整的结构
4. **让 AI 分析结果结构化沉淀** — 模板驱动，目录规范，可持续追加

---

## 当前内容索引

| # | 产品 | 文件 | 类型 | 关键词 | 核心观察 | 后续可复盘方向 |
|---|------|------|------|--------|----------|----------------|
| 1 | Product Hunt | `1.Product-Hunt.md` | 人工 | 产品发现、投票、评论 | 每日榜单机制通过投票和评论组织新产品发现 | 投票机制设计、评论区引导、冷启动策略 |
| 2 | 700bike | `2.700bike.md` | 人工 | 垂直资讯、社区、内容聚合 | 传统资讯网站做垂直化内容，聚合高端骑行用户 | 内容质量控制、线下线上联动 |
| 3 | The Synopsis | `3.The-Synopsis.md` | 人工 | 内容精选、信息过载 | 单页面新闻精选，极简设计解决信息焦虑 | 内容筛选标准、极简产品设计 |
| 4 | Hackster.io | `4.Hackster-io.md` | 人工 | 硬件社区、开源、项目展示 | 硬件骇客社区通过标签/平台分类组织450+项目 | 项目质量筛选、Wiki式内容组织 |
| 5 | Making Society | `5.making-society.md` | 人工 | 开源硬件、博客、内容分类 | 个人博客以开源硬件为主题，内容积累但关联性弱 | 内容关联性设计、个人媒体变现 |
| 6 | Open Library | `6.open-library.md` | 人工 | 数字图书馆、电子书、知识开源 | Internet Archive项目，免费借阅电子书 | 知识公益模式、中文数字图书馆 |
| 7 | Daniel Nordness | `7.Daniel-Nordness.md` | 人工 | 个人网站、静态网站、Jekyll | 静态个人网站设计，Archive内容分类待改进 | 静态网站架构、内容分类体系 |
| 8 | Hack Design | `8.HackDesign.md` | 人工 | 设计教育、课程、内容组织 | 50课设计课程，博客+目录形式，内容覆盖全面 | 课程产品设计、中文化可能性 |
| 9 | OpenROV | `9.OpenROV.md` | 人工 | 开源硬件、机器人、社区生态 | 开源水下机器人，文档+社区+电商完整体系 | 开源硬件商业化、文档即产品 |

---

## 核心主题总结

这 9 篇文章虽然产品类型各异，但折射出几个贯穿始终的主题：

| 主题 | 说明 |
|------|------|
| **产品发现机制** | Product Hunt 的投票排名、The Synopsis 的编辑精选、Hackster 的标签筛选 |
| **内容筛选与质量控制** | 如何从海量内容中选出优质内容？如何让用户信任这个精选过程？ |
| **垂直社区** | 700bike（骑行）、Hackster（硬件骇客）、OpenROV（深海探索者）——小众用户的大能量 |
| **知识组织** | Open Library 的图书元数据、Hack Design 的课程体系、Hackster 的项目 Wiki |
| **开源硬件生态** | Making Society、Hackster、OpenROV — 从爱好者博客到商业化硬件的不同路径 |
| **设计教育** | Hack Design 模式——互联网产品做课程，与传统设计教育的差异 |
| **中文化与本土化机会** | 几乎每篇都有人提到"做一个中文版"——这是真实的本土化需求还是惯性思维？ |

---

## 目录结构

```
Product-Analysis/
├── README.md                      # 本文件，项目总索引
├── CHANGELOG.md                   # 变更记录
├── docs/                          # 方法论文档
│   ├── product-analysis-framework.md    # 产品分析框架
│   └── ai-assisted-analysis-workflow.md # AI 辅助分析工作流
├── templates/                     # 标准化模板
│   ├── product-analysis-template.md     # 文章标准模板（含 YAML front matter）
│   └── ai-product-analysis-prompt.md    # AI 分析提示词模板
├── analyses/                      # AI 辅助分析结果
│   └── ai-assisted/
│       ├── README.md              # AI 分析区说明
│       └── 2026-07-01-perplexity.md    # 第1篇 AI 辅助分析
├── reports/                       # 每轮任务报告
├── [1-9]*.md                      # 旧人工分析（legacy manual analysis）
└── pic/                           # 旧文章图片（勿移动）
```

## AI 辅助分析索引

| 日期 | 产品 | 文件 | 类型 | 关键词 | 核心观察 | 状态 | 来源状态 |
|------|------|------|------|--------|----------|------|----------|
| 2026-07-01 | Perplexity | `analyses/ai-assisted/2026-07-01-perplexity.md` | AI 辅助 | AI 搜索、答案引擎、引用、研究流程 | 将搜索结果页重构为带来源、可追问的答案流 | reviewed | partial |
| 2026-07-01 | Linear | `analyses/ai-assisted/2026-07-01-linear.md` | AI 辅助 | issue tracking、project management、product development、B2B SaaS、collaboration | 将 issue tracking 从任务管理重构为高节奏产品研发工作流 | reviewed | partial |
| 2026-07-01 | Raycast | `analyses/ai-assisted/2026-07-01-raycast.md` | AI 辅助 | productivity、launcher、keyboard-driven、developer-tools、extensions-platform、ai-product | 把命令面板从单点工具重构为可扩展的开发者工作流操作系统 | reviewed | partial |
| 2026-07-01 | Cursor | `analyses/ai-assisted/2026-07-01-cursor.md` | AI 辅助 | ai-coding、developer-tools、ide、agentic-workflow、productivity、llm-product | 把代码编辑器重构为 AI 协作的 agentic coding IDE,实现 Tab/Chat/Composer/Agent/Cloud Agent 统一工作流 | reviewed | partial |
| 2026-07-01 | Figma | `analyses/ai-assisted/2026-07-01-figma.md` | AI 辅助 | design-tools、collaboration、design-systems、dev-mode、ai-design、b2b-saas | 将设计工具从本地文件软件重构为多人协作、设计系统和开发交付基础设施 | reviewed | partial |
| 2026-07-01 | Framer | `analyses/ai-assisted/2026-07-01-framer.md` | AI 辅助 | website-builder、design-tools、ai-website-builder、cms、no-code、b2b-saas | 将设计画布、CMS、发布和 AI agent 工作流结合为 AI 建站平台 | reviewed | partial |
| 2026-07-01 | Notion | `analyses/ai-assisted/2026-07-01-notion.md` | AI 辅助 | productivity、workspace、docs、database、knowledge-management、ai-workspace | 将文档、数据库、知识库、项目管理、日历、邮件和 AI agent 能力整合为可组合的信息工作台 | reviewed | partial |
| 2026-07-01 | Canva | `analyses/ai-assisted/2026-07-01-canva.md` | AI 辅助 | design-tools、ai-design、templates、visual-suite、creator-tools、b2b-saas | 将模板、视觉编辑器、品牌资产、企业协作和 AI 生成能力整合为大众化内容生产平台 | reviewed | partial |
| 2026-07-01 | Webflow | `analyses/ai-assisted/2026-07-01-webflow.md` | AI 辅助 | website-builder、visual-development、no-code、cms、ai-website-builder、b2b-saas | 将视觉设计、CMS、托管、SEO/AEO、优化和 AI 建站能力整合为可视化 Web 生产系统 | reviewed | partial |
| 2026-07-01 | Replit | `analyses/ai-assisted/2026-07-01-replit.md` | AI 辅助 | ai-coding、cloud-ide、agentic-workflow、app-builder、deployment、b2b-saas | 将浏览器 IDE、云端运行环境、部署和 AI Agent 结合为从想法到上线的云端应用工作台 | reviewed | partial |
| 2026-07-01 | Coda | `analyses/ai-assisted/2026-07-01-coda.md` | AI 辅助 | productivity、docs、database、workflow、automation、ai-productivity | 将文档、表格、公式、按钮和自动化组合为可操作的 doc-as-app 工作台 | reviewed | partial |
| 2026-07-01 | Obsidian | `analyses/ai-assisted/2026-07-01-obsidian.md` | AI 辅助 | local-first、markdown、note-taking、personal-knowledge-base、bidirectional-links、plugin-ecosystem | 将本地 Markdown 文件与双向链接、graph view 和插件生态结合，把笔记从"记录工具"重构为"个人知识操作系统" | reviewed | partial |
| 2026-07-01 | Tana | `analyses/ai-assisted/2026-07-01-tana.md` | AI 辅助 | note-taking、knowledge-management、outliner、supertags、ai-agents、meeting-workflow、knowledge-graph、agentic-platform | Tana 把节点式大纲、Supertags、知识图谱、语音/会议输入和 AI agents 结合起来，将笔记从"记录信息"推进到"在上下文中组织、提取并执行工作"的 agentic 知识工作台；当前 tana.inc 已转向"agentic meeting platform"，原 outliner 单独保留为 Tana Outliner | reviewed | partial |

---

- `根目录旧文章` = legacy manual analysis，保留原貌，仅在顶部增加 metadata
- `analyses/ai-assisted/` = 新 AI 分析文章
- `templates/` = 标准化模板
- `docs/` = 方法论文档

---

## 阶段性综合报告

- [AI Product Analysis Phase 1 Synthesis](docs/ai-product-analysis-phase-1-synthesis.md)
  - 汇总第一阶段 13 篇 AI 产品分析（Perplexity / Linear / Raycast / Cursor / Figma / Framer / Notion / Canva / Webflow / Replit / Coda / Obsidian / Tana）；
  - 提炼产品谱系、6 层类型分层、4 张横向对照矩阵、14 条 AI 产品设计规律、source-first 方法论；
  - 建议下一阶段先做公开展示、导航整理和产品地图，而不是继续无限新增产品。
- [Visual Product Map](docs/visual-product-map.md)
  - Mermaid 图谱 + ASCII fallback 可视化 13 篇 AI 产品之间的关系；
  - 包含产品总览图、Tool → Agent 演化图、Cloud vs Local 象限图、Document/Database/Graph/Agent 矩阵、Design-to-Publish、AI Coding/App Builder、Knowledge Workspace、Source-first workflow 等。
- [Product Map Navigation](docs/product-map-navigation.md)
  - 用于按类型、问题和阅读路线阅读 13 篇 AI 产品分析；
  - 6 条推荐阅读路径（基础路线 / 设计到发布 / 知识工作台 / 工具到 Agent / 产品研究方法 / AI 矩阵路线）；
  - 8 个横向对照研究问题；
  - 第二阶段路线图（P33-P35）。

---

## 如何新增一篇 AI 产品分析

1. **选择产品** — 选择一个你想深入了解的产品
2. **收集材料** — 官网链接、截图、产品简介、用户评价、竞品信息、商业模式资料、个人初步观察
3. **生成分析** — 使用 `templates/ai-product-analysis-prompt.md` 提示词，让 AI 分析产品
4. **整理成文** — 按 `templates/product-analysis-template.md` 的结构输出 Markdown
5. **放置文件** — 存入 `analyses/ai-assisted/YYYY-MM-DD-product-name.md`
6. **回填索引** — 在本文"当前内容索引"表格中补充一条记录，同时更新 [analyses/index.yml](analyses/index.yml) 与 [analyses/README.md](analyses/README.md)

---

## 如何校验索引一致性

```bash
python3 scripts/verify_ai_analysis_index.py
```

**说明：**
- 该脚本会检查 AI 分析文章 YAML、analyses/index.yml、README.md、analyses/README.md 是否一致
- 新增文章或人工复核后必须运行
- 脚本退出码：0 = PASS, 1 = FAIL
- 失败时输出具体错误列表
- 详细说明见 [docs/index-sync-validation.md](docs/index-sync-validation.md)

**检查项：** YAML front matter / duplicate key / 必备字段 / source_urls 纯 URL / index.yml 一致性 / README 质量状态 / 产品行状态 / summary count。

**GitHub Actions CI：** 本仓库已接入 GitHub Actions：`.github/workflows/ai-analysis-index-check.yml`，每次 push / PR 会自动运行该校验。本地仍建议在提交前运行。

---

## 当前质量状态

> 更完整的 AI 分析索引与质量状态见：[analyses/README.md](analyses/README.md) 与 [analyses/index.yml](analyses/index.yml)

| 类型 | 数量 | 状态 |
|------|---:|------|
| 旧人工分析 (legacy) | 9 | legacy-note（根目录） |
| 旧文今日复盘 | 1 | Product Hunt (P2) reviewed |
| AI 辅助分析 | 13 | 13 reviewed + 0 draft |
| - reviewed | 13 | 人工复核完成 |
| - draft | 0 | — |
| - verified | 0 | 严格标准下未达成 |
| - partial | 13 | 主体产品功能 verified；高风险事实 partial |

**说明**：partial 是严格质量标准下的合理结果，不是失败。详细评判标准见 [docs/review-status-guide.md](docs/review-status-guide.md)。

## 下一步计划

- [ ] 为旧文章补充"今日复盘"章节（用新框架重新审视旧观察）
- [ ] 增加更多 AI 产品分析案例
- [x] 建立 analyses/README.md + analyses/index.yml 产品数据库
- [x] 建立 docs/review-status-guide.md 质量评判指南
- [x] P16: 新增 Notion AI 辅助分析 (第 7 篇, draft | partial)
- [x] P17: Notion 人工复核 → reviewed (P17 source-hardening +3 verified: introducing-notion-ai / releases / Wikipedia)
- [x] P18: 新增 Canva AI 辅助分析 (第 8 篇, draft | partial;canva.com 30+ URL 403 Datadome;Wikipedia 二手 + Fortune 2025-08-22 + The Verge 2024 verified)
- [x] P19: Canva 人工复核 → reviewed (P19 复验证状态;canva.com 仍 403 Datadome;5 verified sources 不变)
- [x] P19.1: 修复 P19 索引漂移 (Canva 行状态对齐 - draft → reviewed;当前质量状态 7→8 reviewed)
- [x] P21: 人工复核 Webflow 文章 (draft → reviewed;新增 3 个 Webflow official blog posts + 1 个 W3Techs verified;修正 Wikipedia reference vs direct verified media 边界;收购金额未披露 / undisclosed)
- [x] P22: 新增 Replit AI 辅助分析 (第十篇 AI 分析;75 个 source URLs verified 200;主体产品机制 verified;融资/估值/ARR/用户量 partial — 私人公司/未 IPO/主流媒体 paywall)
- [x] P22.1: 修复 Replit YAML 重复 source_quality_notes 字段 (2 → 1)
- [x] P23: 人工复核 Replit 文章 (draft → reviewed;§17.1 升级;§17.2 解决 $250M Series C vs $400M Series D 轮次字母分歧;§17.3 厘清 source count 口径;YAML review_status / reviewed_at / review_notes 同步)
- [x] P23.1: 修复 Replit 复核后 README 质量状态漂移 (9 reviewed → 10 reviewed;AI 辅助分析 / reviewed / partial 三项同步;未改其他三处)
- [x] P24: 新增 AI 分析索引一致性 + YAML 质量检查脚本 (scripts/verify_ai_analysis_index.py + docs/index-sync-validation.md;11 大类检查;首跑 9 项 FAIL 后修复 12 项真实问题后 PASS)
- [x] P25: 接入 AI 分析索引一致性 GitHub Actions CI (.github/workflows/ai-analysis-index-check.yml;触发 push/pull_request/workflow_dispatch;安装 PyYAML + 运行脚本;不访问外部 URL)
- [x] P26: 新增 Coda AI 辅助分析 (第十一篇 AI 分析;55 个 source URLs 实链验证;主体产品机制 verified;Grammarly 收购 primary-source verified;融资/估值/Superhuman rebrand partial — 私人公司/未 IPO/主流媒体 paywall/800+/600+ 数字不一致)
- [x] P27: Coda 人工复核 + source-hardening (draft → reviewed;新增 16 个 HTTP-200 URL — superhuman.com 8 + grammarly.com/blog/company 3 + grammarly.com/press 1 + blog.superhuman.com 2 + coda.io 4;Oct 2025 Superhuman rebrand 从 partial 升级 verified-primary — grammarly.com/press + rebrand blog 2025-10-29 + superhuman.com/ 三源交叉;Superhuman Suite (Mail / Grammarly / Coda / Go) verified-primary;其余高风险事实仍 partial — 私人公司 / 主流媒体 paywall)
- [x] P28: 新增 Obsidian AI 辅助分析 (第十二篇 AI 分析;30 个 source URLs verified 25+;主体产品机制 verified — local-first / markdown / 双向链接 / graph view / plugin ecosystem / Sync 2020 launch / 4000+ plugins 120M downloads 官方 blog verified;创始人 / 收入 / ARR / 融资 / 估值 / 用户量 partial — 私人公司无公开数据 / 主流媒体 paywall)
- [x] P30: 新增 Tana AI 辅助分析 (第十三篇 AI 分析;31 个 source URLs HTTP-200 verified;主体产品机制 verified — tana.inc agentic meeting platform / outliner.tana.inc Tana Outliner 双线分离 / Supertags / Knowledge graph / AI agents / Meeting notetaker / Tana Publish;6 个官方 blog posts verified — Series A $14M 2025-02-03 / Next Chapter 2026-03-31 / Product of Year 2026-02-03 / API+MCP 2026-01-30 / Desktop 2023-10-10 / Text Selection Toolbar 2023-11-08;Pricing 精确提取 — 主线 Free $0 / Pro $30 ($20 early bird) / Max $120 ($80 early bird) / Business Custom;Outliner Free $0 / Plus $8/mo / Pro $14/mo;Total $25M funding / 融资 / 估值 / ARR / 员工数 / 用户数 / 企业客户数 / 收购传言 partial — 私人公司无 SEC / Tola Capital portfolio Cloudflare 403 / Product Hunt 直接页面 403 / HN Algolia API verified 4 个 launch posts;中文 / 主流媒体主线报道无法 found;Wikipedia Tana 不存在)
- [x] P31: 对 Tana AI 辅助分析进行人工复核 (draft → reviewed;YAML review_notes 新增 / source_url_verification_status partial 不变);source-hardening 成功 — TechCrunch 200 (Ingrid Lunden 2025-02-03) + QQ 200 + Northzone portfolio/tana 200 + Lightspeed company/tana 200 四个 dual-source high verified;$25M funding / 3 founders / HQ Palo Alto + Norway / Founded 2020 / 160K waitlist + 24K Slack community 由 partial 升级 dual-source high;Product of the Year 2026-02-03 + Tola Capital 个人 portfolio + SOC2/HIPAA ETA 仍 partial;validator PASS (13/13/0/13/0)
- [x] P32: 完成 AI Product Analysis Phase 1 Synthesis (docs/ai-product-analysis-phase-1-synthesis.md);13 篇 reviewed AI 辅助分析的综合文档 — 产品谱系 / 类型分层 6 层 / 4 张横向对照矩阵 (cloud vs local / doc-db-graph-agent / creator vs operator / human-in-the-loop vs agent-first) / 14 条 AI 产品设计规律 / source-first 方法论沉淀 / 第二阶段是否继续扩展的判断标准;未修改任何 ai-assisted/*.md 或 index.yml;validator PASS (13/13/0/13/0 不变)
- [ ] 未来可升级为 GitHub Pages 产品分析站
- [ ] 长期：逐步把部分 AI 辅助分析从 partial 升级为 verified（不强求）
- [x] P33: 完成公开展示 README cleanup 与产品地图导航（新增 docs/product-map-navigation.md；README 增加 `## 快速入口`、项目定位更新为现在时、`## 阶段性综合报告` 加 product-map 链接；analyses/README.md 加 Product Map Navigation 入口；validator PASS 不变）
- [x] P34: 完成 Visual Product Map / Mermaid 产品图谱（新增 docs/visual-product-map.md，含 8 张 Mermaid 图 + 1 个 ASCII fallback 总图；README `## 快速入口` 与 `## 阶段性综合报告` 加 Visual Product Map 链接；analyses/README.md 加 Visual Product Map 入口；docs/product-map-navigation.md 加 Visual Product Map 链接；validator PASS 不变）
- [x] P35: 完成 Phase 1 Release Notes 与公开展示收口（新增 docs/phase-1-release-notes.md 含 7 节：发布摘要 / 13 篇表格 / 10 篇导航文档 / 质量系统 / 已知限制 / 推荐阅读顺序 / 下一阶段；README `## 快速入口` 加 Release Notes 链接 + `## 项目定位` 后加 Phase 1 状态段；下一步计划加 P35/P36/P37/P38 四项；validator PASS 不变）
- [x] P36: 新增 GitHub Pages 静态展示页（新增 site/ 目录含 index.html / assets/styles.css / assets/app.js / data/products.json / 404.html / .nojekyll；新增 .github/workflows/pages.yml；README `## 快速入口` + GitHub Pages Showcase 链接 + Phase 1 状态段加 Pages 未启用 fallback 说明；下一步计划 [x] P36 + [ ] P37/P38；validator PASS 不变）
- [ ] P37: 可选增强展示页交互 / 页面内容自动同步
- [ ] P38: 仅在有明确 taxonomy 空白时新增产品（候选：Arc / Dia / Claude Code / Lovable / v0）

---

*最后更新：2026-07-02（P32 Phase 1 Synthesis 完成：13 篇 AI 辅助分析全部 reviewed；新增 docs/ai-product-analysis-phase-1-synthesis.md；validator PASS；下一阶段建议先做公开展示与产品地图。）*
