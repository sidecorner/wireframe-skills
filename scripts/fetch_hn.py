#!/usr/bin/env python3
"""
fetch_hn.py - Fetch wireframe/UX/UI design posts from Hacker News via Algolia Search API.

Adapted for the wireframe-skills project: focuses on wireframe tools, information
architecture, user flow design, and UX best practices discussion on HN.

Usage:
    python scripts/fetch_hn.py --year 2026 --output /tmp/hn_raw.json
    python scripts/fetch_hn.py --year 2025 --min-points 5 --output /tmp/hn_raw.json

HN Algolia API is public and requires no authentication.

Date range logic:
    - If TARGET_YEAR == current year (year not yet complete), searches the past 12 months
      from today (e.g., 2026-03 → 2025-03 to 2026-03).
    - If TARGET_YEAR < current year (full year passed), searches Jan 1 to Dec 31 of that year.
"""

import argparse
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta


# Query terms focused on wireframing, information architecture, and UX design tools on HN.
DESIGN_QUERIES = [
    # Wireframe & prototyping tools
    "wireframe tool",
    "prototyping tool",
    "Figma wireframe",
    "UI prototype",
    "lo-fi wireframe",
    # AI-assisted design & wireframing (high HN signal)
    "AI UI generator",
    "AI wireframe",
    "generative UI",
    "app design AI",
    "design automation",
    # Information architecture & UX flows
    "information architecture",
    "user flow design",
    "UX navigation design",
    "onboarding UX",
    "UX design system",
    # Design tools & alternatives
    "Figma alternative",
    "no-code design tool",
    "design system",
    "UI component library",
    # Mobile & web screen design
    "mobile app design",
    "web app UX",
    "dashboard design",
    # Design for non-designers (indie hacker angle)
    "design for developers",
    "startup design",
    "design tool startup",
]

# Keywords that confirm a post is actually about design/wireframe/UX topics.
DESIGN_RELEVANCE_KEYWORDS = [
    "design", "ui", "ux", "interface", "frontend", "css", "figma", "sketch",
    "wireframe", "prototype", "mockup", "component", "layout", "typography",
    "color", "accessibility", "responsive", "mobile", "app", "web app",
    "dashboard", "tailwind", "react", "vue", "svelte", "animation",
    "interaction", "design system", "style guide", "visual", "pixel",
    "information architecture", "user flow", "navigation", "onboarding",
    "sitemap", "screen design",
]

ALGOLIA_BASE = "https://hn.algolia.com/api/v1/search"


def compute_date_range(target_year: int) -> tuple[int, int]:
    """
    Compute Unix timestamp range for the target year.

    If target_year == current year (year not yet complete), use past 12 months from today.
    If target_year < current year (full year has passed), use Jan 1 to Dec 31 of that year.
    """
    now = datetime.now(timezone.utc)
    current_year = now.year

    if target_year >= current_year:
        end_dt = now
        start_dt = now - timedelta(days=365)
    else:
        start_dt = datetime(target_year, 1, 1, tzinfo=timezone.utc)
        end_dt = datetime(target_year, 12, 31, 23, 59, 59, tzinfo=timezone.utc)

    return int(start_dt.timestamp()), int(end_dt.timestamp())


def is_design_relevant(title: str) -> bool:
    """Check if a post title actually relates to design/wireframe/UX topics."""
    title_lower = title.lower()
    return any(kw in title_lower for kw in DESIGN_RELEVANCE_KEYWORDS)


def fetch_hn_posts(query: str, year_start: int, year_end: int,
                   min_points: int = 5) -> list[dict]:
    """Fetch HN posts matching a query within the given timestamp range."""
    params = urllib.parse.urlencode({
        "query": query,
        "tags": "story",
        "numericFilters": f"created_at_i>{year_start},created_at_i<{year_end},points>={min_points}",
        "hitsPerPage": 20,
    })
    url = f"{ALGOLIA_BASE}?{params}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "WireframeResearch/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            return data.get("hits", [])
    except Exception as e:
        print(f"  Warning: HN query '{query}' failed: {e}")
        return []


def normalize_post(hit: dict, query: str) -> dict:
    """Normalize an Algolia HN hit to a standard structure."""
    title = hit.get("title", "")
    return {
        "object_id": hit.get("objectID", ""),
        "title": title,
        "url": hit.get("url", ""),
        "hn_url": f"https://news.ycombinator.com/item?id={hit.get('objectID', '')}",
        "points": hit.get("points", 0),
        "num_comments": hit.get("num_comments", 0),
        "author": hit.get("author", ""),
        "created_at": hit.get("created_at", ""),
        "matched_query": query,
        "design_relevant": is_design_relevant(title),
        "engagement_score": hit.get("points", 0) + hit.get("num_comments", 0) * 2,
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch wireframe/UX HN posts for research")
    parser.add_argument("--year", type=int, default=datetime.now().year,
                        help="Target year (default: current year → past 12 months)")
    parser.add_argument("--min-points", type=int, default=5,
                        help="Minimum HN points threshold (default: 5)")
    parser.add_argument("--output", type=str, default="/tmp/hn_raw.json",
                        help="Output JSON file path")
    parser.add_argument("--queries", type=str, default=None,
                        help="Comma-separated query list (default: built-in wireframe/design list)")
    parser.add_argument("--no-relevance-filter", action="store_true",
                        help="Disable design relevance filtering (include all query matches)")
    args = parser.parse_args()

    queries = args.queries.split(",") if args.queries else DESIGN_QUERIES
    target_year = args.year

    year_start, year_end = compute_date_range(target_year)
    start_label = datetime.fromtimestamp(year_start, tz=timezone.utc).strftime("%Y-%m-%d")
    end_label = datetime.fromtimestamp(year_end, tz=timezone.utc).strftime("%Y-%m-%d")
    print(f"Date range: {start_label} to {end_label}")
    print(f"Fetching HN posts using {len(queries)} queries...")

    seen_ids: set[str] = set()
    all_posts: list[dict] = []
    filtered_out = 0

    for query in queries:
        print(f"  Searching: '{query}'...")
        hits = fetch_hn_posts(query, year_start, year_end, min_points=args.min_points)

        for hit in hits:
            post = normalize_post(hit, query)
            if post["object_id"] not in seen_ids:
                seen_ids.add(post["object_id"])
                if args.no_relevance_filter or post["design_relevant"]:
                    all_posts.append(post)
                else:
                    filtered_out += 1

        time.sleep(0.5)

    all_posts.sort(key=lambda x: x["engagement_score"], reverse=True)

    output = {
        "target_year": target_year,
        "date_range": {
            "start": datetime.fromtimestamp(year_start, tz=timezone.utc).isoformat(),
            "end": datetime.fromtimestamp(year_end, tz=timezone.utc).isoformat(),
        },
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_posts": len(all_posts),
        "filtered_out_irrelevant": filtered_out,
        "queries_used": queries,
        "posts": all_posts,
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Found {len(all_posts)} wireframe/UX relevant HN posts ({filtered_out} filtered).")
    print(f"Output saved to: {args.output}")


if __name__ == "__main__":
    main()
