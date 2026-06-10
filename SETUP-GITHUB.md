# AI4SE 简报 · GitHub 定时生成与发布

## 一、HTML 要不要部署？

| 用途 | 要不要部署 | 做法 |
|---|---|---|
| 自己看、本地打开 | **不需要** | 打开 `archive/AI4SE-每日简报-YYYY-MM-DD.html` |
| 手机/同事访问固定链接 | **需要** | 开 **GitHub Pages**（免费，已配 workflow） |
| 发公众号 / 知识星球 | **不需要 Pages** | 复制 HTML 内容或 Markdown 到平台编辑器 |

结论：**生成 HTML 本身不依赖部署**；想要 `https://你的用户名.github.io/仓库名/` 这种公网地址，才需要开 Pages。

---

## 二、注册 GitHub（需你本人操作）

1. 打开 https://github.com/signup 注册账号
2. 验证邮箱
3. （可选）安装 GitHub CLI：https://cli.github.com/

---

## 三、创建仓库并推送

在本机 **Git Bash** 或已安装 Git 的终端中：

```bash
cd "C:/Users/hi/Documents/04_Cursor/04_AI4SE"

git init
git add .
git commit -m "init: AI4SE daily briefing pipeline"

# 你的仓库（已创建）：
# https://github.com/lei07130520-spec/AI4SE
git branch -M main
git remote add origin https://github.com/lei07130520-spec/AI4SE.git
git push -u origin main
```

---

## 四、开启 GitHub Pages（可选，想要公网链接才做）

1. 仓库 → **Settings** → **Pages**
2. **Build and deployment** → Source 选 **Deploy from a branch**
3. Branch 选 **main**，Folder 选 **/docs**
4. 保存后等 1–2 分钟

访问地址一般为：

```
https://lei07130520-spec.github.io/AI4SE/
```

`docs/index.html` 会列出各期简报；每晚 Actions 会更新 `docs/AI4SE-每日简报-YYYY-MM-DD.html`。

**不开启 Pages 也可以**：HTML 仍在仓库 `docs/` 和 `archive/` 里，本地打开或 Raw 查看即可。

---

## 五、定时任务时间

已在 `.github/workflows/ai4se-daily.yml` 配置：

- **cron: `0 13 * * *`** → 每天 **21:00 北京时间**（UTC+8）
- 也可在 GitHub → **Actions** → **AI4SE Daily Briefing** → **Run workflow** 手动触发

GitHub Actions 在云端跑，**不依赖你电脑开机**。

---

## 六、自动生成 vs 手工精编版

| 版本 | 来源 | 内容 |
|---|---|---|
| **自动采集版** | `scripts/generate_daily.py` | Level 1 Releases + HN；Level 2 占位 |
| **精编版** | Cursor 按 SOP 生成 | 含人物洞察、专题、红线过滤 |

建议：Actions 每晚出采集版 → 你有空时在 Cursor 里精编 → 覆盖 `archive/` 同日期文件 → 再 push。

---

## 七、本地试跑

```bash
python scripts/generate_daily.py
python scripts/generate_daily.py --date 2026-06-11
```

输出：

- `archive/AI4SE-每日简报-YYYY-MM-DD.md`
- `archive/AI4SE-每日简报-YYYY-MM-DD.html`
- `docs/AI4SE-每日简报-YYYY-MM-DD.html`（Pages 用）
