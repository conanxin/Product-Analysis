# Analyses / 产品分析索引

本目录是 Product-Analysis 仓库的 AI 辅助产品分析索引。

## 1. AI 辅助分析总览

| 产品 | 分类 | 文件 | 状态 | 来源状态 | 一句话洞察 |
|------|------|------|------|----------|------------|
| Perplexity | ai-search | [2026-07-01-perplexity.md](ai-assisted/2026-07-01-perplexity.md) | reviewed | partial | 搜索 + 引用 + 对话答案重构为可追问的答案引擎 |
| Linear | product-development | [2026-07-01-linear.md](ai-assisted/2026-07-01-linear.md) | reviewed | partial | 极快交互 + 清晰信息架构重构为高节奏产品开发系统 |
| Raycast | productivity-launcher | [2026-07-01-raycast.md](ai-assisted/2026-07-01-raycast.md) | reviewed | partial | 启动器 → 可扩展开发者命令面板 + Extensions Store + AI |
| Cursor | ai-coding | [2026-07-01-cursor.md](ai-assisted/2026-07-01-cursor.md) | reviewed | partial | 编辑器 + 补全 + 聊天 + agentic + 云端 background agent 合并为同一 IDE |
| Figma | design-collaboration | [2026-07-01-figma.md](ai-assisted/2026-07-01-figma.md) | reviewed | partial | 设计编辑器 + 协作 + 设计系统 + Dev Mode + Config 2025 五产品线 |
| Framer | ai-website-builder | [2026-07-01-framer.md](ai-assisted/2026-07-01-framer.md) | reviewed | partial | 设计画布 + CMS + 发布 + SEO + 模板 + AI agent 重构为 AI 建站平台 |
| Notion | ai-workspace | [2026-07-01-notion.md](ai-assisted/2026-07-01-notion.md) | reviewed | partial | 文档 + 数据库 + 知识库 + 项目 + Calendar + Mail + AI 整合为可组合的信息工作台 |
| Canva | design-ai-platform | [2026-07-01-canva.md](ai-assisted/2026-07-01-canva.md) | reviewed | partial | 模板 + 视觉编辑器 + 品牌资产 + 企业协作 + AI 生成整合为大众化内容生产平台 |
| Webflow | visual-web-development | [2026-07-01-webflow.md](ai-assisted/2026-07-01-webflow.md) | reviewed | partial | 视觉设计 + CMS + 托管 + SEO/AEO + 优化 + AI 建站整合为可视化 Web 生产系统 |
| Replit | ai-cloud-development | [2026-07-01-replit.md](ai-assisted/2026-07-01-replit.md) | reviewed | partial | 浏览器 IDE + 云端运行时 + 部署 + 数据库 + AI Agent 结合为从想法到上线的云端应用工作台 |
| Coda | doc-database | [2026-07-01-coda.md](ai-assisted/2026-07-01-coda.md) | reviewed | partial | 文档 + 表格 + 公式 + 按钮 + 自动化 + Packs + AI 整合为 doc-as-app 工作台（被 Grammarly 收购，2025-10 Superhuman rebrand） |
| Obsidian | local-first-knowledge-base | [2026-07-01-obsidian.md](ai-assisted/2026-07-01-obsidian.md) | draft | partial | 将本地 Markdown 文件与双向链接、graph view 和插件生态结合，把笔记从"记录工具"重构为"个人知识操作系统" |

## 2. 按产品类型分组

### AI Search / Answer Engine
- **Perplexity** — 搜索 + 引用 + 对话式答案

### Product Development / Workflow
- **Linear** — issue tracking + 极快交互 + 高节奏产品开发

### Productivity / Command Layer
- **Raycast** — 启动器 + Extensions Store + AI 命令面板

### AI Coding
- **Cursor** — IDE + 补全 + 聊天 + agentic + 云端 background agent

### Design Collaboration
- **Figma** — 设计编辑器 + 实时协作 + 设计系统 + Dev Mode + Config 2025 五大产品线

### AI Website Builder
- **Framer** — 设计画布 + CMS + 发布 + SEO + 模板 + AI agent

### AI Workspace / Knowledge Management
- **Notion** — block + database + wiki + project + Calendar + Mail + AI agent

### Design AI / Visual Communication
- **Canva** — template-first + Brand Kit + Visual Suite 2 + Magic Studio + Affinity (专业设计) + Leonardo.AI (AI 生成)

### Visual Web Development
- **Webflow** — Designer 视觉开发 + CMS + Hosting + Localization + SEO/AEO + AI site builder + GSAP (动画) + Webflow Cloud + DevLink + Figma to Webflow

### AI Cloud Development
- **Replit** — Browser IDE + Cloud Runtime + Deployments (autoscale/static/reserved VM/scheduled/private) + SQL Database + Object Storage + Auth + Payments + Replit Agent 4 + Templates/Gallery + Teams/Enterprise + MCP/Skills + Figma-to-app + Claude-to-app + Microsoft Azure 合作

### Doc Database / App Doc
- **Coda** — doc + table + formula + button + automation + Packs + Coda AI + Coda Brain；被 Grammarly 收购（2024-12 all-stock deal），为 AI-native productivity suite doc 引擎

### Local-first Knowledge Base
- **Obsidian** — local-first / markdown files / 双向链接 / graph view / plugin ecosystem (4000+ / 120M downloads) / Sync / Publish / Canvas / Mobile / Web Clipper / CLI；私人公司 / bootstrapped

## 3. 当前质量状态

| 维度 | 数值 | 说明 |
|------|------|------|
| AI 辅助分析 | 12 | 11 reviewed + 1 draft |
| reviewed | 11 | 人工复核完成 |
| draft | 1 | Obsidian 待人工复核 |
| verified | 0 | 严格标准下未达成 |
| partial | 12 | 主体产品机制 verified；高风险事实 partial |
| 旧人工分析 (legacy) | 9 | 根目录 legacy notes |
| 旧文今日复盘 | 1 | Product Hunt (P2) reviewed |
| P 报告累计 | 19 | 1 legacy + 10 AI + 1 索引 + 2 review + 1 P21 review + 1 P24 + 1 P25 + 1 P26 + 1 P27 + 1 P28 |

**说明**：
- `partial` 不是失败，而是表示部分**高风险事实**（融资、估值、收入、收购、IPO、用户量、合作金额、价格变化、发布时间线、法律诉讼）仍未达到双源 verified 标准。
- 主体产品机制大多已由官方 sources verified。
- 私人公司（Framer）无 SEC/IR/Wikipedia 时，官网是主体功能事实源，但融资/估值/创始人必须主动降级。
- 公开公司 IPO 早期（Figma）Datadome 401 拦截是常见处境。

详细评判标准见 [docs/review-status-guide.md](../docs/review-status-guide.md) 和 [docs/source-quality-checklist.md](../docs/source-quality-checklist.md)。

## 4. 下一步分析候选

| 候选 | 类型 | 优先 | 备注 |
|------|------|------|------|
| ~~Replit~~ | AI coding + hosting | 已分析 | ~~私人 AI coding / hosting 公司，有私募融资报道~~ P22 draft |
| Coda | workspace | 中 | 与 Notion 重叠 |
| ~~Obsidian~~ | knowledge management | 已分析 | ~~私人 / local-first / markdown / 双向链接 / 插件生态~~ P28 draft
| Tana | knowledge management | 中 | 私人但产品差异化 |
| Arc | browser | 中 | 私人，浏览器赛道 |
| Claude Code | ai-coding | 中 | Anthropic 拥有，但与 Cursor 重叠 |
| Lovable | AI website builder | 中 | 与 Framer 直接竞争 |
| v0 | AI coding | 中 | 私人 |
| Adobe Express | design + AI | 低 | 与 Figma 竞争，数据敏感 |

## 5. 推荐阅读路径

### AI 产品路线
1. **Perplexity** → **Cursor**
   - 理解 AI 改变搜索的工作流 → 理解 AI 改变代码工作流

### 产品研发工具路线
1. **Linear** → **Raycast** → **Cursor**
   - 理解产品研发协作 → 理解个人工作流命令面板 → 理解代码工作流

### 设计 / 建站路线
1. **Figma** → **Framer**
   - 理解设计协作 → 理解设计即上线

### Knowledge Workspace 路线
1. **Notion** → Product-Analysis
   - 理解 AI workspace → 理解产品研究 workspace

### Doc-as-App 路线
1. **Notion** → **Coda**
   - 理解 wiki-style workspace → 理解 doc-as-app 生产力平台

### Knowledge Base 路线
1. **Notion** → **Coda** → **Obsidian**
   - 理解 AI workspace → 理解 doc-as-app → 理解 local-first markdown knowledge base

### Visual Communication 路线
1. **Canva** → **Figma** → **Framer**
   - 理解大众化模板驱动 → 理解设计协作 → 理解设计即上线

### Web Production 路线
1. **Figma** → **Framer** → **Webflow**
   - 理解设计协作 → 理解 AI website builder → 理解 visual web development

### AI App Builder 路线
1. **Cursor** → **Replit**
   - 理解 AI 改变代码工作流 → 理解 AI 改变从想法到部署的工作流
2. **Replit** → **Lovable** / **v0** (尚未写)
   - 理解云端全栈 AI app builder → 理解 AI 生成 UI 的不同路径

### 跨产品对比路线
1. **Cursor** vs **Figma** (Dev Mode)
   - AI 改变代码 vs AI 改变设计
2. **Framer** vs **Webflow**
   - AI website builder vs visual web development
3. **Notion** vs **Coda** / **Airtable** / **Obsidian** (未对比)
   - AI workspace vs 传统 docs / database / 本地笔记
4. **Canva** vs **Adobe Creative Cloud** / **Figma** (未对比)
   - 大众化设计 vs专业设计 vs 设计协作
5. **Replit** vs **Cursor** / **Lovable** / **v0** / **Bolt.new** / **GitHub Codespaces** / **Vercel**
   - 云端全栈 AI app builder vs 本地 IDE + AI / AI UI 生成 / 浏览器 IDE / 部署平台

## 6. 状态流转

```
draft → reviewed → partial-to-verified
```

| 状态 | 含义 | 转换条件 |
|------|------|---------|
| **draft** | AI 初稿, 待人工复核 | YAML 默认值, P 报告归档后人工复核 |
| **reviewed** | 已人工复核, 可作为参考资料 | 通过 source-quality-checklist 主体审查, 人工完成 P 报告 |
| **partial** | reviewed + source_url_verification_status=partial | 主体产品功能 verified, 高风险事实缺乏双独立 verified 媒体 |
| **verified** | reviewed + source_url_verification_status=verified | 高风险事实满足 source-quality-checklist v1.0 最低要求, 双独立 verified 高质量媒体 |

## 7. 维护说明

1. **新增 AI 辅助分析**: 在 `analyses/ai-assisted/` 下创建 `YYYY-MM-DD-product-name.md`, 同步更新 `analyses/index.yml` 和根 `README.md` 的"AI 辅助分析索引"表格。
2. **人工复核升级**: 修改 `review_status: draft → reviewed`, 同步更新 `analyses/index.yml`。
3. **来源状态升级**: 满足 source-quality-checklist 最低要求后, 修改 `source_url_verification_status: partial → verified`。
4. **旧人工分析**: 不在 AI 辅助分析索引中, 保留根目录原位。
5. **index.yml 准确性**: 每篇 P 报告完成后, 检查 `analyses/index.yml` 是否与文章 YAML 一致。

## 8. 关联文件

- [README.md](../README.md) — 仓库主入口
- [docs/source-quality-checklist.md](../docs/source-quality-checklist.md) — 来源质量标准
- [docs/review-status-guide.md](../docs/review-status-guide.md) — review_status 流转指南
- [templates/product-analysis-template.md](../templates/product-analysis-template.md) — 文章模板
- [CHANGELOG.md](../CHANGELOG.md) — 任务历史
- [reports/](../reports/) — 任务报告

---

*本目录由 P15 任务建立 (2026-07-01)。*
