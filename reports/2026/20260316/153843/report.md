# Wireframe Research Report: Small Good / 3 Good Things

**Research Period:** 2025-03-16 to 2026-03-16
**Target Platform:** iOS / Android（両対応）
**Target Users:** 20〜30代・完璧主義傾向・都内一人暮らし働く女性
**Persona:** 「北欧、暮らしの道具店」系・Instagram疲れ・夜寝る前にモヤモヤしがちなOL

---

## Executive Summary

調査期間中、メンタルウェルネス・感情ケア系アプリの需要が高まりつつある一方、**オンボーディングの過剰設計**と**IAP（課金）への摩擦**が最大のユーザー離脱要因であることが判明。Apple自身がLiquid Glass（グラスモーフィズム進化版）をOS標準UIとして採用したことで、ガラス系デザインは「トレンド」から「スタンダード」へ移行中。「Small Good」は、この流れと完全に合致したデザイン方針を持っており、**最小限の摩擦・最大限の感情的報酬**という設計思想を徹底することが最重要課題となる。

---

## Research Data Summary

### Reddit
- 総投稿数: 700件
- ペインポイント判定: 100件
- 調査サブレディット: 15件（UXDesign, UI_Design, userexperience, SideProject, iOSProgramming 等）

### Hacker News
- 総投稿数: 136件
- 主要クエリ: wireframe tool, prototyping tool, onboarding UX, mobile app design 等 25クエリ

### Qiita
- 総記事数: 338件
- 主要クエリ: ワイヤーフレーム作り方, オンボーディング設計, モバイルUI デザイン 等 25クエリ

---

## Key Findings

### Pain Points（避けるべき設計）

| # | ペインポイント | ソース | エンゲージメント |
|---|---|---|---|
| 1 | **オンボーディングを増やしたら離脱率が上がった**（削除したら改善） | Reddit/UXDesign | score=466, 103 comments |
| 2 | **「iPhoneに払ったのになぜアプリにも払う？」** IAP設計への強い拒否感 | Reddit/SideProject | 2178 upvotes |
| 3 | **デザインシステムへの疲弊**（複雑なコンポーネント体系が生産性を下げる） | Reddit/UXDesign | score=517, 143 comments |
| 4 | **Apple Liquid Glassへの賛否混在** → ユーザーはガラス系に慣れつつある | Reddit/UI_Design | score=546, 263 comments |
| 5 | **「キャンセルと完了ボタンの位置で揉める」** UIの一貫性不足 | Reddit/UI_Design | 336 comments |
| 6 | **Google Play審査の理不尽さ** → iOS優先リリース戦略の根拠 | Reddit/androiddev | score=293, 138 comments |

### Desired Patterns（採用すべき設計）

| # | 求められているもの | ソース |
|---|---|---|
| 1 | **シンプルで意図的なアプリ** – Poppy（関係性管理）、Indy（ADHD向け）、Oh Yah（ルーティン）いずれも "intentional" "simple" を前面に | HN |
| 2 | **1画面1アクション** – コアタスクを最小タップ数で完結させる | HN/Reddit共通 |
| 3 | **感情・関係性に特化したニッチアプリ**の需要増加 | HN: Poppy 179pts, 124 comments |
| 4 | **AIによるオンボーディング代替**（短い質問→パーソナライズ）より、**ノーオンボーディング**の方が効果的な場面も | Reddit/UXDesign |
| 5 | **生体認証（FaceID）**が標準期待値 – セキュリティへの意識が高い | Reddit/iOSProgramming |

### Trend-Based Decisions

| トレンド | 根拠 | Small Goodへの適用 |
|---|---|---|
| **Liquid Glass / グラスモーフィズム公式化** | Apple がiOS/macOS標準UIとして採用発表（Reddit/UI_Design 高エンゲ） | ニューモーフィズム+グラスモーフィズムの混在スタイルがApple HIG準拠 |
| **ニッチ・ウェルネスアプリの成功事例** | HNでPoppy, Indy, Oh Yahがいずれも100+ comments獲得 | 感情ケア特化の市場性が確認済み |
| **AIアシスト設計ツールの普及** | Qiita「UIデザインから実装までAIに丸投げ」記事がstocks=35 | Figma/AI設計ツールでの高速プロトタイピングが標準化 |
| **オンボーディング最小化** | 「削除したら活性化率が上がった」事例（Reddit/UXDesign） | Welcome画面は最大2枚、必須質問のみ |

---

## Wireframe Decisions

| 画面 | 設計決定 | 根拠 |
|---|---|---|
| オンボーディング | **1〜2画面のみ**、スキップ可能 | Reddit: elaborate onboarding → 離脱増加 |
| ホーム | **抽象ビジュアル（花束/星/瓶）を最前面**に、テキスト最小化 | ペルソナ: 「キラキラ投稿で疲弊」→ 視覚的静けさが必要 |
| 記録入力 | **3行以内・30〜50文字/行の制約UI**、気分スタンプは最初に選ぶ | HN: 1画面1アクション。入力ハードルを最小化 |
| 完了演出 | **花が咲く・光の粒アニメーション**（全画面） | ペルソナ: 感情的報酬で継続動機を与える |
| 過去の記録 | **カレンダー + タイムラインの切り替え**、記録のある日は絵文字/色でマーク | Visual Growth: ビジュアルで継続を実感 |
| 通知 | **デフォルトOFF**、オプトインで設定 | Reddit: 過度な通知はアンインストール要因 |
| 課金 | **コア機能は無料**、プレミアム機能（テーマ追加等）のみ有料 | Reddit: IAP摩擦が1位の離脱要因 |
| セキュリティ | **FaceID/TouchID が初回起動時にオプションで提示** | Reddit: 生体認証は標準期待値 |

---

## Screen Inventory

| # | 画面名 | 種別 | 備考 |
|---|---|---|---|
| 01 | Splash / ローディング | 起動 | ロゴ + 夜空グラデーション |
| 02 | オンボーディング | 初回のみ | コンセプト説明、スキップ可 |
| 03 | ホーム（記録あり） | コア | 成長ビジュアル + 今日の記録入力CTA |
| 04 | ホーム（記録なし・Empty） | コア | 「今日はどんな日でした？」やさしいプロンプト |
| 05 | 気分スタンプ選択 | 記録フロー | テキストなしで完了可能なフロー |
| 06 | テキスト入力 | 記録フロー | 3行制限UI、自動メタデータ（天気・時刻） |
| 07 | 記録完了演出 | 記録フロー | 全画面アニメーション |
| 08 | 過去の記録（カレンダー） | 振り返り | 記録日にビジュアルマーク |
| 09 | 過去の記録（タイムライン） | 振り返り | リスト形式 |
| 10 | 記録詳細 | 振り返り | 日付・天気・気分・テキスト |
| 11 | 設定 | サブ | 通知・生体認証・テーマ |
| 12 | 通知設定 | サブ | ジェントル通知の時間設定 |

---

## Wireframe File

`small-good-app.pen`（同ディレクトリ内）
