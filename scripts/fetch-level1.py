#!/usr/bin/env python3
"""Level 1 主链路：GitHub Releases API + 官方 Changelog URL 清单。

用法:
  python fetch-level1.py              # 打印 72h 内 releases
  python fetch-level1.py --days 3     # 自定义窗口
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from typing import Any

GITHUB_REPOS = [
    ("claude-code", "anthropics/claude-code"),
    ("codex", "openai/codex"),
    ("gemini-cli", "google-gemini/gemini-cli"),
    ("openclaw", "openclaw/openclaw"),
    ("hermes-agent", "NousResearch/hermes-agent"),
]

CHANGELOG_URLS = [
    ("cursor", "https://cursor.com/changelog"),
    ("github-copilot", "https://github.blog/changelog/"),
    ("anthropic-news", "https://anthropic.com/news"),
    ("openai-news", "https://openai.com/news"),
    ("codex-changelog", "https://developers.openai.com/codex/changelog"),
    ("mcp", "https://modelcontextprotocol.io/"),
]


def fetch_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def fetch_text(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "AI4SE-fetch/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read(500).decode(errors="replace")
    except Exception as exc:  # noqa: BLE001
        return 0, str(exc)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=3, help="lookback window (default 3)")
    args = parser.parse_args()

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    print(f"# Level 1 fetch — window since {cutoff.date()}\n")

    print("## GitHub Releases\n")
    for label, repo in GITHUB_REPOS:
        url = f"https://api.github.com/repos/{repo}/releases?per_page=8"
        try:
            releases = fetch_json(url)
        except Exception as exc:  # noqa: BLE001
            print(f"- {label}: ERROR {exc}")
            continue
        hits = []
        for r in releases:
            published = datetime.fromisoformat(r["published_at"].replace("Z", "+00:00"))
            if published >= cutoff:
                hits.append(f"  - {r['tag_name']} ({published.date()})")
        if hits:
            print(f"### {label} ({repo})")
            print("\n".join(hits))
        else:
            print(f"### {label}: no releases in window")

    print("\n## Changelog URLs (HEAD check)\n")
    for label, url in CHANGELOG_URLS:
        status, preview = fetch_text(url)
        ok = "OK" if 200 <= status < 400 else "FAIL"
        print(f"- [{ok}] {label}: {url} (HTTP {status})")
        if status == 0:
            print(f"    {preview[:120]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
