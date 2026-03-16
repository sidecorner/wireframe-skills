#!/usr/bin/env python3
"""
fetch_qiita.py - Fetch wireframe/UI/UX design articles from Qiita via Qiita API v2.

Adapted for the wireframe-skills project: focuses on wireframe creation,
information architecture, screen design, and UI/UX best practices (Japanese).

Usage:
    python scripts/fetch_qiita.py --year 2026 --output /tmp/qiita_raw.json
    python scripts/fetch_qiita.py --year 2025 --output /tmp/qiita_raw.json

Authentication:
    Reads QIITA_TOKEN from .env file in the project root (or QIITA_TOKEN env var).
    Without a token, requests are rate-limited to 60/hour.

Date range logic:
    - If TARGET_YEAR == current year (year not yet complete), searches the past 12 months
      from today (e.g., 2026-03 → 2025-03 to 2026-03).
    - If TARGET_YEAR < current year (full year passed), searches Jan 1 to Dec 31 of that year.
"""

import argparse
import json
import os
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta
from pathlib import Path


# Qiita search queries focused on wireframe/IA/UX/screen design (Japanese)
DESIGN_QUERIES = [
    # Wireframe creation & tools
    "ワイヤーフレーム 作り方",
    "ワイヤーフレーム ツール",
    "画面設計 方法",
    "UIモックアップ 作成",
    "プロトタイプ 作り方",
    # Information architecture & navigation
    "情報設計 アプリ",
    "画面遷移図 作成",
    "ユーザーフロー 設計",
    "サイトマップ 設計",
    "ナビゲーション UX",
    # UX/UI design practices
    "UXデザイン 改善",
    "UIデザイン 原則",
    "ユーザビリティ 改善",
    "オンボーディング 設計",
    "アクセシビリティ デザイン",
    # Design tools (popular in Japan)
    "Figma 使い方",
    "Figma プラグイン",
    "デザインシステム 構築",
    "UIコンポーネント 設計",
    # Mobile & app design
    "モバイルUI デザイン",
    "アプリ 画面設計",
    "個人開発 デザイン",
    "非デザイナー デザイン",
    # AI-assisted design
    "AIデザイン ツール",
    "生成AI UI デザイン",
]

QIITA_API_BASE = "https://qiita.com/api/v2"


def load_token() -> str | None:
    """Load QIITA_TOKEN from environment or .env file."""
    token = os.environ.get("QIITA_TOKEN")
    if token:
        return token

    # Look for .env in project root (parent of scripts/)
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("QIITA_TOKEN="):
                return line.split("=", 1)[1].strip()
    return None


def compute_date_range(target_year: int) -> tuple[datetime, datetime]:
    """
    Compute the date range to search.

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

    return start_dt, end_dt


def fetch_qiita_articles(query: str, start_dt: datetime, end_dt: datetime,
                         token: str | None = None, per_page: int = 20) -> list[dict]:
    """Fetch Qiita articles matching a query within the given date range."""
    created_filter = (
        f"created:>={start_dt.strftime('%Y-%m-%d')} "
        f"created:<={end_dt.strftime('%Y-%m-%d')}"
    )
    full_query = f"{query} {created_filter}"

    params = urllib.parse.urlencode({
        "query": full_query,
        "per_page": per_page,
        "page": 1,
    })
    url = f"{QIITA_API_BASE}/items?{params}"

    headers = {
        "User-Agent": "WireframeResearch/1.0",
        "Content-Type": "application/json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"  Warning: Qiita query '{query}' failed: {e}")
        return []


def normalize_article(article: dict, query: str) -> dict:
    """Normalize a Qiita article to a standard structure."""
    tags = [t.get("name", "") for t in article.get("tags", [])]
    return {
        "id": article.get("id", ""),
        "title": article.get("title", ""),
        "url": article.get("url", ""),
        "likes_count": article.get("likes_count", 0),
        "stocks_count": article.get("stocks_count", 0),
        "comments_count": article.get("comments_count", 0),
        "author": article.get("user", {}).get("id", ""),
        "created_at": article.get("created_at", ""),
        "tags": tags,
        "matched_query": query,
        # Higher weight on stocks (saves) as a quality signal on Qiita
        "engagement_score": (
            article.get("likes_count", 0)
            + article.get("stocks_count", 0) * 2
            + article.get("comments_count", 0) * 3
        ),
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch wireframe/UX Qiita articles for research")
    parser.add_argument("--year", type=int, default=datetime.now().year,
                        help="Target year (default: current year → past 12 months)")
    parser.add_argument("--output", type=str, default="/tmp/qiita_raw.json",
                        help="Output JSON file path")
    parser.add_argument("--per-page", type=int, default=20,
                        help="Articles per query (max 100, default: 20)")
    parser.add_argument("--queries", type=str, default=None,
                        help="Comma-separated query list (default: built-in wireframe/design list)")
    args = parser.parse_args()

    token = load_token()
    if token:
        print("Qiita token loaded.")
    else:
        print("Warning: No QIITA_TOKEN found. Requests will be rate-limited (60/hour).")

    queries = args.queries.split(",") if args.queries else DESIGN_QUERIES
    target_year = args.year

    start_dt, end_dt = compute_date_range(target_year)
    print(f"Date range: {start_dt.strftime('%Y-%m-%d')} to {end_dt.strftime('%Y-%m-%d')}")
    print(f"Fetching Qiita articles using {len(queries)} queries...")

    seen_ids: set[str] = set()
    all_articles: list[dict] = []

    for query in queries:
        print(f"  Searching: '{query}'...")
        articles = fetch_qiita_articles(
            query, start_dt, end_dt,
            token=token, per_page=args.per_page
        )

        for article in articles:
            normalized = normalize_article(article, query)
            if normalized["id"] not in seen_ids:
                seen_ids.add(normalized["id"])
                all_articles.append(normalized)

        time.sleep(0.5)

    all_articles.sort(key=lambda x: x["engagement_score"], reverse=True)

    output = {
        "target_year": target_year,
        "date_range": {
            "start": start_dt.isoformat(),
            "end": end_dt.isoformat(),
        },
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_articles": len(all_articles),
        "queries_used": queries,
        "articles": all_articles,
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Found {len(all_articles)} unique Qiita articles on wireframe/UX topics.")
    print(f"Output saved to: {args.output}")


if __name__ == "__main__":
    main()
