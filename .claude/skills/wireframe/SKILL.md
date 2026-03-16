---
name: wireframe
description: >
  AI-powered wireframe creation skill for web apps and mobile applications.
  Researches real user pain points from Reddit, Hacker News, and Qiita for the
  specified year, then generates structured wireframes using the Pencil MCP tool.

  Use this skill when the user wants to: design app screens, create wireframes,
  plan information architecture, design user flows, build navigation structures,
  create UI mockups, plan screen layouts, design onboarding flows, or structure
  a web service. Also trigger when the user says "ワイヤーフレーム", "画面設計",
  "情報設計", "UI設計", "アプリのUI", "画面構成", "導線設計", or asks to design
  any kind of app or website from scratch.

  IMPORTANT: Always use this skill for any wireframe, screen design, or
  information architecture task — even if the user only mentions one screen or
  a simple layout. The research phase ensures designs are grounded in real UX pain points.
compatibility:
  tools:
    - Bash
    - mcp__pencil__open_document
    - mcp__pencil__get_guidelines
    - mcp__pencil__get_style_guide
    - mcp__pencil__batch_design
    - mcp__pencil__get_screenshot
    - mcp__pencil__snapshot_layout
---

# Wireframe Creation Skill

All paths are relative to the project root (`wireframe-skills/`).
Reference files: `references/`. Scripts: `scripts/`. Output: `reports/`.

---

## Step 1: Interview the User (in Japanese)

Ask all questions in a single message. Do not proceed until answers are received.

```
以下の情報を教えてください：

1. **調査対象の年号**
   何年のトレンドを調査しますか？（未入力の場合は現在の年 {current_year} を使用します）

2. **アプリ・サービスの概要**
   どんなアプリやWebサービスを作りたいですか？（例：料理レシピの投稿・共有アプリ、タスク管理SaaS など）

3. **プラットフォーム**
   - [ ] iOS アプリ
   - [ ] Android アプリ
   - [ ] Webアプリ（PC）
   - [ ] Webアプリ（モバイル）
   - [ ] レスポンシブ（マルチプラットフォーム）

4. **ターゲットユーザー（ペルソナ）**
   誰のためのサービスですか？（例：20〜35歳の働く女性、中小企業のマーケター、料理好きな主婦 など）

5. **コア機能・主要な画面**
   必ず含めたい機能や画面はありますか？（例：投稿一覧、詳細ページ、投稿作成、プロフィール など）

6. **参考にしたいアプリ・サービス**（任意）
   「このアプリのUIが好き」「このサービスのUXを参考にしたい」といったものがあれば教えてください。

7. **その他の要件**（任意）
   デザインの方向性、ブランドイメージ、特別な制約など何かあれば。
```

---

## Step 2: Determine the Research Period

- No year specified → use `{current_year}`
- Specified year ≥ current year → past 12 months from today
- Specified year < current year → Jan 1 to Dec 31 of that year

The `--year` flag handles this automatically in all three scripts.

---

## Step 3: Run Research Scripts

Run all three in parallel from the project root.

```bash
python scripts/fetch_reddit.py \
  --year {target_year} --limit 50 \
  --output /tmp/wf_reddit_{target_year}.json

python scripts/fetch_hn.py \
  --year {target_year} --min-points 5 \
  --output /tmp/wf_hn_{target_year}.json

python scripts/fetch_qiita.py \
  --year {target_year} \
  --output /tmp/wf_qiita_{target_year}.json
```

---

## Step 4: Synthesize Research

Read the three JSON output files. Follow `references/research-methodology.md` to:
- Identify pain points and map them to wireframe decisions
- Extract desired patterns and trend signals
- Determine the screen inventory for this specific service

Also read `references/wireframe-principles.md` and `references/ui-patterns.md` as needed.

---

## Step 5: Create Report Directory

```
reports/{target_year}/{yyyymmdd}/{hhmmss}/
```

Create the directory before writing any output.

---

## Step 6: Write report.md

Write `reports/{target_year}/{yyyymmdd}/{hhmmss}/report.md`.

Follow the report template in `references/research-methodology.md`.

---

## Step 7: Create Wireframe in Pencil

### 7a. Open the document

```
mcp__pencil__open_document("reports/{target_year}/{yyyymmdd}/{hhmmss}/{service-name}.pen")
```

Use kebab-case for the filename (e.g., `recipe-sharing-app.pen`).

### 7b. Load platform guidelines

```
mcp__pencil__get_guidelines("mobile-app")   # iOS / Android
mcp__pencil__get_guidelines("web-app")      # web applications
```

### 7c. Design the screens

Use the screen inventory defined in `report.md`. Follow `references/pencil-guide.md` for style specs, layout dimensions, and code examples.

Design in this order:
1. Core screens (Home, main feature list, detail)
2. Navigation structure
3. Secondary screens (Profile, Settings)
4. Edge cases (Empty state, Error, Onboarding)

### 7d. Validate with screenshots

Call `mcp__pencil__get_screenshot()` after every 3–4 screens. Fix layout issues before continuing.

---

## Step 8: Final Summary (in Japanese)

```
## 完了しました ✓

**調査概要**
- Reddit: {n}件の投稿を分析（うちペインポイント {n}件）
- Hacker News: {n}件の関連投稿を分析
- Qiita: {n}件の記事を分析

**主要な発見**
1. {top finding 1}
2. {top finding 2}
3. {top finding 3}

**ワイヤーフレーム**
- 作成画面数: {n}画面
- ファイル: `{pen file path}`

**レポート**
- `{report.md path}`

---
{Any specific design decisions worth highlighting}
```

---

## Notes

- "Quick wireframe" requests: still do Step 1, but may skip Steps 3–4 and rely on `references/` directly.
- If a `.pen` file already exists at the target path, create a new timestamped subdirectory.
- Reports are cumulative — do not overwrite existing files in a directory.
