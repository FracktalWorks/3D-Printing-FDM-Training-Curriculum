"""
search_web_resources.py
-----------------------
Search the web for articles, docs, and guides on a given 3D printing topic.
Uses SerpAPI if SERPAPI_KEY is set; falls back to a basic DuckDuckGo scrape.

Usage:
    python execution/search_web_resources.py --query "3D printer bed leveling guide" --max 5
    python execution/search_web_resources.py --query "Klipper input shaping" --site github.com

Requires: SERPAPI_KEY in .env (optional — has fallback)
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path


def load_env():
    for env_path in [Path(".env"), Path("../.env")]:
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, _, value = line.partition("=")
                        os.environ.setdefault(key.strip(), value.strip())
            return


load_env()


def search_serpapi(query: str, max_results: int = 5, site: str = None) -> list[dict]:
    """Search via SerpAPI (requires SERPAPI_KEY)."""
    api_key = os.environ.get("SERPAPI_KEY", "")
    if not api_key:
        return None  # signal fallback needed

    if site:
        query = f"site:{site} {query}"

    params = urllib.parse.urlencode({
        "q": query,
        "api_key": api_key,
        "engine": "google",
        "num": max_results,
        "hl": "en",
        "gl": "us",
    })
    url = f"https://serpapi.com/search?{params}"

    req = urllib.request.Request(url, headers={"User-Agent": "3d-training-agent/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())

    results = []
    for item in data.get("organic_results", [])[:max_results]:
        results.append({
            "title": item.get("title", ""),
            "url": item.get("link", ""),
            "snippet": item.get("snippet", ""),
            "source": "serpapi",
        })
    return results


def search_duckduckgo(query: str, max_results: int = 5, site: str = None) -> list[dict]:
    """Fallback: query DuckDuckGo Instant Answer API (no key required)."""
    if site:
        query = f"site:{site} {query}"

    params = urllib.parse.urlencode({
        "q": query,
        "format": "json",
        "no_html": "1",
        "skip_disambig": "1",
    })
    url = f"https://api.duckduckgo.com/?{params}"

    req = urllib.request.Request(url, headers={"User-Agent": "3d-training-agent/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(f"DuckDuckGo API error: {e}", file=sys.stderr)
        return []

    results = []

    # Abstract result
    if data.get("AbstractURL") and data.get("AbstractText"):
        results.append({
            "title": data.get("Heading", query),
            "url": data["AbstractURL"],
            "snippet": data["AbstractText"][:300],
            "source": "duckduckgo_abstract",
        })

    # Related topics
    for topic in data.get("RelatedTopics", []):
        if len(results) >= max_results:
            break
        if isinstance(topic, dict) and topic.get("FirstURL") and topic.get("Text"):
            results.append({
                "title": topic.get("Text", "")[:80],
                "url": topic["FirstURL"],
                "snippet": topic.get("Text", "")[:300],
                "source": "duckduckgo_related",
            })

    return results[:max_results]


def format_markdown_list(results: list[dict]) -> str:
    """Format results as Markdown reference list."""
    lines = ["## 📚 Further Reading", ""]
    for r in results:
        snippet = r.get("snippet", "")[:120].replace("\n", " ")
        lines.append(f"- [{r['title']}]({r['url']}) — {snippet}")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search web for 3D printing training resources")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--max", type=int, default=5, help="Max results (default: 5)")
    parser.add_argument("--site", help="Restrict to a specific site (e.g. github.com)")
    parser.add_argument("--output", help="Save JSON results to this file")
    parser.add_argument("--markdown", action="store_true", help="Print as Markdown list")
    args = parser.parse_args()

    print(f"Searching for: '{args.query}'...", file=sys.stderr)

    results = None
    if os.environ.get("SERPAPI_KEY"):
        try:
            results = search_serpapi(args.query, args.max, args.site)
            print("Using SerpAPI.", file=sys.stderr)
        except Exception as e:
            print(f"SerpAPI failed: {e} — falling back to DuckDuckGo.", file=sys.stderr)

    if not results:
        print("Using DuckDuckGo fallback.", file=sys.stderr)
        results = search_duckduckgo(args.query, args.max, args.site)

    if not results:
        print("No results found.", file=sys.stderr)
        sys.exit(1)

    if args.markdown:
        print(format_markdown_list(results))
    else:
        print(json.dumps(results, indent=2))

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"Saved to {out_path}", file=sys.stderr)

    print(f"Found {len(results)} results.", file=sys.stderr)


if __name__ == "__main__":
    main()
