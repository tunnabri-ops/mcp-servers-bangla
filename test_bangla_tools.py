#!/usr/bin/env python3
"""Test the Bangla tools in bangla_tools_server.py — no `mcp` install needed.

The real server needs `pip install mcp`, but the tool logic (Bangla date
formatting and the feed list) can be checked without it: we stub out the
`mcp.server.fastmcp` module before importing the server, then call the
plain functions directly.

Run: python3 test_bangla_tools.py
"""
import sys
import types
from pathlib import Path

# --- Stub the `mcp` package so the server module imports without it. ---
mcp_pkg = types.ModuleType("mcp")
mcp_server_pkg = types.ModuleType("mcp.server")
mcp_fastmcp_pkg = types.ModuleType("mcp.server.fastmcp")


class _DummyFastMCP:
    def __init__(self, name):
        self.name = name

    def tool(self):
        def decorator(fn):
            return fn
        return decorator

    def run(self):
        raise RuntimeError("stub FastMCP cannot run a server")


mcp_fastmcp_pkg.FastMCP = _DummyFastMCP
mcp_server_pkg.fastmcp = mcp_fastmcp_pkg
mcp_pkg.server = mcp_server_pkg
sys.modules["mcp"] = mcp_pkg
sys.modules["mcp.server"] = mcp_server_pkg
sys.modules["mcp.server.fastmcp"] = mcp_fastmcp_pkg

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bangla_tools_server as server  # noqa: E402


def test_bangla_date():
    out = server.bangla_date()
    assert out.startswith("আজ "), out
    # Bangla digits must appear (year), no Latin digits at all.
    assert any("০" <= ch <= "৯" for ch in out), out
    assert not any(ch.isascii() and ch.isdigit() for ch in out), out
    assert any(day in out for day in server.BANGLA_WEEKDAYS), out
    assert any(month in out for month in server.BANGLA_MONTHS), out
    print("bangla_date OK:", out)


def test_bangla_news_feeds():
    out = server.bangla_news_feeds()
    assert len(server.NEWS_FEEDS) == 5, server.NEWS_FEEDS
    for name, url in server.NEWS_FEEDS:
        assert name in out, name
        assert url in out, url
        assert url.startswith("https://"), url
    print("bangla_news_feeds OK: 5 feeds listed")


if __name__ == "__main__":
    test_bangla_date()
    test_bangla_news_feeds()
    print("All Bangla tools tests passed.")
