#!/usr/bin/env python3
"""按天生成 AI4SE 简报（Markdown + HTML）。

在 GitHub Actions 中每晚 21:00（北京时间）运行；也可本地：
  python scripts/generate_daily.py
  python scripts/generate_daily.py --date 2026-06-10
"""

from __future__ import annotations

import argparse
import html
import json
import re
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive"
DOCS = ROOT / "docs"

GITHUB_REPOS = [
    ("Claude Code", "anthropics/claude-code"),
    ("Codex", "openai/codex"),
    ("Gemini CLI", "google-gemini/gemini-cli"),
    ("OpenClaw", "openclaw/openclaw"),
    ("Hermes Agent", "NousResearch/hermes-agent"),
]

LEVEL2_PEOPLE = [
    "@karpathy",
    "@bcherny",
    "@sundarpichai",
    "@sama",
    "@gdb",
    "@DarioAmodei",
]

HTML_CSS = """
    :root { --text:#1f2937; --muted:#6b7280; --border:#e5e7eb; --accent:#2563eb; }
    * { box-sizing:border-box; }
    body { font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
           line-height:1.7; color:var(--text); max-width:720px; margin:0 auto; padding:2rem 1.25rem 4rem; }
    h1 { font-size:1.75rem; margin:0 0 1rem; }
    h2 { font-size:1.25rem; margin:2.5rem 0 1rem; padding-bottom:.4rem; border-bottom:2px solid var(--border); }
    h3 { font-size:1.05rem; margin:1.75rem 0 .75rem; }
    p, li { margin:.35rem 0; }
    a { color:var(--accent); text-decoration:none; }
    a:hover { text-decoration:underline; }
    .meta, .footnote { color:var(--muted); font-size:.9rem; }
    blockquote { margin:1rem 0; padding:.75rem 1rem; background:#f9fafb; border-left:4px solid var(--border); color:var(--muted); }
    hr { border:none; border-top:1px solid var(--border); margin:2rem 0; }
    code { font-family:ui-monospace,Consolas,monospace; font-size:.88em; background:#f3f4f6; padding:.1em .35em; border-radius:4px; }
    table { width:100%; border-collapse:collapse; table-layout:auto; margin:1rem 0; font-size:.92rem; }
    th, td { vertical-align:top; padding:.6rem .85rem; border:1px solid var(--border); }
    th { white-space:nowrap; background:#f9fafb; text-align:left; }
    .badge { display:inline-block; background:#eff6ff; color:#1d4ed8; padding:.15rem .5rem; border-radius:4px; font-size:.8rem; }
"""


def fetch_json(url: str) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "AI4SE-daily/1.0",
    }
    token = __import__("os").environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode())


def fetch_releases(cutoff: datetime) -> list[dict]:
    items: list[dict] = []
    for product, repo in GITHUB_REPOS:
        url = f"https://api.github.com/repos/{repo}/releases?per_page=10"
        try:
            releases = fetch_json(url)
        except Exception as exc:  # noqa: BLE001
            items.append(
                {
                    "product": product,
                    "repo": repo,
                    "error": str(exc),
                }
            )
            continue
        for r in releases:
            published = datetime.fromisoformat(r["published_at"].replace("Z", "+00:00"))
            if published < cutoff:
                continue
            body = (r.get("body") or "").strip()
            summary = body.split("\n")[0][:200] if body else "（无 release notes）"
            items.append(
                {
                    "product": product,
                    "repo": repo,
                    "tag": r["tag_name"],
                    "name": r.get("name") or r["tag_name"],
                    "published": published.date().isoformat(),
                    "url": r["html_url"],
                    "summary": summary,
                }
            )
    items.sort(key=lambda x: x.get("published", ""), reverse=True)
    return items


def fetch_hn(since: datetime, limit: int = 5) -> list[dict]:
    ts = int(since.timestamp())
    query = urllib.parse.urlencode(
        {
            "query": "AI coding",
            "tags": "story",
            "numericFilters": f"created_at_i>{ts}",
        }
    )
    url = f"https://hn.algolia.com/api/v1/search?{query}"
    try:
        data = fetch_json(url)
    except Exception:  # noqa: BLE001
        return []
    hits = []
    for h in data.get("hits", [])[:limit]:
        hits.append(
            {
                "title": h.get("title", ""),
                "url": h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
                "points": h.get("points", 0),
                "comments": h.get("num_comments", 0),
                "created": datetime.fromtimestamp(h["created_at_i"], tz=timezone.utc).date().isoformat(),
            }
        )
    return hits


def find_previous_briefing(before: date) -> str | None:
    if not ARCHIVE.exists():
        return None
    dates: list[date] = []
    for p in ARCHIVE.glob("AI4SE-每日简报-*.md"):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", p.name)
        if m:
            d = date.fromisoformat(m.group(1))
            if d < before:
                dates.append(d)
    if not dates:
        return None
    return max(dates).isoformat()


def build_headlines(releases: list[dict], max_items: int = 3) -> list[str]:
    lines: list[str] = []
    for r in releases:
        if "error" in r:
            continue
        text = f"{r['product']} {r['tag']}——{r['summary'][:48]}"
        lines.append(text)
        if len(lines) >= max_items:
            break
    if not lines:
        lines.append("本窗口内 GitHub Releases 无新增——详见 Level 1 采集日志")
    return lines


def render_markdown(
    today: date,
    period_start: date,
    prev: str | None,
    releases: list[dict],
    hn: list[dict],
) -> str:
    headlines = build_headlines(releases)
    prev_note = prev or "无 — 首期 archive"
    lines = [
        f"# AI x 研发效能 每日简报 {today.isoformat()}",
        "",
        f"> 覆盖周期：{period_start.isoformat()} ~ {today.isoformat()}（上一期：{prev_note}）",
        "",
        "> **采集方式**：GitHub Actions 自动采集（Level 1 GitHub API + Level 4 HN API）｜Level 2/3 待人工或 API 密钥补充",
        "",
        "---",
        "",
        "## 头条速览",
        "",
    ]
    for i, h in enumerate(headlines, 1):
        lines.append(f"{i}. **{h.split('——')[0]}**——{h.split('——', 1)[-1]}")
    lines.extend(["", "---", "", "## 一、AI 增强软件研发（AI4SE）", "", "### 1.1 Level 1：核心产品与工程更新", ""])

    n = 0
    for r in releases:
        if "error" in r:
            continue
        n += 1
        lines.extend(
            [
                f"#### {n}️⃣ {r['product']} {r['tag']}（{r['published']}）",
                "",
                r["summary"],
                "",
                f"来源：[{r['tag']}]({r['url']}) — {r['published']}",
                "",
            ]
        )
    if n == 0:
        lines.append("_本窗口内无 GitHub Release 更新。_")
        lines.append("")

    lines.extend(["---", "", "### 1.2 Level 2：关键人物战略洞察", ""])
    lines.append("| 人物 | 动态 | 日期 |")
    lines.append("|---|---|---|")
    for handle in LEVEL2_PEOPLE:
        lines.append(f"| {handle} | 自动采集未配置（需 WebSearch / X 间接源） | — |")
    lines.extend(
        [
            "",
            "---",
            "",
            "### 1.3 Level 3：行业研究与数据",
            "",
            "> **本日未扫描**（周报/月报降频）。",
            "",
            "---",
            "",
            "### 1.4 Level 4：补充信源（HN）",
            "",
        ]
    )
    if hn:
        for h in hn:
            lines.append(
                f"- **{h['created']}**：[{h['title']}]({h['url']}) "
                f"（{h['points']} pts / {h['comments']} comments）"
            )
    else:
        lines.append("- 本窗口无 HN 命中")
    lines.extend(
        [
            "",
            "---",
            "",
            "## 附录：采集日志",
            "",
            "| 环节 | 状态 |",
            "|---|---|",
            f"| GitHub Releases API | ✅ {n} 条 |",
            f"| HN Algolia API | ✅ {len(hn)} 条 |",
            f"| 生成时间 (UTC) | {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} |",
            "",
            "*自动生成版 · 可在 Cursor 中基于本稿补充 Level 2 分析与专题*",
            "",
        ]
    )
    return "\n".join(lines)


def md_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text


def render_html(md: str, today: date) -> str:
    """轻量 Markdown → HTML（覆盖本脚本产出结构）。"""
    body_parts: list[str] = []
    in_table = False
    table_rows: list[str] = []

    def flush_table() -> None:
        nonlocal in_table, table_rows
        if not table_rows:
            return
        html_table = ["<table>"]
        for i, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            tag = "th" if i == 0 else "td"
            html_table.append("<tr>" + "".join(f"<{tag}>{md_inline(c)}</{tag}>" for c in cells) + "</tr>")
        html_table.append("</table>")
        body_parts.append("\n".join(html_table))
        table_rows = []
        in_table = False

    for line in md.splitlines():
        if line.startswith("|"):
            in_table = True
            table_rows.append(line)
            continue
        flush_table()
        if line.startswith("# "):
            body_parts.append(f"<h1>{md_inline(line[2:])}</h1>")
        elif line.startswith("## "):
            body_parts.append(f"<h2>{md_inline(line[3:])}</h2>")
        elif line.startswith("### "):
            body_parts.append(f"<h3>{md_inline(line[4:])}</h3>")
        elif line.startswith("#### "):
            body_parts.append(f"<h4>{md_inline(line[5:])}</h4>")
        elif line.startswith("> "):
            body_parts.append(f"<blockquote><p>{md_inline(line[2:])}</p></blockquote>")
        elif line.strip() == "---":
            body_parts.append("<hr>")
        elif re.match(r"^\d+\.\s", line):
            if not body_parts or not body_parts[-1].startswith("<ol"):
                body_parts.append("<ol>")
            item = re.sub(r"^\d+\.\s", "", line)
            body_parts.append(f"<li>{md_inline(item)}</li>")
        elif line.startswith("- "):
            if not body_parts or not body_parts[-1].endswith("</ul>") and "<ul>" not in body_parts[-1:]:
                body_parts.append("<ul>")
            body_parts.append(f"<li>{md_inline(line[2:])}</li>")
        elif line.strip() == "":
            if body_parts and body_parts[-1] in ("<ol>", "<ul>"):
                body_parts.append("</ol>" if body_parts[-1] == "<ol>" else "</ul>")
            continue
        elif line.startswith("_") and line.endswith("_"):
            body_parts.append(f"<p><em>{md_inline(line.strip('_'))}</em></p>")
        else:
            body_parts.append(f"<p>{md_inline(line)}</p>")

    flush_table()
    body = "\n".join(body_parts)
    body = body.replace("<ol>\n", "<ol>\n").replace("<ul>\n", "<ul>\n")
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI x 研发效能 每日简报 {today.isoformat()}</title>
  <style>{HTML_CSS}</style>
</head>
<body>
<p class="meta"><span class="badge">自动采集版</span> 由 GitHub Actions 生成</p>
{body}
</body>
</html>"""


def write_index(briefing_dates: list[str]) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    items = "\n".join(
        f'    <li><a href="AI4SE-每日简报-{d}.html">{d}</a></li>'
        for d in sorted(briefing_dates, reverse=True)
    )
    latest = sorted(briefing_dates, reverse=True)[0] if briefing_dates else ""
    redirect = (
        f'<meta http-equiv="refresh" content="0; url=AI4SE-每日简报-{latest}.html">'
        if latest
        else ""
    )
    index_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI4SE 每日简报</title>
  {redirect}
  <style>{HTML_CSS}</style>
</head>
<body>
  <h1>AI4SE 每日简报</h1>
  <p class="meta">GitHub Pages 索引 · 最新一期优先</p>
  <ul>
{items}
  </ul>
</body>
</html>"""
    (DOCS / "index.html").write_text(index_html, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="简报日期 YYYY-MM-DD（默认今天 UTC+8）")
    parser.add_argument("--days", type=int, default=3, help="Level 1 回看天数")
    parser.add_argument(
        "--force",
        action="store_true",
        help="覆盖 archive 中同日期手工稿（默认仅写 -auto 后缀 + docs/）",
    )
    args = parser.parse_args()

    if args.date:
        today = date.fromisoformat(args.date)
    else:
        # 北京时间
        bj = datetime.now(timezone.utc) + timedelta(hours=8)
        today = bj.date()

    period_start = today - timedelta(days=args.days - 1)
    cutoff = datetime.combine(period_start, datetime.min.time(), tzinfo=timezone.utc)

    ARCHIVE.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)

    releases = fetch_releases(cutoff)
    hn = fetch_hn(cutoff - timedelta(days=1))
    prev = find_previous_briefing(today)

    md = render_markdown(today, period_start, prev, releases, hn)
    html_out = render_html(md, today)

    stem = f"AI4SE-每日简报-{today.isoformat()}"
    auto_stem = f"{stem}-auto"
    md_path = ARCHIVE / f"{auto_stem if not args.force else stem}.md"
    html_archive = ARCHIVE / f"{auto_stem if not args.force else stem}.html"
    html_docs = DOCS / f"{stem}.html"

    md_path.write_text(md, encoding="utf-8")
    html_archive.write_text(html_out, encoding="utf-8")
    html_docs.write_text(html_out, encoding="utf-8")

    dates = []
    for p in DOCS.glob("AI4SE-每日简报-*.html"):
        m = re.search(r"(\d{4}-\d{2}-\d{2})", p.name)
        if m:
            dates.append(m.group(1))
    write_index(dates)

    print(f"Wrote {md_path}")
    print(f"Wrote {html_docs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
