# wireframe-skills

Reddit・Hacker News・Qiitaのリアルなユーザーの声をもとに、AIがワイヤーフレームを自動生成するローカルスキルです。

---

## 概要

このスキルは、アプリやWebサービスのUI/UX設計を「最新のトレンドとユーザーのペインポイント」に基づいて行います。
ヒアリング → 調査 → レポート生成 → Pencilワイヤーフレーム出力まで、一気通貫で実行します。

**このスキルは `wireframe-skills/` ディレクトリ内でのみ有効です。**

---

## ディレクトリ構成

```
wireframe-skills/
├── .claude/
│   ├── CLAUDE.md                          # プロジェクト説明
│   └── skills/
│       └── wireframe/
│           └── SKILL.md                   # スキル本体（英語）
├── scripts/
│   ├── fetch_reddit.py                    # Reddit調査スクリプト
│   ├── fetch_hn.py                        # Hacker News調査スクリプト
│   └── fetch_qiita.py                     # Qiita調査スクリプト
├── references/
│   ├── wireframe-principles.md            # ワイヤーフレームの原則
│   ├── ui-patterns.md                     # UIパターン・画面テンプレート
│   ├── pencil-guide.md                    # Pencil MCP使い方ガイド
│   └── research-methodology.md            # 調査データの読み方・活用法
├── reports/                               # 生成されたレポート（自動作成）
│   └── {調査年}/
│       └── {yyyymmdd}/
│           └── {hhmmss}/
│               ├── report.md              # 調査まとめ＋設計根拠
│               └── {service-name}.pen     # Pencilワイヤーフレーム
├── .env                                   # QIITA_TOKEN を記載
└── README.md                              # このファイル
```

---

## セットアップ

### Qiita APIトークンの設定

Qiitaの認証なしでも動作しますが（60リクエスト/時間制限）、トークンを設定すると安定します。

```
# wireframe-skills/.env
QIITA_TOKEN=your_token_here
```

---

## 使い方

`wireframe-skills/` ディレクトリで Claude Code を開き、日本語で話しかけるだけです。

**呼び出し例：**
- 「ワイヤーフレームを作りたい」
- 「料理レシピ共有アプリのUI設計をしてほしい」
- 「タスク管理SaaSの画面構成を考えて」
- 「このアプリの情報設計とワイヤーフレームをお願い」

---

## スキルの動作フロー

```
1. ヒアリング（日本語）
   ↓
   ・調査対象の年号（未指定 → 現在の年）
   ・アプリ・サービスの概要
   ・プラットフォーム（iOS / Android / Web）
   ・ターゲットユーザー（ペルソナ）
   ・コア機能・主要画面
   ・参考サービス（任意）

2. 調査実行
   ↓
   ・Reddit：デザイン系サブレディットからペインポイントを収集
   ・Hacker News：高エンゲージメントのUI/UX投稿を収集
   ・Qiita：日本語のUIデザイン記事を収集

3. 調査分析
   ↓
   ・ペインポイントを整理
   ・ワイヤーフレーム設計の根拠に変換

4. レポート生成
   ↓
   reports/{year}/{yyyymmdd}/{hhmmss}/report.md

5. Pencilワイヤーフレーム出力
   ↓
   reports/{year}/{yyyymmdd}/{hhmmss}/{service-name}.pen
```

---

## 調査期間のロジック

| 指定 | 調査範囲 |
|------|---------|
| 年号を指定しない | 現在の年（過去12ヶ月） |
| 現在の年を指定（例：2026） | 過去12ヶ月（2025-03〜2026-03） |
| 過去の年を指定（例：2025） | その年の1月1日〜12月31日 |

---

## 調査対象

### Reddit
デザイン・UX系サブレディットからワイヤーフレーム・情報設計に関するペインポイントを収集します。

| サブレディット | 内容 |
|---|---|
| r/UXDesign | UX設計の議論・ペインポイント |
| r/UI_Design | UIデザインのフィードバック・議論 |
| r/userexperience | ユーザー体験の改善議論 |
| r/webdesign | Webデザインのトレンド |
| r/ProductDesign | プロダクト設計全般 |
| r/SideProject | 個人開発者のデザイン悩み |
| r/startups | スタートアップのUI/UX議論 |
| r/FigmaDesign | デザインツールの議論 |
| その他 | androiddev, iOSProgramming, reactjs, Frontend など |

### Hacker News
Algolia Search APIを使い、UI/UXデザインツール・ワイヤーフレーム・情報設計に関する高評価投稿を収集します。

### Qiita
日本語のワイヤーフレーム・画面設計・UIデザイン記事をQiita API v2で収集します。
「ワイヤーフレーム 作り方」「画面遷移図 作成」「UIモックアップ」など25クエリを対象にします。

---

## スクリプトの直接実行

調査スクリプトは単独でも実行できます。

```bash
# Reddit調査
python scripts/fetch_reddit.py --year 2026 --output /tmp/reddit.json

# Hacker News調査
python scripts/fetch_hn.py --year 2026 --output /tmp/hn.json

# Qiita調査
python scripts/fetch_qiita.py --year 2026 --output /tmp/qiita.json
```

---

## リファレンスドキュメント

| ファイル | 内容 |
|---|---|
| `references/wireframe-principles.md` | ワイヤーフレームの基礎・UI要素・情報設計の原則 |
| `references/ui-patterns.md` | 最新UIトレンド・画面パターン集・スクリーンインベントリ |
| `references/pencil-guide.md` | Pencil MCPでのワイヤーフレーム作成コード例 |
| `references/research-methodology.md` | 調査データの解釈方法・wireframe意思決定フレームワーク |
