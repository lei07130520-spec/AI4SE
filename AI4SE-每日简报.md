# AI4SE 每日简报 · 实战工作流（对外分享版）

> 一份可以**直接复用**的"AI 行业内容追踪 + 结构化产出"工作流。
> 包含完整的信源清单、关键词库、人物名单、产出模板与红线规则。
> 适用场景：垂直领域信息追踪、行业简报运营、研究型内容生产。

---

## 一、任务定义

每天用 AI 自动追踪过去 **24-72 小时** AI4SE（AI for Software Engineering）领域的关键动态，产出一份结构化简报，发布到内容平台（公众号/知识星球/Substack 等均可）。

**为什么聚焦 AI4SE 而不是泛 AI 新闻**：垂直领域才有信号密度。"AI 行业新闻"是噪音，"AI 编码工具产品动态 + 研发范式变化"是可决策的信号。

**节奏建议**：每天上午 10:30（中国时区）执行，正好覆盖前一天美东工作日 + 当天上午国内动态。

---

## 二、覆盖范围

### ✅ 在范围内

**1. AI 编码工具**
- Cursor — 产品更新、Agent 工作流、Parallel Build、企业治理
- Claude Code — 版本发布、Agent View、`/goal`、Skills 体系
- Claude Cowork — 协作场景下的 Agent 能力
- GitHub Copilot — 企业版功能、Workspace、Agent 模式
- OpenAI Codex（双产品线）：Codex CLI（终端 Agent）+ Codex App（云端平台）
- Google Gemini Code Assist + Gemini CLI + Antigravity
- Devin — SWE-bench 进展、企业部署案例

**2. AI Agent 框架与基础设施**
- Hermes Agent（Nous Research）
- OpenClaw（开源 Agent 框架）
- MCP 生态（modelcontextprotocol.io + 主流 MCP Server）
- 多 Agent 编排、子 Agent 协议

**3. 研发范式与方法论**
- Harness Engineering — 治理框架
- Context Engineering — 范式迁移
- Vibe Coding — Bolt.new、v0、Lovable、Replit Agent
- Agentic Coding — 自主编码、人机协作演进

**4. 效率与实证**
- 大规模实证数据（效率/PR/漏洞率）
- 企业规模化部署案例（量化指标优先）
- 研发岗位结构变化数据

**5. AI Agent 安全治理**
- Agent 沙箱隔离、AI 漏洞情报
- 供应链安全（SLSA/SBOM/AI BOM）
- 决策审计、ADLC 框架、安全专用模型

### ❌ 明确排除

- 消费级个人助理
- 非研发 AI 自动化（HR、财务、销售、客服、营销）
- AI 硬件、消费电子
- 算力供应链/芯片合作（除非直接影响编码产品）
- 公司财报/估值/IPO 八卦（除非披露编码产品营收）
- 公司治理/法务/股权八卦
- 政治/伦理纯辩论

---

## 三、信源四级体系（含完整清单）

### Level 1（必抓，深度精读）

#### 1.1 核心 AI 编码工具

| 信源 | URL |
|---|---|
| Cursor 博客 + Changelog | `cursor.com/blog`、`cursor.com/changelog` |
| Claude 产品博客 | `claude.com/blog` |
| Claude Code Releases | `github.com/anthropics/claude-code/releases` |
| Claude Cowork 官方动态 | `anthropic.com/news`（含 Cowork） |
| GitHub Copilot Changelog | `github.blog/changelog` |
| Anthropic 工程博客 | `anthropic.com/engineering` |
| OpenAI 新闻 | `openai.com/news` |
| Codex Changelog | `developers.openai.com/codex/changelog` |
| Codex CLI Releases | `github.com/openai/codex/releases` |
| Gemini CLI Releases | `github.com/google-gemini/gemini-cli/releases` |
| Google AI 博客 | `blog.google/technology/ai` |

#### 1.2 核心研发 Agent 基础设施

| 信源 | URL |
|---|---|
| OpenClaw 工程进展 | `github.com/openclaw/openclaw` |
| OpenClaw 博客 | `openclaw.ai/blog` |
| Hermes Agent | `github.com/NousResearch/hermes-agent` |
| MCP 官方 | `modelcontextprotocol.io` |

#### 1.3 研发范式方法论

- Harness Engineering — `anthropic.com/engineering`、HN/Dev.to/Medium
- Context Engineering — Karpathy、Simon Willison 长文

**Level 1 处理要求**：
- 24 小时内文章：完整抓取全文，深度精炼
- 3 天内文章：标注「📌 重要回顾」+ 日期，要点提取
- 来源标注：标题 + 链接 + 作者 + 日期
- 量化指标优先（数字、百分比、版本号）

---

### Level 2（关键人物战略洞察）

#### 核心 6 人（每期必检索）

| 人物 | X handle | 角色 |
|---|---|---|
| Andrej Karpathy | @karpathy | Agent 编码范式（已加入 Anthropic 预训练团队） |
| Boris Cherny | @bcherny | Claude Code 负责人、Harness Engineering 布道者 |
| Sundar Pichai | @sundarpichai | Google CEO（Gemini 3.5 / Antigravity 主战场） |
| Sam Altman | @sama | OpenAI CEO |
| Greg Brockman | @gdb | OpenAI 联创（Codex 方向） |
| Dario Amodei | @DarioAmodei | Anthropic CEO |

#### 重点观察 3 人

| 人物 | X handle | 角色 |
|---|---|---|
| Michael Truell | @mntruell | Cursor 创始人 |
| Aman Sanger | @amansanger | Cursor 创始人 |
| Eric Simons | @ericrsimons | Bolt.new CEO（Vibe Coding 标杆） |
| Simon Willison | @simonw | AI 工具实践 + 安全洞察 |

#### 按需观察 3 人

@AndrewYNg（AI 教育）、@hwchase（LangChain CEO）、@ilyasut（Agent 安全）

#### Level 2 检索关键词模板

```
"<handle> twitter MAY 2026"
"<handle> announcement <YYYY-MM-DD>"
"<name> Anthropic OR OpenAI OR Google news"
"<name> claude code OR cursor OR codex"
```

#### Level 2 主题筛选铁律

只保留与 AI 编码工具、Agent 框架、研发范式、研发效能数据相关的动态。

❌ **严禁**拿融资八卦、法务诉讼、公司治理、个人八卦凑数
✅ 6 人都无主题相关动态时，老老实实标"无新增"

---

### Level 3（行业研究报告）

- Anthropic Agentic Coding Trends Report、Economic Index
- GitHub Octoverse / Copilot 报告
- LinearB / GitClear / Pluralsight PR 与代码质量报告
- Snyk / Cycode / GitGuardian AI 代码安全报告
- Gartner / Forrester / IDC AI4SE 象限报告
- a16z / Sequoia / Bessemer 企业 AI 落地报告
- 学术论文（南京大学 TSE、CMU、MIT 等）

### Level 4（补充信源）

- **国内 AI 编码** — Qwen-Coder、CodeGeeX、智谱、阿里云通义灵码
- **企业实践博客** — Atlassian、GitLab、Uber、Netflix、Shopify
- **技术媒体** — InfoQ、The New Stack、9to5Mac、ITHome、智东西、量子位、36 氪
- **社区** — HackerNews "AI coding"、`r/cursor`、`r/ClaudeAI`
- **Vibe Coding 平台** — Bolt.new、v0、Lovable、Replit Agent

---

## 四、搜索关键词库（可直接复用）

```yaml
核心 AI 编码工具:
  - "cursor update 2026"
  - "cursor changelog"
  - "claude code update 2026"
  - "claude code release notes"
  - "claude cowork 2026"
  - "github copilot update 2026"
  - "github copilot changelog"
  - "openai codex CLI 2026"
  - "openai codex app 2026"
  - "codex changelog"
  - "gemini CLI update 2026"
  - "antigravity google update"
  - "devin update 2026"

Agent 框架与方法论:
  - "hermes agent coding"
  - "openclaw release"
  - "harness engineering AI development"
  - "boris cherny harness"
  - "context engineering AI 2026"
  - "MCP model context protocol update"
  - "MCP server new release"
  - "multi-agent orchestration coding 2026"
  - "agentic coding trends 2026"
  - "agent view claude code"
  - "goal mode codex"

Vibe Coding:
  - "bolt.new update 2026"
  - "v0 vercel update 2026"
  - "lovable AI coding"
  - "replit agent update 2026"

AI 安全治理:
  - "AI agent sandbox security"
  - "AI agent supply chain attack"
  - "AI BOM SLSA AI development"
  - "OWASP LLM AI coding security"
  - "ADLC AI development lifecycle"

关键人物（每期强制）:
  - "@karpathy twitter <月份>"
  - "@bcherny twitter <月份>"
  - "@sundarpichai twitter <月份>"
  - "@sama twitter <月份>"
  - "@gdb twitter <月份>"
  - "@DarioAmodei twitter <月份>"

国内动态:
  - "通义灵码更新"
  - "CodeGeeX 发布"
  - "腾讯AI编码工具"
  - "字节豆包编程"
  - "智谱 AI 编码"
```

---

## 五、产出结构（完整模板）

```markdown
# AI x 研发效能 每日简报 YYYY-MM-DD

> 覆盖周期：YYYY-MM-DD ~ YYYY-MM-DD（上一期：YYYY-MM-DD）

---

## 头条速览

1. **<头条 1>**——<50 字以内一句话概括>
2. **<头条 2>**——<50 字以内>
3. **<头条 3>**——<50 字以内>

---

## 一、AI 增强软件研发（AI4SE）

### 1.1 Level 1：核心产品与工程更新

#### 1️⃣ <事件标题>（YYYY-MM-DD）

<事件描述要点>

**技术细节：**
- ...

**对研发效能的影响**：<分析>

来源：[官方链接](url) — YYYY-MM-DD

#### 2️⃣ ...

### 1.2 Level 2：关键人物战略洞察

| 人物 | 动态 | 日期 |
|---|---|---|
| @karpathy | <AI4SE 主题动态 / 无新增> | — |
| @bcherny | ... | — |
| ... |

### 1.3 Level 3：行业研究与数据

#### <报告/趋势标题>
- 关键数据 1
- 关键数据 2

### 1.4 Level 4：补充信源

#### <补充话题>
<简评，1-2 段>

---

## 二、专题板块：<围绕当期最大头条的多维解读>

<4-5 个维度展开，配对比表/时间线/数据卡>

---

## 三、今日关键数字

- **<数字 1>**：<含义>
- **<数字 2>**：<含义>

---

## 四、明日值得关注

- ...
```

**每个 Level 1 条目固定四件套**：
1. 事件描述
2. 技术细节（版本号、API、参数、价格）
3. 对研发效能的影响（独家分析）
4. 来源（链接 + 日期）

---

## 六、两条红线（避免简报漂移的关键）

### 🔴 红线 1：主题红线

**判定标准**（必须满足任一才能进头条/Level 1/Level 2）：
- 直接讲 AI 编码工具/Agent 框架的产品功能、版本、定价、性能
- 直接讲软件研发流程中的 AI 实践、效能数据、岗位变化
- 直接讲研发范式（Harness / Context / MCP / Agent 编排）

**反面案例**（即使涉及头部 AI 公司也拒绝上头条）：
- ❌ 算力供应链/芯片合作（如 Maia、Trainium、TPU 采购）
- ❌ 模型公司财报/估值/IPO 进度（除非披露编码产品营收占比）
- ❌ 公司治理/法务/股权八卦
- ❌ AI 通用应用动态（消费助手、电商 AI）
- ❌ 政府监管纯政策文本（除非明确指向 AI 编码工具合规）

### 🔴 红线 2：时效红线

- **超 7 天**的内容**不得**作为今日新闻报道
- 如要援引，必须在 Level 4 标注「📌 重要回顾」+ 明确日期
- **严禁**把数日前的内容包装成"今日头条"

---

## 七、头条排序原则

```
主题红线过滤
  → 行业影响力（人才地震 / 战略联盟 / 范式拐点）
  → 重磅产品发布 GA
  → 重要版本更新
  → 行业实证数据
  → 方法论文章
  → 博客观点
```

**头条速览强制要求**：
- 1-3 条编号列表
- 每条不超过 50 字
- 同一公司多条更新合并为一条头条

---

## 八、排版强制规范

### 8.1 表格使用准则

**严禁两列表格用于"短键 + 长描述"结构**——浏览器会均分列宽，导致左列大片空白。

```
❌ 错误：
| 5/17 | Gemini 3.1 模型别名 + thinking 配置；安全依赖更新... |
| 5/15 | RAG 片段导出本地日志；企业网关 auth 凭证冲突修复... |

✅ 正确：
- **5/17**：Gemini 3.1 模型别名 + thinking 配置；安全依赖更新
- **5/15**：RAG 片段导出本地日志；企业网关 auth 凭证冲突修复
```

**表格只用于以下场景**：
- 真正的多列对比（≥3 列）
- 两列且左右内容长度相近
- 数据矩阵（基准测试分数对比）

**两列表格强制要求**：
- 左列内容若 ≤6 字（版本号、日期、姓名），**必须**改用列表
- 不得有任何单元格超过对侧 3 倍长度

### 8.2 HTML 表格 CSS 必备

```css
table {
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;        /* 自动列宽 */
}
th, td {
  vertical-align: top;       /* 内容顶对齐 */
  padding: 0.6rem 0.85rem;
  border: 1px solid #e5e7eb;
}
th {
  white-space: nowrap;       /* 表头不换行，避免被强制拉宽 */
}
```

### 8.3 列表项格式

- 「**粗体前缀**：描述」是最通用格式
- 嵌套不超过 2 层
- 单项不超过 3 行（超过则拆分或独立成段）

---

## 九、执行流程（七步工作流）

1. **读历史记忆** — 加载上一期内容与执行记录，避免重复
2. **采信源** — 按 L1 → L2 → L3 → L4 顺序覆盖
   - L1：每个一手源至少抓一次
   - L2：核心 6 人每人主动检索一次
   - L3 / L4：按关键词库批量搜索
3. **排头条** — 主题红线 + 时效红线 + 影响力优先级 → 1-3 条
4. **生成简报** — 按模板产出 Markdown + HTML 双版本
5. **去重检查** — 与上一期内容比对，剔除重复
6. **发布前自检**（5 维度）：
   - ✅ 主题：每条是否直接讲 AI 编码工具/Agent/研发效能？
   - ✅ 时效：是否有超 7 天的旧闻被包装成今日新闻？
   - ✅ Level 2：是否注水了？无新增就老老实实标无新增
   - ✅ 排版：两列表格短键长描述检查、HTML CSS 三件套检查
   - ✅ 去重：与上一期是否有重复条目
7. **发布** — 推送到目标内容平台

---

## 十、迭代经验：四类典型翻车（带修复方案）

### 翻车 1：主题漂移

- **症状**：把"Anthropic 洽谈微软 Maia 芯片"作头条——属于算力供应链，不是 AI4SE
- **根因**：把"AI 行业新闻"和"AI4SE 新闻"混淆
- **修复**：加入主题红线，**第零原则——主题不符直接砍**

### 翻车 2：旧闻当新闻

- **症状**：把 13 天前的 Hermes 登顶事件作为今日 Level 3 报道
- **根因**：信源覆盖太宽，吸纳了滞后内容
- **修复**：加入时效红线 7 天，超期必须标「重要回顾」

### 翻车 3：Level 2 注水

- **症状**：人物动态栏拿"YC token 协议""股权庭审"等八卦凑数
- **根因**：怕"显得空"，违反主题筛选
- **修复**：宁可写"无新增"，也不能注水

### 翻车 4：两列表格列宽失衡

- **症状**：「日期 \| 长描述」表格，左列大片空白，阅读体验糟糕
- **根因**：浏览器自动均分列宽 + 短键 + 长值
- **修复**：改用「**粗体前缀**：描述」列表；表格 CSS 加 `table-layout: auto` + `th nowrap`

---

## 十一、给同行的五条建议

1. **垂直定位是护城河** — "AI 行业简报"竞争激烈到没价值，"AI4SE 简报"才有差异化空间
2. **一手源是底线** — 读 changelog、工程博客、GitHub Releases，不要满足于二手翻译
3. **红线机制比写作技巧重要** — 每天有"今日没什么 AI4SE 大事"的勇气，才能避免被噪音稀释
4. **迭代驱动规范** — 不要试图一次写出完美规范，让每次翻车都变成一条新规则
5. **量化指标优先** — "效率提升 40%、Token 消耗 271B、GitHub Star 14 万" 比"显著提升、广受关注"有用 100 倍

---

## 十二、推荐工具栈

| 环节 | 工具 |
|---|---|
| 信息检索 | Tavily、Perplexity、Brave Search、Google Search |
| 网页抓取 | Firecrawl、Jina Reader、原生 fetch |
| AI 写作 | Claude / GPT-5.5 / Gemini 3.5 Pro |
| 自动化执行 | Cursor / Claude Code / Codex CLI 的定时任务能力 |
| 内容平台 | 微信公众号、知识星球、Substack、Notion 公开页 |

---

*整理：AI x 研发效能｜对外分享版｜2026-05-25*
