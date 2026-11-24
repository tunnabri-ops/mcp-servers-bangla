#!/usr/bin/env python3
"""Bangla tools MCP server (stdio transport).

Tools:
- bangla_date: today's date in Bangla, Asia/Dhaka timezone.
- bangla_news_feeds: the 5 verified Bangla news RSS feeds.

Run: python3 bangla_tools_server.py
Wire it into Claude Desktop with mcp-bangla.json in this repo.
Requires: pip install mcp
"""
from datetime import datetime
from zoneinfo import ZoneInfo

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("bangla-tools")

BANGLA_DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
BANGLA_WEEKDAYS = [
    "সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার",
    "শুক্রবার", "শনিবার", "রবিবার",
]
BANGLA_MONTHS = [
    "জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন",
    "জুলাই", "আগস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর",
]

NEWS_FEEDS = [
    ("প্রথম আলো", "https://www.prothomalo.com/stories.rss"),
    ("বিবিসি বাংলা", "https://feeds.bbci.co.uk/bengali/rss.xml"),
    ("বিডিনিউজ টোয়েন্টিফোর ডটকম (বাংলা)", "https://bangla.bdnews24.com/rss"),
    ("The Daily Star", "https://www.thedailystar.net/rss.xml"),
    ("চ্যানেল আই অনলাইন", "https://www.channelionline.com/rss"),
]


@mcp.tool()
def bangla_date() -> str:
    """Today's date in Bangla (Asia/Dhaka)."""
    now = datetime.now(ZoneInfo("Asia/Dhaka"))
    day = str(now.day).translate(BANGLA_DIGITS)
    year = str(now.year).translate(BANGLA_DIGITS)
    return (
        f"আজ {BANGLA_WEEKDAYS[now.weekday()]} "
        f"{day} {BANGLA_MONTHS[now.month - 1]} {year}।"
    )


@mcp.tool()
def bangla_news_feeds() -> str:
    """List of verified Bangla news RSS feeds (all HTTP 200 on 2026-11-24)."""
    lines = ["বাংলা খবরের RSS ফিড:"]
    for name, url in NEWS_FEEDS:
        lines.append(f"- {name}: {url}")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
