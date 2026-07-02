# P26 - Coda AI-Assisted Product Analysis Report

**日期：** 2026-07-02
**任务类型：** AI-assisted content + index sync

---

## Task Overview

新增第十一篇 AI 辅助产品分析 Coda，严格遵循 source-first workflow：
1. 先收集并验证 URL
2. 再写文章
3. 同步 4 个索引文件（article YAML / README.md / analyses/README.md / analyses/index.yml）
4. 运行 P24 validator 确认 PASS
5. commit + push

**分析对象：** Coda
**任务源：** Xin Conan Telegram 2026-07-02 10:44 GMT+8

---

## Final Status

```
STATUS: PASS
REPOSITORY: https://github.com/conanxin/Product-Analysis
BRANCH: master
BASE_COMMIT: f20a6d1 (P25)
NEW_COMMIT: (TBD at commit time)
PUSH_RESULT: (TBD at push time)
```

---

## Git State (Pre-Change)

```
$ git log --oneline -10
f20a6d1 P25: add AI analysis index validation CI
fc09a7d P24: add AI analysis index consistency validator
db5a5ab P24.1: rewrite validation script output to spec format
70defde P24: add AI analysis index validation script
4414283 P23.1: fix Replit README quality status drift
e81df08 P23: review Replit analysis and sync index status
a4cb31f P23: review Replit analysis and sync index status
086cebe P22.1: fix Replit YAML duplicate source quality notes
6ca0d8b P22: add Replit AI-assisted product analysis
cf497a9 P21: review Webflow analysis and sync index status
```

---

## Step 0 — Local Pre-Check

```
$ python3 scripts/verify_ai_analysis_index.py
PASS: AI analysis index consistency verified
- analyses found: 10
- reviewed: 10
- draft: 0
- partial: 10
- verified: 0
```

本地 PASS → 可继续 P26。

---

## Step 1 — Source URL 实链验证

P26 共验证 50+ 个 Coda / Grammarly / Wikipedia URL，结果如下：

### Verified (HTTP 200)

| 类别 | 数量 | 主要 URL |
|------|---:|----------|
| Coda 官方主页 | 7 | coda.io / welcome / about / product / product/ai / product/docs-and-team-hubs |
| Coda Packs / Integrations | 13 | product/packs / product/integrations + 10 pack 详情页 |
| Coda Blog | 3 | blog / about-coda/grammarly-acquires-coda / productivity/build-with-advanced-features / productivity/coda-style-guide-for-grammarly |
| Coda Gallery / Templates / Pricing / Compare | 6 | gallery / pricing / compare / compare/notion |
| Coda Auth / Account | 3 | login / signup / dashboard |
| Coda Sales / Demo | 3 | contact / contact/sales / contact/sales/request-a-demo |
| Coda Company / Careers / Press | 1 | careers |
| Coda Security / Trust | 3 | security / trust/security / trust/privacy |
| Coda Docs / API | 2 | docs / api |
| Coda Customer case | 1 | solutions/case-studies/intercom |
| Coda Gallery templates (Case studies) | 5 | @ross/root-cause-reasoning / @codatemplates/engineering-team-hub / @yuhki/figma-product-roadmap / @shivar/rethinking-googles-famous-launchcal / @noah/... / @ben-parker/... |
| Grammarly 官方 | 7 | grammarly.com / about / business / enterprise / products / blog / coda |
| Wikipedia Reference | 2 | Coda_(document_editor) / Grammarly |

**总计 verified 200：** 55 个 source_urls 全部 HTTP 200 可访问

### Unverified / Paywalled / Redirect / 404

| URL | 状态 | 备注 |
|-----|------|------|
| coda.io/product/coda-brain | 301 → 403 | Cloudflare protected |
| help.coda.io | 403 | Cloudflare protected |
| coda.io/enterprise | 301 | 重定向 |
| coda.io/templates | 301 | 重定向 |
| coda.io/ai | 301 | 重定向 |
| coda.io/api | 302 | 重定向 |
| coda.io/automations / buttons / tables | 404 | 路径不存在 |
| coda.io/press / announcements | 404 | 无此页面 |
| Fast Company Coda article | 403 | paywall |
| Axios / CNBC / Bloomberg Coda coverage | 403 / 404 | paywall / 不存在 |
| Crunchbase Coda funding | 403 | paywall |
| Forbes Coda valuation 2021 | paywalled | Wikipedia 二手 |

---

## Step 2 — Article YAML Front Matter

```
product: Coda
category: doc-database
tags:
 - productivity
 - docs
 - database
 - workflow
 - automation
 - ai-productivity
source_urls:
 - 55 verified URLs
analysis_type: ai-assisted
created_at: 2026-07-01
review_status: draft
reviewed_at: null
review_notes: "P26 AI-assisted draft;..."
source_url_verified_at: 2026-07-01
source_url_verification_status: partial
source_quality_notes: "..."
one_line_insight: Coda 将文档、表格、公式、按钮、自动化和应用集成组合成同一个 doc-as-app 工作台，把团队协作从"文档记录"重构为"可操作的业务应用"。
```

YAML 严格使用 custom StrictSafeLoader 解析（PyYAML safe_load 在 P22.1 已知会静默覆盖重复 key）。

---

## Step 3 — Article Body

17 节结构：

| # | 节 | 内容要点 |
|---|----|--------|
| 1 | 一句话定位 | Coda = doc-as-app / app-doc platform；与 Notion / Airtable / Docs/Sheets 差异；Grammarly 收购 |
| 2 | 目标用户 | 9 类：PM / Ops / 创业 / PMO / 内部工具 builder / 文档重度 / data / AI / Superhuman-Grammarly 生态 |
| 3 | 核心场景 | 13 个：team docs / tracker / roadmap / OKR / CRM / meeting notes / decision log / approval / automations / packs / AI / dashboards / internal tools |
| 4 | 产品解决的问题 | 7 个：doc-table 分离 / 数据缺上下文 / 文档缺结构化 / workflow 跳转 / 知识分散 / 非工程内部工具 / AI 缺结构化上下文 |
| 5 | 首页与第一印象 | 官网叙事 + 4 大转化路径 + 未亲验部分 |
| 6 | 核心用户路径 | 创建 doc → table → column → view → formula → button → automation → pack → team → AI → publish |
| 7 | 信息架构 | 16 个核心对象表（Workspace / Doc / Page / Table / Row / Column / View / Formula / Button / Automation / Pack / Template / Permission / AI / Brain / API） |
| 8 | 交互与视觉设计 | 7 大关键点：doc+table 混合 / formula anywhere / buttons / automations / packs / templates / views |
| 9 | 内容 / 社区 / 增长机制 | 5 飞轮：templates / makers / packs / PM-ops-startup / founder-led storytelling |
| 10 | 商业模式 | Maker-based + tier；Free / Pro / Team / Enterprise；AI 含在 Maker；具体金额 partial |
| 11 | 竞品与替代方案 | 13 竞品：Notion / Airtable / Google Docs-Sheets / Excel-Loop-365 / Confluence / Asana / Jira / Monday / ClickUp / Smartsheet / Retool / Obsidian-Tana / Superhuman-Grammarly |
| 12 | 主要优点 | 8 条 |
| 13 | 主要问题 | 8 条 |
| 14 | 如果我来重做 | 中文 MVP: 面向 AI 项目管理和产品研究的 doc-as-app 工作台 |
| 15 | 对我自己项目的启发 | 8 条对 Product-Analysis 的 doc-as-app 启发 |
| 16 | 今日复盘 | 2 条总结 |
| 17 | 人工复核结论 | 17.1 当前状态 / 17.2 可信度分级表 / 17.3 后续 AI 改进 8 条 / 17.4 Sources 实链验证表 |

每条事实按 P17 约定标注 [事实] / [判断] / [primary-source verified] / [partial] / [judgment]。

---

## Step 4 — Index Sync

### README.md 改动

1. AI 辅助分析索引表新增 Coda 行
2. 当前质量状态：AI 辅助分析 10 → 11 / draft 0 → 1 / partial 10 → 11
3. 下一步计划新增 P26 todo
4. 最后更新改为 P26 记录

### analyses/README.md 改动

1. AI 辅助分析总览表新增 Coda 行
2. 按产品类型分组新增 "Doc Database / App Doc" 分类
3. 当前质量状态同步更新（P 报告累计 16 → 17）
4. 下一步分析候选移除 Coda
5. 推荐阅读路径新增 "Doc-as-App 路线"

### analyses/index.yml 改动

1. updated_at: 2026-07-01 → 2026-07-02
2. 新增 Coda 条目（完整字段）
3. summary 更新：total 10→11 / draft 0→1 / partial 10→11 / p_reports_total 16→17
4. by_category 新增 doc-database / Coda
5. reading_paths 新增 doc_as_app_path: Notion → Coda

### CHANGELOG.md 改动

顶部 prepend P26 记录，说明 source-first workflow + 验证结果 + 修复的真实问题

---

## Step 5 — validator 验证结果

### 初跑

```
$ python3 scripts/verify_ai_analysis_index.py
FAIL: AI analysis index consistency errors
1. analyses/index.yml 解析失败: mapping values are not allowed here
  in "<unicode string>", line 251, column 28:
          下一步人工复核 review_status: draft → reviewed。
                               ^
- analyses found: 11
- reviewed: 10
- draft: 1
- partial: 11
- verified: 0
```

### 修复

index.yml 中 quality_notes 的字符串内出现 `review_status: draft`，冒号被解析为 YAML key。删除冒号：

```
下一步人工复核 review_status draft → reviewed。
```

### 复跑

```
$ python3 scripts/verify_ai_analysis_index.py
PASS: AI analysis index consistency verified
- analyses found: 11
- reviewed: 10
- draft: 1
- partial: 11
- verified: 0
```

---

## Step 6 — Pre-Commit 检查清单

- [x] analyses/ai-assisted/2026-07-01-coda.md 存在（618 行）
- [x] YAML front matter 用 custom StrictSafeLoader 解析 OK
- [x] 17 节完整
- [x] source_urls 是纯 URL 字符串列表（55 个）
- [x] review_status: draft
- [x] source_url_verification_status: partial
- [x] one_line_insight 在 YAML 和 index.yml 一致
- [x] README.md AI 索引新增 Coda 行
- [x] README.md 当前质量状态同步
- [x] analyses/README.md AI 辅助分析总览新增 Coda 行
- [x] analyses/README.md 当前质量状态同步
- [x] analyses/index.yml 新增 Coda 条目
- [x] analyses/index.yml summary 计数更新
- [x] analyses/index.yml by_category 新增 doc-database
- [x] analyses/index.yml reading_paths 新增 doc_as_app_path
- [x] CHANGELOG.md 顶部 P26 记录
- [x] reports/P26-coda-ai-assisted-analysis-report.md 存在
- [x] validator PASS
- [x] 不修改 scripts/verify_ai_analysis_index.py
- [x] 不修改旧 10 篇 AI 辅助分析文章
- [x] 不修改旧人工分析文章
- [x] 不移动 pic/ / templates/
- [x] 不引入前端框架 / 构建系统 / GitHub Pages
- [x] 1 项真实问题（YAML 解析错误）已修复

---

## Changed Files

```
analyses/ai-assisted/2026-07-01-coda.md          | new (618 lines)
analyses/index.yml                                | modified (+Coda entry +summary +by_category +reading_paths)
analyses/README.md                                | modified (+Coda row + Doc Database 分组 + 质量状态 + Doc-as-App 路线)
README.md                                         | modified (+Coda row + 质量状态 + P26 todo + 最后更新)
CHANGELOG.md                                      | modified (顶部 P26 记录)
reports/P26-coda-ai-assisted-analysis-report.md   | new
```

**共 6 个文件改动**

---

## Files Intentionally Not Changed

- scripts/verify_ai_analysis_index.py — 未动
- analyses/ai-assisted/2026-07-01-{perplexity,linear,raycast,cursor,figma,framer,notion,canva,webflow,replit}.md — 未动
- 旧人工分析文章（根目录 / legacy notes） — 未动
- pic/ / templates/ — 未动
- .github/workflows/ai-analysis-index-check.yml — 未动
- docs/ — 未动
- .gitignore / package.json / 任何前端文件 — 不存在也不动

---

## Validation Summary

| 检查项 | 结果 |
|--------|------|
| YAML front matter 可解析 | ✅ |
| YAML 不存在重复 key | ✅ |
| source_urls 纯 URL | ✅ |
| source_urls 数量 | 55 |
| 17 节完整 | ✅ |
| §17.1 当前状态 | ✅ draft / partial |
| §17.2 可信度分级 | ✅ 22 行表 |
| §17.3 后续 AI 改进 | ✅ 8 条 |
| §17.4 Sources 实链验证 | ✅ 60+ 行表 |
| README.md AI 索引 Coda 行 | ✅ |
| README.md 当前质量状态 | ✅ 11/10/1/11/0 |
| analyses/README.md AI 总览 Coda 行 | ✅ |
| analyses/README.md 当前质量状态 | ✅ 11/10/1/11/0 |
| analyses/index.yml Coda 条目 | ✅ |
| analyses/index.yml summary | ✅ 11/10/1/11/0 |
| analyses/index.yml by_category | ✅ doc-database 新增 |
| analyses/index.yml reading_paths | ✅ doc_as_app_path 新增 |
| CHANGELOG.md P26 | ✅ |
| validator PASS | ✅ |

---

## NEXT_STEP

1. **P27**：人工复核 Coda 文章（review_status: draft → reviewed），解决 partial 项
   - 主动尝试 Forbes / Fast Company / TechCrunch / Axios 2021 / 2024 报道
   - 验证 800+ vs 600+ integrations 数字
   - 验证 Coda Brain 产品页（cookie / 浏览器）
   - 验证 coda.io/pricing 具体金额
2. **P28 候选**：新增第十二篇 AI 分析（Obsidian / Tana / Arc / Claude Code / Lovable / v0）
3. **P29 (候选)**：pre-commit hook — commit 前自动跑脚本
4. **P30 (候选)**：报告 JSON 输出 — 机器可读
5. **P31 (候选)**：自动生成 analyses/index.yml — 从 article YAML 自动同步
6. **长期**：主流媒体 paywall / 403 / 401 仍是主要 partial 来源；Coda / Notion / Replit / Framer 都是私人公司，需双源验证

---

_报告生成时间：2026-07-02_
_P26 完成状态：PASS（文章 + 索引同步 + validator PASS，待 commit/push）_