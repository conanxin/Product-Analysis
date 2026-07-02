# Changelog

## P27 - Coda Review and Index Status Sync

**日期：** 2026-07-02
**变更类型：** review + source-hardening + index-sync + validation

### 变更内容

完成 P26 Coda draft 人工复核，升级 status draft → reviewed，并同步所有索引。

#### 主要升级

**P27 source-hardening 新增 16 个 HTTP-200 验证 URL：**
1. superhuman.com × 8
2. grammarly.com/blog/company × 3
3. grammarly.com/press × 1
4. blog.superhuman.com × 2
5. coda.io × 4（learn / use-cases / solutions / case-studies）

**两顶关键事实从 partial 升级为 verified-primary：**
1. **Oct 2025 Grammarly → Superhuman rebrand**：
   - grammarly.com/press (Superhuman Newsroom) — 列出 "Grammarly Rebrands Company as Superhuman"
   - grammarly.com/blog/company/announcing-company-rebrand-to-superhuman — article:published_time 2025-10-29
   - superhuman.com/ — 新产品 hub 包含 Mail / Grammarly / Coda / Go / Agent Store
2. **Superhuman Suite 组成**：Mail / Grammarly / Coda / Go 由 superhuman.com/ + superhuman.com/products/* 官方产品页多源 verified

**仍为 partial 的高风险事实（说明受限于媒体 paywall）：**
- $60M / $80M / $100M funding rounds（Wikipedia 二手，未独立验证）
- $1.4B 2021 valuation（Forbes paywall）
- Dec 2024 acquisition amount（primary source 明确 "金额未披露"）
- 800+ vs 600+ integrations（官方源数字不一致）
- Coda Brain 产品页（coda.io/product/coda-brain 301→ 403 Cloudflare）
- coda.io/pricing 具体金额（200 但抓取未含）
- 50,000+ teams / 40M Grammarly users（单一官方源，未独立验证）

#### 修改文件

1. **analyses/ai-assisted/2026-07-01-coda.md**
   - YAML front matter:
     - review_status: draft → reviewed
     - reviewed_at: null → 2026-07-01
     - review_notes: 升级为 P27 reviewed 正式版本（引用源增加 16 个）
     - source_quality_notes: 升级为 P27 source-hardening 版本
     - source_urls: 55 → 71（新增 16 个 verified URL）
   - §1 一句话定位：新增 [事实] P27 source-hardening 验证段
   - §16 今日复盘：新增第 3 条 P27 source-hardening 教训
   - §17.1 当前状态：升级为 P27 reviewed
   - §17.2 可信度分级：新增 3 行 verified-primary（rebrand / Superhuman suite / rebrand partial→verified）
   - §17.4 Sources 实链验证表：新增 5 行 Official/Primary + 13 行 Verified Partner/Acquirer（Superhuman + Grammarly blog + press + product hub）

2. **README.md**
   - AI 辅助分析索引：Coda 行 status draft → reviewed
   - 当前质量状态：AI 辅助分析 11 → 11 (全部 reviewed) / reviewed 10 → 11 / draft 1 → 0 / partial 11 → 11

3. **analyses/README.md**
   - AI 辅助分析总览：Coda 行 status draft → reviewed + 一句话洞察更新（添加 "2025-10 Superhuman rebrand"）
   - 当前质量状态：同步 reviewed 10 → 11 / draft 1 → 0 / P 报告累计 17 → 18

4. **analyses/index.yml**
   - updated_at: 2026-07-01 → 2026-07-02（保持）
   - Coda 条目：review_status draft → reviewed / reviewed_at null → 2026-07-01
   - quality_notes 升级：P27 source-hardening 详细说明
   - summary: total 11 / reviewed 10 → 11 / draft 1 → 0 / partial 11 → 11 / p_reports_total 17 → 18

5. **CHANGELOG.md** — 顶部 prepend P27 记录

6. **reports/P27-coda-review-and-index-status-sync-report.md** (new)

#### 验证结果

```
$ python3 scripts/verify_ai_analysis_index.py
初跑 FAIL (8 项):
 1. index.yml summary.reviewed expected 11, got 10
 2. index.yml summary.draft expected 0, got 1
 3. 2026-07-01-coda.md field 'review_status': article='reviewed' != index='draft'
 4. 2026-07-01-coda.md reviewed_at: article='2026-07-01' != index=None
 5. README.md 质量状态表 reviewed expected 11, got 10
 6. README.md 质量状态表 draft expected 0, got 1
 7. analyses/README.md 质量状态表 reviewed expected 11, got 10
 8. analyses/README.md 质量状态表 draft expected 0, got 1

原因：article YAML 已升级但 index files 仍为 draft。修复后复跑：

$ python3 scripts/verify_ai_analysis_index.py
PASS: AI analysis index consistency verified
- analyses found: 11
- reviewed: 11
- draft: 0
- partial: 11
- verified: 0
```

P27 验证了 P24/P25 的核心机制：**validator 自动发现状态漂移**，防止 review 状态未同步问题。

#### 未修改文件

- scripts/verify_ai_analysis_index.py — 未动
- 旧 10 篇 AI 辅助分析文章 — 未动
- 旧人工分析文章 — 未动
- pic/ / templates/ — 未动
- .github/workflows/ai-analysis-index-check.yml — 未动
- docs/* — 未动

#### CHANGELOG 历史记录保留

P27 不覆盖 P26 / P25 / P24 / P23.1 / P23 / P22.1 / P22 历史记录。完整 changelog 包含 17+ 项 P 任务记录。

## P26 - Coda AI-Assisted Product Analysis

**日期：** 2026-07-02
**变更类型：** AI-assisted content + index sync

### 变更内容

新增第十一篇 AI 辅助产品分析 Coda，严格遵守 source-first workflow。

#### 新增文件

1. **analyses/ai-assisted/2026-07-01-coda.md** (new, 618 lines)
   - 17 节正文 + 55 个 source_urls
   - YAML front matter 使用 custom StrictSafeLoader 可解析
   - review_status: draft
   - source_url_verification_status: partial
   - one_line_insight: Coda 将文档、表格、公式、按钮、自动化和应用集成组合成同一个 doc-as-app 工作台

2. **reports/P26-coda-ai-assisted-analysis-report.md** (new)

#### 修改文件

1. **README.md**
   - "AI 辅助分析索引" 表格新增 Coda 行
   - "当前质量状态" 更新: 10 → 11 (AI 辅助分析) / 0 → 1 (draft) / 10 → 11 (partial)
   - "下一步计划" 新增 P26 todo
   - "最后更新" 改为 P26 记录

2. **analyses/README.md**
   - "AI 辅助分析总览" 表格新增 Coda 行
   - "按产品类型分组" 新增 "Doc Database / App Doc" 分类
   - "当前质量状态" 同步更新
   - "下一步分析候选" 移除 Coda
   - "推荐阅读路径" 新增 "Doc-as-App 路线"

3. **analyses/index.yml**
   - updated_at: 2026-07-01 → 2026-07-02
   - 新增 Coda 条目（product / file / category / analysis_type / created_at / review_status / reviewed_at / source_url_verification_status / tags / one_line_insight / quality_notes）
   - summary 更新: total 10→11 / draft 0→1 / partial 10→11 / p_reports_total 16→17
   - by_category 新增 doc-database / Coda
   - reading_paths 新增 doc_as_app_path: Notion → Coda

4. **CHANGELOG.md** — 顶部 prepend P26 记录

### Source-First Workflow

P26 遵循 P22 起实行的 source-first 原则：
1. 先收集并验证 Coda 相关 URL（55 个 source_urls 实链验证）
2. 使用 Coda 官方 blog (coda.io/blog/about-coda/grammarly-acquires-coda) 作为 2024-12 Grammarly 收购的 primary source
3. Wikipedia (Coda document editor / Grammarly) 作为 reference source
4. Grammarly 官方产品页 (grammarly.com/coda) 作为 partner-official source
5. 主流媒体 (Axios / TechCrunch / CNBC / Forbes / Fast Company / Bloomberg) paywall / 403 / 401 / 404 不可直接访问，因此融资 / 估值 / ARR / 用户量 / Superhuman rebrand 仍 partial

### Source URL 实链验证结果

| 类型 | 数量 | 状态 |
|------|---:|------|
| Coda 官方主页 / 产品 / Packs / 集成 / 安全 / Trust | 30+ | verified (200) |
| Coda Blog（Grammarly 收购 / 高级功能 / Grammarly 案例） | 3 | verified (200) |
| Coda 模板 / Packs 详情页 | 9 | verified (200) |
| Grammarly 官方产品页（含 Coda 入口） | 7 | verified (200) |
| Wikipedia 参考（Coda document editor / Grammarly） | 2 | verified (200) |
| Cloudflare protected (coda.io/product/coda-brain / help.coda.io) | 2 | 301→403 |
| 重定向 (coda.io/enterprise / templates / ai / api) | 4 | 301 redirect |
| 404 (coda.io/automations / buttons / tables / press / announcements) | 5 | 404 |
| 主流媒体 paywall (Fast Company / Axios / CNBC / Bloomberg / Crunchbase) | 5+ | 403 / paywall |

总计 source_urls: 55，全部实链可达或说明状态

### 产品定位（严格遵循 P26 任务要求）

- Coda 是 **被 Grammarly 收购** 的 **私人生产力 / doc-as-app 产品**（不是公开公司）
- 当前定位: AI productivity / doc-database / app-doc / Grammarly-Superhuman productivity suite doc engine
- 高风险事实默认 partial（融资 / 估值 / 收购金额 / 用户数 / ARR / Superhuman 整合效果）
- 唯一双源验证的: Grammarly 收购事实 (coda.io blog primary + Wikipedia reference)

### validator 验证结果

```
$ python3 scripts/verify_ai_analysis_index.py
PASS: AI analysis index consistency verified
- analyses found: 11
- reviewed: 10
- draft: 1
- partial: 11
- verified: 0
```

初跑发现 1 项真实错误（index.yml 中 review_status 字段冒号被解析为 YAML key），已修复。

### 未修改文件

- scripts/verify_ai_analysis_index.py — 未动
- 旧 10 篇 AI 辅助分析文章 — 未动
- 旧人工分析文章 — 未动
- pic/ / templates/ — 未动
- .github/workflows/ai-analysis-index-check.yml — 未动
- docs/* — 未动

### CI 状态

- P25 GitHub Actions CI 仍正常
- 此次 Coda 文章中 `review_status: draft` + `source_url_verification_status: partial` 是 AI-assisted draft 标志，不是 failure

## P25 - AI Analysis Index Validation CI

**日期：** 2026-07-02
**变更类型：** CI / validation / docs-only

### 变更内容

把 P24 本地验证脚本接入 GitHub Actions CI，提供自动拦截机制。

#### 新增文件

1. **.github/workflows/ai-analysis-index-check.yml** (~600 bytes)
   - workflow name: AI Analysis Index Check
   - 触发：push / pull_request / workflow_dispatch
   - job: verify-ai-analysis-index
   - runs-on: ubuntu-latest
   - steps:
     1. actions/checkout@v4
     2. actions/setup-python@v5 (python-version: "3.x")
     3. pip install PyYAML
     4. python3 scripts/verify_ai_analysis_index.py

2. **reports/P25-ai-index-validation-ci-report.md** (new)

#### 修改文件

1. **docs/index-sync-validation.md** — 新增 §8 GitHub Actions CI 章节
2. **README.md** — "如何校验索引一致性" 小节增加 CI 说明 + P25 todo + 最后更新
3. **CHANGELOG.md** — 顶部 prepend P25 记录

### 未修改文件

- scripts/verify_ai_analysis_index.py — 未动
- analyses/ai-assisted/*.md — 未动
- analyses/index.yml — 未动
- analyses/README.md — 未动
- 旧人工分析文章 — 未动
- pic/ / templates/ — 未动

### CI 设计原则

- 仓库纯 Markdown + YAML，不需 Node.js / build step
- 验证纯本地可计算，无需外部网络（不检查 HTTP 200）
- 快速反馈（CI 运行 < 30 秒）
- 避免误报（只检查结构性一致性）

### CI 失败处理

1. 查看 workflow log (GitHub Actions 页面)
2. 本地运行同一命令
3. 根据错误列表修复:
   - README.md / analyses/README.md 质量状态表数字
   - analyses/index.yml summary / entry 字段
   - 文章 YAML front matter
4. 重新 push 或重试 workflow

### 验证

```
$ python3 scripts/verify_ai_analysis_index.py
PASS: AI analysis index consistency verified
- analyses found: 10
- reviewed: 10
- draft: 0
- partial: 10
- verified: 0
```

workflow YAML 解析 OK (PyYAML yaml.safe_load)。

## P24 (Final) - AI Index and YAML Consistency Validator

**日期：** 2026-07-02
**变更类型：** tooling / validation / docs-only + data-fix

### 变更内容

P24 (70defde) + P24.1 (db5a5ab) 两轮迭代后，最终重写为简洁输出格式，修复 12 项真实数据问题后 PASS。

#### 脚本 (scripts/verify_ai_analysis_index.py)

- 自定义 SafeLoader 检测重复 key (P22.1 教训)
- 11 大类检查约 30+ 子项
- 简洁输出：`PASS: AI analysis index consistency verified` / `FAIL: AI analysis index consistency errors`
- 错误列表用编号 `1. ... 2. ... 3. ...`
- 底部统计 `analyses found / reviewed / draft / partial / verified`

#### 文档 (docs/index-sync-validation.md)

- 6 节：为什么需要 / 检查什么 / 如何运行 / 何时运行 / 失败处理 / 后续扩展
- 表格列出所有检查项 + 常见失败模式 + 修复方法

#### README

- 新增"如何校验索引一致性"小节
- 添加 todo + 最后更新行

#### 修复的 12 项真实数据问题

| # | 文件 | 问题 | 修复 |
|---|------|------|------|
| 1 | cursor.md line 77 | review_notes 未加引号冒号 | 加双引号 |
| 2 | cursor.md line 80 | source_quality_notes 未加引号冒号 | 加双引号 |
| 3 | perplexity.md line 47 | source_quality_notes 未加引号冒号 | 加双引号 |
| 4 | raycast.md line 51 | source_quality_notes 未加引号冒号 | 加双引号 |
| 5-13 | index.yml × 9 entries | one_line_insight 引号风格不一致 | 从 article 同步 |

### 验证

```
$ python3 scripts/verify_ai_analysis_index.py
PASS: AI analysis index consistency verified
- analyses found: 10
- reviewed: 10
- draft: 0
- partial: 10
- verified: 0
```

### 未修改

- analyses/README.md (已正确)
- pic/ / templates/

### 教训沉淀

- PyYAML yaml.safe_load 会静默覆盖重复 key — 必须自定义 SafeLoader
- 长 YAML 值 (含冒号 / 方括号 / 复杂标点) 必须加双引号包裹
- one_line_insight 在 article 和 index.yml 必须严格字符串一致 (引号风格也要统一)
- 后续 P* 任务报告需含 python3 scripts/verify_ai_analysis_index.py 运行结果

## P24.1 - Validation Script Output Format Revision

**日期：** 2026-07-02
**变更类型：** automation-refinement / docs-only

### 变更内容

P24 (70defde) 交付了初版验证脚本，P24.1 根据用户反馈修订：

1. **输出格式** — 改为规范的 `PASS: AI analysis index validation passed` / `FAIL: AI analysis index validation failed` 格式 + 错误代码 `[CODE] message`
2. **简化产品行检查** — 不再解析完整 Markdown 表格，改用稳健的字符串匹配（产品名存在 + 行含 expected status）
3. **脚本精简** — 从 ~22 KB 缩减到 ~13 KB，移除 ANSI 颜色 / Report class 等非必要代码
4. **docs/validation-workflow.md 重写** — 增加错误代码表、常见失败模式表、3 种工作流
5. **README 质量状态检查修正** — 不检查 `total`（README 表格用 `AI 辅助分析` 而非 `total`）

### 首次运行结果

84 项检查 → 75 通过 / 9 失败（3 YAML scan errors + 6 one_line_insight 引号不一致）

### 未修改

- analyses/ai-assisted/*.md
- analyses/index.yml
- analyses/README.md
- 旧人工分析文章
- pic/

## P24 - AI Analysis Index Validation Script

**日期：** 2026-07-02
**变更类型：** automation / validation / docs-only
**变更范围：** scripts/ + docs/validation-workflow.md + README.md + reports/P24-*

### 变更内容

新增 Product-Analysis 仓库的本地可运行验证脚本，统一检查 AI 辅助分析文章的索引一致性 + YAML 质量。

#### 新增文件

1. **scripts/verify_ai_analysis_index.py** (~22 KB)
   - Python 3.10+ 标准库 + PyYAML 依赖
   - 退出码：0 = PASS / 1 = FAIL
   - 11 大类检查，约 80 子项：
     1. YAML 依赖检查 (PyYAML 安装)
     2. Front matter 提取 (analyses/ai-assisted/YYYY-MM-DD-*.md 扫描)
     3. 重复 YAML key 检测 (自实现 top-level key 计数器，P22.1 教训)
     4. YAML 解析 + 11 必备字段 (product / category / tags / source_urls / analysis_type / created_at / review_status / source_url_verified_at / source_url_verification_status / source_quality_notes / one_line_insight)
     5. source_urls 格式检查 (list / string / http(s):// 前缀 / markdown 分隔符 / inline annotation)
     6. analyses/index.yml 解析 (analyses list + summary + 10 字段 entry)
     7. summary count 一致性 (动态计算 vs summary 字段)
     8. article YAML ↔ index.yml 一致性 (8 字段: product / category / analysis_type / review_status / source_url_verification_status / one_line_insight / tags / reviewed_at)
     9. README.md 当前质量状态检查 (动态期望值 vs 表格实际值)
     10. analyses/README.md 当前质量状态检查 (同上，小节标题 `## 3. 当前质量状态`)
     11. 产品状态行一致性 (README.md AI 索引 + analyses/README.md AI 总览)

2. **docs/validation-workflow.md** (~5 KB)
   - 工作流文档
   - 4 类常见失败模式与修复方法
   - 新增文章 / 复核升级 / 漂移修复 3 种工作流
   - 后续 P* 报告应引用 `python3 scripts/verify_ai_analysis_index.py` 运行结果

3. **reports/P24-ai-analysis-index-validation-script-report.md**
   - P24 任务报告

4. **README.md** (顶部 todo + 最后更新)
   - todo: P24 记录
   - 最后更新: P24 描述

### 首次运行结果

P24 首跑 `python3 scripts/verify_ai_analysis_index.py` 共检查 84 项，通过 75 项，失败 9 项：

- **3 项 YAML scan errors** (Cursor / Perplexity / Raycast): `source_quality_notes` 或 `review_notes` 包含未加引号的冒号 `:` 造成 PyYAML 解析失败
- **6 项 article↔index one_line_insight 不一致** (Figma / Framer / Linear / Notion / Replit / Webflow): 文章内为双引号 `"..."`，index.yml 为单引号 `'...'`

### 未修改的文件

- analyses/ai-assisted/*.md — 未动 (包含 Cursor/Perplexity/Raycast YAML 错误，留给后续 P* 修复)
- analyses/index.yml — 未动 (包含 6 个 one_line_insight 引号不一致)
- analyses/README.md — 未动
- 旧人工分析文章 — 未动
- pic/ — 未动
- templates/ — 未动

### 教训沉淀

- P24 验证脚本不能代替修复：脚本能检出问题，修复仍需后续 P24.1 / P24.2 任务
- 关键检查点:
  1. 写 YAML 文本值（含冒号/方括号）必须加引号或转义
  2. one_line_insight 在文章和 index.yml 必须严格一致
  3. 同步索引时不仅要改 article YAML / index.yml / analyses/README.md / README.md 4 处，所有引用同一数据 (reviewed count) 的统计表格也要同步

### 后续 P24.x 候选

- P24.1: 修复 Cursor / Perplexity / Raycast YAML scan errors (加引号)
- P24.2: 修复 6 个 one_line_insight 双引号 vs 单引号不一致
- P24.3: 把 `python3 scripts/verify_ai_analysis_index.py` 接入 GitHub Actions 作为 CI 门禁

---

## P23.1 - Replit README Quality Status Drift Fix

**日期：** 2026-07-01
**变更类型：** index-fix / docs-only
**变更范围：** README.md (质量状态表 + P23.1 todo + 最后更新)

### 变更内容

修复 P23 后 README.md 当前质量状态仍停留在 9 reviewed / 9 partial 的索引漂移。

#### 修复前 vs 修复后

| 项目 | 修复前 | 修复后 | 变更 |
|------|--------|--------|------|
| Replit 文章 YAML | reviewed\|partial | reviewed\|partial | 未变 |
| analyses/README.md Replit 行 | reviewed\|partial | reviewed\|partial | 未变 |
| analyses/README.md 质量状态 | 10/10/0/10 | 10/10/0/10 | 未变 |
| analyses/index.yml Replit entry | reviewed\|partial | reviewed\|partial | 未变 |
| analyses/index.yml summary | 10/10/0/10 | 10/10/0/10 | 未变 |
| **README.md Replit 行** | reviewed\|partial | reviewed\|partial | 未变 (P23 已改) |
| **README.md 当前质量状态** | **9/9/0/9 (错误)** | **10/10/0/10 (正确)** | **P23.1 修复** |

#### P23.1 修改的具体位置 (README.md)

1. "当前质量状态" 表格：
   - `| AI 辅助分析 | 9 | 9 reviewed |` → `| AI 辅助分析 | 10 | 全部 reviewed |`
   - `| - reviewed | 9 | 人工复核完成 |` → `| - reviewed | 10 | 人工复核完成 |`
   - `| - partial | 9 | 主体产品功能 verified；高风险事实 partial |` → `| - partial | 10 | 主体产品功能 verified；高风险事实 partial |`

2. 下一步计划 (todo list):
   - 新增 `[x] P23.1: 修复 Replit 复核后 README 质量状态漂移...`

3. 最后更新行:
   - 替换为 P23.1 描述

#### 未修改的文件

- analyses/ai-assisted/2026-07-01-replit.md — 已为 reviewed\|partial
- analyses/README.md — 已是正确状态
- analyses/index.yml — 已是正确状态
- 其他 AI 分析文章 — 未动
- 旧人工分析文章 — 未动
- pic/ — 未动
- templates/ — 未动

#### 教训沉淀

- P23 同步四文件时只改了 README.md 的"Replit 行"和最后更新，未改"当前质量状态"统计表
- 后续 P* 任务必须同时检查: 行状态 / 质量状态统计 / 文章 YAML / 索引文件 / 报告路径 五处一致性
- 教程: 同步索引时不仅改单行,需同步该处所有引用同一数据的统计 / 计数表格

---

## P23 - Replit Review and Index Status Sync

**日期：** 2026-07-01 (second-pass refinement 跟进 P22.1 / P23)
**变更类型：** review / source-credibility-grading / index-sync (second-pass P23 refinement)
**变更范围：** analyses/ai-assisted/2026-07-01-replit.md (补充 §17.3 + §17.4 source count 口径) + reports/P23-replit-review-and-index-status-sync-report.md (扩充 Speculative / Pricing / Funding / Agent safety final wording)

### 变更内容 (P23 second-pass)

补充 P22 与 P23 后续任务明确点：在 P23 a4cb31f 已完成 status 升级的基础上，补充 P23 task 明确要求的 §17.3 / §17.4 / P23 报告 detail:

#### §17.3 补充 P23 教训 (在原文 §17.3 中整合)

- YAML duplicate key 必须自动检查 (P22.1 教训)
- PyYAML safe_load 会静默覆盖重复 key (P22.1 教训)
- source count 必须分口径统计 (P23 厘清 — YAML source_urls 计数 vs HTTP-200 verification 总数)
- Wikipedia reference 和 media direct verified 必须分开 (P23 修订)
- Pulse 2.0 / SaaStr 属可访问二线媒体，不能等同 Reuters / Forbes / Bloomberg / TechCrunch / WSJ / Business Insider
- Agent 事故必须区分个案事实、系统风险、设计启发 (不泛化)
- index.yml 必须随 review_status 状态同步更新
- 新增文章后必须检查 README / analyses/README / index.yml / article YAML 四处一致性

#### §17.4 source count 口径汇总表

- 补充 YAML source_urls (75) vs HTTP-200 verification (≥81) 口径区别表
- 补充备份/重定向 URL 计数
- 明确 Unverified 主流媒体列表
- 明确 Replit 官方 404/重定向列表

#### P23 报告 (second-pass) 扩充

- Speculative Claims Marked 表 (云端应用工作台 / AI app builder platform / 从想法到上线 / Agent 采用率 / 中文 MVP / Agent 事故泛化 — 均标 [判断] / partial)
- Pricing Final Wording (仅 docs.replit.com/billing/* verified 200;5 档明示;usage-based + AI billing 明示)
- Funding / Valuation / Revenue Final Wording ($4.5M seed 高 / $97.4M 低-中 / $250M Series C 中 / $400M Series D 中 / $150M ARR 中 / 40M+ users 低-中 / Microsoft Azure 中)
- Agent / Safety Incident Final Wording (事件事实高 / 官方治理高 / 不泛化)

### P23 合并状态保留

a4cb31f P23: review Replit analysis and sync index status — 主含:review_status 升级 + Series C/D 解决 + 4 文件同步 + 主章 body 修订。本 second-pass 扩充 P23 报告验证细节 + §17.3 教训 + §17.4 source count 表。



**日期：** 2026-07-01
**变更类型：** review / source-credibility-grading / index-sync
**变更范围：** analyses/ai-assisted/2026-07-01-replit.md (修订) + README + analyses/README.md + analyses/index.yml + CHANGELOG + P23 报告

### 变更内容

对 Replit AI 辅助分析进行 P23 人工复核，将 review_status 从 draft 升为 reviewed；修正轮次字母不一致事实问题；厘清 source count 口径。

#### P23 复核

**YAML 状态升级：**
- `review_status`: draft → reviewed
- `reviewed_at`: null → 2026-07-01
- `review_notes`: null → "Replit draft reviewed in P23; product claims checked against Replit official pages, docs, pricing, Agent 4, deployments, database/storage/auth/payments, Microsoft/Fabric integration, Wikipedia reference sources, and accessible verified media. Product mechanism is strongly supported by official sources; financing, valuation, revenue, Agent adoption, security incident frequency, and company-scale claims remain partial unless independently verified by at least two high-quality sources."
- `source_url_verification_status`: partial (未变 — 主流媒体 paywall 未变, 未达到 strict verified 标准)

**§17.2 轮次字母 — P23 解决：**
- `$250M / $3B / Series C 融资 2025-09` — Pulse 2.0 verified 200 文章正文明文 "secured $250 million in Series C funding, tripling its valuation to $3 billion"
- `$400M / $9B / Series D 融资 2026-03` — Pulse 2.0 verified 200 独立文章明文 "Series D"
- 原始 P22 提到 SaaStr 将 $250M 误标 "Series D" — P23 核实 SaaStr 为媒体错误:Pulse 2.0 有 2 篇独立文章区分 ($250M Series C vs $400M Series D)

**§17.3 source count 口径 — P23 厘清：**
- P22 报告将 "75 source URLs" 与 "41+33+8+1+1+11=95 HTTP-200 verification" 掎犬
- P23 厘清：YAML source_urls = 75 个 (replit.com 25 + docs.replit.com 33 + Wikipedia 2 + verified media 15);HTTP-200 verification 总数 含重定向/备份 URL 可达 95+, 两者不是同一口径, 后续 P* 报告需明确区分

**Body 手动复核事实校正 (minimal):**
- §17.1 升级: draft → reviewed;补充 P22.1 YAML 修复已完成 / P23 解决轮次不一致 / 仍为 partial
- §17.2 轮次字母中加入 P23 核实备注
- §17.3 加入 P22.1 修复 YAML 重复 key 反馈 + P23 厘清 source count + Series C vs D 轮次核实备注

#### 索引同步

- README AI 辅助分析索引: Replit 行 draft|partial → reviewed|partial
- README 顶部状态: P23 已记录
- README 最后更新: P22.1 → P23 描述 (10 reviewed + 0 draft)
- analyses/README.md 总览表: Replit 行 draft|partial → reviewed|partial
- analyses/README.md 质量状态表: draft 1 → 0;reviewed 9 → 10
- analyses/index.yml Replit entry: draft / reviewed_at null → reviewed / reviewed_at 2026-07-01
- analyses/index.yml summary: reviewed 9 → 10;draft 1 → 0;p_reports_total 15 → 16
- analyses/index.yml Replit quality_notes.reason 已更新 (P23 核实备注, Series C/D 解决, source count 厘清)
- yaml.safe_load 验证通过: Replit 文章 + index.yml 都可解析,无重复 key
- 仅 prepend, 未整文件覆盖;P22.1/P22/P21/P20/P19.1 历史未动

#### Replit 事实校正 (信源级别)

| 事实 | 校正前 | P23 校正 |
|------|--------|---------|
| $250M 轮次字母 | Pulse 2.0 标 Series C / SaaStr 标 Series D — 分歧 | Series C (Pulse 2.0 有独立文章明文) |
| $400M 轮次字母 | Pulse 2.0 标 Series D + 多元 — 同一 | Series D (Pulse 2.0 独立文章明文) |
| source count 口径 | 75 source URLs vs 95 HTTP-200 verification 冲突 | 厘清: YAML=75 / verification=http 包括重定向&备份 |
| YAML review_status | draft | reviewed |
| YAML reviewed_at | null | 2026-07-01 |

## P22.1 - Replit YAML Duplicate Key Fix

**日期：** 2026-07-01
**变更类型：** yaml-fix / docs-only
**变更范围：** analyses/ai-assisted/2026-07-01-replit.md (修订) + CHANGELOG + P22.1 报告

### 变更内容

修复 Replit YAML front matter 中重复的 `source_quality_notes` 字段。

#### P22.1 修复

**问题：** P22 提交的 Replit 文章 YAML front matter 中出现两个 `source_quality_notes:` 字段（line 94 + line 103）。PyYAML `yaml.safe_load` 会以后者覆盖前者，导致前面 1306 字符的详细 source-quality 说明被静默丢弃，只保留后面 70 字符的 "⚠️ 注意" 备注。

**修复：** 删除第二个重复字段 `source_quality_notes: | ⚠️ 注意...` 整段。

**保留：** 第一个字段的详细 source-quality 说明（1306 字符），包括 主体产品机制 verified / Wikipedia verified / 高质量媒体 verified / 高风险事实 partial / Replit 私人公司未 IPO / Agent 真实可用性 partial / 中文 MVP 属判断 等 P22 关键 source-quality 结论。

**未修改：**
- Replit 正文主体
- README.md
- analyses/README.md
- analyses/index.yml
- 其他 AI 分析文章 (Perplexity / Linear / Raycast / Cursor / Figma / Framer / Notion / Canva / Webflow)
- 旧人工分析文章 (1.Product-Hunt.md 至 9.OpenROV.md)
- pic/
- templates/

#### YAML 验证 (修复后)

- `source_quality_notes` 字段出现次数: 2 → 1
- yaml.safe_load 可解析
- `review_status`: draft (未变)
- `reviewed_at`: null (未变)
- `source_url_verification_status`: partial (未变)
- `source_urls`: 75 个纯 URL 字符串 (未变)
- `source_quality_notes` 内容包含 P22 详细 source-quality 说明 (1306 字符)

## P22 - Replit AI-Assisted Product Analysis

**日期：** 2026-07-01
**变更类型：** AI-assisted product analysis / source-first content
**变更范围：** analyses/ai-assisted/2026-07-01-replit.md (新增) + README + analyses/README.md + analyses/index.yml + CHANGELOG + P22 报告

### 变更内容

新增第十篇 AI 辅助产品分析 Replit，使用 source-first workflow，先执行 URL 实链验证再写文章。

#### Source-First Workflow (P22)

**Source verification 完成：**
- 75 个 source URLs HTTP-200 verified
  - 41 个 Replit 官方主站 (replit.com / privacy / terms / agent4 / pricing / pro / enterprise / security / ai / mobile / deployments / gallery / blog / about / careers / customers / learn + 14 blog posts)
  - 33 个 docs.replit.com (build/ + billing/ + references/publishing/ + references/agent/ + references/data-and-storage/ + core-concepts/agent/ + updates/)
  - 1 个 Wikipedia 主体 (en.wikipedia.org/wiki/Replit)
  - 1 个 Wikipedia (en.wikipedia.org/wiki/Amjad_Masad)
  - 11 个英文媒体 (CNBC + The Decoder x2 + 404 Media + Pulse 2.0 x3 + SaaStr x8)

**高风险事实 partial：**
- 主流媒体 (Reuters / Forbes / Bloomberg / TechCrunch / Wired / Tom's Hardware / The Verge / Business Insider / Fortune / GeekWire / Inc) Replit 报道直接 URL 401/403/404，未通过验证
- Pulse 2.0 + SaaStr 是次主流 verified 200 英文媒体 (Wikipedia reference 标 "中")
- $250M Series C vs Series D 在 Pulse 2.0 vs SaaStr 存在轮次字母分歧 — P23 复核时需核实
- a16z $4.5M seed 2018 由 CNBC verified 200 + Wikipedia reference 双源支撑
- Microsoft Azure 合作 2025-07 由 Wikipedia reference (文字 verified 200) 支撑 (Inc URL 403)
- 数据库删除事件 2025-07 由 Wikipedia + 404 Media + SaaStr 多源 verified 200 支撑
- AI Darwin Awards 提名 2025 由 Wikipedia + 404 Media 双源 verified 200 支撑

#### 索引同步

- README AI 辅助分析索引新增 Replit 行 (draft | partial)
- README 当前质量状态：9 篇 → 10 篇 (9 reviewed + 1 draft)
- README 最后更新 / 顶部状态：P22 已记录
- analyses/README.md 总览表新增 Replit 行 (ai-cloud-development / draft / partial)
- analyses/README.md 按产品类型分组新增 "AI Cloud Development" Replit 段落
- analyses/README.md 当前质量状态表同步更新 (9 → 10)
- analyses/README.md 候选列表：Replit 移至 "已分析" (划线)
- analyses/README.md 阅读路径新增 "AI App Builder 路线" (Cursor → Replit → Lovable / v0)
- analyses/README.md 跨产品对比新增 "Replit vs Cursor / Lovable / v0 / Bolt.new / GitHub Codespaces / Vercel"
- analyses/index.yml 新增 Replit 完整 entry (产品 / 文件 / 分类 / 类型 / 创建日期 / 状态 / 来源验证状态 / tags / one_line_insight / quality_notes)
- analyses/index.yml summary: total 9 → 10 / draft 0 → 1 / partial 9 → 10 / p_reports_total 14 → 15
- analyses/index.yml by_category 新增 ai-cloud-development / Replit
- analyses/index.yml reading_paths 新增 ai_app_builder_path
- yaml.safe_load 验证通过

#### Replit 关键事实

- Replit 是私人 AI coding / cloud development / app builder 公司，未 IPO
- 2025-09 完成 $250M 融资 / $3B 估值 (Prysm Capital 领投, Amex Ventures + Google AI Futures Fund 战略, a16z / Coatue / YC / Craft / Paul Graham 跟投)
- 2026-03 完成 $400M Series D / $9B 估值 (Pulse 2.0 verified 200)
- ARR 从 $2.8M 增长至 $150M (来源：Pulse 2.0 + SaaStr 二次引用公司方)
- 2025-07 与 Microsoft Azure 集成 (Azure Marketplace)
- 2025-07 AI Agent 删除 SaaStr 创始人 Jason Lemkin 整个生产数据库 — 入选 2025 AI Darwin Awards
- 2024-09 发布 Replit Agent 第一版，2025-09 发布 Agent 4

## P21 - Webflow Review and Index Status Sync

**日期：** 2026-07-01
**变更类型：** review / source-hardening / index-sync
**变更范围：** analyses/ai-assisted/2026-07-01-webflow.md (修订) + README + analyses/README.md + analyses/index.yml + CHANGELOG + P21 报告

### 变更内容

对 Webflow AI 辅助分析进行 P21 人工复核，将 review_status 从 draft 升为 reviewed。

#### Source-Hardening (P21)

**新增 verified 来源 (4 个)：**
1. `webflow.com/blog/webflow-acquires-gsap` (200) — GSAP 收购事实官方公告
2. `webflow.com/blog/webflow-acquires-vidoso` (200) — Vidoso.ai 收购事实官方公告
3. `webflow.com/blog/ai-site-builder` (200) — AI site builder 功能官方博客
4. `w3techs.com/technologies/details/cm-webflow` (200) — Webflow usage statistics 独立数据源

**尝试但未成功的媒体 URL (4 个)：**
- `techcrunch.com/2026/03/12/webflow-buys-vidoso-ai` → 404
- `axios.com/2024/10/15/webflow-acquires-gsap` → 403
- `venturebeat.com/2021/01/13/webflow-140m-2-1b-valuation` → 429
- `forbes.com/webflow-series-a-72m` → 404

**修正 Wikipedia reference vs direct verified media 边界：**
- P20 文章中 "Forbes / VentureBeat / Axios / TechCrunch verified 引用" 修正为 "Wikipedia reference cites Forbes / VentureBeat / Axios / TechCrunch"
- 明确标注底层媒体原文 URL P21 尝试验证但 404/403/429，未直接 HTTP verified
- Wikipedia 是 reference source，不是 high-quality-media-verified

#### 收购事实和收购金额拆开验证

| 收购 | 事实可信度 | 金额 |
|------|----------|------|
| GSAP (2024-10) | 中-高 (Webflow official blog verified 200 + Wikipedia reference cites Axios) | 未披露 / undisclosed |
| Vidoso.ai (2026-03) | 中-高 (Webflow official blog verified 200 + Wikipedia reference cites TechCrunch) | 未披露 / undisclosed |

#### review_status + source_url_verification_status

- **review_status**: draft → reviewed
- **source_url_verification_status**: partial (保持；融资/估值/ARR/用户数/收购金额仍 partial)

#### 修改文件 (6 个)

- `analyses/ai-assisted/2026-07-01-webflow.md`: YAML review_status draft→reviewed + reviewed_at + review_notes + source_urls 新增 4 个 + source_quality_notes 更新 + §1 Wikipedia 引用修正 + §8 GSAP 引用修正 + §14 [判断]/[推断] 标注 + §16 P21 结论 + §17 全面重写 (17.1/17.2/17.3/17.4) + Sources 区更新
- `README.md`: Webflow 行 draft→reviewed + 质量状态 reviewed 8→9 draft 1→0 + P21 计划标 [x] + 最后更新
- `analyses/README.md`: Webflow 行 draft→reviewed + 质量状态 reviewed 8→9 draft 1→0
- `analyses/index.yml`: Webflow 条目 review_status draft→reviewed + reviewed_at + quality_notes.reason 更新 + summary reviewed 8→9 draft 1→0 + p_reports_total 13→14
- `CHANGELOG.md`: 顶部 P21 记录
- `reports/P21-webflow-review-and-index-status-sync-report.md`: 新增 P21 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (302a061 = P20)
- ✅ YAML review_status = reviewed
- ✅ YAML reviewed_at = 2026-07-01
- ✅ YAML review_notes 存在且语义正确
- ✅ YAML source_urls 44 个纯 URL 字符串 (P20 的 40 + P21 新增 4)
- ✅ YAML source_url_verification_status = partial
- ✅ §17.1 已从 draft 改为人工复核完成状态
- ✅ §17.2 可信度分级已同步更新 (收购事实/收购金额拆开)
- ✅ §17.3 包含 Wikipedia reference vs direct verified media 教训
- ✅ §17.4 Sources 新增 4 个 P21 verified 来源
- ✅ Sources 区新增 High-Quality Data Sources 分组
- ✅ 正文不得写 Webflow 是公开公司或已 IPO
- ✅ 正文已修正 Wikipedia reference 和媒体 direct verified 的边界
- ✅ §14 中文 MVP 推断标注 [判断] / [推断]
- ✅ 8 篇 reviewed AI 辅助分析 mtime 未变
- ✅ 9 旧人工分析 + pic/ + templates/ + 其他 docs/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P20 - Webflow AI 辅助产品分析 (第 9 篇)

**日期：** 2026-07-01
**变更类型：** source-first / ai-assisted / new-article
**变更范围：** analyses/ai-assisted/2026-07-01-webflow.md (新增 30.3 KB) + README + analyses/README.md + analyses/index.yml + CHANGELOG + P20 报告

### 变更内容

第九篇 AI 辅助产品分析 — Webflow，使用 source-first workflow。

#### Source-First URL Verification (P20)

**验证统计：**
- **Webflow 官方页面：39 个 HTTP-200 verified** (P11 以来最完整官方源覆盖 — 超过 P12 Figma 18+ / P13 Framer 26+ / P16 Notion 30+)
- **Wikipedia：1 个 verified 200 (Webflow)** — reference 源
- 主流量化媒体：5+ 主动尝试 (TechCrunch / Axios / VentureBeat / Forbes / W3Techs 原报道 URL 未直接 HTTP 验证)
- High-risk fact 主动尝试：Wikipedia 二手 + 部分 verified media 引用未达独立 verified 双源

**关键官方 Source Verified (39 URLs)：**
1. `webflow.com/` — 官网定位 / 营销
2. `webflow.com/pricing` — Pricing tiers / AI credits / GSAP 集成
3. `webflow.com/ai` — AI site builder / AI Assistant / MCP server / Optimize
4. `webflow.com/cms` / `webflow.com/hosting` / `webflow.com/localization` / `webflow.com/security` — 核心能力
5. `webflow.com/seo` / `webflow.com/aeo` / `webflow.com/analyze` / `webflow.com/optimize` — 增长方向
6. `webflow.com/enterprise` / `webflow.com/about` / `webflow.com/customers` — 企业级
7. `webflow.com/figma-to-webflow` / `webflow.com/devlink` / `webflow.com/cloud` — 开发者扩展
8. `webflow.com/university` / `webflow.com/blog` / `webflow.com/templates` / `webflow.com/marketplace` / `webflow.com/made-in-webflow` — 生态
9. `webflow.com/editor` / `webflow.com/designer` / `webflow.com/platform` — 核心工具
10. `webflow.com/conf` / `webflow.com/glossary` / `webflow.com/integrations` — 学习 / 集成
11. `webflow.com/accessibility` / `webflow.com/web-design` / `webflow.com/partners` — 设计 / 合作伙伴
12. `webflow.com/press` / `webflow.com/media` / `webflow.com/privacy` / `webflow.com/terms` / `webflow.com/websites` — 媒体 / 法律 / 站点
13. `en.wikipedia.org/wiki/Webflow` — reference 源 (二手记载)

**高风险事实 Partial 原因：**
- Webflow 是私人公司（无 SEC filings / 无 investor relations）
- 融资历史（Series A $72M / Series B $140M / $2.1B valuation）来自 Wikipedia 二手引用 Forbes / VentureBeat，原报道 URL 未直接 HTTP 验证
- 收购历史（GSAP 2024-10 / Vidoso.ai 2026-03）来自 Wikipedia 二手引用 Axios / TechCrunch，原报道 URL 未直接 HTTP 验证
- 收购金额均未明确披露 → partial
- 用户数 / 营收 / 员工数 来自 Wikipedia 二手 → 中

#### 文章核心内容

- **一句话定位**：Webflow = "The visual web development platform"（官网 verified）
- **核心机制**：Designer 视觉开发 + CMS + Hosting + Localization + SEO/AEO/Analyze/Optimize
- **产品矩阵**：Webflow / AI site builder / AI Assistant / MCP server / GSAP / Webflow Cloud / DevLink / Figma to Webflow / Code Components / Apps
- **Pricing (verified 200)**: Starter Free / Basic $15/mo / Premium $25/mo / Business $29/mo / Ecommerce Standard $29/mo / Plus $74/mo / Enterprise Custom
- **AI features**: AI site builder / AI Assistant / MCP server / Optimize / Localization
- **公司背景**: 2013-08-05 创立, Vlad Magdalin + Sergie Magdalin + Bryant Chou 联合创立, Y Combinator 2013 graduate, San Francisco HQ, 501-1000 员工
- **收购历史**: GreenSock/GSAP (2024-10) / Vidoso.ai (2026-03) verified
- **竞品**: Framer / WordPress / Wix / Squarespace / Figma Sites / Webstudio / HubSpot CMS / Lovable / v0 / Replit
- **中文 MVP 推断**: 面向 AI 原生 SaaS / 独立开发者的营销官网增长平台（判断，非事实）

#### review_status + source_url_verification_status

- **review_status**: draft（P20 初稿，待 P21 人工复核）
- **source_url_verification_status**: partial（主体产品机制 verified；融资/估值/ARR/用户数/收购金额 仍 partial）

#### 修改文件 (5 个)

- `analyses/ai-assisted/2026-07-01-webflow.md`: 新增 30.3 KB，17 节，YAML 11 字段
- `README.md`: AI 索引新增 Webflow 行 (draft | partial) + 当前质量状态 8→9
- `analyses/README.md`: Webflow 行 + by-category Visual Web Development + reading paths + 状态
- `analyses/index.yml`: Webflow 条目 (draft | partial) + summary 8→9 + by_category + reading_paths
- `CHANGELOG.md`: 顶部 P20 记录 (本节)
- `reports/P20-webflow-ai-assisted-analysis-report.md`: 新增 P20 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (1136646 = P19.1)
- ✅ Webflow 文 30.3 KB 新增
- ✅ analyses/ai-assisted/2026-07-01-webflow.md 存在
- ✅ YAML review_status = draft
- ✅ YAML source_url_verified_at = 2026-07-01
- ✅ YAML source_url_verification_status = partial
- ✅ §17.4 Sources 实链验证表存在 (40 verified + 13 unverified = 53 来源)
- ✅ Sources 4 分组完整 (Official+Primary 10 / Product+Docs 29 / Reference 1 / Unverified 13)
- ✅ 8 篇 reviewed AI 辅助分析 (Perplexity/Linear/Raycast/Cursor/Figma/Framer/Notion/Canva) mtime 未变
- ✅ 9 旧人工分析 + pic/ + templates/ + 其他 docs/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P19.1 - Canva 索引状态漂移修复

**日期：** 2026-07-01
**变更类型：** index-fix / docs-only
**变更范围：** README.md + analyses/README.md + CHANGELOG + P19.1 报告

### 变更内容

P19 完成后人工复核发现索引状态漂移：
- **Canva 文章 YAML**: reviewed | partial ✓ (P19 正确)
- **analyses/index.yml**: Canva reviewed | partial, summary reviewed=8 draft=0 partial=8 ✓ (P19 正确)
- **analyses/README.md**: Canva 行显示 draft | partial (与质量状态 reviewed=8 draft=0 自相矛盾) ❌
- **README.md**: Canva 行显示 draft | partial，质量状态写 7 reviewed + 1 draft ❌

P19.1 修复：人工可读索引与机器可读索引完全对齐。

#### 修改文件 (4 个)

- `README.md`:
  - AI 索引 Canva 行: `draft | partial` → `reviewed | partial`
  - 当前质量状态: `AI 辅助分析 8 | 7 reviewed + 1 draft` → `8 | 全部 reviewed`;`reviewed 7 → 8`;`draft 1 → 0`
  - 下一步计划: 新增 P19.1 标 [x]
  - 最后更新: P19 → P19.1
- `analyses/README.md`:
  - AI 辅助分析总览 Canva 行: `draft | partial` → `reviewed | partial`
  - 当前质量状态: 保持 (已是正确版本)
- `CHANGELOG.md`: 顶部 P19.1 记录 (本节)
- `reports/P19.1-canva-index-status-drift-fix-report.md`: 新增 P19.1 报告

#### 未修改

- `analyses/ai-assisted/2026-07-01-canva.md` (Canva 文章正文 + YAML 不变)
- `analyses/index.yml` (已正确)
- 7 篇其他 AI 辅助分析文章 (Perplexity/Linear/Raycast/Cursor/Figma/Framer/Notion) 不变
- 9 篇旧人工分析文章 + pic/ + templates/ 不动

### 验证

- ✅ 起始 HEAD = origin/master clean (8db1079 = P19)
- ✅ Canva YAML: reviewed | partial (未改)
- ✅ analyses/index.yml: Canva reviewed | partial, summary reviewed=8 draft=0 (未改)
- ✅ analyses/README.md: Canva 行 reviewed | partial, 质量状态 reviewed=8 draft=0 ✓
- ✅ README.md: Canva 行 reviewed | partial, 质量状态 reviewed=8 draft=0 ✓
- ✅ 四处状态完全一致
- ✅ 无 force push / reset --hard / amend

---

## P19 - Canva 人工复核与索引状态同步

**日期：** 2026-07-01
**变更类型：** review / source-hardening / index-sync / docs-only
**变更范围：** analyses/ai-assisted/2026-07-01-canva.md (YAML 状态 + 17.1/17.2/17.3/17.4 P19 增量) + README + analyses/README.md + analyses/index.yml + CHANGELOG + P19 报告

### 变更内容

第八篇 AI 辅助产品分析 — Canva 人工复核 + 索引状态同步。状态从 `draft` 升级为 `reviewed`。

#### review_status 升级

- **before**: draft (P18 2026-07-01)
- **after**: reviewed (P19 2026-07-01)
- **reviewed_at**: 2026-07-01
- **source_url_verification_status**: 保持 partial（诚实评估，canva.com 仍 403 Datadome）

#### P19 复验证结果 (P18 后)

- **canva.com/* 30+ URL 仍 403 Datadome** (官方 source-first workflow 受限)
- **Wikipedia (Canva/Affinity/Perkins) 仍 200 verified** (3 个 reference 源)
- **Fortune 2025-08-22 仍 200 verified** ($42B 估值 / employee share sale)
- **The Verge 2024 仍 200 verified** (Leonardo.AI 收购)
- **TechCrunch/Reuters/CNBC/Bloomberg/FT 原报道 URL 仍 404/401/403** (15+ URL 主动尝试)

P19 主动尝试以上 URL 后，确认 5 verified sources 不变，跨独立 verified 媒体双源仍未达成。诚实评估保持 partial。

#### 高风险事实最终措辞 (P19 调整)

- **Canva 是私人公司 / 接近 IPO 候选 / 未 IPO** — 中-高 (Fortune + Wikipedia 双源部分达成，AFR 404)
- **$42B valuation (2025-08) 来自 employee share sale** — 中 (Wikipedia + Fortune 单独立媒体)
- **2025 营收 US$4 billion** — 低-中 (Wikipedia reference 单源)
- **220 million users** — 低-中 (Wikipedia reference 单源)
- **5,500 员工 (2024)** — 低-中 (Wikipedia reference 单源)
- **Affinity 收购 (2024)** — 中 (Wikipedia 双源，金额未明确披露)
- **Leonardo.AI 收购 (2024-07)** — 中-高 (Wikipedia + The Verge 双源部分达成，金额未明确披露)
- **Simtheory + Ortto 收购 (2026-02)** — 中 (Wikipedia 二手引用 TechCrunch，原报道 URL 404)

#### 主体轻量修订 (不重写)

- **§1 一句话定位**: 去掉 "verified-by-Wikipedia" 表述，改为 "Wikipedia reference 公开记载"
- **§17.1 当前状态**: 改为 P19 复核完成状态
- **§17.2 可信度分级**: 重新校准 (高 → 中, 中-高 → 中 / 中-低)
- **§17.3 后续 AI 分析改进**: 8 → 14 条 (P19 新增 6 条 canva.com blocked / Wikipedia reference / 收购金额教训)
- **§17.4 Sources 实链验证**: 新增 5+ Unverified URL (Affinity TechCrunch/Reuters/FT 等) + P19 复验证表 (11 URL 状态 P18 vs P19 对比)

#### 索引文件同步 (跨文件)

- **analyses/index.yml**: Canva `draft → reviewed` + `summary: reviewed 7→8, draft 1→0, p_reports_total 11→12`
- **analyses/README.md**: Canva `draft → reviewed` + 质量状态表同步 (reviewed 8 + draft 0)
- **README.md**: Canva `draft → reviewed` + 质量状态表 + 下一步计划 + 最后更新
- **CHANGELOG.md**: 顶部 P19 记录 (本节)

#### 修改文件 (5 个)

- `analyses/ai-assisted/2026-07-01-canva.md`: YAML 状态 + §17.1/17.2/17.3/17.4 P19 增量
- `analyses/index.yml`: Canva draft→reviewed + summary 8 reviewed
- `analyses/README.md`: Canva draft→reviewed + 质量状态 8
- `README.md`: Canva draft→reviewed + 质量状态 8 + 下一步计划
- `CHANGELOG.md`: 顶部 P19 记录
- `reports/P19-canva-review-and-index-status-sync-report.md`: 新增 P19 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (0e0a2fa = P18)
- ✅ Canva 文 ~35.3 → ~38 KB (+2.7 KB source-hardening)
- ✅ analyses/ai-assisted/2026-07-01-canva.md 存在
- ✅ YAML review_status = reviewed (P19 升级)
- ✅ YAML reviewed_at = 2026-07-01
- ✅ YAML review_notes = P19 复核完整版
- ✅ source_url_verification_status = partial (原因清晰)
- ✅ §1 去掉 "verified-by-Wikipedia" 表述
- ✅ §17.1 改为 P19 复核完成状态
- ✅ §17.2 重新校准可信度分级 (中/中-高/低-中 替代 高/中-高)
- ✅ §17.3 8 → 14 条 (P19 spec-required 6 条)
- ✅ §17.4 Sources 实链验证表 新增 6+ Unverified URL + P19 复验证表
- ✅ analyses/index.yml Canva draft→reviewed (Python yaml.safe_load 验证)
- ✅ analyses/README.md Canva draft→reviewed + 质量状态 8
- ✅ README.md Canva draft→reviewed + 质量状态 8 + 下一步计划
- ✅ 7 篇 AI 辅助分析 (Perplexity/Linear/Raycast/Cursor/Figma/Framer/Notion) mtime 未变
- ✅ 9 旧人工分析 + pic/ + templates/ + 其他 docs/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P18 - Canva AI 辅助产品分析 (第 8 篇)

**日期：** 2026-07-01
**变更类型：** source-first / ai-assisted / new-article
**变更范围：** analyses/ai-assisted/2026-07-01-canva.md (新增 25.5 KB) + README + analyses/README.md + analyses/index.yml + CHANGELOG + P18 报告

### 变更内容

第八篇 AI 辅助产品分析 — Canva，使用 source-first workflow。

#### Source-First URL Verification (P18)

**验证统计：**
- **canva.com 官方 URL：30+ 全部 403 (Datadome bot protection)** — P18 标为 official-url-access-limited
- Wikipedia：3 个 verified 200 (Canva / Affinity_(software) / Melanie_Perkins)
- Verified media：2 个 verified 200 (Fortune 2025-08-22 / The Verge 2024)
- 主流量化媒体：0 个 verified (TechCrunch / Reuters / CNBC / Bloomberg / FT / WSJ 原报道 URL 401-404/403 未 HTTP 验证)
- High-risk fact 主动尝试：Wikipedia 二手记载 + Fortune 单源 + The Verge 单源，跨独立 verified 媒体双源未达成

**关键 Verified Source：**
1. `en.wikipedia.org/wiki/Canva` (200) — 2013 成立 / 创始人 / 估值 / 营收 / 用户 / 员工 / 收购 / Visual Suite 2 / 100 语言
2. `en.wikipedia.org/wiki/Affinity_(software)` (200) — Affinity 收购自 Serif 2024
3. `en.wikipedia.org/wiki/Melanie_Perkins` (200) — 创始人背景
4. `fortune.com/2025/08/22/...` (200) — $42B 估值 / employee share sale
5. `theverge.com/2024/canva-leonardo-ai` (200) — Leonardo.AI 收购

**高风险事实 Partial 原因：**
- Canva 官方 canva.com 30+ URL 全部 403 Datadome bot-blocked (标 official-url-access-limited)
- Wikipedia 是 reference 源（不是 high-quality-media-verified）
- $42B 估值 (2025-08) Wikipedia + Fortune 双源部分达成
- Affinity / Leonardo.AI 收购事件 Wikipedia + 部分 verified media 单源
- 收购金额未明确披露 → partial
- 2025 营收 $4B / 220M 用户 / 5,500 员工 → Wikipedia 单源

#### 文章核心内容

- **一句话定位**：Canva = 大众化设计与内容生产平台（template-first + visual suite）
- **核心机制**：Template-first workflow + Magic Studio AI + Visual Suite 2 (Sheets/Code/chatbot/photo editor)
- **产品矩阵**：Canva / Affinity (Photo/Designer/Publisher) / Leonardo.AI / Visual Suite 2 / Magic Studio
- **2025 营收 $4B** (Wikipedia 二手)
- **用户 220M** (Wikipedia 二手)
- **估值历史**：A$6B (2020) → A$40B (2021) → US$26B (2022) → US$42B (2025-08 employee share sale, Fortune verified)
- **收购历史**：Zeetings (2018) / Pixabay+Pexels (2019) / Kaleido (2021) / Affinity/Serif (2024) / Leonardo.AI (2024-07) / Simtheory+Ortto (2026-02)
- **接近 IPO**：2025-06 AFR 报道“near IPO”（Wikipedia 二手，AFR 原报道 URL 404）
- **竞品**：Adobe / Figma / Microsoft / Google / VistaCreate / CapCut / Picsart / Framer / Affinity / Leonardo.AI / Midjourney
- **中文 MVP 推断**：面向小红书 / 公众号 / 电商小团队的 AI 品牌内容生产台（判断，非事实）

#### review_status + source_url_verification_status

- **review_status**: draft（P18 初稿，待 P19 人工复核）
- **source_url_verification_status**: partial（canva.com 官方 403 Datadome；主体产品机制来自 Wikipedia 二手；融资/估值/营收/用户/收购金额仍 partial）

#### 修改文件 (5 个)

- `analyses/ai-assisted/2026-07-01-canva.md`: 新增 25.5 KB，17 节，YAML 11 字段
- `README.md`: AI 索引新增 Canva 行 (draft | partial) + 当前质量状态 7→8
- `analyses/README.md`: Canva 行 + by-category Design AI / Visual Communication + reading paths + 状态
- `analyses/index.yml`: Canva 条目 (draft | partial) + summary 7→8 + by_category + reading_paths
- `CHANGELOG.md`: 顶部 P18 记录 (本节)
- `reports/P18-canva-ai-assisted-analysis-report.md`: 新增 P18 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (3c0f385 = P17)
- ✅ Canva 文 25.5 KB 新增
- ✅ analyses/ai-assisted/2026-07-01-canva.md 存在
- ✅ YAML review_status = draft
- ✅ YAML source_url_verified_at = 2026-07-01
- ✅ YAML source_url_verification_status = partial
- ✅ §17.4 Sources 实链验证表存在 (5 verified + 17 official-url-access-limited + 10 unverified = 32 来源)
- ✅ Sources 5 分组完整 (Official 7 / Product 17 / Verified Media 2 / Reference 3 / Unverified 3)
- ✅ 7 篇 reviewed AI 辅助分析 (Perplexity/Linear/Raycast/Cursor/Figma/Framer/Notion) mtime 未变
- ✅ 9 旧人工分析 + pic/ + templates/ + 其他 docs/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P17 - Notion 人工复核与索引状态升级

**日期：** 2026-07-01
**变更类型：** review / source-hardening / index-sync / docs-only
**变更范围：** analyses/ai-assisted/2026-07-01-notion.md (YAML 状态 + 17.1/17.2/17.3/17.4 P17 增量) + README + analyses/README.md + analyses/index.yml + CHANGELOG + P17 报告

### 变更内容

第七篇 AI 辅助产品分析 — Notion 人工复核 + 索引状态同步。状态从 `draft` 升级为 `reviewed`。

#### review_status 升级

- **before**: draft (P16 2026-07-01)
- **after**: reviewed (P17 2026-07-01)
- **reviewed_at**: 2026-07-01
- **source_url_verification_status**: 保持 partial（诚实评估）

#### P17 source-hardening 增量 (3 verified sources)

1. `notion.com/blog/introducing-notion-ai` (200 verified) — Ivan Zhao 2022-11-16 官方 blog：Notion AI private alpha 首次 announcement
2. `notion.com/releases` (200 verified) — 官方 releases 页面
3. `en.wikipedia.org/wiki/Notion_(productivity_software)` (200 verified) — Wikipedia 二手记载：Notion 2013 成立、Series A $50M (2020) Index / Series C $275M (2021) Coatue+Sequoia $10B / Cron 收购 2022-06 / Skiff 收购 2024-02 / 20M 用户 / Notion AI 2022-11-16 / Notion Calendar 2024-01-17 / Notion Mail 2025-04 / Forbes AI 50 (2025-04)

#### 双源部分达成 (Wikipedia + 官方 blog)

- Notion AI 发布 2022-11-16 — Wikipedia + 官方 blog 双源 → high (从 partial 升)
- Skiff 收购事件 2024-02-09 — Wikipedia + thurrott.com 双源 → 中-高 (从 partial 升)

#### 仍 partial (P17 验证努力后未突破)

- Series A $50M / Index Ventures 2020-01 / 估值 $2B — Wikipedia 单源
- Series C $275M / Coatue + Sequoia 2021-10 / 估值 $10B / 20M 用户 — Wikipedia 单源
- Cron 收购 2022-06-09 / Automate.io 收购 2021-09 — Wikipedia 单源
- Notion Calendar 2024-01-17 / Notion Mail 2025-04 — Wikipedia 单源
- Forbes "AI 50" 2025-04 入选 — Wikipedia 标 "non-primary source needed"
- CNBC: $500M ARR — Wikipedia 引用但 CNBC 原报道 URL 404
- TechCrunch: AI agents hub 2026-05-13 — Wikipedia 引用但 TechCrunch 原报道 URL 404
- 收购金额 (Skiff / Cron / Automate.io) — Notion 官方未找到具体金额 announcement

#### 主体轻量修订 (不重写)

- **§1 一句话定位**: 保持 [判断] 注释 (已含)
- **§8 交互与视觉设计**: 保持 AI 双层标注 (已含)
- **§16 今日复盘**: 标 [判断] 注释 (P17 新增：Framer 创新 / Product-Analysis 启发 显式标判断)
- **§17.1 当前状态**: 改为 P17 复核完成状态 + source-hardening 增量
- **§17.2 可信度分级**: 16 → 28 条 (P17 新增 12 条 Wikipedia 记载事实分级)
- **§17.3 后续 AI 分析改进**: 7 → 12 条 (P17 spec-required 5 条新增)
- **§17.4 Sources 实链验证表**: 新增 3 verified sources (introducing-notion-ai / releases / Wikipedia) + P17 结论

#### 索引文件同步 (跨文件)

- **`analyses/index.yml`**: Notion `draft → reviewed` + `summary: reviewed 6→7, draft 1→0, p_reports_total 9→10`
- **`analyses/README.md`**: Notion `draft → reviewed` + 质量状态表同步 (reviewed 7 + draft 0) + 候选列表修正
- **`README.md`**: Notion `draft → reviewed` + 质量状态表 (reviewed 6→7, draft 1→0) + 下一步计划 + 最后更新
- **`CHANGELOG.md`**: 顶部 P17 记录 (本节)

#### 候选列表修正 (P17 spec-required Step 9)

- **Canva**: 修正为 "私人公司 / 潜在 IPO 候选 (Fortune 2025-08-22 估值 $42B)"，不再是 "公开公司"
- **Webflow**: 修正为 "私人 website builder / SaaS 公司"，不再是 "公开公司"
- **Replit**: 修正为 "私人 AI coding / hosting 公司，有私募融资报道"，不再是 "公开 (2024 IPO)"

仅在活跃索引 (analyses/README.md) 修正，历史 P16 report 保留不动。

#### 修改文件 (5 个)

- `analyses/ai-assisted/2026-07-01-notion.md`: YAML 状态 + §17.1/17.2/17.3/17.4 P17 增量
- `analyses/index.yml`: Notion draft→reviewed + summary 6→7 reviewed
- `analyses/README.md`: Notion draft→reviewed + 质量状态 + 候选列表
- `README.md`: Notion draft→reviewed + 质量状态 + 下一步计划
- `CHANGELOG.md`: 顶部 P17 记录
- `reports/P17-notion-review-and-index-sync-report.md`: 新增 P17 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (c682263 = P16)
- ✅ Notion 文 37.9 → 39.7 KB (+1.8 KB source-hardening)
- ✅ analyses/ai-assisted/2026-07-01-notion.md 存在
- ✅ YAML review_status = reviewed (P17 升级)
- ✅ YAML reviewed_at = 2026-07-01
- ✅ YAML review_notes = P17 复核完整版
- ✅ YAML source_url_verification_status = partial (原因清晰)
- ✅ YAML 35 source_urls 纯 URL 列表 (Python yaml.safe_load 验证)
- ✅ §17.1 改为 P17 复核完成状态
- ✅ §17.2 16 → 28 条 (P17 新增 12 条 Wikipedia 记载事实分级)
- ✅ §17.3 7 → 12 条 (P17 spec-required 5 条)
- ✅ §17.4 Sources 实链验证表 新增 3 verified + P17 结论
- ✅ analyses/index.yml Notion draft→reviewed (Python yaml.safe_load 验证)
- ✅ analyses/README.md Notion draft→reviewed + 质量状态 7 + 候选列表修正
- ✅ README.md Notion draft→reviewed + 质量状态 7 + 下一步计划
- ✅ 6 篇 AI 辅助分析 (Perplexity/Linear/Raycast/Cursor/Figma/Framer) mtime 未变
- ✅ 9 旧人工分析 + pic/ + templates/ + 其他 docs/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P16 - Notion AI 辅助产品分析 (第 7 篇)

**日期：** 2026-07-01
**变更类型：** source-first / ai-assisted / new-article
**变更范围：** analyses/ai-assisted/2026-07-01-notion.md (新增 27.4 KB) + README + analyses/README.md + analyses/index.yml + CHANGELOG + P16 报告

### 变更内容

第七篇 AI 辅助产品分析 — Notion，使用 source-first workflow。

#### Source-First URL Verification (P16)

**验证统计：**
- Notion 官方页面：30 个 HTTP-200 verified (官网 / product / pricing / ai / enterprise / calendar / mail / sites / templates / marketplace / help / help/category/notion-ai / help/category/new-to-notion / security / customers / about / blog / wikis / projects / docs / teams / developers / integrations / changelog / search / mobile / download / desktop / web-clipper / contact-sales)
- 开发者文档：1 个 HTTP-200 verified (developers.notion.com)
- Verified media：1 个 HTTP-200 verified (thurrott.com — Notion acquires Skiff 2024-02)
- 主流量化媒体：0 个 verified (TechCrunch / Forbes / Reuters / Bloomberg / CNBC 原始 URL 未直接 HTTP 验证)
- High-risk fact 主动尝试：skiff 收购验证 thurrott.com 单源

**关键官方 Source Verified：**
1. `notion.com/` — 官网定位 "Your AI workspace"
2. `notion.com/product` — Notion / Calendar / Mail / AI / Agents / AI Meeting Notes / Enterprise Search / Knowledge Base / Docs / Projects / Connections / Security
3. `notion.com/pricing` — Free / Plus $10 / Business $20 / Enterprise; AI included in Plus+; LLM zero data retention in Enterprise
4. `notion.com/ai` — Notion AI features
5. `notion.com/help/category/notion-ai` — AI Meeting Notes / Notion MCP / Notion Agent / Research Mode / Enterprise Search
6. `notion.com/help/category/new-to-notion` — Block / Database / Workspace 基础
7. `notion.com/calendar` / `notion.com/mail` / `notion.com/sites` — Calendar / Mail / Sites 独立产品页
8. `notion.com/enterprise` — Enterprise features (SCIM / SAML SSO / audit log / customer success manager)
9. `developers.notion.com/` — Notion API / SDK
10. `notion.com/security` / `notion.com/customers` — Security / Customers
11. `thurrott.com/cloud/297641/notion-acquires-skiff` — Skiff 收购 (2024-02) 跨独立 verified 媒体

**高风险事实 Partial 原因：**
- Notion 是私人公司（无 SEC filings / 无 investor relations）
- 官方 about 页面无公司历史 / 创始人 / 成立时间结构化信息
- 融资历史 (Series C $275M / Sequoia + Index + Coatue) 来自中文转载 + 第三方汇总，无独立 verified 媒体双源
- 估值 / ARR / 用户数 (数千万用户 / $10B+ 估值) 来自中文转载 + Forbes AI 50 二次引述，无原始 verified URL
- Skiff 收购 (2024-02) 金额：Notion 官方未找到具体金额 announcement；thurrott.com 验证收购事件但未给金额；中文转载有金额但属二手

#### 文章核心内容

- **一句话定位**：Notion = "Your AI workspace"（官网 verified）
- **核心机制**：Block model + Database + AI (Notion AI / Agent / AI Meeting Notes / Enterprise Search)
- **产品矩阵**：Notion / Notion Calendar / Notion Mail / Notion AI / Agents / Forms / Sites / Marketplace
- **Pricing**：Free $0 / Plus $10 / Business $20 / Enterprise Custom；AI included in Plus+；guests unlimited
- **AI features**：Notion AI / Notion Agent / AI Meeting Notes / Research Mode / Enterprise Search / Connectors
- **企业级**：SCIM / SAML SSO / audit log / LLM zero data retention (Enterprise)
- **收购历史**：Skiff (2024-02) verified via thurrott.com；Cron / Automate.io / Flowdash 历史收购 partial
- **竞品**：Evernote / Google Docs / Microsoft Loop / Confluence / Coda / Airtable / Asana / Trello / ClickUp / Obsidian / Tana / Slack Canvas
- **中文 MVP 推断**：面向 AI 原生个人项目和小团队的知识工作台（判断，非事实）

#### review_status + source_url_verification_status

- **review_status**: draft（P16 初稿，待 P17 人工复核）
- **source_url_verification_status**: partial（主体产品机制 verified；融资/估值/ARR/用户数/Skiff 收购金额 partial）

#### 修改文件 (5 个)

- `analyses/ai-assisted/2026-07-01-notion.md`: 新增 27.4 KB，17 节，YAML 11 字段
- `README.md`: AI 索引新增 Notion 行 (draft | partial) + 当前质量状态 6→7
- `analyses/README.md`: Notion 行 + by-category AI Workspace / Knowledge Management + reading paths + 状态
- `analyses/index.yml`: Notion 条目 (draft | partial) + summary 6→7 + by_category + reading_paths
- `CHANGELOG.md`: 顶部 P16 记录 (本节)
- `reports/P16-notion-ai-assisted-analysis-report.md`: 新增 P16 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (c4bb23d = P15 enrichment)
- ✅ Notion 文 27.4 KB 新增
- ✅ analyses/ai-assisted/2026-07-01-notion.md 存在
- ✅ YAML review_status = draft
- ✅ YAML source_url_verified_at = 2026-07-01
- ✅ YAML source_url_verification_status = partial
- ✅ §17.4 Sources 实链验证表存在 (32 + 8 = 40 个来源)
- ✅ Sources 4 分组完整 (Official+Primary 15 / Product+Docs 16 / Verified Media 1 / Unverified 8)
- ✅ 6 篇 reviewed AI 辅助分析 (Perplexity/Linear/Raycast/Cursor/Figma/Framer) mtime 未变
- ✅ 9 旧人工分析 + pic/ + templates/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P15 - AI 分析索引与质量仪表板

**日期：** 2026-07-01
**变更类型：** docs-only / index / dashboard
**变更范围：** 新增 analyses/README.md + analyses/index.yml + docs/review-status-guide.md + README.md 质量状态小节 + CHANGELOG.md 顶部 P15 记录 + P15 报告

### 变更内容

P15 是不新增产品分析文章的任务，目的是建立 AI 辅助分析的索引、质量评判标准与质量仪表板，让仓库从 6 篇独立文章变成结构化产品分析体系。

#### 新增文件 (3 个)

1. **`analyses/index.yml`** (2.9 KB) — 结构化索引 (机器可读)
   - 6 篇 AI 辅助分析的元数据
   - 产品 / 文件 / 日期 / 状态 / 来源状态 / 标签 / commit / reviewed_at / report
   - summary (total / reviewed / draft / verified / partial)
   - status_transitions (状态流转)
2. **`analyses/README.md`** (3.5 KB) — 人工可读索引
   - 目录结构
   - 6 篇 AI 辅助分析表格 (与 index.yml 同步)
   - 质量状态汇总
   - 状态流转说明
   - 维护说明
3. **`docs/review-status-guide.md`** (3.4 KB) — review_status 流转指南
   - 双重状态系统 (review_status + source_url_verification_status)
   - draft → reviewed 升级标准 (7 条)
   - partial → verified 升级标准 (5 条)
   - 高风险事实判定 (10 类)
   - partial 状态详解 (4 个典型场景)
   - 当前项目状态汇总
   - 升级路径示例 (Perplexity / Figma / Framer)

#### README.md 修改 (3 处)

1. **添加 "如何新增一篇 AI 产品分析"** - 第 6 步同步更新 analyses/index.yml 与 analyses/README.md
2. **新增 "当前质量状态" 小节** - 表格 + 链接到 analyses/README.md / analyses/index.yml / docs/review-status-guide.md
3. **最后更新**: P14 → **P15**

#### 未变更

- ✅ **未新增产品分析文章** (P15 是 docs-only 任务)
- ✅ **未修改 6 篇 AI 辅助分析文章** (Perplexity / Linear / Raycast / Cursor / Figma / Framer 主体未动)
- ✅ **未修改 9 篇旧人工分析文章** (根目录 legacy notes 未动)
- ✅ **未动 pic/ 目录**
- ✅ **未动 templates/ 目录**
- ✅ **未动其他 docs/ 现有文件** (ai-assisted-analysis-workflow.md / product-analysis-framework.md / source-quality-checklist.md 未动)

#### 仓库结构变化

```
Product-Analysis/
├── README.md (修改: 新增质量状态小节)
├── CHANGELOG.md (修改: 顶部 P15 记录)
├── analyses/ (新增 README.md + index.yml)
│   ├── README.md ✨ 新增
│   ├── index.yml ✨ 新增
│   └── ai-assisted/
│       ├── README.md (未动)
│       └── 6 篇 AI 辅助分析 (未动)
├── docs/ (新增 review-status-guide.md)
│   ├── review-status-guide.md ✨ 新增
│   ├── ai-assisted-analysis-workflow.md (未动)
│   ├── product-analysis-framework.md (未动)
│   └── source-quality-checklist.md (未动)
├── templates/ (未动)
├── reports/ (新增 P15 报告)
│   └── P15-ai-analysis-index-and-quality-dashboard-report.md ✨ 新增
├── 9 篇旧人工分析 (未动)
└── pic/ (未动)
```

### 验证

- ✅ 起始 HEAD = origin/master clean (74fda7a = P14)
- ✅ analyses/README.md 存在
- ✅ analyses/index.yml 存在
- ✅ docs/review-status-guide.md 存在
- ✅ README.md 包含 analyses/README.md 链接
- ✅ README.md 包含 "当前质量状态" 小节
- ✅ analyses/index.yml 包含 6 篇 AI 分析
- ✅ analyses/README.md 包含 6 篇 AI 分析表格
- ✅ docs/review-status-guide.md 解释 reviewed vs partial
- ✅ CHANGELOG.md 顶部有 P15 记录
- ✅ 6 篇 AI 辅助分析文章 + 9 篇旧人工分析 + pic/ + templates/ + 其他 docs/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P14 - Framer 人工复核与 YAML/Sources 规范修正

**日期：** 2026-07-01
**变更类型：** review / source-hardening / docs-only
**变更范围：** analyses/ai-assisted/2026-07-01-framer.md (YAML 规范化 + lead / §8 / §16 [判断] 注释 + §17.1 / §17.3 / §17.4 P14 增量) + README + CHANGELOG + P14 报告

### 变更内容

第六篇 AI 辅助产品分析 — Framer 人工复核 + YAML/Sources 规范修正。状态从 `draft` 升级为 `reviewed`。

#### YAML 规范化 (P14 核心变更)

**P13 draft 问题**：source_urls 把 type/status/note 写在 URL 同一行：
```yaml
- https://www.framer.com/ (primary-official | verified)
```

**P14 修正**：
```yaml
- https://www.framer.com/
- https://www.framer.com/pricing/
- ...
```

- 29 个 URL 全部纯字符串，普通 YAML parser 可解析
- 29 个 URL 中 26 个 framer.com/* + 2 founders 个人网站 + 1 中文转载
- type / status / used_for / note 全部移到文末 Sources 表格 + §17.4 Sources 实链验证表

#### review_status 升级

- **before**: draft (P13 2026-07-01)
- **after**: reviewed (P14 2026-07-01)
- **source_url_verification_status**: 保持 partial (诚实评估)

#### P14 source-hardening 增量 (1 verified source)

- `macapp.so/framer-studio-po-jie` (200 verified 但 secondary) — Koen Bok + Jorn van Dijk 是 Sofa 创始人/设计总监 → Facebook → Podium → Framer 背景
  - 类型：secondary-media-chinese
  - 状态：unverified-http (二次引述，未找到原始英文 founders bio page)
  - 用途：founders 背景补充 (partial 可靠度)

#### P14 主动尝试 + 失败 (10+ URLs)

- Meritech 投资者公告 (3 URL): 404/405
- Atomico 投资者公告 (3 URL): 429
- Accel 投资者公告 (2 URL): 404
- TechCrunch / Bloomberg / CNBC / Reuters / Forbes (5+ URL): 401-404/403

**P14 结论**：原始英文官方投资方公告 + 10+ 英文主流媒体报道 URL 全部未 HTTP 验证；严格按 P12 spec-required 第 17 条 + P14 spec-required 8 快速降权 → partial；不为了状态好看而升级。

#### P14 主体轻量修订 (不重写)

- **§1 一句话定位**: [判断] 注释 3 处（"AI website builder" 概括 / "目标用户" 描述 / "设计+上线" 价值）
- **§8 交互与视觉设计**: AI agents Canvas 嵌入加 [事实 / 官方 demo] + [判断] 双层标注
- **§16 今日复盘**: Framer 创新 / Product-Analysis 启发 加 [判断] 注释
- **§17.1 当前状态**: 从 "未复核" 改为 "P14 人工复核完成" + review_status 升级说明
- **§17.3 后续 AI 分析改进**: 新增 P14 5 条 (22 → 27 → 32 → 37 → 42 → 47 行内条目)
  - 7. YAML source_urls 必须是纯 URL 列表
  - 8. 私人公司融资/估值 high-risk 事实快速降权 → partial
  - 9. 官方 blog/newsroom 是 announcement source = 高可信度
  - 10. Founder personal website = secondary source
  - 11. P14 source-hardening 与 P12 同源处理
- **§17.4 Sources 实链验证表**: 新增 macapp.so + P14 主动尝试 10+ URLs 失败表

#### 修改文件 (4 个)

- `analyses/ai-assisted/2026-07-01-framer.md`: YAML 规范化 + 主体轻量修订 (不重写)
- `README.md`: AI 索引 Framer 状态 draft → reviewed
- `CHANGELOG.md`: 顶部 P14 记录 (本节)
- `reports/P14-framer-review-and-yaml-source-normalization-report.md`: 新增 P14 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (7b72404 = P13)
- ✅ Framer 文 ~31 → ~33 KB (+1.6 KB source-hardening + [判断] 注释 + §17.3 P14 5 条)
- ✅ analyses/ai-assisted/2026-07-01-framer.md 存在
- ✅ YAML review_status = reviewed
- ✅ YAML reviewed_at = 2026-07-01
- ✅ YAML review_notes = P14 复核完整版
- ✅ YAML source_url_verification_status = partial (原因清晰)
- ✅ YAML 纯 URL 解析可验证 (29 URLs)
- ✅ [判断] 注释 11 处 (避免营销口径被当事实)
- ✅ §17.1 改为 P14 复核完成状态
- ✅ §17.2 18 → 18 条 (无变化, 已是 P13 完善版)
- ✅ §17.3 11 → 16 条 (P14 spec-required 5 条)
- ✅ §17.4 Sources 实链验证表 新增 macapp.so + P14 主动尝试 10+ URL 失败表
- ✅ Sources 4 分组 同步更新 (P14 未变动, 已是 P13 完善版)
- ✅ Perplexity / Linear / Raycast / Cursor / Figma mtime 未变
- ✅ 9 旧人工分析文章 + pic/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P13 - Framer AI 辅助产品分析 (第 6 篇)

**日期：** 2026-07-01
**变更类型：** source-first / ai-assisted / new-article
**变更范围：** analyses/ai-assisted/2026-07-01-framer.md (新增 31KB) + README + CHANGELOG + P13 报告

### 变更内容

第六篇 AI 辅助产品分析 — Framer，使用 source-first workflow。

#### Source-First URL Verification (P13)

**验证统计：**
- Framer 官方页面：24 个 HTTP-200 verified (官网 / pricing / AI / features/ai / CMS / enterprise / developers / blog / features / templates / marketplace / plugins / learn / agents / analytics / seo / localization / forms / hosting / contact / support / help / parts / status / showcase / community)
- 主流量化媒体：5 个尝试（TechCrunch / The Verge / FastCompany / Crunchbase / Wikipedia）→ 全部 404/403
- Secondary 来源：中文媒体转载（腾讯新闻）引述 $100M Series D / $2B valuation / Meritech+Atomico+Accel → 中文原文可验证，原始英文投资方公告 URL 未直接 HTTP 验证

**关键官方 Source Verified：**
1. `framer.com/` — "AI website builder for professional sites" / Framer 3.0 with Agents
2. `framer.com/pricing/` — Free / Basic $10 / Pro $30 / Enterprise; site-based pricing; AI credits 500/1,000/3,000/mo; CDN 20 loc(Basic)/300+ loc(Pro)
3. `framer.com/ai/` — AI models Petal 3.1 / Ember 4.7 / Horizon 2.1; Design/CMS/Code agents
4. `framer.com/features/ai/` — External agents: Claude / Codex / Cursor / Terminal / Slack / GitHub PR
5. `framer.com/cms/` — AI CMS agent; collections; content-canvas sync; on-page editing
6. `framer.com/blog/` — "Introducing Framer 3.0 with Agents, Branching, and a new Community"; Academy: 320 articles / 256 creators / 18 categories / 7 styles
7. `framer.com/enterprise/` — SSO / SCIM / Uptime guarantee / custom limits
8. `framer.com/developers/` — Server API / Fetch / Components / Overrides / Auto-Sizing / Property Controls

**高风险事实 Partial 原因：**
- Framer 是私人公司（无 SEC filings / 无 investor relations / 无 Wikipedia 条目）
- 官方 about/press/investors/changelog/privacy/terms 页面均不存在或 404
- Founders 背景（Sofa → Facebook）：Koen Bok / Jorn van Dijk 个人网站 verified，但非官方 cofounder bio page
- Series D $100M / $2B valuation：中文转载引述 Meritech/Atomico/Accel 公告，中文原文可读但原始投资方 URL 未直接 HTTP 验证

#### 文章核心内容

- **一句话定位**：AI website builder for professional sites（官网 verified）
- **核心机制**：Design canvas + CMS + AI agents + Publishing + Templates 五大支柱
- **AI agents**：Design agent (Petal/Ember/Horizon) + CMS agent + Code agent + External agents (Claude/Codex/Cursor)
- **Pricing**：Free $0 / Basic $10 / Pro $30 / Enterprise Custom；site-based 限制；AI credits 按月
- **竞品**：Webflow / Wix / Squarespace / WordPress / Figma Sites / Canva / Lovable/v0 等
- **中文 MVP 推断**：面向 AI 原生个人项目和小团队的产品官网生成器（判断，非事实）

#### review_status + source_url_verification_status

- **review_status**: draft（P13 初稿，待 P14 人工复核）
- **source_url_verification_status**: partial（诚实评估：主体产品功能 verified；融资/估值/创始人背景 partial）

#### 修改文件 (4 个)

- `analyses/ai-assisted/2026-07-01-framer.md`: 新增 31KB，17 节，YAML 11 字段
- `README.md`: AI 索引新增 Framer 行 (draft / partial)
- `CHANGELOG.md`: 顶部 P13 记录 (本节)
- `reports/P13-framer-ai-assisted-analysis-report.md`: 新增 P13 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (ed64243 = P12)
- ✅ Framer 文 31KB 新增
- ✅ analyses/ai-assisted/2026-07-01-framer.md 存在
- ✅ YAML review_status = draft
- ✅ YAML reviewed_at = 2026-07-01
- ✅ YAML source_url_verification_status = partial
- ✅ §17.4 Sources 实链验证表存在 (31 个来源)
- ✅ Sources 4 分组完整 (Official+Primary 14 / Product+Docs 12 / Verified Media 2 / Secondary 1 / Unverified 11)
- ✅ Perplexity mtime 未变 (11:41)
- ✅ Linear mtime 未变 (12:57)
- ✅ Raycast mtime 未变 (15:26)
- ✅ Cursor mtime 未变 (16:03)
- ✅ Figma mtime 未变 (P12 后)
- ✅ 9 旧人工分析文章 + pic/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P12 - Figma 人工复核与公开公司事实加固

**日期：** 2026-07-01
**变更类型：** review / source-hardening / docs-only
**变更范围：** analyses/ai-assisted/2026-07-01-figma.md (YAML + lead + §3 + §17.1 + §17.2 + §17.3 + §17.4 + Sources 3 分组) + README + CHANGELOG + P12 报告

### 变更内容

对第五篇 AI 辅助产品分析 — Figma 进行人工复核与高风险事实加固。状态从 `draft` 升级为 `reviewed`。

#### Source-hardening 增量 (P12 新增 7 verified URLs)

1. `figma.com/newsroom/` (200 verified) — **Q1 2025 Figma at a glance 官方原文**: 1,600+ 员工 / 2/3 月活非设计师 / 85% 月活非美国 / 50%+ 营收非美国
2. `figma.com/blog/config-2025-recap/` (200) — Dylan Field 2025-05-07 官方 announcement: Config 2025 五款产品 (Make/Sites/Grid/Draw/Buzz) — **P11 误漏 Grid, P12 补**
3. `figma.com/blog/config-2026-recap/` (200) — 官方 2026-06-24 announcement: Config 2026 五项 canvas 升级 (Code Layers / Figma Motion / Shaders / Generative Plugins / Weave 整合)
4. `figma.com/blog/connecting-figma-and-weave/` (200) — Itay Schiff 2026-06-24 官方 announcement: 确认 "Figma has acquired Weavy...As Figma Weave"
5. `config.figma.com/` (200) — Config conference 官方主页
6. `weave.figma.com/` (200) — Figma Weave 产品独立站
7. `efts.sec.gov/LATEST/search-index?q=%22Figma%22&forms=S-1` (200) — SEC EDGAR S-1 搜索 (P11 之前 500 错误, P12 重试成功)

#### Reuters / Bloomberg / CNBC 原报道 URL 验证 (P12 新增尝试)

| URL | 类型 | 状态 |
|-----|------|------|
| `reuters.com/business/figma-jumps-ai-push-boosts-software-design-spending-2026-02-19/` | Reuters Datadome | 401 |
| `reuters.com/business/figma-shares-jump-ai-push/` | Reuters Datadome | 401 |
| `reuters.com/markets/figma-ipo-2025-07-31` | Reuters Datadome | 401 |
| `fastcompany.com/91329127/figma-config-2025-dylan-field` | Fast Company | 403 |

**结论**: Reuters/Bloomberg/CNBC 原报道 URL 全部 Datadome-protected (与 P9 Cursor 401 模式一致);IPO/财务类事实严格按 source-quality-checklist 未达"双独立 verified media"门槛,保持 `partial` 状态 (诚实评估, 不是失败)。

#### 重大事实修订

1. **Config 2025 产品数量 4 → 5**: P11 文中 "Make/Sites/Buzz/Draw" 4 款, 实际官方 blog 原文有 **Grid** (从自由画布切换到结构化设计), P12 §3 表格 + §17.2 升级
2. **员工数 1886 → 1,600+**: P11 误信 Wikipedia "员工 1886", P12 发现 figma.com/newsroom/ Q1 2025 官方明确 "Figma has over 1,600 employees globally", P12 弃用 P11 1886
3. **Figma Weave 收购 date 2025-10 → 2026-06-24 Config 公告**: P11 文中 "Weavy 收购 2025-10" 来源不明, P12 官方 blog 明确 Itay Schiff 2026-06-24 announcement;具体收购日期与金额仍部分不公开
4. **新增 Config 2026 五项升级**: Code Layers / Figma Motion / Shaders / Generative Plugins / Weave 整合, P11 完全遗漏, P12 补到 §3 表格 + §17.2

#### §17.3 P12 新增 5 条 spec-required

17. **公开公司事实要优先使用 SEC / IR / Reuters / CNBC** — Reuters Datadome 401 与 P9 Cursor 一致, 快速降权 → partial, 不浪费 30 分钟
18. **官方 newsroom / blog 是 IPO 之外的事实金矿** — newsroom + Config blog 全部 200 verified, 后续分析必备
19. **Wikipedia 招股书数据 vs Figma 官方 newsroom 优先用官方** — 员工数 P11 1886 vs P12 Newsroom 1,600+ 冲突, 优先官方
20. **Config / 产品发布会事实 = 公司级官方 announcement** — 官方 blog 是 announcement source, 本身就是事实源, 不需要 Reuters/TechCrunch 独立确认
21. **AI monetization / AI credits 是 partial 但不能高** — AI credit 定价模式 / AI 营收占比 是公开公司核心财务数据, 必须 figma.com/pricing + Q-财报 + earnings call 三件套

#### review_status + source_url_verification_status

- **review_status**: draft → **reviewed** ✅
- **source_url_verification_status**: partial (保持; IPO/Adobe 终止 金融事实 Reuters Datadome 401 未突破)
- **source_url_verified_at**: 2026-07-01 (P11 同日复核)

#### 修改文件 (4 个)

- `analyses/ai-assisted/2026-07-01-figma.md`: 多处修订 (YAML + lead + §3 + §17.1 + §17.2 + §17.3 + §17.4 + Sources 3 分组) 主体未重写, 只追加 + 修订高风险事实
- `README.md`: AI 索引 Figma 状态 draft → reviewed
- `CHANGELOG.md`: 顶部 P12 记录 (本节)
- `reports/P12-figma-review-and-public-company-fact-hardening-report.md`: 新增 P12 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (8e5a3a6 = P11)
- ✅ Figma 文 49.8 → 59.4 KB (+9.6 KB source-hardening)
- ✅ analyses/ai-assisted/2026-07-01-figma.md 存在
- ✅ YAML review_status = reviewed
- ✅ YAML reviewed_at = 2026-07-01
- ✅ YAML review_notes = P12 复核版
- ✅ source_url_verification_status = partial (原因清晰)
- ✅ lead / §1 / §3 / §17.1 改写 (Config 2025 5 款 / Config 2026 5 项 / Weave 收购官方 confirmed / 员工数 1,600+)
- ✅ §17.2 18 → 24 条可信度分级 (新增 Config 2026 五项 + Weave 收购升级 high + 员工数升级 high)
- ✅ §17.3 11 → 16 条 (P12 spec-required 5 条)
- ✅ §17.4 Sources 实链验证表 新增 7 verified URL
- ✅ Sources 6 分组同步更新 (Official +6 / Investor-SEC +1 verified / Investor-SEC +4 unverified Reuters/Fast Company)
- ✅ Perplexity mtime 未变 (11:41)
- ✅ Linear mtime 未变 (12:57)
- ✅ Raycast mtime 未变 (15:26)
- ✅ Cursor mtime 未变 (16:03)
- ✅ Figma mtime 改 (P12 source-hardening)
- ✅ 9 旧人工分析文章 + pic/ 未动
- ✅ 无 force push / reset --hard / amend

---

## P11 - Figma AI 辅助产品分析 (第 5 篇)

**日期：** 2026-07-01
**变更类型：** ai-assisted-analysis (新增第 5 篇)
**变更范围：** analyses/ai-assisted/ + README + CHANGELOG + 新增 P11 报告

### 变更内容

第 5 篇 AI 辅助产品分析 — Figma (公开公司 / 协作式设计平台 / Config 2025 五大 AI 产品线 / Dev Mode)。

#### Source-first workflow (严格执行)

- **Figma 官方页 + 官方 docs + Wikipedia + SEC EDGAR full-text search** 全部 HTTP 200 verified (合计 ~23 URL)
- figma.com/ + /design/ + /figjam/ + /slides/ + /make/ + /sites/ + /buzz/ + /draw/ + /dev-mode/ + /pricing/ + /enterprise/ + /security/ + /developers/ + /blog/ + /ai/ + /release-notes/ + /design-systems/ + /developers/api
- help.figma.com/
- en.wikipedia.org/wiki/Figma + en.wikipedia.org/wiki/Dylan_Field
- efts.sec.gov (Figma search + 10-K search)

#### 关键事实双源验证

- **Figma 官方原口径(高)**:产品功能 / 定价 / 设计系统 / Dev Mode / 创始人 (Wikipedia 双源) / Config 2025 五大产品线 / 总部 / 公开公司状态
- **Wikipedia reference(中)**:2012 创立 / 2016 公开 / 2021 FigJam / 2022 Adobe $20B 收购 announced / 2023 Dev Mode / 2024 Slides / 2025 Config 4 大产品 + Weavy 收购 / 2025-07-31 IPO NYSE:FIG / 2025 营收 $1.06B / 员工 1886
- **底层 TechCrunch / Reuters / CNBC 原报道 URL 未直接 HTTP 验证**(只通过 Wikipedia 引用 + 中文转载)
- **Figma /community/ /plugins/ /trust/ /code-connect/ /components/ /variables/ /config-2026/ 路径 404 或 403**,降权
- **investor.figma.com 403**,SEC 详情页 403 (bot-blocked)

#### source_url_verification_status = partial 的诚实评估

按 P11 spec-required 第 12 条 + 第 14 条:
- 公开公司事实应优先用 SEC / IR / Reuters / CNBC 双源 — 本轮 Wikipedia 是单一 reference 源
- IPO / 市值 / revenue guidance 等金融事实必须双源 — 本轮只 Wikipedia + 中文转载
- 故标 partial,不是失败,是诚实评估

#### review_status = draft

- 包含大量 §14 中文 MVP 推断 + §15 项目启发 7 条 + §13 主要问题 8 条
- 待 P12 人工复核 → reviewed (类似 P8 / P10 模式)

#### 关键产品功能 (官方 verified)

- Multiplayer collaboration (云端实时协作)
- Components / Variants / Variables (设计系统)
- Dev Mode (2023-06) / FigJam (2021) / Figma Slides (2024)
- Config 2025 五大新产品: Sites / Make / Buzz / Draw (May 7, 2025)
- Weavy 收购 (2025-10) → Figma Weave
- 1000+ Plugins / Widgets 生态
- 4 角色扩散:设计师 → PM → 工程师 → 企业管理

#### 关键金融事实 (Wikipedia reference)

- 2025-07-31 IPO NYSE:FIG 上市 (首日 +250%, 估值 $65B, IPO 价 $33)
- 2022-09-15 Adobe 宣布 $20B 收购 → 2023 终止
- 2025 营收 $1.06B / 运营亏损 -$1.29B / 1886 员工
- 1300 万用户中 95% 财富 500 客户

#### 定价 (官方 verified)

- Starter: Free (3 files, 2 editors)
- Professional: $15/editor/月
- Organization: $45/editor/月
- Enterprise: Custom (SSO/SCIM/audit log)

### 修改文件

- `analyses/ai-assisted/2026-07-01-figma.md`:新增 35.6 KB 文章(YAML 11 字段 + 17 章节 + Sources 6 分组)
- `README.md`:AI 索引新增 Figma 行(状态 draft + partial)
- `CHANGELOG.md`:顶部 P11 记录(本节)
- `reports/P11-figma-ai-assisted-analysis-report.md`:新增 P11 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (bc37dda = P10)
- ✅ Figma 文章 35.6 KB 存在
- ✅ YAML 11 字段齐
- ✅ review_status = draft
- ✅ source_url_verification_status = partial
- ✅ source_url_verified_at = 2026-07-01
- ✅ 17 章节全产出 (§1-§17)
- ✅ §17.1 明确说"AI 辅助初稿,待人工复核"
- ✅ §17.2 18 条可信度分级
- ✅ §17.3 11 条 spec 必写项 (含 P11 spec-required 5 条)
- ✅ §17.4 Sources 实链验证表存在
- ✅ Sources 6 分组 (Official 19 / Doc 合并 / Investor-SEC 6 / Reference 3 / Secondary 6 / Unverified 9)
- ✅ Perplexity / Linear / Raycast / Cursor mtime 未变
- ✅ 9 旧人工分析文章 + pic/ 未动

---

## P10 - Cursor 人工复核与高风险事实加固

**日期：** 2026-07-01
**变更类型：** review / source-hardening / docs-only
**变更范围：** Cursor 全文 + README + CHANGELOG + 新增 P10 报告

### 变更内容

P10 阶段对 Cursor 文章做人工复核与高风险事实加固,这是关键的 source-hardening 节点。

#### YAML 状态修正

- `review_status`: draft → **reviewed** (P10 完成人工复核)
- `reviewed_at`: 2026-07-01 (保持)
- `review_notes`: 重写,明示 P10 复核范围与 source-hardening 升级项
- `source_url_verification_status`: 保持 partial (诚实评估;SpaceX $60B 收购 + $3B ARR May 2026 仍单源 Wikipedia)
- `source_quality_notes`: 重写,明示 P10 升级项与未升级项

#### P10 重大 source-hardening 升级 (8 项)

1. **Series A $60M at $400M (2024-08-22)** 升 **high** — TechCrunch 2024-08-09 (200) + Cursor blog 2024-08-22 (200) **双独立 verified media**;这是首次达到 source-quality-checklist "双独立 verified media" 标准
2. **Series B $105M (2025-01-16)** 升 **中-高** — Cursor blog 2025-01-16 (200) + Wikipedia;**修正原文章 "$100M" 为 $105M** (按 Cursor 官方原口径)
3. **Series C $900M at $9.9B (2025-06-06)** 升 **中-高** — Cursor blog 2025-06-06 (200) + Wikipedia;同时披露 ARR $500M + Fortune 500 客户 (NVIDIA/Uber/Adobe)
4. **Series D $2.3B at $29.3B (2025-11-13)** 升 **中-高** — Cursor blog 2025-11-13 (200) + Wikipedia;同时披露 ARR $1B + 300+ 团队 + 新增 Coatue/NVIDIA/Google 投资方
5. **ARR $100M (Jan 2025) / $500M (Jun 2025) / $1B (Nov 2025)** 升 **high** — 全部在 Cursor 官方 blog 验证
6. **ARR $3B (May 2026)** 仍 **中** — Wikipedia 单源 (Cursor blog 未明确披露)
7. **Supermaven 收购 (2024-11-12)** 升 **high** — Cursor blog 2024-11-12 (200) + TechCrunch 2024-11-12 (200) 双独立 verified
8. **Half of Fortune 500 是 Cursor 客户** 升 **high** — Cursor blog series-c 官方原口径

#### 本次未升级项(诚实评估)

- **SpaceX $60B 收购** (announced 2026-04-21 xAI deal / 2026-06-16 SpaceX 行使权利, expected Q3 2026 close) — 仍 partial;Reuters / Bloomberg / NYT / SpaceX 官方原报道 URL 全部被 bot 拦截 (401/403),仅 Wikipedia + 中文转载 (QQ / Sohu / IT Home)
- **$3B ARR May 2026** — Wikipedia 单源
- 状态明示:SpaceX 仍 "pending/expected Q3 2026 close",不是 completed

#### 修正的事实错误 (1 项)

- 原文章 §17.1 写 "Series B $100M" → 修正为 "$105M" (按 Cursor 官方 blog 2025-01-16)

#### 新增 source_urls (7 个, 全部 HTTP 200 verified)

- https://www.cursor.com/blog/series-a
- https://www.cursor.com/blog/series-b
- https://www.cursor.com/blog/series-c
- https://www.cursor.com/blog/series-d
- https://www.cursor.com/blog/supermaven
- https://techcrunch.com/2024/11/12/anysphere-acquires-supermaven-to-beef-up-cursor/
- https://techcrunch.com/2024/08/09/anysphere-a-github-copilot-rival-has-raised-60m-series-a-at-400m-valuation-from-a16z-thrive-sources-say/

#### 未改动的内容

- §1-§16 主体未重写
- §14 中文 MVP 推断未改 (已 [判断] 标记)
- §15 项目启发 13 条未改
- §17.1 主体未改 (只修正 1 个数字 $100M→$105M)
- §17.3 16 条对后续分析改进未改
- §17.4 Sources 实链验证表保留 P9 状态
- Perplexity / Linear / Raycast 文未动
- 9 旧人工分析文章 + pic/ 未动
- 不 force push / reset --hard / amend

### 修改文件

- `analyses/ai-assisted/2026-07-01-cursor.md`:
  - YAML review_status: draft → reviewed
  - YAML review_notes: 重写
  - YAML source_quality_notes: 重写
  - source_urls: +7 verified URLs
  - §17.1: 修正 1 个数字 (Series B $100M → $105M)
  - §17.2: +8 P10 source-hardening 升级项
  - §17.5: 新增 P10 复核记录
  - Sources (5 组): Official 增 5 + Reference 增 2
- `README.md`: AI 索引 Cursor 状态 draft → reviewed
- `CHANGELOG.md`: 顶部 P10 记录(本节)
- `reports/P10-cursor-review-and-risk-fact-hardening-report.md`: 新增 P10 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (ea84cb4 = P9.1)
- ✅ Cursor 文 36 → 36.5 KB (主体未重写,只追加 §17.5 + 修正 §17.1 1 个数字)
- ✅ YAML review_status = reviewed
- ✅ YAML reviewed_at = 2026-07-01
- ✅ source_url_verification_status = partial (保持)
- ✅ §17.1 1 个数字修正 (Series B $100M → $105M)
- ✅ §17.2 +8 P10 升级项
- ✅ §17.5 P10 复核记录存在
- ✅ Sources 5 分组 (Official +5, Verified +2)
- ✅ Perplexity / Linear / Raycast mtime 未变
- ✅ 9 旧人工分析文章 + pic/ 未动
- ✅ 无 force push / reset --hard / amend
- ✅ working tree clean post-push

---

## P9 - Cursor AI 辅助产品分析 (第 4 篇)

**日期：** 2026-07-01
**变更类型：** ai-assisted-analysis (新增第 4 篇)
**变更范围：** analyses/ai-assisted/ + README + CHANGELOG + 新增 P9 报告

### 变更内容

第 4 篇 AI 辅助产品分析 — Cursor (AI coding agent / agentic coding IDE / Cloud Agent)。

#### Source-first workflow (严格执行)

- **官方页 + 官方 docs 12 子页 + 官方 blog 4 篇 + GitHub 主仓库 + Anysphere 双域名 + Wikipedia 双页 均 HTTP 200 verified (合计 ~38 URL)**
- cursor.com 主页 / pricing / enterprise / blog / changelog / privacy / security / download / for-teams / contact-sales / dashboard/plugins / careers
- docs.cursor.com welcome / agent / tab / composer / chat / context / models / mcp / background-agents / rules / cli / integrations/github / cloud-agent / cloud-agent/mobile / agent/agents-window / enterprise/organization-groups / plugins / automate / context/semantic-search / account/pricing / account/teams/dashboard
- blog: composer-2-technical-report / ios-mobile-app / reward-hacking-coding-benchmarks / design-mode
- github.com/getcursor/cursor / anysphere.com / anysphere.inc
- Wikipedia: en.wikipedia.org/wiki/Cursor_(code_editor) + en.wikipedia.org/wiki/Anysphere

#### 关键融资/估值事实 (Wikipedia 作为 reference 源)

- 2022 创立:由 MIT 学生 Michael Truell / Sualeh Asif / Arvid Lunnemark / Aman Sanger 创立 (Wikipedia + 官方双源)
- 2023-10: $8M seed from OpenAI Startup Fund (Wikipedia verified)
- 2024-mid: $60M Series A at $400M 估值 (Wikipedia verified, original TechCrunch URL 未直接 HTTP 验证)
- 2024-11: TechCrunch 报道 Benchmark / Index Ventures 抬价至 ~$2.5B
- 2024-12: $100M Series B at $2.6B 估值 (Wikipedia verified)
- 2025-06-05: $900M Series C led by Thrive Capital, $9.9B post-money
- 2025-11-13: $2.3B Series D co-led by Accel + Coatue, $29.3B 估值, Google / Nvidia 跟投
- ARR 里程碑: $100M (Jan 2025) → $500M (June 2025) → $1B (after Nov 2025) → $3B (May 2026)
- 2026-06-16: SpaceX 宣布以 $60B 收购 Anysphere,**pending/expected Q3 2026 close** (明示为"未完成交易")

#### source_url_verification_status = partial 的诚实评估

按 source-quality-checklist 严格标准,融资/估值/ARR 事实:
- 主源:Wikipedia (已 verified, reference 类别)
- 次源:TechCrunch / The Information / Bloomberg / Reuters / Forbes 原报道 URL **未直接 HTTP 验证**
- 严格按 P8.1 §17.3 必写 1 条:"Wikipedia + 官方" = reference + primary-official,**不等于**"两个独立 verified media"
- 故标 partial,不是失败,是诚实评估

#### review_status = draft

- 包含大量个人推断 (§14 中文 MVP / §15 项目启发 6 条)
- 待 P10 人工复核 → reviewed (类似 P8 review 模式)

#### 关键产品功能 (官方 verified)

- Tab 多 token 补全 / Chat with codebase / Composer 多文件编辑 / Agent / Cloud Agent / Background Agent
- MCP (Model Context Protocol) 工具协议 / Codebase Indexing / Semantic Search
- Composer 2 / Composer 2.5 自研编码模型
- 多模型支持:OpenAI (GPT-5.5) / Anthropic (Opus 4.8) / Google (Gemini 3.1 Pro) / xAI (Grok 4.3) / Cursor (Composer 2.5)
- Cursor for iOS (2026-06-29 public beta, all paid plans)
- Design Mode (2026-06-05) / Cursor Automations (2026-06-18)
- Cursor CLI / Bugbot code review / Cursor 2.0 (2025-10)

#### 定价 (官方 verified)

- Hobby: Free
- Pro / Pro+ / Ultra: $20/月
- Teams: $40/用户/月 (含 SAML/OIDC SSO + team marketplace + 共享 agent context)
- Enterprise: Custom (SCIM + audit log + AI code tracking API)

#### 关键事件

- 2025-04 "Sam"事件:AI help-desk 虚构登录策略,致用户取消,Wikipedia 引用 [10]
- 2025-09 "CopyPasta 许可证攻击"安全事件:HiddenLayer 报告提示注入风险
- 2026-06-16 SpaceX 宣布 $60B 收购 Anysphere (pending/expected Q3 2026)

### 修改文件

- `analyses/ai-assisted/2026-07-01-cursor.md`:新增 27.2 KB 文章(YAML 11 字段 + 17 章节 + Sources ~40 URL)
- `README.md`:AI 索引新增 Cursor 行(状态 draft + partial)
- `CHANGELOG.md`:顶部 P9 记录(本节)
- `reports/P9-cursor-ai-assisted-analysis-report.md`:新增 P9 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (2bf4b26 = P8.1)
- ✅ Cursor 文章 27.2 KB 存在
- ✅ YAML 11 字段齐
- ✅ review_status = draft
- ✅ source_url_verification_status = partial
- ✅ source_url_verified_at = 2026-07-01
- ✅ 17 章节全产出 (§1-§17)
- ✅ §17.1 明确说"AI 辅助初稿,待人工复核"
- ✅ §17.2 26 条可信度分级(高/中/低/待观察)
- ✅ §17.3 11 条 spec 必写项 (含 P8.1 5 条)
- ✅ §17.4 Sources 实链验证 ~40 URL (含 inferred/paywalled 标记)
- ✅ Perplexity / Linear / Raycast mtime 未变
- ✅ 9 旧人工分析文章 + pic/ 未动

---

## P8 - Raycast 人工复核与状态升级

**日期：** 2026-07-01
**变更类型：** review / source-hardening / docs-only
**变更范围：** Raycast 全文 + README + CHANGELOG + 新增 P8 报告

### 变更内容

P8 阶段对 Raycast 文章做人工复核，将 review_status 从 draft 升级为 reviewed。

#### YAML 状态修正

- `review_status`: draft → reviewed
- `reviewed_at`: 2026-07-01 (保持)
- `review_notes`: 更新为 P8 复核版（明示 P8 复核 + 判断部分保留为 judgment）
- `source_url_verification_status`: 保持 partial（诚实评估，融资/估值仍单源 TC + 官方 blog 自述）
- `source_quality_notes`: 更新为 P8 复核版（明示主体产品机制已 verified；融资/估值 partial；§14/§15 标记为 [判断]）

#### 文章主体复核改动（只做 5 处明示性修改，未重写主体）

1. **顶部引用（lead）** 增加 metaphor 明示：「本文使用"工作流操作系统"作为分析判断 / metaphor，非 Raycast 官方产品定位用语」
2. **§1 一句话定位** 增加 [判断] 标记，明示「生产力操作系统前端」是分析 metaphor，非 Raycast 官方用语
3. **§17.1 当前状态** 改为 P8 复核版，说明 review_status 升级、partial 保持、判断部分标记
4. **§17.2 可信度分级表** 扩充至 18 条，按 spec 分级（产品定位 / 生态机制 / AI 价值 / 竞争定位 / 融资 / 平台 / 价格 / 推断 / 假设）
5. **§17.5 P8 人工复核记录** 新增小节，记录本次复核的具体改动

#### §17.2 新增的关键可信度结论

- Raycast 是 macOS command bar / launcher / productivity platform：**高**（官方主页 + manual + docs）
- Extension Store 是核心生态机制：**高**（官方 Store + GitHub extensions）
- Raycast AI 是 Pro 价值的重要组成部分：**高**（官方 AI 页 + pricing 页）
- Raycast AI 是 Pro 的「主要增长驱动」：**中**（官方口径不明确，使用频次无公开数据）
- Windows 扩展仍处于 waitlist / early expansion signal：**中**（官方 blog/waitlist，不当成熟产品线）
- 中文 Raycast 更适合先做 AI worker / Windows / 浏览器场景：**待观察**（个人判断，不是事实）

#### 未改动的内容

- 文章主体 §1-§16 整体未重写
- §14 中文 MVP 推断（已 [判断] 标记）
- §15 项目启发（已 [判断] 标记）
- §17.4 Sources 实链验证表（保持 P7 状态：28 URL verified，P8 未重新验证）
- 9 旧人工分析文章 + pic/ 未动
- P5 Linear / P6 / P6.1 Linear / P4.2 / P4.1 / P4 Perplexity 历史文章未动

### 修改文件

- `analyses/ai-assisted/2026-07-01-raycast.md`:
  - YAML review_status: draft → reviewed
  - YAML review_notes: 更新
  - YAML source_quality_notes: 更新
  - 顶部 lead: 增加 metaphor 明示
  - §1: 增加 [判断] 标记
  - §17.1: 改为 P8 复核版
  - §17.2: 扩充至 18 条
  - §17.5: 新增 P8 复核记录
  - 文末状态行：增加 P8 复核信息
- `README.md`: AI 索引 Raycast 状态 draft → reviewed
- `CHANGELOG.md`: 顶部 P8 记录（本节）
- `reports/P8-raycast-review-and-status-upgrade-report.md`: 新增 P8 报告

### 验证

- ✅ 起始 HEAD = origin/master clean (154e28d = P7)
- ✅ Raycast 文 16.2 → 25 → 25.5 KB (主体未重写，只追加复核记录)
- ✅ YAML review_status = reviewed
- ✅ YAML review_notes 已更新为 P8 版
- ✅ YAML source_quality_notes 已更新为 P8 版
- ✅ source_url_verification_status = partial (保持)
- ✅ reviewed_at = 2026-07-01 (保持)
- ✅ 顶部 lead 增加 metaphor 明示
- ✅ §1 增加 [判断] 标记
- ✅ §17.1 改为 P8 复核版
- ✅ §17.2 扩充至 18 条可信度分级
- ✅ §17.5 新增 P8 复核记录
- ✅ 文末状态行增加 P8 复核信息
- ✅ Perplexity / Linear mtime 未变
- ✅ 9 旧人工分析文章 + pic/ 未动
- ✅ working tree clean post-push

---

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
