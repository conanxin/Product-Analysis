# Product Analysis / 产品分析档案

## 项目定位

这是一个**产品设计观察与分析项目**。

早期内容来自人工分析（2015年前后），以"特点 / 问题 / 设想"结构记录对各类互联网产品的观察笔记。后续计划逐步加入 **AI 辅助分析**，通过结构化模板持续沉淀对产品的深度分析。

> "因为想要做一些东西，但是不知道如何下手。最近想清楚了，可以先快速学习一下原型的制作。"——早期动机

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

---

- `根目录旧文章` = legacy manual analysis，保留原貌，仅在顶部增加 metadata
- `analyses/ai-assisted/` = 新 AI 分析文章
- `templates/` = 标准化模板
- `docs/` = 方法论文档

---

## 如何新增一篇 AI 产品分析

1. **选择产品** — 选择一个你想深入了解的产品
2. **收集材料** — 官网链接、截图、产品简介、用户评价、竞品信息、商业模式资料、个人初步观察
3. **生成分析** — 使用 `templates/ai-product-analysis-prompt.md` 提示词，让 AI 分析产品
4. **整理成文** — 按 `templates/product-analysis-template.md` 的结构输出 Markdown
5. **放置文件** — 存入 `analyses/ai-assisted/YYYY-MM-DD-product-name.md`
6. **回填索引** — 在本文"当前内容索引"表格中补充一条记录

---

## 下一步计划

- [ ] 为旧文章补充"今日复盘"章节（用新框架重新审视旧观察）
- [ ] 增加更多 AI 产品分析案例
- [ ] 未来可升级为 GitHub Pages 产品分析站
- [ ] 未来可增加产品数据库 `index.yml`

---

*最后更新：2026-07-01 (P12 Figma 人工复核 → reviewed;P12 source-hardening +7 官方URL;Config 2025 修订为 5 款产品 + Config 2026 五项升级 + Weave 收购官方 confirmed;员工数 1886 弃用 → Newsroom 1,600+ 替代;IPO/Adobe 终止 仍 partial - Reuters Datadome)*
