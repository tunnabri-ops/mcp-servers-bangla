# MCP Servers Bangla — Claude/AI অ্যাপে বাংলা টুলস যোগ করুন

Bangla-ready Model Context Protocol setup, built on **modelcontextprotocol/servers**.

- **Original repo:** https://github.com/modelcontextprotocol/servers (Model Context Protocol reference servers — the official servers that let AI apps read files, fetch web pages, query databases and more)

## কী আছে / What is inside

- `mcp-bangla.json` — ready client config (Claude Desktop format): filesystem, fetch, memory, sqlite and GitHub servers, with Bangla comments on what each one does.
- `bangla_tools_server.py` — a small working MCP server of your own: two tools, `bangla_date` (today's date in Bangla, Asia/Dhaka) and `bangla_news_feeds` (the 5 verified Bangla news RSS feeds).
- `requirements.txt` — the official `mcp` Python SDK.

## যা ঠিক করা হয়েছে / What was fixed

- Upstream is a big monorepo of many servers with no "start here" config — a new user has to read each server's README to wire one up. This config is a ready first set: the 5 most useful servers, already named and pointed at safe folders.
- The example server in the upstream docs is a toy weather server. This one is a real Bangla utility (date + news feeds) that actually answers a question a Bangladeshi user asks.
- Safety: the filesystem server is pointed at `~/Documents` only — not your whole home directory — so the AI app can read your documents but not your keys or configs.

## ব্যবহার / How to use

```bash
# 1. Install the MCP Python SDK
pip install -r requirements.txt

# 2a. Claude Desktop: copy the config (merge with your existing servers)
cp mcp-bangla.json ~/Library/Application\ Support/Claude/claude_desktop_config.json
#     Linux: ~/.config/Claude/claude_desktop_config.json

# 2b. Or run the Bangla tools server directly (stdio transport)
python3 bangla_tools_server.py
```

Then ask Claude: "আজকের তারিখ বাংলায় বলো" — it will call `bangla_date`.
