# Product Map Navigation / 产品地图导航

**日期：** 2026-07-02
**关联：** [AI Product Analysis Phase 1 Synthesis](ai-product-analysis-phase-1-synthesis.md) · [AI 辅助分析索引](../analyses/README.md) · [README](../README.md)

---

## 1. 这张产品地图解决什么问题

13 篇 AI 辅助产品分析不是简单列表，而是一个 AI 产品谱系 — 用户可以按产品类型、工作流、阅读路径、研究问题来阅读。本文是导航，不是替代 Phase 1 Synthesis；如果要看规律和方法论，请直接读 Phase 1 Synthesis；如果要看具体产品，请读 `analyses/README.md`。

**适用读者：**
- 第一次访问这个仓库的陌生读者
- 想按问题找对应分析的研究者
- 想横向对比多个产品的产品经理 / 设计 / 工程负责人
- 想学习 source-first 工作流的研究方法学习者

---

## 2. 产品总览

| 产品 | 类别 | 推荐阅读场景 | 对照产品 |
|------|------|-------------|---------|
| **Perplexity** | AI Search / Answer Engine | 搜索结果被 LLM 答案替代时、AI 引用 + 可追问、citation transparency 怎么落地 | Google、You.com、Arc Search |
| **Linear** | Product Development / Workflow | 节奏紧的产品团队、键盘驱动 issue tracking、GraphQL API 让 AI 索引 | Jira、Height、Shortcut |
| **Raycast** | Productivity / Command Layer | macOS 启动器、Extensions Store 把 app 变成命令、AI 命令面板 | Alfred、Spotlight、Quicksilver |
| **Cursor** | AI Coding IDE | 编辑器内 AI、补全 + Composer + Agent + Cloud Agent long-running | GitHub Copilot、Claude Code、Codeium |
| **Figma** | Design Collaboration | 云端协作画布、Design system、Dev Mode + AI site builder | Sketch、Adobe XD、Penpot |
| **Framer** | AI Website Builder | 设计即上线、design → publish、CMS、Forms、Localization | Webflow、Typedream、WordPress + AI |
| **Notion** | AI Workspace | block + database + AI agent + doc-as-workspace + mail + projects | Coda、Slite、Quip |
| **Canva** | Design AI Platform | 大众化设计、品牌套件、Magic Studio、Content Planner | Adobe Express、Figma Express、Microsoft Designer |
| **Webflow** | Visual Web Development | 可视化设计 + CMS + Logic + Ecommerce + SEO，design → 上线 → 增长 | Wix、Squarespace、Webstudio |
| **Replit** | AI Cloud Development | 浏览器 IDE + AI Agent + Deployments + DB + Auth + Payments，整套交付 | GitHub Codespaces、StackBlitz、Glitch |
| **Coda** | Doc-as-App / Doc-Database | doc 变 app、formula + button + Packs + automation、Superhuman Suite 一部分 | Airtable、Smartsheet、Notion |
| **Obsidian** | Local-first Knowledge Base | 本地 Markdown、双向链接、graph view、plugin ecosystem、Sync + Publish | Roam Research、Logseq、Notion（cloud 对比）|
| **Tana** | AI Structured Knowledge / Agentic Meeting Platform | supertag + 知识图谱 + voice + meeting notetaker + agentic AI tasks delivery；当前 tana.inc 已转向 agentic meeting、outliner 单独保留为 Tana Outliner | Notion、Coda、Heptabase、Roam |

---

## 3. 按问题阅读

### 3.1 我想理解 AI 搜索

- **Perplexity** — AI search / answer engine；citation 透明、可追问、page sessions

### 3.2 我想理解 AI coding

- **Cursor** — 编辑器内 AI + Agent + Cloud Agent
- **Replit** — 浏览器 IDE + Replit Agent + Deployments

### 3.3 我想理解设计与视觉生产

- **Figma** — 云端画布 + 实时协作 + Dev Mode + config 2025/2026 工具集
- **Canva** — 模板 + 编辑器 + 品牌资产 + Magic Studio + Content Planner
- **Framer** — AI site builder（设计即上线）
- **Webflow** — 可视化开发 + CMS + Logic + Ecommerce

### 3.4 我想理解知识工作台

- **Notion** — block + database + AI agent
- **Coda** — doc + table + formula + button + Packs
- **Obsidian** — local-first Markdown + 双向链接 + graph + 插件生态
- **Tana** — supertags + 节点 + 知识图谱 + AI agents + meeting（双产品定位）

### 3.5 我想理解 agentic workflow

- **Cursor** — 代码侧的 agentic execution
- **Replit** — 部署侧的 agentic execution
- **Tana** — 会议与工作系统的 agentic delivery
- **Perplexity** — 浏览器侧的 agentic（Comet 方向）

### 3.6 我想理解 source-first 产品研究方法

- [Phase 1 Synthesis](ai-product-analysis-phase-1-synthesis.md) — 13 篇综合、14 条规律
- [review-status-guide.md](review-status-guide.md) — 状态机定义、升级标准
- [source-quality-checklist.md](source-quality-checklist.md) — 来源分级
- [index-sync-validation.md](index-sync-validation.md) — 索引一致性

---

## 4. 推荐阅读路径

每条路线 30-60 分钟，按顺序读完之后即可掌握一条完整线。

### 路线 A：AI 产品基础路线

**主题：**理解 AI 如何重构搜索与编程
**1.** Perplexity → **2.** Raycast → **3.** Cursor → **4.** Replit

### 路线 B：设计到发布路线

**主题：**设计工具如何演化为发布系统
**1.** Figma → **2.** Canva → **3.** Framer → **4.** Webflow

### 路线 C：知识工作台路线

**主题：**doc / database / graph / agent 四种工作台哲学
**1.** Notion → **2.** Coda → **3.** Obsidian → **4.** Tana

### 路线 D：从工具到 Agent 路线

**主题：**AI agent 如何进入产品研发
**1.** Linear → **2.** Cursor → **3.** Replit → **4.** Tana

### 路线 E：产品研究方法路线

**主题：**学习 Product-Analysis 的研究方法
**1.** legacy 人工分析（含 Perplexity 之前的 9 篇）+ **2.** Perplexity → **3.** Phase 1 Synthesis → **4.** Source-first docs

### 路线 F：AI 产品矩阵路线

**主题：**横向对比多产品形态
**1.** Phase 1 Synthesis §3 6 层类型分层 → **2.** Phase 1 Synthesis §4 4 张横向矩阵 → **3.** 本文（路线导航）

---

## 5. 横向对照问题

每读一篇文章，可以尝试用以下 8 个问题做读后笔记：

1. **核心对象是什么？** — 产品描述的是 doc / database / node / canvas / code / terminal / browser / meeting？
2. **它把什么工作流重新组织了？** — AI 把原有边界打掉在哪一步？
3. **AI 是功能、入口，还是执行层？** — AI 是按钮、入口、agent？
4. **数据结构是什么？** — block / table / file / node / graph / typed schema？
5. **可信度依赖哪些 source？** — 主体 verified 还是 high-risk partial？
6. **cloud-first 还是 local-first？** — 13 个产品里只有 Obsidian 是 local-first
7. **creator tool 还是 operator tool？** — 用户做出新东西，还是掌控已有流程？
8. **对 Product-Analysis 项目有什么启发？** — 这篇文章能否迁移到自己的研究/工作系统？

---

## 6. 下一步地图

| 任务 | 内容 | 何时 | 是否必须 |
|------|------|------|---------|
| **P33（本次）** | 公开展示 README cleanup + 产品地图导航 | 2026-07-02 | ✅ 已完成 |
| **P34** | 视觉产品地图（Mermaid 图谱 + 可视化图） | P33 后 | 可选 |
| **P35** | 新增 1 个产品（仅当有明确空白时）| P34 后评估 | 仅当用户主动需要 |
| **P35 候选方向** | Arc / Dia（浏览器）、Claude Code（终端 coding agent）、Lovable（prompt-to-app）、v0（AI UI generation）| — | — |

**当前阶段不建议无止境新增产品。** 13 篇分析已能覆盖主要 AI 产品谱系；边际收益在快速下降；更稀缺的是综合、视觉化与公开展示。

如果出现 P35 评估空白，可判断标准：
- 是否填补了 AI product taxonomy 中已存在的明显空缺？
- 是否 user 主动请求？
- 是否源材料 real verified 达到 90%+？
- 是否能补到现有矩阵中的某个类别（不重复覆盖）？

回答 ≥ 2 是"是"再进入 P35；否则继续 P33-P34 整理。

---

*文档版本：v1.0 · 2026-07-02*
*关联项目：[Product-Analysis](https://github.com/conanxin/Product-Analysis)*

_辛 🔮_
