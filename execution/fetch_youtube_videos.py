"""
fetch_youtube_videos.py
-----------------------
Search YouTube Data API v3 for videos on a given 3D printing topic.
Returns a JSON list of results sorted by view count.

Usage:
    python execution/fetch_youtube_videos.py --topic "3D printer bed leveling" --max 10
    python execution/fetch_youtube_videos.py --topic "stepper motors" --max 8 --output .tmp/videos.json

Requires: YOUTUBE_API_KEY in .env
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Load .env from parent directory or current directory
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
    print("WARNING: .env file not found. Relying on system environment variables.", file=sys.stderr)

load_env()

try:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("ERROR: google-api-python-client not installed.")
    print("Run: pip install google-api-python-client")
    sys.exit(1)


def search_youtube(query: str, max_results: int = 10, api_key: str = None) -> list[dict]:
    """Search YouTube and return a list of video dicts."""
    if not api_key:
        api_key = os.environ.get("YOUTUBE_API_KEY", "")
    if not api_key:
        print("ERROR: YOUTUBE_API_KEY is not set. Add it to your .env file.", file=sys.stderr)
        print("Get a key at: https://console.cloud.google.com → YouTube Data API v3", file=sys.stderr)
        sys.exit(1)

    youtube = build("youtube", "v3", developerKey=api_key)

    # Search for videos
    search_response = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=min(max_results * 2, 50),  # fetch more, then filter
        relevanceLanguage="en",
        order="relevance",
    ).execute()

    video_ids = [item["id"]["videoId"] for item in search_response.get("items", [])]

    if not video_ids:
        print("No results found.", file=sys.stderr)
        return []

    # Fetch video statistics for view count and duration
    stats_response = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=",".join(video_ids),
    ).execute()

    results = []
    for item in stats_response.get("items", []):
        video_id = item["id"]
        snippet = item["snippet"]
        stats = item.get("statistics", {})
        details = item.get("contentDetails", {})

        results.append({
            "title": snippet.get("title", ""),
            "channel": snippet.get("channelTitle", ""),
            "description": snippet.get("description", "")[:200],
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "short_url": f"https://youtu.be/{video_id}",
            "view_count": int(stats.get("viewCount", 0)),
            "like_count": int(stats.get("likeCount", 0)),
            "duration": details.get("duration", "PT0S"),
            "published_at": snippet.get("publishedAt", ""),
        })

    # Sort by view count descending
    results.sort(key=lambda x: x["view_count"], reverse=True)
    return results[:max_results]


def format_markdown_table(videos: list[dict]) -> str:
    """Format video list as a Markdown table for embedding in docs."""
    lines = [
        "## 🎥 Recommended Videos",
        "",
        "| Title | Channel | Views | Why Watch |",
        "|-------|---------|-------|-----------|",
    ]
    for v in videos:
        views = f"{v['view_count']:,}"
        title_link = f"[{v['title']}]({v['short_url']})"
        lines.append(f"| {title_link} | {v['channel']} | {views} | *(add reason)* |")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search YouTube for 3D printing training videos")
    parser.add_argument("--topic", required=True, help="Search query / topic")
    parser.add_argument("--max", type=int, default=8, help="Max results to return (default: 8)")
    parser.add_argument("--output", help="Save JSON results to this file path")
    parser.add_argument("--markdown", action="store_true", help="Print as Markdown table instead of JSON")
    args = parser.parse_args()

    print(f"Searching YouTube for: '{args.topic}'...", file=sys.stderr)
    videos = search_youtube(args.topic, max_results=args.max)

    if not videos:
        print("No videos found for that query.", file=sys.stderr)
        sys.exit(1)

    if args.markdown:
        print(format_markdown_table(videos))
    else:
        output = json.dumps(videos, indent=2)
        print(output)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(videos, f, indent=2, ensure_ascii=False)
        print(f"Saved to {out_path}", file=sys.stderr)

    print(f"\nFound {len(videos)} videos.", file=sys.stderr)


if __name__ == "__main__":
    main()
