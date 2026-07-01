# Analyses 索引

本目录是 Product-Analysis 仓库的 AI 辅助产品分析索引。

## 目录结构

```
analyses/
├── README.md                # 本文件 - 索引与质量状态
├── index.yml                # 结构化索引 (机器可读)
├── ai-assisted/             # AI 辅助产品分析文章
│   ├── README.md            # AI 辅助分析目录说明
│   ├── 2026-07-01-perplexity.md
│   ├── 2026-07-01-linear.md
│   ├── 2026-07-01-raycast.md
│   ├── 2026-07-01-cursor.md
│   ├── 2026-07-01-figma.md
│   └── 2026-07-01-framer.md
└── (旧人工分析位于根目录)
```

## AI 辅助产品分析索引 (6 篇)

| # | 产品 | 文件 | 日期 | 状态 | 来源状态 | 报告 |
|---|------|------|------|------|---------|------|
| 1 | Perplexity | [2026-07-01-perplexity.md](ai-assisted/2026-07-01-perplexity.md) | 2026-07-01 | reviewed | partial | [P4](../reports/P4-perplexity-review-and-source-hardening-report.md) |
| 2 | Linear | [2026-07-01-linear.md](ai-assisted/2026-07-01-linear.md) | 2026-07-01 | reviewed | partial | [P6](../reports/P6-linear-review-and-source-upgrade-report.md) |
| 3 | Raycast | [2026-07-01-raycast.md](ai-assisted/2026-07-01-raycast.md) | 2026-07-01 | reviewed | partial | [P8](../reports/P8-raycast-review-and-status-upgrade-report.md) |
| 4 | Cursor | [2026-07-01-cursor.md](ai-assisted/2026-07-01-cursor.md) | 2026-07-01 | reviewed | partial | [P10](../reports/P10-cursor-review-and-risk-fact-hardening-report.md) |
| 5 | Figma | [2026-07-01-figma.md](ai-assisted/2026-07-01-figma.md) | 2026-07-01 | reviewed | partial | [P12](../reports/P12-figma-review-and-public-company-fact-hardening-report.md) |
| 6 | Framer | [2026-07-01-framer.md](ai-assisted/2026-07-01-framer.md) | 2026-07-01 | reviewed | partial | [P14](../reports/P14-framer-review-and-yaml-source-normalization-report.md) |

## 质量状态

| 维度 | 数值 | 说明 |
|------|------|------|
| AI 辅助分析 | 6 | 全部 reviewed |
| reviewed | 6 | 已人工复核 |
| draft | 0 | - |
| verified | 0 | 严格标准下未达成 |
| partial | 6 | 主体产品功能 verified, 高风险事实 partial |
| 旧人工分析 | 9 | 仓库根目录 legacy notes |
| 旧文今日复盘 | 1 | Product Hunt (P2) |

## 状态流转

```
draft → reviewed → partial-to-verified
```

| 状态 | 含义 | 转换条件 |
|------|------|---------|
| **draft** | AI 初稿, 待人工复核 | 写入 analyses/ai-assisted/, YAML review_status: draft |
| **reviewed** | 已人工复核, 可作为参考资料 | 通过 source-quality-checklist 主体审查, 人工复核后 P 报告归档 |
| **partial** | review_status=reviewed + source_url_verification_status=partial | 主体产品功能 verified, 高风险事实 (融资/估值/收购/收入/法律) 缺乏双独立 verified 媒体 |
| **verified** | review_status=reviewed + source_url_verification_status=verified | 高风险事实满足 source-quality-checklist v1.0 最低要求, 双独立 verified 高质量媒体 |

**重要**: partial 不是失败, 是严格质量标准下的诚实评估。

详见 [docs/review-status-guide.md](../docs/review-status-guide.md) 和 [docs/source-quality-checklist.md](../docs/source-quality-checklist.md)。

## 维护说明

1. **新增 AI 辅助分析**: 在 `analyses/ai-assisted/` 下创建 `YYYY-MM-DD-product-name.md`, 同步更新 `analyses/index.yml` 和根 `README.md` 的"AI 辅助分析索引"表格。
2. **人工复核升级**: 修改 `review_status: draft → reviewed`, 同步更新 `analyses/index.yml`。
3. **来源状态升级**: 满足 source-quality-checklist 最低要求后, 修改 `source_url_verification_status: partial → verified`。
4. **旧人工分析**: 不在 AI 辅助分析索引中, 保留根目录原位。

## 关联文件

- [README.md](../README.md) — 仓库主入口
- [docs/source-quality-checklist.md](../docs/source-quality-checklist.md) — 来源质量标准
- [docs/review-status-guide.md](../docs/review-status-guide.md) — review_status 流转指南
- [templates/product-analysis-template.md](../templates/product-analysis-template.md) — 文章模板
- [CHANGELOG.md](../CHANGELOG.md) — 任务历史
- [reports/](../reports/) — 任务报告

---

*本目录由 P15 任务建立 (2026-07-01)。*
