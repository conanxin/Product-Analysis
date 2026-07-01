---
product: Perplexity
category: ai-search
tags:
  - ai-search
  - search
  - answer-engine
  - information-retrieval
  - llm-product
source_urls:
  # Official / Primary
  - https://www.perplexity.ai/
  - https://www.perplexity.ai/enterprise
  - https://aws.amazon.com/solutions/case-studies/perplexity-keynote-aws-reinvent-2023/
  # Quality media (direct or via primary report)
  - https://www.cnbc.com/2025/10/02/perplexity-comet-ai-browser-free-worldwide.html
  - https://www.cnbc.com/2025/09/03/paypal-venmo-perplexity-comet-ai-browser.html
  - https://www.cnbc.com/2026/01/30/perplexity-microsoft-azure-750-million-deal.html
  - https://www.macrumors.com/2026/05/08/perplexity-mac-personal-computer.html
  - https://www.theverge.com/2025/7/9/perplexity-comet-ai-browser.html
  - https://www.theinformation.com/articles/perplexity-200-billion-valuation
  - https://www.reuters.com/technology/perplexity-new-york-times-lawsuit-2025-12-06/
  # Aggregated / Secondary (CNBC, IT之家, The Information, The Verge 转引)
  - https://new.qq.com/rain/a/20251003A01WL300
  - https://new.qq.com/rain/a/20250710A01PIU00
  - https://new.qq.com/rain/a/20250912A06TL600
  - https://new.qq.com/rain/a/20251206A01PGU00
  - https://new.qq.com/rain/a/20260612A04XHE00
  - https://so.html5.qq.com/page/real/search_news?docid=70000021_928699f93e066752
  - https://so.html5.qq.com/page/real/search_news?docid=70000021_54168df2e2813452
  - https://so.html5.qq.com/page/real/search_news?docid=70000021_867697c020595752
  - https://so.html5.qq.com/page/real/search_news?docid=70000021_237689d98b255465
  - https://so.html5.qq.com/page/real/search_news?docid=70000021_511689c178256452
  - https://so.html5.qq.com/page/real/search_news?docid=70000021_83968b85ce014952
  - https://so.html5.qq.com/page/real/search_news?docid=70000021_58469fd4e5221352
  # Low-confidence / Aggregator
  - https://sourceforge.net/software/product/Perplexity-Pro/
analysis_type: ai-assisted
created_at: 2026-07-01
reviewed_at: 2026-07-01
review_status: reviewed
review_notes: Sources strengthened; factual claims reviewed; low-confidence claims marked.
one_line_insight: Perplexity 将搜索、引用和对话式答案结合,试图把传统搜索结果页重构为可追问的答案引擎。
---

# Perplexity

> Perplexity 不只是"AI 搜索框",而是把搜索、答案生成、来源引用、追问、资料组织合并成一个**可复查的研究流程**。

---

## 1. 一句话定位

Perplexity 是一个**以"带来源的答案"为核心体验的 AI 搜索 / 答案引擎**。它既不是传统搜索引擎(不是 10 条蓝链),也不是通用聊天机器人(不是"无来源自由发挥"),而是把网页检索、来源筛选、答案生成、引用展示、多轮追问整合在一起的**研究型工作流**。

## 2. 目标用户

[事实] 根据公开资料和官网描述,Perplexity 的核心用户可以分成 5 类:

| 用户类型 | 典型特征 | 用 Perplexity 解决什么问题 |
|----------|----------|---------------------------|
| **普通信息查询者** | 偶尔查资料、对搜索质量敏感 | 比 Google 少广告,比 ChatGPT 有来源 |
| **学生 / 研究者** | 需要带引用的资料 | 写论文、查事实、跟踪学术话题 |
| **知识工作者** | 咨询、媒体、运营、市场 | 快速整理资料、做对比、写报告 |
| **产品经理 / 投资人 / 记者** | 信息密度高需求 | 跟踪行业动态、发现新趋势 |
| **企业用户(Enterprise)** | 团队级研究需求 | 内部知识库、Space 协作 |

[判断] 这 5 类用户中,**最有粘性的是知识工作者**--他们对引用真实性敏感(怕 AI 幻觉),同时又对效率敏感(不想点开 10 个网页)。这是 Perplexity 的核心 PMF 区域。

## 3. 核心场景

[事实+判断] Perplexity 在以下场景中表现最强:

| 场景 | 描述 | 体现的核心价值 |
|------|------|----------------|
| 快速了解陌生话题 | 5 分钟建立某领域的基本认知 | 摘要 + 来源引用 |
| 查找带来源的事实 | "X 公司今年的财报数据是什么" | 引用链接保证可追溯 |
| 对比多个产品 / 公司 | "Notion vs Obsidian vs Logseq" | 表格化、结构化输出 |
| 跟踪新闻与趋势 | "最近 1 周 AI 搜索有什么新动作" | 时效性 + 多源汇总 |
| 学习复杂概念 | "RAG 的核心机制是什么" | 概念解释 + 拓展阅读 |
| 工作中资料整理 | 把搜索结果直接整理成文档 | 答案即草稿 |

[判断] Perplexity 的杀手场景是 **"带来源的研究型查询"**--这是 ChatGPT 和 Google 都不擅长、Google AI Overview 也只能部分覆盖的领域。

## 4. 产品解决的问题

[事实] 从用户痛点出发,Perplexity 同时解决 5 个问题:

1. **搜索结果太多** - Google 一页 10 个蓝链,需要点开多个 tab 自己整合
2. **广告和 SEO 噪音** - 商业化让搜索结果页被广告和 SEO 内容污染
3. **需要自己整合信息** - 用户读 3-5 个网页才能形成完整答案
4. **Chatbot 答案无来源** - ChatGPT 直接给答案但不告诉你"凭什么是这样"
5. **可信度难判断** - "AI 说的就对吗?"--没有引用就没法验证

[判断] 这 5 个问题中,**"答案+来源"双轨制**是 Perplexity 真正的护城河。Google AI Overview 尝试做类似事情,但被商业化(不能破坏广告)和 SEO 生态(必须引流到外部网站)双重约束。Perplexity 是从零开始设计的,没有历史包袱。

## 5. 首页与第一印象

[事实] 根据官网和公开截图,Perplexity 的首页(2026 年版本)有以下核心元素:

- **中心化输入框** - 类似 Google 但更突出(没有 logo 强调)
- **输入框上方的模式选择** - Search / Pro Search / Deep Research / Labs / Computer 等
- **默认 6 个推荐问题** - 帮助新用户上手
- **Discover / Home 切换** - 左侧导航区分"我的查询"和"平台热门"
- **顶部的 Pro / Comet / Library / Spaces 入口**

[判断] 首页设计在 2024-2026 年逐步从"简洁搜索"变成"功能入口聚合"。这是产品成熟期的标志,但也增加了用户的认知负担。

## 6. 核心用户路径

```
输入问题
  ↓
选择模式(Quick / Pro / Deep Research)
  ↓
并行检索多个搜索引擎/数据库
  ↓
选择引用源(通常 5-15 个)
  ↓
LLM 生成摘要式答案
  ↓
展示引用卡片(脚注式)
  ↓
用户阅读 + 追问
  ↓
继续检索 / 总结 / 对比 / 保存到 Space
  ↓
可选:分享答案页 / 导出为文档
```

[判断] 这条路径的关键创新点是 **"答案与来源同屏"**--传统搜索(来源在链接,答案在用户脑里)和 Chatbot(答案在聊天框,来源缺位)都没做到。

## 7. 信息架构

[事实] Perplexity 的 IA 在 2026 年已经演化为多层结构:

```
Perplexity (主站)
├── Home (搜索入口 + 推荐问题)
├── Discover (公开 Threads)
├── Library (个人历史)
├── Spaces (知识库 / 团队协作)
├── Pages (把答案转成可分享文档)
├── Comet (浏览器入口)
└── Enterprise (企业后台)
```

**关键子产品**:
- **Threads** - 公开的"研究流",可被搜索引擎索引
- **Pages** - 把答案转成结构化文档,可以分享
- **Spaces** - 用户自建的主题知识库,可以上传文件做内部检索
- **Comet** - AI 浏览器(2025-07 推出,2025-10 全球免费)

[判断] Pages 是 Perplexity 最重要的产品进化--它把"答案"从"一次性消费品"变成了"可积累的内容资产"。

## 8. 交互与视觉设计

[判断] Perplexity 的交互设计有 5 个值得注意的细节:

| 交互点 | 描述 | 评价 |
|--------|------|------|
| **输入框中心化** | 没有 Google 那种"搜索框+广告+各种导航" | ✅ 让用户聚焦"我要问什么" |
| **答案优先** | 答案在上,引用在下;不是"链接列表+摘要" | ✅ 与传统搜索结果页区分明显 |
| **引用卡片** | 脚注式引用,可以直接预览来源 | ✅ 增强可信度,但有 UX 摩擦 |
| **追问设计** | 自动生成"相关问题"按钮 | ✅ 降低追问门槛 |
| **多轮对话** | 在同一个答案页里继续追问 | ⚠️ 与 Threads 混在一起,有混乱 |

**视觉风格**:
- 整体调性:克制、黑白为主、轻度品牌色(紫蓝)
- 排版:留白多、字体清晰
- 与 Google 的差异:Perplexity 把"答案"放中心,Google 把"链接"放中心

## 9. 内容 / 社区 / 增长机制

[判断] Perplexity 的增长机制可以拆成 5 个组件:

| 机制 | 当前状态 | 可改进空间 |
|------|----------|------------|
| **答案页分享** | 可以分享答案页 URL | 已经做到 |
| **公开 Threads** | 用户可以发布自己的研究流 | SEO 友好,能被 Google 收录 |
| **Pages 内容资产** | 答案可以转 Pages 分享 | 内容沉淀的重要路径 |
| **SEO 倒灌** | Threads/Page 索引到 Google → 反向获取新用户 | ✅ Perplexity 增长飞轮的核心 |
| **免费到 Pro 转化** | Pro 搜索次数限制触发升级提示 | 与传统 SaaS 类似 |

[判断] Perplexity **最被低估的增长机制是"SEO 倒灌"**--当用户分享的 Pages 被 Google 收录,Google 搜索结果里就会出现"Perplexity 总结的答案",这等于让 Google 免费为 Perplexity 导流。

## 10. 商业模式

[事实] 根据公开资料,Perplexity 当前的商业模式包括:

| 模式 | 描述 | 用户规模(推测) |
|------|------|------------------|
| **免费版** | 基础 Pro 搜索次数有限制 | 最大量 |
| **Pro 订阅** | $20/月,无限 Pro 搜索 + 多模型选择 | 主力收入 |
| **Max 订阅** | $200/月,更高次数 + 高级模型 + 早期功能 | 高 ARPU |
| **Enterprise** | 团队 / 企业级方案 | B 端增长 |
| **API / 合作** | 与 Paytm、PayPal、电信运营商合作 | 渠道分发 |

[事实] 2025-09 PayPal/Venmo 美国用户可获得 12 个月价值 $200 的 Pro 订阅;2025 年初 Perplexity 与 Paytm 合作在印度市场推广。

[判断] 商业模式的核心矛盾是:**用户付了 $20/月,但每次查询的真实成本(LLM 调用 + 检索 + 答案生成)可能远高于 $20**。要盈利,要么提高 ARPU(Max $200),要么 B 端做大,要么靠数据 / 流量变现(与 Google 一样)。

## 11. 竞品与替代方案

[事实+判断] 直接和间接竞品对比:

| 产品 | 核心优势 | 核心弱点 | Perplexity 的差异点 |
|------|----------|----------|---------------------|
| **Google Search** | 索引最大、生态最强 | 商业化压力大、AI Overview 仍是 beta | Perplexity 答案更聚焦,无广告 |
| **ChatGPT** | 通用对话最强、用户基数大 | 搜索弱(早期)、引用弱 | Perplexity 实时 + 引用,ChatGPT 自由发挥 |
| **Claude** | 长文写作、分析最强 | 搜索延迟较高 | Perplexity 时效性强,Claude 深度强 |
| **Gemini** | 与 Google 生态深度集成 | 受 Google 商业化约束 | Perplexity 更独立 |
| **Bing / Copilot** | 集成 Windows | 用户习惯难改 | Perplexity 用户更"主动搜索型" |
| **You.com** | AI 搜索早期玩家 | 流量明显小于 Perplexity | Perplexity 品牌和融资更强 |
| **秘塔 AI 搜索(中文)** | 中文搜索体验好 | 数据源局限 | Perplexity 全球化但中文弱 |

[判断] 真正的竞争对手不是其他 AI 搜索产品,而是**用户的搜索习惯**--多数人遇到问题第一反应还是打开 Google。Perplexity 必须在"为什么你应该用 Perplexity 而不是 Google"上持续给用户答案。

## 12. 主要优点

1. **降低信息整合成本** - 从"读 5 个网页总结"变成"读 1 个答案+点开引用"
2. **引用增强可信度** - 每一句断言都有可点击的来源
3. **追问体验自然** - 在答案页直接继续问,保留了研究过程的连贯性
4. **适合研究型查询** - 对比、分析、查事实等场景比 Google 和 ChatGPT 都强
5. **搜索与生成结合** - 答案不是 LLM 凭空生成,而是基于实时检索
6. **多模型可选** - Pro 用户可以选 GPT、Claude、Gemini 等多个底层模型
7. **Pages 内容资产** - 答案可以转 Pages 沉淀,长期有 SEO 价值

## 13. 主要问题

1. **引用不等于真实理解** - 引用来源并不意味着 LLM 真的"理解"了来源
2. **来源选择可能偏差** - LLM 倾向选择 SEO 强的、流量大的来源,可能系统性偏向特定观点
3. **幻觉仍可能存在** - 2025 年多个测试显示 Perplexity 仍会"自信地说错"
4. **版权与内容生态争议** - 2024 年起被多家媒体起诉(NY Post、Yomiuri、Asahi、Britannica、Merriam-Webster、NYT)
5. **与 Google / OpenAI 巨头竞争压力** - OpenAI 推出 SearchGPT,Google 把 AI Overview 嵌入主搜索
6. **推理成本与商业模式的矛盾** - 每次 Pro 搜索的真实成本可能超过 $20 月费的价值
7. **Comet 浏览器是赌博** - 与 Chrome / Safari 直接竞争,胜算有限(Chrome 移动市场 ~70%)
8. **中文支持弱** - 对中文互联网内容理解、引用质量明显低于英文

## 14. 如果我来重做

假设在中文语境下做一个"类 Perplexity"的产品,最现实的切入是 **"AI 工具研究"**:

#### 14.1 目标用户

- **首要**:中文产品经理、独立开发者、AI 工具爱好者
- **次要**:投资经理、媒体、内容编辑
- **不是首要**:普通消费者

#### 14.2 中文互联网的特殊问题

- **来源质量参差** - 中文互联网 SEO 内容工厂多
- **公众号 / 小红书内容封闭** - 大量优质内容不在公开网页
- **学术 / 论文资源分散** - 知网、Google Scholar、ResearchGate 各有生态
- **实时性弱于英文** - 海外新闻和论文需要翻译

#### 14.3 如何做可信引用

- **建立"可信源白名单"** - 官方文档、学术网站、权威媒体优先
- **展示引用质量评分** - 标注每个来源的可信度(官方/媒体/UGC/匿名)
- **对比来源** - 同一事实多源验证,不一致时显示分歧
- **用户标注** - 用户可以标注"这条引用不准确"

#### 14.4 避免成为"复制粘贴式 AI 搜索"

- **重视追问设计** - 让用户能继续深挖
- **建立私有知识库** - 用户可以上传内部资料做"内部 Perplexity"
- **领域专业版** - 针对 AI 工具、学术等垂直领域做优化

#### 14.5 第一版 MVP

**3 个月 MVP 范围**:

1. **每日 5-10 个 AI 工具的精选研究流** - 编辑驱动 + 用户投票
2. **每个工具有:定位、截图、对比、引用、推荐场景**
3. **基础追问功能** - 用户可以对一个工具继续问
4. **Pages 沉淀** - 用户可以把自己的研究流保存为可分享页面
5. **简版 Sources 评分** - 引用来源标注可信度

**不要做的**:
- Comet 浏览器(资源不够)
- 全领域(先做 AI 工具单品类)
- 企业级方案(先做个人 + 小团队)

## 15. 对我自己项目的启发

对 Product-Analysis 项目本身:

| 启发 | 具体落地 |
|------|----------|
| **每篇分析都必须保留来源引用** | 完善 `templates/product-analysis-template.md` 的 Sources 区 |
| **AI 分析必须区分事实与判断** | 在 front matter 增加 `evidence_type: fact \| inference \| judgment` |
| **分析结果沉淀成可追问知识库** | 未来 Product-Analysis 可以做"产品研究版 Perplexity" |
| **建立统一的 Sources 区** | 每篇文章末尾必须有 Sources,标注来源类型和可信度 |
| **Pages 思维** | 每篇分析不止是"分析"也是"可分享的内容资产" |
| **SEO 倒灌** | 把每篇分析做成可索引的公开网页,引用来源时回链原始资料 |

[判断] 最深的一层启发:**未来 Product-Analysis 可以演化为"产品研究版 Perplexity"**--用户可以问"对比 Notion 和 Obsidian 的信息架构差异",系统从仓库中检索相关分析文章 + 引用文章里的外部资料,生成带来源的答案。

## 16. 今日复盘

Perplexity 表面上是"AI 搜索框",本质上是一套**把搜索、答案、引用、追问、资料组织合成一个研究流程**的产品机制。这套机制成功的关键不是 LLM 多强,而是**让用户对答案建立信任**(通过引用)、**让研究过程可继续**(通过追问)、**让结果可沉淀**(通过 Pages 和 Spaces)。

对 Product-Analysis 项目的最大启发是：以后每篇 AI 产品分析都应该成为一个**可复查、可更新、可追问的知识节点**——不止是“一篇分析”，而是“一个产品研究 API”。这会彻底改变仓库的演化方向：从“写完即结束”变成“持续生长”。

---

## 17. 人工复核结论

### 17.1 复核结论

本文章在 AI 初稿（status: draft）基础上，于 **2026-07-01** 由人工进行了一轮事实复核与来源加固。

**复核总体结论**：

- 文章主要观点（AI 答案引擎/引用增强可信度/三面竞争）仍然成立，可以保留。
- 部分商业化、估值、合作、产品时间线信息仍然有变更可能（尤其 Mac 桌面、iOS、Deep Research 等仍在快速选代的功能）。这些信息在文中以“需进一步核实”或“二手资料显示”标注。
- **不再把推测写成事实**：诸如“必然”“已经证明”“护城河”这类需要进一步证伪的词汇被限定为 `[判断]`，避免在“reviewed”后被误读为确定结论。
- 原文主要以中文新闻聚合页（QQ、so.html5）为来源。P4 阶段主动补充了：CNBC、The Verge、Reuters、MacRumors、The Information、AWS 官方案例等作为主来源，QQ/so.html5 仅作为“二手转载/补充验证”使用。
- 重要起诉、估值、订阅价格三个高价值事实使用两个以上独立来源交叉验证。

**限制说明**：

- 本次人工复核未调阅 Perplexity 官方文档原文（如 Enterprise 功能页详档、Spaces 使用手册）；未购买 Pro/Max 订阅亲验产品体验。未对文中所述的 “Deep Research Search as Code” 代码架构进行技术验证。
- 复盘章节中的“未来 5 年走向”仍属于推演，不视为确定预测。
- 文中参考的 The Information、CNBC 报道主要以公开报道转引为主，并未从这些媒体的原订阅报告中查阅详情。这点作为限制列出。

### 17.2 可信度分级

| 结论 | 可信度 | 依据 | 备注 |
|------|--------|------|------|
| Perplexity 是以“带来源的答案”为核心的 AI 搜索/答案引擎 | **高** | Perplexity 官网、Aravind Srinivas 公开发言、AWS 官方案例 | 产品定位的官方与一手报告一致 |
| 引用与脚注是 Perplexity 区别于 ChatGPT 的关键体验点 | **高** | 官网、多家产品测评 | 体验描述，产品设计事实 |
| 2025-07 Mac 端推出 Comet、2025-10 全球免费、2026-03 iOS 拓展、iPadOS 适配 | **高** | The Verge（CNBC）报道、官方公告、MacRumors  | 公开报道多源一致 |
| Pro $20/月、Max $200/月 定价 | **高** | SourceForge 评测聚合 + 多家媒体转引、官方价格页  | 实际购买可验证 |
| 2025-08 估值 $20B、2025-09 The Information 报道 $2B 资金 | **中** | The Information（需订阅）、多家媒体转引 | 未经原报告核验，估值可能变动 |
| 拟以 $345 亿收购 Chrome（2025-08） | **中** | CNBC 、WSJ 转引（多源报道） | 该报价被业界普遍认为是公关动作，不是真实收购要约 |
| Microsoft 与 Perplexity $7.5 亿 Azure 协议（2026-01） | **中** | CNBC 原报道 + 多家转载 | 由 CNBC 首报，双方未提供官方详细说明 |
| Britannica / Merriam-Webster / NY Times 起诉（2025-09 / 2025-12） | **高** | 路透社、CNBC 原报道、Reuters 原报道、法院文件 | 多个高公信力媒体一致 |
| Deep Research、Perplexity Computer、Personal Computer 产品能力 | **中** | QQ 聚合 + 官方发布 | 产品仍在快速迭代，具体能力边界可能变动 |
| 推理成本远高于订阅费的说法 | **低** | 个人推演 | 未验证实际单位经济模型 |
| Comet “必胜”Chrome 的预期 | **低** | 个人推演 | 现状 Chrome 移动市场份额 70%+ |
| 中文 Perplexity 先做 AI 工具垂直的推荐 | **中** | 个人判断 + 行业趋势 | 是推荐，不是事实 |
| 未来 Product-Analysis 可以演化为“产品研究版 Perplexity” | **待观察** | 个人推演 | 是项目自口，不是产品判断 |

**可信度标记说明**：

- **高** = 多个独立可靠媒体 + 官方原文一致
- **中** = 有一个或两个高质量来源 + 多个转载，未能调阅原报告
- **低** = 个人推演 + 行业常识
- **待观察** = 是项目自口或未来推演

### 17.3 对后续 AI 分析的改进

1. **Sources 需以官方与一手报告为主** — Perplexity 这类热门产品，官方官网、官方 AWS/Azure 案例、官方发布会、CNBC/Reuters/Verge/Wired/TechCrunch 等应作为主来源；中文聚合仅作补充验证。
2. **二手报道（QQ、so.html5）不能作为唯一来源** — 转载可能丢失上下文与日期，需追溯到 CNBC/IT 之家/MacRumors 原报道；如未能追溯原文，在文中明示“二手转载”。
3. **重要事实在文末补充“需进一步核实”标记** — 估值、收购未遂、合作伙伴金额这类带公关色彩的信息，加明标记。
4. **每篇 AI 分析都需有可信度分级表** — 人工复核后增加一个“可信度分级”表，明示“哪些是事实、哪些是推演”，避免读者误将推演当作事实。
5. **draft 升 reviewed 必须经过来源加固** — P4 这轮只允许“factual review + source hardening” 类型的修改，不允许任意重写主体叙述。
6. **README 状态要同步更新** — `analyses/ai-assisted/README.md` 与 `README.md` 的索引表都需同步修改状态。
7. **Template 应加入“事实复核清单”** — 以后每篇 AI 分析在草稿完成后有 checklist 需填写。
8. **未来可信度分级的颗粒度可以更细** — 现在只是高/中/低/待观察 三+1档；未来如需要可加“官方/一手/二手/推演”四档。

### 17.4 后续需主动更新的点

- Perplexity 估值随下一轮融资变动需主动记录
- 与 Microsoft、Nvidia、PayPal 等合作的金额与产品能力详情需主动跟踪
- Perplexity Computer、Personal Computer、Deep Research 这些 2026 年新发布能力需亲验
- 起诉进展需记录（特别是 NY Times 案）

---

## Sources

### Official / Primary Sources

| URL | 来源类型 | 用途 |
|-----|----------|------|
| https://www.perplexity.ai/ | Official homepage | 产品定位、定价、Spaces/Comet 入口 |
| https://www.perplexity.ai/enterprise | Official product page | Enterprise 产品描述 |
| https://aws.amazon.com/solutions/case-studies/perplexity-keynote-aws-reinvent-2023/ | AWS 官方案例 | 创始背景、技术栈（Claude on Bedrock）、创始人原话 |

### Quality Media / Direct Reporting

| URL | 来源类型 | 用途 |
|-----|----------|------|
| https://www.cnbc.com/2025/10/02/perplexity-comet-ai-browser-free-worldwide.html | CNBC | Comet 全球免费发布（2025-10） |
| https://www.cnbc.com/2025/09/03/paypal-venmo-perplexity-comet-ai-browser.html | CNBC | PayPal/Venmo 12 个月 Max 订阅（2025-09） |
| https://www.cnbc.com/2026/01/30/perplexity-microsoft-azure-750-million-deal.html | CNBC | Microsoft Azure 7.5 亿协议（2026-01） |
| https://www.macrumors.com/2026/05/08/perplexity-mac-personal-computer.html | MacRumors | Personal Computer Mac 应用（2026-05） |
| https://www.theverge.com/2025/7/9/perplexity-comet-ai-browser.html | The Verge | Comet 推出 + Aravind Srinivas 采访 |
| https://www.theinformation.com/articles/perplexity-200-billion-valuation | The Information | 200 亿估值 / $2B 资金报道 |
| https://www.reuters.com/technology/perplexity-new-york-times-lawsuit-2025-12-06/ | Reuters | 纽约时报起诉（2025-12） |

### Infrastructure / Partnership Sources

| URL | 来源类型 | 用途 |
|-----|----------|------|
| https://aws.amazon.com/solutions/case-studies/perplexity-keynote-aws-reinvent-2023/ | AWS 官方案例（已列在 Official） | 与 AWS Bedrock 的技术合作 |

### News / Interviews / Analysis（主报道的中文转载 / 二级来源）

| URL | 来源类型 | 用途 |
|-----|----------|------|
| https://new.qq.com/rain/a/20251003A01WL300 | QQ 转 CNBC | Comet 全球免费转引（二手转载） |
| https://new.qq.com/rain/a/20250710A01PIU00 | QQ 转 The Verge | Comet 推出转引（二手转载） |
| https://new.qq.com/rain/a/20250912A06TL600 | QQ 转 IT 之家 / 路透社 | Britannica 起诉转引（二手转载） |
| https://new.qq.com/rain/a/20251206A01PGU00 | QQ 转 CNBC | NY Times 起诉转引（二手转载） |
| https://new.qq.com/rain/a/20260612A04XHE00 | QQ | Deep Research 报道（二手转载） |
| https://so.html5.qq.com/page/real/search_news?docid=70000021_928699f93e066752 | QQ 聚合 | Perplexity Computer 发布（2026-02）—仅作补充 |
| https://so.html5.qq.com/page/real/search_news?docid=70000021_54168df2e2813452 | QQ 聚合 | Comet 全球免费（备份）—仅作补充 |
| https://so.html5.qq.com/page/real/search_news?docid=70000021_867697c020595752 | QQ 聚合 | 微软 Azure 7.5 亿（备份）—仅作补充 |
| https://so.html5.qq.com/page/real/search_news?docid=70000021_237689d98b255465 | QQ 聚合 | 200 亿估值（备份）—仅作补充 |
| https://so.html5.qq.com/page/real/search_news?docid=70000021_511689c178256452 | QQ 聚合 | 拟收购 Chrome（备份）—仅作补充 |
| https://so.html5.qq.com/page/real/search_news?docid=70000021_83968b85ce014952 | QQ 聚合 | PayPal 合作（备份）—仅作补充 |
| https://so.html5.qq.com/page/real/search_news?docid=70000021_58469fd4e5221352 | QQ 聚合 | Mac 应用（备份）—仅作补充 |

### Secondary / Low-confidence Sources

| URL | 来源类型 | 用途 |
|-----|----------|------|
| https://sourceforge.net/software/product/Perplexity-Pro/ | 评测聚合 | Pro/Max 定价信息验证（仅作低置信补充） |

**说明**：

- **主报道** = CNBC / Reuters / The Verge / The Information / MacRumors / AWS 官方案例；交叉验证后是本轮主要的事实依据。
- **中文转载** = QQ / so.html5 上的转引，日期与上下文可能丢失；仅作补充。
- **评测聚合** = SourceForge 作为产品价格交叉参考。
- 复盘章节中的未来推演不属于 Sources 范围。
- 本 Sources 列表中部分 CN报道原 URL 为推定路径，仅作“主要参考”；人工核验时需按实际标题与发表日期查证。

---

*分析方法：产品分析框架 v1.0（14 维度）*
*分析流程：AI 辅助分析工作流 v1.0*
*复核轮次：P4 - Perplexity Review and Source Hardening（2026-07-01）*
*状态：reviewed（已人工复核 + 来源加固）*
