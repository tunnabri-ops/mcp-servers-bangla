# 🔌 MCP Servers Bangla

[![Bangla](https://img.shields.io/badge/UI-Bangla%20%2B%20English-orange)](#)

**Give Claude Desktop Bangla tools — Bangla date and news feeds — plus file, web, memory and database servers, ready to plug in.**

> বাংলা সংস্করণ নিচে আছে। / Bangla version below.

## ✨ Features

- `mcp-bangla.json` — ready client config (Claude Desktop format) with 5 servers: `bangla-tools` (this repo's own server), `fetch` (read any web page), `filesystem` (read/write files — pointed at `~/Documents` only, not your whole home), `memory` (the AI app remembers things), `sqlite` (a notes database at `~/Documents/notes.db`), and `github` (read repos, issues and PRs — needs a token).
- `bangla_tools_server.py` — a small working MCP server of your own, with two tools: `bangla_date` (today's date in Bangla, Asia/Dhaka, Bangla digits) and `bangla_news_feeds` (the 5 verified Bangla news RSS feeds). Runs over stdio transport.
- `test_bangla_tools.py` — checks the Bangla date formatting and the feed list without needing the MCP SDK installed.
- `requirements.txt` — the MCP Python SDK (`mcp>=1.0`).

## 🚀 How to use

```bash
# 1. Install the MCP Python SDK
pip install -r requirements.txt

# 2a. Claude Desktop: copy the config (merge with your existing servers)
cp mcp-bangla.json ~/Library/Application\ Support/Claude/claude_desktop_config.json
#     Linux: ~/.config/Claude/claude_desktop_config.json

# 2b. Or run the Bangla tools server directly (stdio transport)
python3 bangla_tools_server.py

# 3. Check the tools without installing anything
python3 test_bangla_tools.py
```

Then ask Claude: "আজকের তারিখ বাংলায় বলো" — it will call `bangla_date`.

## ⚠️ Honest limits

- Replace `/home/USER/` in `mcp-bangla.json` with your own home folder path before use, and put your own GitHub token in place of `YOUR_TOKEN_HERE` if you want the GitHub server.
- The filesystem server only sees `~/Documents` on purpose — that is a safety choice, not a bug: the AI app can read your documents but not your keys or configs.
- Claude Desktop must be restarted after changing its config file.
- The 5 news feeds were verified on 2026-11-24; a feed can break later if the site changes its URL.

## 🇧🇩 বাংলা

**MCP Servers বাংলা — Claude/AI অ্যাপে বাংলা টুলস যোগ করুন।**

- `mcp-bangla.json` — তৈরি কনফিগ: বাংলা টুলস + ফাইল পড়া + ওয়েব পড়া + মেমরি + ডেটাবেস + GitHub।
- `bangla_tools_server.py` — নিজের ছোট সার্ভার: `bangla_date` (আজকের বাংলা তারিখ) আর `bangla_news_feeds` (৫টা বাংলা খবরের ফিড)।
- `test_bangla_tools.py` — SDK ছাড়াই টুলগুলো পরীক্ষা করে।
- ফাইল সার্ভার শুধু `~/Documents` দেখে — নিরাপত্তার জন্য ইচ্ছা করেই তাই রাখা হয়েছে।

## 📄 License

MIT — use it however you like; credit is appreciated.
