#!/usr/bin/env python3
"""
fetch_reddit.py - Fetch wireframe/UX/UI pain-point posts from design subreddits.

Adapted for the wireframe-skills project: focuses on wireframe creation,
information architecture, user flow, and screen design pain points.

Usage:
    python scripts/fetch_reddit.py --year 2026 --output /tmp/reddit_raw.json
    python scripts/fetch_reddit.py --year 2025 --limit 50 --output /tmp/reddit_raw.json

No authentication required (uses Reddit's public JSON API).
"""

import argparse
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta


DESIGN_SUBREDDITS = [
    # Core design/UX — highest signal for wireframe pain points
    "UXDesign",
    "UI_Design",
    "userexperience",
    "webdesign",
    "ProductDesign",
    # Information architecture & interaction design
    "interaction_design",
    # Indie builders/founders who need wireframing help (non-designer angle)
    "SideProject",
    "startups",
    "Entrepreneur",
    "indiehackers",
    # Platform-specific UI/screen design discussions
    "androiddev",
    "iOSProgramming",
    # Frontend dev with design needs
    "reactjs",
    "Frontend",
    # Design tools discussion
    "FigmaDesign",
]

# Pain-point keywords scoped to wireframe/IA/UX design context.
PAIN_SIGNAL_KEYWORDS = [
    # Frustration signals
    "frustrated", "can't figure out", "confused", "overwhelmed", "struggling",
    "hate", "terrible", "awful", "annoying", "broken",
    # Request signals
    "looking for", "recommendation", "alternative", "feedback", "review",
    "critique", "roast my", "what do you think", "rate my", "how do I",
    # Wireframe/IA/flow specific pain
    "wireframe", "user flow", "information architecture", "navigation design",
    "screen flow", "sitemap", "onboarding flow", "how to design",
    "best way to design", "design help", "ui help", "ux help",
    # Non-designer / no budget signals
    "no designer", "without designer", "non-designer", "design on a budget",
    "free wireframe", "wireframe tool", "prototype tool",
    # Generic demand signals
    "wish", "need help", "stuck", "looks bad", "ugly", "not intuitive",
    "users are confused", "users don't understand",
]

HEADERS = {
    "User-Agent": "WireframeResearch/1.0 (educational research tool)",
}


def compute_filter_year_range(target_year: int) -> tuple[int, int]:
    """
    Return (start_timestamp, end_timestamp) for client-side year filtering.

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


def fetch_subreddit_posts(subreddit: str, limit: int = 25, sort: str = "top",
                          target_year: int | None = None) -> list[dict]:
    """Fetch posts from a subreddit using Reddit's public JSON API."""
    current_year = datetime.now(timezone.utc).year
    time_filter = "year" if target_year is None or target_year >= current_year - 1 else "all"
    url = f"https://www.reddit.com/r/{subreddit}/{sort}.json?limit={limit}&t={time_filter}"
    req = urllib.request.Request(url, headers=HEADERS)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            posts = data.get("data", {}).get("children", [])
            return [p["data"] for p in posts]
    except Exception as e:
        print(f"  Warning: Failed to fetch r/{subreddit}: {e}")
        return []


# Keywords indicating wireframe/IA/UX design context
DESIGN_CONTEXT_KEYWORDS = [
    "design", "ui", "ux", "interface", "app", "website", "layout",
    "wireframe", "prototype", "mockup", "user flow", "navigation",
    "information architecture", "screen", "onboarding", "sitemap",
    "color", "font", "typography", "figma", "component", "visual",
    "branding", "css", "frontend", "mobile app", "web app",
]


def is_pain_point(post: dict) -> bool:
    """
    Heuristic: does this post signal a wireframe/UX design pain point or demand?

    Requires both a design context keyword AND a pain signal keyword.
    """
    title = post.get("title", "").lower()
    selftext = post.get("selftext", "").lower()[:200]
    flair = (post.get("link_flair_text") or "").lower()
    content = title + " " + flair + " " + selftext

    has_design_context = any(kw in content for kw in DESIGN_CONTEXT_KEYWORDS)
    has_pain_signal = any(kw in content for kw in PAIN_SIGNAL_KEYWORDS)
    return has_design_context and has_pain_signal


def filter_by_range(post: dict, start_ts: int, end_ts: int) -> bool:
    """Filter posts within the given timestamp range."""
    created = post.get("created_utc", 0)
    return start_ts <= created <= end_ts


def score_post(post: dict) -> int:
    """Simple engagement score combining upvotes and comment count."""
    return post.get("score", 0) + post.get("num_comments", 0) * 3


def main():
    parser = argparse.ArgumentParser(description="Fetch wireframe/UX subreddit posts for research")
    parser.add_argument("--year", type=int, default=datetime.now().year,
                        help="Target year for filtering posts (default: current year)")
    parser.add_argument("--limit", type=int, default=25,
                        help="Max posts to fetch per subreddit (default: 25)")
    parser.add_argument("--output", type=str, default="/tmp/reddit_raw.json",
                        help="Output JSON file path")
    parser.add_argument("--subreddits", type=str, default=None,
                        help="Comma-separated subreddit list (default: built-in design list)")
    args = parser.parse_args()

    subreddits = args.subreddits.split(",") if args.subreddits else DESIGN_SUBREDDITS
    target_year = args.year

    start_ts, end_ts = compute_filter_year_range(target_year)
    from datetime import datetime as _dt
    start_label = _dt.fromtimestamp(start_ts, tz=timezone.utc).strftime("%Y-%m-%d")
    end_label = _dt.fromtimestamp(end_ts, tz=timezone.utc).strftime("%Y-%m-%d")
    print(f"Date range: {start_label} to {end_label}")
    print(f"Fetching posts from {len(subreddits)} subreddits...")

    all_posts = []
    pain_posts = []

    for sub in subreddits:
        print(f"  Fetching r/{sub}...")
        posts = fetch_subreddit_posts(sub, limit=args.limit, sort="top", target_year=target_year)

        for post in posts:
            if not filter_by_range(post, start_ts, end_ts):
                continue

            entry = {
                "subreddit": sub,
                "title": post.get("title", ""),
                "selftext": post.get("selftext", "")[:500],
                "score": post.get("score", 0),
                "num_comments": post.get("num_comments", 0),
                "flair": post.get("link_flair_text", ""),
                "url": f"https://reddit.com{post.get('permalink', '')}",
                "created_utc": post.get("created_utc", 0),
                "engagement_score": score_post(post),
                "is_pain_point": is_pain_point(post),
            }
            all_posts.append(entry)
            if entry["is_pain_point"]:
                pain_posts.append(entry)

        time.sleep(1)  # be polite to Reddit's API

    all_posts.sort(key=lambda x: x["engagement_score"], reverse=True)
    pain_posts.sort(key=lambda x: x["engagement_score"], reverse=True)

    output = {
        "target_year": target_year,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_posts": len(all_posts),
        "pain_point_posts": len(pain_posts),
        "subreddits_searched": subreddits,
        "top_pain_points": pain_posts[:50],
        "all_posts": all_posts[:100],
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Fetched {len(all_posts)} posts, {len(pain_posts)} flagged as pain points.")
    print(f"Output saved to: {args.output}")


if __name__ == "__main__":
    main()
