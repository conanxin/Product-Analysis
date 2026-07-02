# Validation Workflow / 验证工作流

**创建日期：** 2026-07-02 (P24)
**对应脚本：** `scripts/verify_ai_analysis_index.py`

---

## 1. 为什么需要自动验证

近期出现过三类质量问题：

1. **YAML duplicate key**（P22 教训）：Replit 文章出现两个 `source_quality_notes:` 字段，PyYAML `yaml.safe_load` 静默覆盖前一个，P22.1 修复。
2. **索引漂移**（P19 / P23 / P23.1 教训）：文章 YAML 与 index.yml 同步后，README.md 或 analyses/README.md 的"当前质量状态"统计未同步。
3. **source_urls 格式**（P22/P23 教训）：source_urls 必须保持纯 URL 字符串，不能混入 type/status 备注。

P24 脚本将这些检查从人工转为自动。

---

## 2. 如何运行

```bash
cd <repo-root>
python3 scripts/verify_ai_analysis_index.py
```

**退出码：**
- `0` = PASS
- `1` = FAIL

**依赖：** Python 3.10+ + PyYAML (`pip install pyyaml`)

---

## 3. 检查项

| # | 检查 | 错误代码 | 说明 |
|---|------|----------|------|
| 1 | Front matter 提取 | `NO_FRONT_MATTER` | 每篇 `analyses/ai-assisted/YYYY-MM-DD-*.md` 必须有 `---` 包裹的 YAML |
| 2 | 重复 YAML key | `YAML_DUPLICATE_KEY` | 自实现 top-level key 计数器（不依赖 yaml.safe_load） |
| 3 | YAML 解析 | `YAML_PARSE_ERROR` | yaml.safe_load 解析 front matter |
| 4 | 必备字段 | `MISSING_FIELDS` | 11 字段：product / category / tags / source_urls / analysis_type / created_at / review_status / source_url_verified_at / source_url_verification_status / source_quality_notes / one_line_insight |
| 5 | review_status 条件 | `MISSING_REVIEWED_AT` / `MISSING_REVIEW_NOTES` | reviewed 必须有 reviewed_at + review_notes |
| 6 | source_urls 格式 | `SOURCE_URLS_FORMAT` | list / string / http(s):// 前缀 / 无 markdown 分隔符 |
| 7 | index.yml 解析 | `INDEX_YAML_PARSE_ERROR` / `INDEX_MISSING_KEYS` | analyses list + summary 存在 |
| 8 | index entry 字段 | `INDEX_ENTRY_MISSING_FIELDS` | 10 字段完整性 |
| 9 | summary count | `SUMMARY_MISMATCH` | 动态计算 vs summary 字段 |
| 10 | article ↔ index | `FIELD_MISMATCH` / `TAGS_MISMATCH` / `REVIEWED_AT_MISMATCH` | 8 字段对比 |
| 11 | README 质量状态 | `README_SUMMARY_MISMATCH` | 动态期望值 vs 表格实际值 |
| 12 | 产品状态行 | `PRODUCT_ROW_MISSING` / `PRODUCT_STATUS_MISMATCH` | 字符串匹配：产品名存在 + 行含 expected status |

---

## 4. 输出格式

### PASS 示例

```
PASS: AI analysis index validation passed
- articles_checked: 10
- index_entries: 10
- reviewed: 10
- draft: 0
- partial: 10
- verified: 0
```

### FAIL 示例

```
FAIL: AI analysis index validation failed
[YAML_DUPLICATE_KEY] 2026-07-01-replit.md duplicate key: source_quality_notes
[README_SUMMARY_MISMATCH] README.md reviewed count expected 10, got 9

- articles_checked: 10
- index_entries: 10
- reviewed: 10
- draft: 0
- partial: 10
- verified: 0
```

---

## 5. 常见失败模式与修复

| 错误代码 | 根因 | 修复 |
|----------|------|------|
| `YAML_PARSE_ERROR` | `source_quality_notes` / `review_notes` 值含未加引号冒号 `:` | 用双引号包裹整个值 |
| `YAML_DUPLICATE_KEY` | 同一字段写了两次 | 删除一个，合并内容 |
| `SUMMARY_MISMATCH` | index.yml summary 与实际 analyses list 不一致 | 重新计算并修正 summary |
| `README_SUMMARY_MISMATCH` | README 质量状态表格数字漂移 | 修改 README.md 表格 |
| `FIELD_MISMATCH` | article 与 index.yml 字段值不一致（如引号风格 `"..."` vs `'...'`） | 同步两边文本 |
| `PRODUCT_STATUS_MISMATCH` | README 产品行 status 与 index.yml 不一致 | 修改 README 产品行 |

---

## 6. 工作流

### 新增 AI 辅助分析时

1. 撰写 `analyses/ai-assisted/YYYY-MM-DD-<product>.md`
2. 在 `analyses/index.yml` 加 entry
3. 在 `analyses/README.md` + `README.md` 加产品行
4. 更新质量状态表格
5. **运行 `python3 scripts/verify_ai_analysis_index.py` → 必须 PASS**
6. commit + push

### 人工复核升级 (draft → reviewed) 时

1. 修改文章 `review_status: draft → reviewed` + `reviewed_at` + `review_notes`
2. 更新 `analyses/index.yml` 对应 entry
3. 更新 `analyses/README.md` + `README.md` 产品行 + 质量状态 + todo + 最后更新
4. 更新 `CHANGELOG.md`
5. **运行 `python3 scripts/verify_ai_analysis_index.py` → 必须 PASS**
6. commit + push

### 索引漂移修复时

1. 修改 README.md / analyses/README.md 质量状态表格数字
2. **运行 `python3 scripts/verify_ai_analysis_index.py` → 必须 PASS**
3. commit + push

---

## 7. 后续 P* 引用

每个新 P* 任务报告应包含：

```markdown
## Validation
python3 scripts/verify_ai_analysis_index.py → PASS / FAIL
```

---

_P24 (2026-07-02) 引入，承接 P19.1 / P22.1 / P23.1 的索引漂移教训。_