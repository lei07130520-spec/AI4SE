# AI4SE 简报 Archive

本地 archive 用于：

1. **去重** — 每期生成前加载最近一期，剔除重复条目
2. **重要回顾** — 超 7 天但仍需引用的内容标注 `📌 重要回顾` + 原始日期
3. **执行记录** — 附录中的采集日志对照信源覆盖

## 命名规范

```
AI4SE-每日简报-YYYY-MM-DD.md   # 源稿 / 去重基准
AI4SE-每日简报-YYYY-MM-DD.html # 发布版（公众号 / 知识星球 / Substack）
```

## 下一期去重提示

生成 `2026-06-11` 简报时，跳过或合并以下已报道条目（除非有实质性更新）：

- Claude Fable 5 → Copilot / Claude Code v2.1.170
- Copilot CLI `/security-review`
- Gemini CLI v0.47 Antigravity 迁移
- Cursor 3.7 Design Mode + SDK（6/4–6/5，6/11 起进入「回顾」窗口）
