# Changelog

## P7 - Raycast AI 辅助产品分析

**日期：** 2026-07-01
**变更类型：** ai-assisted-analysis (新增第 3 篇)
**变更范围：** analyses/ai-assisted/ + README + CHANGELOG + 新增 P7 报告

### 变更内容

第 3 篇 AI 辅助产品分析 — Raycast (命令面板 / 扩展平台 / AI 工作流)。

#### Source-first workflow

- **官方页 22 个全 HTTP 200 verified**:raycast.com 主站 + /about + /pricing + /ai + /store + /teams + /enterprise + /pro + /changelog + manual.raycast.com + developers.raycast.com + /api-reference + 10 篇 blog
- **GitHub 官方仓库**:github.com/raycast/extensions (56k+ stars) verified (200)
- **TechCrunch 3 篇 verified**:
  - 2022 Series A $19M (Accel)
  - 2024 Series B $100M (Coatue, $1B 估值)
  - 2023 AI 功能发布
- **Wikipedia verified** (200):en.wikipedia.org/wiki/Raycast
- **关键事实双源**:Series A $19M (TC+blog) / Series B $100M (TC+blog) / 创始人 (TC+Wikipedia+blog) / AI 功能发布 (TC+blog)
- **降权的辅助来源**:Product Hunt 主域名 403 (bot 防护);Bloomberg / Reuters 主域名 403/401 (bot 防护)

#### 文章结构

- 17 节全产出 (§1-§17)
- §14 "如果我来重做" — 中文语境 MVP 分析 (Tauri + 中文 Snippets + 微信/飞书命令 + 本地 LLM)
- §15 "对 Product-Analysis 项目的启发" — 6 条
- §17.1-17.4 人工复核结论齐

#### review_status

- **draft** (AI 初稿,待人工复核)
- 与 Linear / Perplexity 的 `reviewed` 不同 — Raycast 含更多个人推断(§14 中文 MVP、§15 启发),保留 draft 给人工审视

#### source_url_verification_status

- **partial** — 主体产品事实 27 URL 全 verified;但 Series A/B 融资信息主要依赖 TechCrunch 单一媒体 + Raycast 官方 blog 自述(非独立验证),按 source-quality-checklist 诚实标注 partial

### 修改文件

- `analyses/ai-assisted/2026-07-01-raycast.md`:新增 16.2 KB 文章(YAML 11 字段 + 17 章节 + Sources 28 行)
- `README.md`:AI 索引新增 Raycast 行(状态 draft + partial)
- `CHANGELOG.md`:顶部 P7 记录(本节)
- `reports/P7-raycast-ai-assisted-analysis-report.md`:新增 P7 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (8062089 = P6.1)
- ✅ Raycast 文章 16.2 KB 存在
- ✅ YAML 11 字段齐
- ✅ review_status = draft
- ✅ source_url_verification_status = partial
- ✅ source_url_verified_at = 2026-07-01
- ✅ 17 章节全产出 (§1-§17)
- ✅ §17.1 明确说"AI 辅助初稿,待人工复核"
- ✅ §17.2 11 条可信度分级(高/中/低/待观察)
- ✅ §17.4 Sources 实链验证 28 条 URL
- ✅ README draft + partial 列齐
- ✅ Perplexity / Linear mtime 未变
- ✅ 9 旧人工分析文章 + pic/ 未动

---

## P6.1 - Linear Reuters URL Verification

**日期：** 2026-07-01
**变更类型：** source-verification / docs-only
**变更范围：** Linear 全文 + CHANGELOG

### 变更内容

P6.1 阶段补查请求人提供的 Reuters 关于 Linear 2025 融资的候选 URL。

#### 验证结果

- URL: https://www.reuters.com/business/atlassian-competitor-linear-raises-funding-125-billion-valuation-2025-06-10/
- HTTP 401 (Datadome bot 拦截) — 未能直接验证
- web_search 未返回该标题
- Wayback Machine 仅为通用 reuters.com
- **结论：datadome-protected（URL 存在形式，但未 HTTP 验证）**

#### 修改文件

- `analyses/ai-assisted/2026-07-01-linear.md`:
  - YAML source_urls 增加 1 条 datadome-protected URL
  - §17.6 新增 P6.1 验证记录
  - Sources Verified Media 表格加 1 URL（datadome 标记）
  - 文末状态标注增加 P6.1 轮次

- `CHANGELOG.md`：顶部 P6.1 记录

#### 新增文件

- `reports/P6.1-linear-reuters-url-verification-report.md`

### 保持

- `source_url_verification_status` 仍为 **partial** (诚实评估)
- `review_status` 仍为 **reviewed** (不变)
- README 状态仍为 `reviewed | partial` (不变)
- Perplexity 文 mtime 未变
- 9 篇旧文章 + pic/ 未动

### P6.1 评估

- Reuters URL 真实存在形式但 HTTP 不可达；与 Perplexity P4.1 对 Reuters URL 处理一致
- $82M 2025 估值仍单源 TechCrunch
- 未达成 verified 升级要求（需要 HTTP 200 + 标题匹配）
- 保持 partial 是诚实评估的产物

### P6.1 目标达成

- [x] 验证请求人提供的 Reuters URL
- [x] 标注 datadome-protected 状态
- [x] 在 Linear 文章中加入该 URL（datadome 标记）
- [x] §17.6 P6.1 验证记录
- [x] Sources Verified Media 表格更新
- [x] CHANGELOG P6.1 记录
- [x] P6.1 报告生成
- [x] 保持 source_url_verification_status: partial (诚实)

---

## P6 - Linear Review and Source Status Upgrade

**日期：** 2026-07-01
**变更类型：** review + source-upgrade
**变更范围：** Linear 全文 + README + CHANGELOG

### 变更内容

对 P5 产出的 Linear AI 辅助分析进行人工复核与来源升级。

#### P6 升级

- **找到 2 个新 verified URLs**：
  - `https://linear.app/blog/series-b` (primary-official, 200) - Linear 官方 $35M Series B 公告
  - `https://en.wikipedia.org/wiki/Linear_(software)` (reference, 200) - 公司/创始人 second source
- **升级可信度**：
  - $35M Series B (Accel 领投): 中→高 (Linear 官方 blog + TechCrunch 双源)
  - 创始人 Tuomas Artman, Karri Saarinen: 中→高 (TC + Wikipedia 双源)
- **review_status**: draft → reviewed
- **增加**: reviewed_at + review_notes + source_url_verified_at
- **source_url_verification_status 仍为 partial** (诚实评估):
  - $82M 2025 轮仍单源依赖 TechCrunch
  - 未找到 Bloomberg/Reuters 2025 报道
  - COO Cristina Cordova 仍单源

#### 修改文件

- `analyses/ai-assisted/2026-07-01-linear.md`:
  - YAML: review_status reviewed + reviewed_at + review_notes + 增加 2 URLs
  - source_quality_notes 更新
  - §17.1 由 draft 改为 reviewed
  - §17.2 升级 Series B 与创始人可信度
  - §17.4 增加 P6 阶段验证表
  - Sources Product/Doc 区增加 2 URLs
  - 文末 P6 轮次标注

- `README.md`: AI 索引 Linear 状态 draft → reviewed

#### 新增文件

- `reports/P6-linear-review-and-source-upgrade-report.md`

### 保留

- 9 篇旧文章、CHANGELOG 旧条目、主体 1-16 节内容
- Perplexity 文 mtime 未变
- pic/

### P6 目标达成

- [x] 找到 Linear 官方 blog Series B 公告
- [x] 找到 Wikipedia second source
- [x] review_status draft → reviewed
- [x] reviewed_at + review_notes 加入 YAML
- [x] §17.1 改为 reviewed 状态描述
- [x] §17.2 升级 2 条可信度
- [x] §17.4 增加 P6 验证表
- [x] Sources 区增加 2 URLs
- [x] README 状态同步
- [x] CHANGELOG P6 记录
- [x] P6 报告生成

---

## P5 - Second AI-Assisted Product Analysis: Linear

**日期：** 2026-07-01
**变更类型：** AI-assisted analysis + source-first
**变更范围：** Linear 全文 + README + CHANGELOG

### 变更内容

产出第二篇 AI 辅助产品分析文章：Linear。严格执行 P4.1+P4.2 流程 — **先做 sources 收集与 URL 实链验证，再写文章**。

#### 验证结果

- **24 个 Linear 官方 URL verified (HTTP 200 + 标题匹配)**:
  - 主站 / docs / changelog / method / pricing / enterprise / customers / security / integrations / about / blog / features / careers
  - 8 个 docs 子页: projects / triage / inbox / teams / issue-relations / notifications / cycles / roadmaps / views / integrations
- **3 个 TechCrunch 报道 verified**:
  - 2019 A 轮 $4.2M (Sequoia 领投)
  - 2025-06 $82M 融资 $1.25B 估值
  - 2025-05 COO Cristina Cordova 访谈
- **总 verified URLs: 27** （P4 Perplexity 为 4 verified，3 datadome-protected）

#### 修改文件

- `analyses/ai-assisted/2026-07-01-linear.md` (新增 16.8KB)
- `README.md` — AI 辅助分析索引增加 Linear 一行（draft, partial）
- `CHANGELOG.md` — 顶部增加 P5 记录

#### 新增文件

- `reports/P5-linear-ai-assisted-analysis-report.md`

### P5 关键决策

- **review_status: draft** (不升 reviewed — AI 初稿待人工复核)
- **source_url_verification_status: partial** (诚实评估)
  - 官方 + docs/method 主页 24 个 verified
  - TechCrunch × 3 verified
  - **但高风险事实 (融资/估值) 单源依赖 TC 一家** — 未找到第二家高质量媒体
  - The Verge / Forbes / Business Insider 推定 URL 全部 404
  - Bloomberg / Crunchbase / Product Hunt 被 bot 拦截
  - 按 source-quality-checklist 最低要求，partial 是诚实评估

### P5 目标达成

- [x] 严格按 source-first 流程：先验证 URL 再写文章
- [x] 主体来源齐全 (24 官方 + 3 高质量媒体)
- [x] source_url_verification_status 在 YAML 中明示
- [x] 17 章节完整（含 §17.1-17.4）
- [x] review_status: draft (不升 reviewed)
- [x] README 增加 Linear 一行
- [x] CHANGELOG P5 记录
- [x] P5 报告生成

---

## P4.2 - Perplexity Verified Source Recovery

**日期：** 2026-07-01
**变更类型：** source-recovery / docs-only
**变更范围：** Perplexity 一文 + README + CHANGELOG

### 变更内容

P4.1 中 6/7 高质量媒体 URL 为推定路径未能验证。P4.2 阶段主动检索与验证可访问原报道 URL。

#### P4.2 验证结果

- **3 个新 verified URL（HTTP 200 + 标题匹配）**：
  - https://www.theverge.com/news/703037/perplexity-ai-web-browser-comet-launch (Comet 2025-07 推出)
  - https://www.theverge.com/news/790419/perplexity-comet-available-everyone-free (Comet 2025-10 免费)
  - https://www.businessinsider.com/perplexity-makes-200-ai-browser-free-to-battle-ai-slop-2025-10 (Comet 免费 + $200 Max 门槛)
- **2 个 Datadome-protected (URL 真实但 bot 拦截)**:
  - Reuters NYT 起诉 URL (HTTP 401 + x-datadome: protected)
  - Reuters Microsoft Azure 协议 URL (HTTP 401)
- **1 个 paywalled**: The Information 200 亿估值 (HTTP 403)
- **6 个 inferred URL 被移除** (CNBC×3、Verge 推定、MacRumors 推定、Reuters 旧推定路径)

#### 修改文件

- `analyses/ai-assisted/2026-07-01-perplexity.md`:
  - YAML source_urls 增 3 个 verified、替换 6 个 inferred、2 个 Reuters URL 保留(datadome 注释)
  - source_quality_notes 记录 P4.2 恢复过程与仍为 partial 的原因
  - Sources Quality Media 小节表格重写，每条加状态+备注
  - §17.2 可信度分级：Comet 时间线保持高; 估值/Chrome/Azure 仍为低
  - §17.5 验证表分 P4.1 与 P4.2 两阶段
  - 文末状态标注增加 P4.2 轮次

- `README.md`: AI 索引 Perplexity 状态仍为 `partial` (P4.2 后未升到 verified)

#### 新增文件

- `reports/P4.2-perplexity-verified-source-recovery-report.md`

### 保留

- 9 篇旧文章、CHANGELOG 旧条目、主体内容、1-16 章节主体未动
- pic/ 未动
- templates 未动
- docs/source-quality-checklist.md 未动

### P4.2 状态说明

- `source_url_verification_status` 仍为 `partial`
- 主体产品事实(Comet 推出/免费/商业模式)已有 3+ verified 源
- 估值/Chrome 报价/Azure 协议仍主要依靠 paywalled 或 Datadome-protected 源
- 估值与 Chrome 报价保持"低"可信度

### P4.2 目标达成

- [x] 主动检索与验证可访问的 verified 主体源
- [x] 替换 P4.1 中标记的 6 个 inferred URL
- [x] 在 YAML 中标注新的 source_url_verified_at 与 quality notes
- [x] Sources 区每条 verified URL 有 type/status/used_for/note
- [x] §17.5 验证表分两阶段
- [x] 诚实评估仍为 partial 的原因
- [x] P4.2 报告生成

---

## P4.1 - Perplexity Source URL Verification

**日期：** 2026-07-01
**变更类型：** source-verification / docs-only
**变更范围：** Perplexity 一文 + 模板 + docs + README + CHANGELOG

### 变更内容

对 P4 中添加的高质量媒体 URL 做实链验证，发现推定路径需修正。

#### 验证结果

- **仅 1 个主体来源被 HTTP 200 验证**：AWS 官方案例
- **7 个 high-quality-media-verified (planned) URL 中 6 个未能验证**：
  - CNBC × 3 为 404
  - The Verge 路径返回 400
  - MacRumors 返回 522（超时）
  - The Information 被 Cloudflare 拦截
  - Reuters 超时
- **perplexity.ai 与 /enterprise**：timeout 未能取得正文但页面推定存在
- **SourceForge**：被 Cloudflare 拦截

#### 修改文件

- `analyses/ai-assisted/2026-07-01-perplexity.md`：
  - YAML 新增 `source_url_verified_at`, `source_url_verification_status: partial`, `source_quality_notes`
  - Sources 中 “Quality Media” 小节所有 URL 状态改为 `unverified` 并附备注
  - 新增 `§ 17.5 Sources 实链验证` 表格
  - § 17.2 可信度分级表中估值/Chrome/Azure 三条从"中"降为"低"
  - Sources 末尾说明重写，诚实评估“主要事实依据仍是中文转载”
  - 文末状态标注增加 “P4.1 - Source URL Verification”轮次

- `templates/product-analysis-template.md`：
  - YAML front matter 示例增加 `source_url_verified_at` / `source_url_verification_status` / `source_quality_notes` 三字段
  - 第 17 章增加 `17.4 Sources 实链验证` 子节

- `README.md`：AI 辅助分析索引增加“来源状态”列；Perplexity 状态填 `partial`

#### 新增文件

- `docs/source-quality-checklist.md`：来源质量门禁（分级、最低要求、draft→reviewed→verified 条件、URL 验证流程、常见错误）
- `reports/P4.1-perplexity-source-url-verification-report.md`

### 保留

- 9 篇旧文章、CHANGELOG 旧条目、主体内容、1-16 章节主体未动
- pic/ 未动
- templates 增加内容是追加不破坏原有结构

### 诚实评估

P4 阶段“高质量媒体为主来源”的声明是**高估**的。本轮 P4.1 修正了这一评估。中文转载（new.qq.com / so.html5.qq.com）是**目前唯一被明确验证可访问的报道载体**。P5 阶段需手动查实实际原报道 URL。

### P4.1 目标达成

- [x] 实链验证 10 个主体质量来源
- [x] 替换 / 降级未验证 URL
- [x] YAML 新增 3 个字段
- [x] § 17.5 Sources 实链验证 表格
- [x] 17.2 可信度分级同步调整
- [x] 模板增加 17.4 占位 + YAML 字段
- [x] docs/source-quality-checklist.md 新建
- [x] README 增加来源状态列
- [x] CHANGELOG P4.1 记录
- [x] P4.1 报告生成

---

## P4 - Perplexity Review and Source Hardening

**日期：** 2026-07-01
**变更类型：** content-review / source-hardening
**变更范围：** Perplexity 一文 + 模板 + README + CHANGELOG

### 变更内容

对 P3 产出的第一篇 AI 辅助产品分析进行人工复核与来源加固。

#### 修改文件

- `analyses/ai-assisted/2026-07-01-perplexity.md`：
  - YAML front matter：`review_status: draft` → `reviewed`
  - YAML front matter：增加 `reviewed_at` 和 `review_notes` 字段
  - 增加「17. 人工复核结论」章节（17.1 复核结论 / 17.2 可信度分级 / 17.3 对后续 AI 分析的改进 / 17.4 后续需主动更新的点）
  - 重写 Sources 区域，分为五组：Official / Quality Media / Infrastructure / News (中文转载) / Secondary
  - 增加可信度分级表（高/中/低/待观察），明示哪些是事实哪些是推演
  - 更新文末状态标注为 `reviewed`

- `templates/product-analysis-template.md`：增加「17. 人工复核结论」占位章节（17.1/17.2/17.3）

- `README.md`：AI 辅助分析索引中 Perplexity 状态从 `draft` 改为 `reviewed`

#### 新增文件

- `reports/P4-perplexity-review-and-source-hardening-report.md`

### 保留

- 9 篇旧文章、CHANGELOG 旧条目、`docs/`、`pic/`、`analyses/ai-assisted/2026-07-01-perplexity.md` 主体正文均未动
- 主体叙述、机制分析、复盘判断保持原状；本轮仅做事实复核、来源加固、可信度分级

### Sources 统计

- 官方来源：3 个（perplexity.ai, /enterprise, AWS case study）
- 高质量媒体：7 个（CNBC × 3, The Verge, MacRumors, Reuters, The Information）
- 中文转载：12 个（new.qq.com / so.html5.qq.com，仅作补充）
- 低置信源：1 个（SourceForge）
- 总计：23 个 URL（从 P3 的 13 个增加 10 个，结构化分组）

### P4 目标达成

- [x] `review_status` 改为 `reviewed`
- [x] `reviewed_at` 和 `review_notes` 加入 YAML
- [x] Sources 分五组重写
- [x] 17. 人工复核结论 章节加入（17.1/17.2/17.3/17.4）
- [x] 可信度分级表（高/中/低/待观察）
- [x] 模板增加「17. 人工复核结论」占位
- [x] README 状态同步
- [x] CHANGELOG P4 记录
- [x] P4 报告生成

---

## P3 - First AI-Assisted Product Analysis: Perplexity

**日期：** 2026-07-01
**变更类型：** 新增内容
**变更范围：** AI 辅助产品分析首篇

### 变更内容

新增第一篇 AI 辅助产品分析，使用 `templates/product-analysis-template.md` 结构。

#### 新增文件

- `analyses/ai-assisted/2026-07-01-perplexity.md` — Perplexity 全 16 维度分析
- `reports/P3-perplexity-ai-assisted-analysis-report.md` — P3 报告

#### 修改文件

- `README.md` — 新增"AI 辅助分析索引"小节
- `CHANGELOG.md` — 顶部增加 P3 记录

### 文章覆盖

- 16 维度全分析（一句话定位 / 目标用户 / 核心场景 / 解决的问题 / 首页 / 用户路径 / IA / 交互 / 内容增长 / 商业模式 / 竞品 / 优点 / 问题 / 重做 / 启发 / 复盘）
- 公开 sources 列表（13 个 URL + 来源类型）
- 明确区分事实 / 推断 / 判断

### 状态

- 文章状态：`review_status: draft`（等待人工复核）
- 区分证据强弱：在文中用 `[事实]` `[事实+判断]` `[判断]` 标注

### P3 目标达成

- [x] 按模板产出第 1 篇 AI 辅助分析
- [x] 公开资料检索（13 个来源）
- [x] 区分事实 / 推断 / 判断
- [x] README 增加 AI 分析索引
- [x] CHANGELOG 增加 P3 记录
- [x] 生成 P3 报告

---

## P2.5 - Add P1 Archive Upgrade Report

**日期：** 2026-07-01
**变更类型：** reports-only
**变更范围：** 补齐 P1 报告入库

- 将 `reports/P1-archive-upgrade-report.md` 纳入 git 跟踪
- commit: `P2.5: add P1 archive upgrade report`

---

## P2 - Product Hunt Legacy Review

**日期：** 2026-07-01
**变更类型：** 内容补充
**变更范围：** 1.Product-Hunt.md 末尾追加复盘章节

### 变更内容

为 `1.Product-Hunt.md` 追加"今日复盘"章节，从旧框架（特点/问题/设想）升级为 14 维度分析框架。

#### 复盘内容

- 一句话重新定位
- 真正解决的问题（三类用户）
- 核心机制拆解（7 机制 × 4 维度表）
- 信息架构分析
- 社区机制分析（4 个"为什么"）
- 早期笔记中判断准确的地方
- 早期笔记中可以深化的地方
- 如果我来重做一个中文 Product Hunt
- 可迁移到我自己项目的启发
- 小结

#### 新增报告

- `reports/P2-product-hunt-legacy-review-report.md`

### 保留

- `1.Product-Hunt.md` 原始正文（YAML metadata + 特点/问题/设想）完全未改
- `pic/` 目录及所有图片未动
- 其他 8 篇旧文章未动

---

## P1 - Product Analysis Archive Structure

**日期：** 2026-07-01
**变更类型：** 结构升级
**变更范围：** README、新增文档、新增模板、旧文章 metadata

### 变更内容

#### 新增文件

| 文件 | 说明 |
|------|------|
| `docs/product-analysis-framework.md` | 产品分析框架 v1.0（14维度，旧框架升级） |
| `docs/ai-assisted-analysis-workflow.md` | AI 辅助分析工作流（10步骤） |
| `templates/product-analysis-template.md` | 文章标准模板（含 YAML front matter） |
| `templates/ai-product-analysis-prompt.md` | AI 分析提示词模板 |
| `analyses/ai-assisted/README.md` | AI 分析区目录说明 |
| `CHANGELOG.md` | 变更记录 |

#### 修改文件

| 文件 | 说明 |
|------|------|
| `README.md` | 重写，新增项目定位、目标、索引表、主题总结、使用指南 |
| `1.Product-Hunt.md` | 顶部增加 YAML metadata |
| `2.700bike.md` | 顶部增加 YAML metadata |
| `3.The-Synopsis.md` | 顶部增加 YAML metadata |
| `4.Hackster-io.md` | 顶部增加 YAML metadata |
| `5.making-society.md` | 顶部增加 YAML metadata |
| `6.open-library.md` | 顶部增加 YAML metadata |
| `7.Daniel-Nordness.md` | 顶部增加 YAML metadata |
| `8.HackDesign.md` | 顶部增加 YAML metadata |
| `9.OpenROV.md` | 顶部增加 YAML metadata |

### 保留内容（未改动）

- `pic/` 目录及所有图片
- 旧文章正文内容（仅顶部增加 metadata，未修改正文）
- 原有 git 历史

### 新增目录

```
docs/                      # 方法论文档
templates/                # 标准化模板
analyses/ai-assisted/     # AI 辅助分析文章
```

### P1 完成标准

- [x] README 重写，包含项目定位、索引表、使用指南
- [x] 产品分析框架文档
- [x] AI 辅助分析工作流文档
- [x] 文章标准模板
- [x] AI 分析提示词模板
- [x] AI 分析区目录
- [x] 旧文章 metadata 标记
- [x] CHANGELOG 记录

---

*初始版本记录于 2026-07-01*
