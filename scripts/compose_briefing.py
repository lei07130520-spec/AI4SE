#!/usr/bin/env python3
"""用 LLM 将采集 JSON 按 SOP 写成完整 Markdown 简报。"""

from __future__ import annotations

import json
import os
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = ROOT / "prompts" / "compose-system.md"


def _chat_openai(system: str, user: str, api_key: str, model: str, base_url: str) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "temperature": 0.3,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode())
    content = data["choices"][0]["message"]["content"]
    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("LLM returned empty content")
    return content.strip()


def compose_markdown(payload: dict) -> str:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "未设置 OPENAI_API_KEY。请在 GitHub Secrets 或本地环境变量中配置。"
        )

    model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")

    system = PROMPT_PATH.read_text(encoding="utf-8")
    user = (
        "请根据以下 JSON 生成今日完整简报 Markdown。\n\n"
        "```json\n"
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + "\n```"
    )
    md = _chat_openai(system, user, api_key, model, base_url)

    # 去掉模型可能包裹的 ```markdown fence
    if md.startswith("```"):
        md = md.split("\n", 1)[-1]
        if md.rstrip().endswith("```"):
            md = md.rstrip()[:-3].rstrip()
    return md
