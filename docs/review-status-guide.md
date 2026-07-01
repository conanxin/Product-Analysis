# Review Status Guide / 人工复核状态指南

**版本：** v1.0
**日期：** 2026-07-01
**维护：** P15 任务建立
**关联：** [source-quality-checklist.md](./source-quality-checklist.md)

---

## 1. 状态定义

Product-Analysis 仓库的 AI 辅助产品分析采用**双重状态系统**：

| 状态字段 | 含义 | 值范围 |
|---------|------|-------|
| `review_status` | 人工复核状态 | `draft` / `reviewed` |
| `source_url_verification_status` | 来源 URL 验证状态 | `verified` / `partial` |

### 1.1 review_status

| 值 | 含义 | 转换条件 |
|----|------|---------|
| `draft` | AI 初稿, 待人工复核 | YAML 默认值, P 报告归档后人工复核 |
| `reviewed` | 已人工复核, 可作为参考资料 | 通过 source-quality-checklist 主体审查, 人工完成 P 报告 (P 报告路径记录在 `index.yml`) |

### 1.2 source_url_verification_status

| 值 | 含义 | 升级条件 |
|----|------|---------|
| `partial` | 主体产品功能 verified, 高风险事实缺乏双独立 verified 媒体 | 需要补充高质量 verified 媒体 |
| `verified` | 满足 source-quality-checklist v1.0 最低要求, 高风险事实有双独立 verified 媒体 | 严格按 source-quality-checklist 评估 |

## 2. 状态升级标准

### 2.1 draft → reviewed

要求：
- YAML 字段完整 (product / category / tags / source_urls / analysis_type / created_at / review_status / source_url_verified_at / source_url_verification_status)
- 17 节完整 (§1-§17)
- §17.1 当前状态描述清晰
- §17.2 可信度分级明确 (高/中/低)
- §17.3 后续 AI 分析改进至少 5 条
- §17.4 Sources 实链验证表存在
- 明显判断已标 [判断] / [推断] / [事实]
- README 状态同步
- 对应 P 报告归档

### 2.2 partial → verified

要求（按 source-quality-checklist v1.0 最低要求）：
- 主体 sources HTTP 200 verified
- 关键事实有双源
- 高风险事实至少 2 个独立 verified 高质量来源 (非 Wikipedia 单源, 非中文转载, 非公司自述)
- 融资 / 估值 / 收入 / 收购等不能只靠 Wikipedia / 中文转载 / 公司自述
- Sources 表格完整

## 3. 高风险事实判定

以下事实属于高风险事实，**必须**双独立 verified 高质量媒体：

- 融资
- 估值
- ARR / revenue
- IPO / 市值
- 收购 / 并购 / option / pending transaction
- 用户量 / 客户数
- 法律 / 诉讼 / 监管
- 合作金额
- 价格 / 套餐变化
- 产品发布时间线

## 4. partial 状态详解

`partial` 是 `review_status: reviewed` 下的**正常状态**，不是失败。

典型 partial 场景：
- **私人公司 (无 SEC filings)**: 融资/估值只能依赖中文转载 + 个人网站 + 媒体原报道 URL 401-429/404-405
- **公开公司 IPO 早期**: Reuters / Bloomberg / CNBC 原报道 URL Datadome 401 bot 拦截, Wikipedia 单一来源
- **Wikipedia 是 reference 源, 不是 high-quality-media-verified**

**partial 状态的诚实评估价值**：
- 严格 source-quality-checklist 是产品质量核心
- partial 让读者了解事实可信度边界
- partial 让后续 P 任务有明确升级目标 (寻找 verified 媒体)

## 5. 当前项目状态 (2026-07-01)

| 类型 | 数量 | 状态 |
|------|---:|------|
| 旧人工分析 (legacy) | 9 | legacy-note (根目录) |
| 旧文今日复盘 | 1 | Product Hunt (P2) reviewed |
| AI 辅助分析 | 6 | 全部 reviewed |
| - reviewed | 6 | - |
| - verified | 0 | 严格标准下未达成 |
| - partial | 6 | 主体产品功能 verified, 高风险事实 partial |

**未来目标**：逐步把部分文章升级为 verified，但不强求。partial 是质量标准的合理结果。

## 6. 升级路径示例

### 示例 1: Perplexity 升级 partial → verified (假设)

需要：
- Wikipedia 单一来源 → 至少 1 个独立 verified 媒体 (TechCrunch/Reuters/CNBC 原报道 URL HTTP 200)
- Datadome 401 URL 突破 → agent-browser 或直接订阅
- 公司自述 (perplexity.ai) → 至少 1 个独立 verified 媒体交叉验证

### 示例 2: Figma 升级 partial → verified (P12 已部分尝试)

需要：
- Figma IPO ($33/$65B/+250%) → 至少 2 个独立 verified 媒体 (TechCrunch/Reuters/CNBC)
- Figma Adobe 收购 ($20B/terminated) → 至少 2 个独立 verified 媒体 (FT/WSJ/NYT)
- 招股书数据 (员工/营收/用户) → 至少 1 个独立 verified 财经媒体

### 示例 3: Framer 升级 partial → verified (P14 已尝试)

需要：
- Series D ($100M/$2B) → 至少 2 个独立 verified 媒体 (TechCrunch/Reuters/Atomico 公告)
- Founders (Koen Bok + Jorn van Dijk) → 至少 1 个独立 verified 媒体 (创始人采访原文)
- 中文转载只作 partial 来源

## 7. 维护规则

- `analyses/index.yml` 是结构化索引，必须与文章 YAML 同步
- 根 `README.md` 的 AI 辅助分析索引表是人工可读版本
- `CHANGELOG.md` 顶部记录每次状态变更 (P 报告)
- 旧人工分析不在 AI 辅助分析索引中，保留根目录原位

---

*维护人：辛*
*下次升级：P 报告升级 verified 状态时同步更新本指南*
