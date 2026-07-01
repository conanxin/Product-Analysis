# AI 辅助产品分析

本目录存放 AI 辅助生成的产品分析文章。

## 目录说明

所有 AI 辅助分析的文章都放在本目录下，使用统一格式：

```
YYYY-MM-DD-product-name.md
```

例如：
- `2026-07-01-notion.md`
- `2026-07-02-readwise.md`

## 文章标准

每篇文章必须：
1. **符合模板** — 使用 `templates/product-analysis-template.md` 的结构
2. **包含 YAML front matter** — 在文档顶部声明元数据
3. **经过人工复核** — AI 初稿必须经过人工复核后才能将 `review_status` 改为 `reviewed`

## 质量门槛

不只总结功能，要分析机制。
不只夸优点，也要指出问题。
不只写"可以做中文版"，要说明本土化的用户、场景和差异化。

## 回填主索引

每次新增一篇 AI 分析后，记得在 `README.md` 的"当前内容索引"表格中补充记录：

```markdown
| # | 产品 | analyses/ai-assisted/YYYY-MM-DD-product-name.md | AI辅助 | 分类 | 核心洞察 | 复盘方向 |
```

## 元数据说明

`review_status` 状态流转：

```
draft → reviewed → published
```

- `draft` — AI 初稿，待人工复核
- `reviewed` — 已人工复核，可作为参考资料
- `published` — 最终版，内容质量确认无误

---

*本目录用于沉淀 AI 辅助分析成果，与根目录旧人工分析（legacy manual analysis）区分。*
