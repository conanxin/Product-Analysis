# AI 辅助分析索引一致性 + YAML 质量验证工作流

**创建日期：** 2026-07-02 (P24)
**维护者：** 辛 / Xin Conan
**对应脚本：** `scripts/verify_ai_analysis_index.py`

---

## 背景

Product-Analysis 仓库持续产出 AI 辅助产品分析文章，截至 P24 已有 10 篇（Perplexity / Linear / Raycast / Cursor / Figma / Framer / Notion / Canva / Webflow / Replit）。

近期出现过三类质量问题：

1. **YAML 重复 key**（P22 教训）：Replit 文章的 front matter 出现两个 `source_quality_notes:` 字段，PyYAML `safe_load` 静默覆盖前一个，P22.1 修复。
2. **索引漂移**（P19 / P23 / P23.1 教训）：文章 YAML 与 index.yml 同步后，根 README.md 或 analyses/README.md 的"当前质量状态"统计表未同步，导致 reviewed/draft/partial 数字不对。
3. **Source count 口径混乱**（P22 / P23 教训）：报告中混淆 "YAML source_urls 数量" 和 "HTTP-200 verification 总数" 两个不同口径的数字。

P24 提供一个本地可运行的验证脚本，将这些检查从人工转为自动。

---

## 脚本

**路径：** `scripts/verify_ai_analysis_index.py`
**依赖：** Python 3.10+ 标准库 + PyYAML (`pip install pyyaml`)
**退出码：**
- `0` = PASS（所有检查通过）
- `1` = FAIL（有失败项）

### 运行

```bash
# 仓库根目录
cd <repo-root>

# 运行验证
python3 scripts/verify_ai_analysis_index.py

# 验证 + 查看退出码
python3 scripts/verify_ai_analysis_index.py
echo $?  # 0 = PASS, 1 = FAIL
```

### 检查项（共 10 大类，约 80 子项）

#### 1. YAML 依赖检查
- PyYAML 是否安装及版本号。

#### 2. Front matter 提取
- 扫描 `analyses/ai-assisted/YYYY-MM-DD-*.md`（排除 README.md）。
- 每篇文章必须以 `---` 包裹 YAML front matter。

#### 3. 重复 YAML key 检测
- 自实现 top-level key 计数器（不依赖 yaml.safe_load，因为它会静默覆盖）。
- P22.1 教训：必须能检测 Replit 那种同级重复 `source_quality_notes`。

#### 4. YAML 解析与必备字段
- 11 个必备字段：`product` / `category` / `tags` / `source_urls` / `analysis_type` / `created_at` / `review_status` / `source_url_verified_at` / `source_url_verification_status` / `source_quality_notes` / `one_line_insight`。
- `review_status: reviewed` 时必须有 `reviewed_at` + `review_notes`。
- `review_status: draft` 时允许 `reviewed_at` 缺失。

#### 5. source_urls 格式检查
- 必须是 list，每项是 string。
- 每项必须以 `http://` 或 `https://` 开头。
- 每项不得包含 markdown 表格分隔符 `|`。
- 检测明显的 inline annotation（`verified` / `partial` / `primary` / `secondary` 等关键词跟 URL 同行）。

#### 6. analyses/index.yml 解析
- 必须可被 yaml.safe_load 解析。
- 必须包含 `analyses` list + `summary` dict。
- 每个 entry 必须包含 10 个字段：`product` / `file` / `category` / `analysis_type` / `created_at` / `review_status` / `source_url_verification_status` / `tags` / `one_line_insight` / `quality_notes`。

#### 7. summary count 一致性
- 从 analyses list 动态计算：`total` / `reviewed` / `draft` / `verified` / `partial`。
- 与 index.yml `summary` 字段对比。
- 任一不一致报 FAIL。

#### 8. article YAML ↔ index.yml 一致性
- 对每篇文章，按 `file` 路径匹配 index entry。
- 比对 8 字段：`product` / `category` / `analysis_type` / `review_status` / `source_url_verification_status` / `one_line_insight` / `tags` / `reviewed_at`。
- 任一不一致报 FAIL，输出 article value vs index value。

#### 9. README.md 当前质量状态检查
- 提取 `## 当前质量状态` 小节（含 `## N. 当前质量状态` 编号格式）。
- 解析表格中的 `AI 辅助分析` / `reviewed` / `draft` / `verified` / `partial` 计数。
- 与 index.yml summary 动态对比。

#### 10. analyses/README.md 当前质量状态检查
- 同上，但小节标题是 `## 3. 当前质量状态`。

#### 11. 产品状态行一致性（README.md AI 索引 + analyses/README.md AI 总览）
- 解析每个产品在表格中的状态（`reviewed` / `partial` / `draft` / `verified`）。
- 与 index.yml 对应 entry 比对。
- 任一不一致报 FAIL。

---

## 工作流

### 新增 AI 辅助分析时

1. 在 `analyses/ai-assisted/YYYY-MM-DD-<product>.md` 撰写文章。
2. 写入 front matter（含 `product` / `tags` / `source_urls` 等）。
3. 在 `analyses/index.yml` 加 entry。
4. 在 `analyses/README.md` 加产品行。
5. 在 `README.md` 加产品行。
6. 更新 `analyses/README.md` + `README.md` 的"当前质量状态"小节。
7. **运行验证：**
   ```bash
   python3 scripts/verify_ai_analysis_index.py
   ```
8. 必须 PASS 才能 commit + push。

### 人工复核升级 (draft → reviewed) 时

1. 修改文章的 `review_status: draft → reviewed`，加 `reviewed_at` + `review_notes`。
2. 更新 `analyses/index.yml` 对应 entry 的 `review_status` + `reviewed_at` + `quality_notes.reason`。
3. 更新 `analyses/README.md` 产品行的 status。
4. 更新 `README.md` 产品行的 status + 顶部 todo + 最后更新行。
5. 更新 `CHANGELOG.md` 顶部 prepend 复核记录。
6. **运行验证：**
   ```bash
   python3 scripts/verify_ai_analysis_index.py
   ```
7. 必须 PASS 才能 commit + push。

### 索引漂移修复时 (如 P19.1 / P23.1)

1. 修改根 README.md / analyses/README.md 的"当前质量状态"表格数字。
2. **运行验证：**
   ```bash
   python3 scripts/verify_ai_analysis_index.py
   ```
3. PASS 后 commit + push。

---

## 常见失败模式

| 失败信息 | 根因 | 修复 |
|----------|------|------|
| `YAML 解析失败: mapping values are not allowed here` | `source_quality_notes` / `review_notes` 包含未加引号的冒号 `:` | 用双引号包裹整个值，或转义为 `:` |
| `重复 top-level key: source_quality_notes` | 同一字段写了两次（通常合并 P23 + P23.1 / P22.1 修改时发生） | 删除一个，合并内容 |
| `summary.X 期望 N,实际 M` | index.yml summary 与实际 analyses list 计算结果不一致 | 重新计算并修正 summary |
| `README.md 当前质量状态` 不一致 | 数字漂移（如 P23.1 教训） | 修改 README.md 表格 |
| `article→index 一致性 (X)` one_line_insight 不一致 | index.yml 与文章的 one_line_insight 字符串不一致（如 `"..."` vs `'...'`） | 同步两边文本 |

---

## 教程位置

- 脚本：`scripts/verify_ai_analysis_index.py`
- 报告：`reports/P24-ai-analysis-index-validation-script-report.md`
- CHANGELOG：顶部 `## P24` 条目

---

## 后续 P* 引用方式

每个新 P* 任务报告必须包含：

```markdown
## Validation
- python3 scripts/verify_ai_analysis_index.py
- 结果：PASS / FAIL
- 失败项：（如有）
```

这是 P24 起的硬性要求。

---

_本工作流由 P24 (2026-07-02) 引入，承接 P19.1 / P22.1 / P23.1 的索引漂移教训。_