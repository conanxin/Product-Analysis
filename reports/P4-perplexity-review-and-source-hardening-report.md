# P4 - Perplexity Review and Source Hardening 报告

**日期：** 2026-07-01
**仓库：** https://github.com/conanxin/Product-Analysis
**分支：** master
**BASE_COMMIT：** 043dc6983ee9927f7073674cb7b16e8fe3cbee7a
**目标文件：** `analyses/ai-assisted/2026-07-01-perplexity.md`

---

## 状态

**STATUS: PASS**

对 P3 产出的第一篇 AI 辅助产品分析 Perplexity 进行人工复核与来源加固，所有任务项已完成，commit 已 push。

---

## 变更概览

| 文件 | 变更类型 | 主要变更 |
|------|----------|----------|
| `analyses/ai-assisted/2026-07-01-perplexity.md` | 修改 | YAML 升级 + 17. 人工复核结论 + Sources 分组重写 |
| `templates/product-analysis-template.md` | 修改 | 增加 17. 人工复核结论占位 |
| `README.md` | 修改 | AI 索引状态 draft → reviewed |
| `CHANGELOG.md` | 修改 | 顶部增加 P4 记录 |
| `reports/P4-perplexity-review-and-source-hardening-report.md` | 新增 | 本文件 |

---

## Sources 替换统计

### P3 → P4 来源变化

| 来源类型 | P3 数量 | P4 数量 | 变化 |
|----------|---------|---------|------|
| 官方 / Primary | 2 | 3 | +1（perplexity.ai/enterprise） |
| 高质量媒体（CNBC/Reuters/Verge/Information/MacRumors） | 0 | 7 | +7（新增） |
| 中文转载（QQ / so.html5 聚合） | 11 | 12 | +1（增加 Mac 应用备份） |
| 评测聚合（SourceForge） | 1 | 1 | 0（保留为低置信补充） |
| **总计** | **13** | **23** | **+10** |

### P4 Sources 分组结构

| 分组 | 数量 | 来源 |
|------|------|------|
| Official / Primary Sources | 3 | perplexity.ai, /enterprise, AWS case study |
| Quality Media / Direct Reporting | 7 | CNBC × 3, The Verge, MacRumors, Reuters, The Information |
| Infrastructure / Partnership | 1 | AWS 案例（同 Official 中已列） |
| News / Interviews / Analysis（中文转载） | 12 | new.qq.com × 5 + so.html5.qq.com × 7 |
| Secondary / Low-confidence | 1 | SourceForge |

### 官方与高质量媒体来源数量

- **官方来源**：3 个
- **高质量媒体来源**：7 个
- **聚合/低置信来源**：12 + 1 = 13 个（保留作为补充验证，不作为唯一依据）

---

## Review Status 变化

| 字段 | P3 | P4 |
|------|-----|-----|
| `review_status` | draft | **reviewed** |
| `reviewed_at` | （无） | 2026-07-01 |
| `review_notes` | （无） | Sources strengthened; factual claims reviewed; low-confidence claims marked. |

---

## README 状态变化

| 字段 | P3 | P4 |
|------|-----|-----|
| AI 辅助分析索引中 Perplexity 状态 | draft | **reviewed** |

---

## 模板更新

- 在 `templates/product-analysis-template.md` 增加「17. 人工复核结论」占位章节
- 子节：17.1 复核结论 / 17.2 可信度分级（表格）/ 17.3 对后续 AI 分析的改进
- 未破坏模板原有 16 章节结构

---

## 复核结论摘要

### 主要结论保留

- Perplexity 是以"带来源的答案"为核心的 AI 搜索 / 答案引擎（高）
- 引用与脚注是区别于 ChatGPT 的关键体验点（高）
- Comet 时间线：2025-07 Mac、2025-10 全球免费、2026-03 iOS、2026-04 iPadOS（高）
- Pro $20/月、Max $200/月（高）
- 起诉列表 NY Post / Yomiuri / Nikkei / Asahi / Britannica / Merriam-Webster / NYT（高）
- 商业模式矛盾、SEO 倒灌、Comet 高风险赌注（个人推演，标[判断]）

### 需进一步核实

- 2025-08 估值 $20B（中）
- 2025-08 拟 $34.5B 收购 Chrome（中，普遍认为是公关动作）
- 2026-01 Microsoft $7.5 亿 Azure 协议（中）
- 推理成本远高于订阅费（低，个人推演）
- Comet "必胜"Chrome（低，个人推演）

### 主要不确定

- Deep Research / Perplexity Computer / Personal Computer 的能力边界（中，需亲验）
- 中文版 Perplexity 切入 AI 工具垂直的判断（中，个人推演）

---

## 验证清单

| 验证项 | 状态 | 说明 |
|--------|------|------|
| 起始工作区干净 | ✅ | git status clean (HEAD = 043dc69 = origin/master) |
| `review_status` 改为 `reviewed` | ✅ | YAML 已更新 |
| `reviewed_at` 加入 YAML | ✅ | 2026-07-01 |
| `review_notes` 加入 YAML | ✅ | 已加 |
| 17. 人工复核结论 章节加入 | ✅ | 17.1/17.2/17.3/17.4 |
| Sources 分组重写 | ✅ | 5 个分组（Official/Quality Media/Infra/News/Secondary） |
| 可信度分级表 | ✅ | 高/中/低/待观察 |
| 模板增加 17. 占位 | ✅ | product-analysis-template.md 已更新 |
| README 状态同步 | ✅ | draft → reviewed |
| CHANGELOG P4 记录 | ✅ | 顶部 |
| 9 篇旧文章 mtime 未变 | ✅ | 未触碰 |
| `pic/` 未动 | ✅ | 20 张图保留 |
| 主体正文未大幅重写 | ✅ | 仅增加 17 节、调整文末、重写 Sources；不重写 1-16 节内容 |
| 推送后 working tree clean | ✅ | 推送成功 |

---

## P4 任务项

- [x] 对 Perplexity 文章做事实复核
- [x] 替换或补充低质量聚合来源
- [x] 增加"人工复核结论"小节
- [x] 将 `review_status` 从 draft 改为 reviewed
- [x] 更新 README AI 辅助分析索引状态
- [x] 更新 CHANGELOG
- [x] 产出 P4 报告

---

## 后续

- 进入 P5：开始对第 2 个产品做 AI 辅助分析（建议：Notion / Cursor / Raycast / Readwise）
- 在 P4 模板基础上应用新的"可信度分级"流程
- 长期：建立"每 6 个月自动复核" 机制

---

*报告生成于 2026-07-01*
