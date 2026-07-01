# Source Quality Checklist / 来源质量检查清单

**版本：** v1.0
**日期：** 2026-07-01
**目的：** 为 Product-Analysis 仓库的 AI 辅助产品分析提供统一的来源质量标准。

---

## 1. 来源分级

| 等级 | 类型 | 示例 | 使用方式 |
|---|---|---|---|
| **primary-official** | 产品官方主页、官方文档、官方发布 | `perplexity.ai`, `aws.amazon.com/...case-study` | 最高权重 |
| **primary-partner** | 合作方官方说明、案例研究 | AWS case study, Microsoft Azure 案例 | 高权重 |
| **high-quality-media-verified** | 主流媒体（CNBC/Reuters/Verge/TechCrunch/WSJ）已实链验证 | 实链 200 + 标题匹配 | 高权重 |
| **high-quality-media-paywalled** | 主流媒体报道但需订阅 | The Information, FT, WSJ 部分文章 | 需付订阅才能验证全文 |
| **high-quality-media-inferred** | 主流媒体 URL 推定但未能 HTTP 验证 | CNBC/Verge 推定路径 | **不能**作为 verified 来源；需后续补全 |
| **secondary-syndication** | 中文转载、第三方转引 | QQ 转载 CNBC、IT 之家、MacRumors | 仅作补充验证 |
| **aggregator** | 评测聚合、目录站 | SourceForge, G2, Capterra | 仅作产品信息交叉 |
| **low-confidence** | 博客、自媒体、未经验证的报告 | 个人博客、SEO 软文 | 不作事实来源 |
| **unavailable** | URL 404、403、被防抓取 | 已删除页面、Paywall | 需补全或换源 |

---

## 2. AI 产品分析的最低来源要求

每篇 AI 辅助产品分析（`analyses/ai-assisted/YYYY-MM-DD-product-name.md`）至少满足：

### 2.1 数量与覆盖

- 至少 **1 个 primary-official** 或 primary-partner 来源
- 至少 **2 个 high-quality-media-verified** 或 **1 个 verified + 1 个 paywalled** 来源
- 至少 1 个 secondary-syndication 作为补充验证

### 2.2 关键事实双源验证

下列高风险事实**必须**有 2 个以上独立来源交叉验证：

- 估值 / 融资 / 上市 / 股价
- 收购 / 合并 / 投资
- 合作 / 战略联盟 / 资金金额
- 重大产品发布时间线
- 重大法律 / 监管 / 诉讼
- 商业模式 / 定价
- 用户规模 / DAU / MAU / 渗透率

### 2.3 禁止的来源方式

- **聚合页** (QQ/so.html5/baike) 不能作为唯一来源
- **推定 URL** (基于日期/标题猜的) 不能作为 verified 来源
- **未调阅原文** 的付费墙报道 (The Information/FT) 需标注 paywalled-but-not-verified
- **自相矛盾** 的转载（同一事件不同日期/不同数字）需在文中标注冲突

---

## 3. 从 draft 到 reviewed 的要求

`review_status: draft → reviewed` 需要：

- [ ] 文章结构完整（按 16 维度模板）
- [ ] Sources 分组清晰（至少分 Official/Quality Media/News-Aggregator/Secondary）
- [ ] 人工复核结论（17.1）已写
- [ ] 可信度分级（17.2）已写，至少 8 条结论
- [ ] 每条结论标注 [事实] / [事实+判断] / [判断] 证据强度
- [ ] review_notes 已加入 YAML

## 4. 从 reviewed 到 source_url_verified 的要求

`source_url_verification_status: partial → verified` 需要：

- [ ] 全部 primary-official / primary-partner 来源已 HTTP 200 验证
- [ ] 至少 1 个 high-quality-media-verified 来源已 HTTP 200 验证
- [ ] 全部 high-quality-media-inferred 来源已替换为可验证 URL 或移到 Unverified 区
- [ ] 全部 paywalled 来源在文中标注"未能核验全文"
- [ ] 在 § 17.5 Sources 实链验证 中记录每条 URL 的验证状态

---

## 5. URL 验证流程

```
对每条 source_url:
  1. 发起 HTTP HEAD/GET 请求
  2. 记录状态码:
     - 200 + 标题匹配 → verified
     - 200 + 标题不匹配 → unverified (title-mismatch)
     - 200 但内容被登录墙遮挡 → paywalled-but-verified (标题可见)
     - 301/302 重定向到首页 → unverified (redirect-to-home)
     - 404 / 410 → unverified (not-found)
     - 403 / 401 → paywalled-or-blocked
     - 522/524/timeout → unverified (timeout)
  3. 若 unverified:
     - 在 Sources 中标记 "需进一步核实"
     - 在 § 17.2 可信度分级 同步降级
     - 移到 Unverified / Needs Follow-up Sources 小节
```

---

## 6. 不允许的 source handling 错误

P4 中出现的错误案例（用于复盘，P4.1 已修正）：

1. **基于标题/日期推定 URL 后未做 HTTP 验证**：7 个高质量媒体 URL 中 6 个未能验证
2. **声称"以高质量媒体为主"但实际依靠转载**：诚实评估需在文中明示
3. **在 § 17.2 给出"高"可信度但未在 § 17.5 做实链验证**：可信度分级表与实链验证脱节
4. **Paywalled 报道（The Information）未标注"未能核验全文"**：默认当作已验证

P4.1 起所有新增 AI 分析应避免上述错误。

---

## 7. 后续维护

- 每月检查 P3+ 已发布分析的实链状态
- 每年至少重新验证一次主来源
- 与 P1-P4 一致：P5+ 的 AI 分析在 release 前需通过本 checklist

---

*建立日期：2026-07-01 | 与 P4.1 同时发布*
