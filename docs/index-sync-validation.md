# Index Sync Validation / 索引一致性校验

**创建日期：** 2026-07-02 (P24)
**对应脚本：** `scripts/verify_ai_analysis_index.py`

---

## 1. 为什么需要这个脚本

近期出现过两类索引 / YAML 质量问题：

1. **YAML duplicate key**（P22 教训）：Replit 文章 front matter 出现两个 `source_quality_notes:` 字段，PyYAML `yaml.safe_load` 静默覆盖前一个，P22.1 修复。
2. **README / analyses/README / index.yml 索引漂移**（P19 / P23 / P23.1 教训）：文章 YAML 与 index.yml 同步后，README.md 或 analyses/README.md 的"当前质量状态"统计未同步；`one_line_insight` 在 article 与 index.yml 之间的引号风格不一致。

手工同步多个索引容易遗漏，P24 把这些检查从人工转为自动。

---

## 2. 脚本检查什么

| # | 检查 | 说明 |
|---|------|------|
| 1 | YAML front matter 提取 | 每篇 `analyses/ai-assisted/YYYY-MM-DD-*.md` 必须有 `---` 包裹的 YAML |
| 2 | YAML duplicate key | 自定义 SafeLoader (P22.1 教训，PyYAML 静默覆盖) |
| 3 | 必备字段 | product / category / tags / source_urls / analysis_type / created_at / review_status / source_url_verified_at / source_url_verification_status / source_quality_notes / one_line_insight |
| 4 | review_status 条件 | reviewed 必须有 reviewed_at + review_notes；只允许 draft / reviewed |
| 5 | source_url_verification_status | 只允许 partial / verified |
| 6 | analysis_type | 只允许 ai-assisted |
| 7 | source_urls 格式 | list[string] / http(s):// 前缀 / 无 inline annotation (verified/partial/primary/secondary/type:/status:) / 无 markdown 分隔符 `\|` |
| 8 | analyses/index.yml 解析 | version / analyses / summary / by_category / reading_paths 必须存在 |
| 9 | index entry 字段 | 10 字段；quality_notes 含 product_mechanism / high_risk_facts / reason |
| 10 | summary 一致性 | 动态计算 vs summary 字段 |
| 11 | article ↔ index | 8 字段对比：product / category / analysis_type / review_status / source_url_verification_status / one_line_insight / tags / reviewed_at |
| 12 | README.md 质量状态 | 动态期望值 vs 表格实际值 |
| 13 | analyses/README.md 质量状态 | 同上 |
| 14 | README.md 产品行 | 字符串匹配：产品名存在 + 行含 expected review_status + source_url_verification_status |
| 15 | analyses/README.md 产品行 | 同上 |

---

## 3. 如何运行

```bash
cd <repo-root>
python3 scripts/verify_ai_analysis_index.py
```

**退出码：**
- `0` = PASS
- `1` = FAIL

**依赖：** Python 3.10+ + PyYAML (`pip install pyyaml`)

### PASS 输出

```
PASS: AI analysis index consistency verified
- analyses found: 10
- reviewed: 10
- draft: 0
- partial: 10
- verified: 0
```

### FAIL 输出

```
FAIL: AI analysis index consistency errors
1. README.md 质量状态表 reviewed expected 10, got 9
2. analyses/ai-assisted/2026-07-01-replit.md duplicate YAML key: 'source_quality_notes'
3. analyses/index.yml Replit review_status=draft but article YAML review_status=reviewed

- analyses found: 9
- reviewed: 9
- draft: 0
- partial: 9
- verified: 0
```

---

## 4. 何时运行

- ✅ 每次新增 AI 分析文章后
- ✅ 每次 review_status 从 draft 升 reviewed 后
- ✅ 每次修改 README / analyses/README / analyses/index.yml 后
- ✅ commit 前
- 🔮 未来可以接入 GitHub Actions / pre-commit hook

---

## 5. 失败如何处理

| 错误类型 | 示例 | 修复方法 |
|----------|------|----------|
| YAML duplicate key | `duplicate YAML key: 'source_quality_notes'` | 删除一个，合并内容 |
| YAML parse error | `yaml.safe_load 失败: mapping values are not allowed here` | 用双引号包裹含冒号的值 |
| Summary mismatch | `index.yml summary.reviewed expected 10, got 9` | 重新计算并修正 summary |
| README summary mismatch | `README.md 质量状态表 reviewed expected 10, got 9` | 修改 README 表格数字 |
| Field mismatch | `one_line_insight: article='...' != index='...'` | 同步两边文本（通常是引号风格） |
| Missing field | `cursor.md 缺失字段: source_url_verified_at` | 添加缺失字段 |
| Product row missing | `README.md 找不到产品 'Replit' 的行` | 在 README 索引表中添加行 |

---

## 6. 后续扩展

- GitHub Actions CI（`.github/workflows/validate.yml`）— 每次 PR 自动跑
- pre-commit hook — commit 前自动跑
- 报告 JSON 输出 — 机器可读
- 自动生成 `analyses/index.yml` — 从 article YAML 自动同步
- 自动生成 README 表格 — 从 index.yml 自动生成 AI 辅助分析索引

---

## 7. P24 修复的真实问题

P24 在最终 PASS 前修复了 12 项真实问题（"如果失败：修脚本或 README/doc；不要修改 AI 文章和 analyses/index.yml，除非发现真实错误并说明"）：

| # | 文件 | 问题 | 修复 |
|---|------|------|------|
| 1 | cursor.md line 80 | `source_quality_notes` 含未加引号冒号 | 加双引号 |
| 2 | cursor.md line 77 | `review_notes` 含未加引号冒号 | 加双引号 |
| 3 | perplexity.md line 47 | `source_quality_notes` 含未加引号冒号 | 加双引号 |
| 4 | raycast.md line 51 | `source_quality_notes` 含未加引号冒号 | 加双引号 |
| 5-13 | index.yml × 9 entries | `one_line_insight` 引号风格不一致（`'` vs `"`） | 从 article 同步 |

这些是脚本自动检测到的真实数据问题。修复后脚本 PASS。

---

_P24 (2026-07-02) 引入，承接 P19.1 / P22.1 / P23.1 的索引漂移教训。_