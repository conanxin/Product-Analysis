# Changelog

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
