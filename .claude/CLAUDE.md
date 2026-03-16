# wireframe-skills Project

This directory contains the **wireframe** skill for AI-powered wireframe creation.

## Available Skills

- **wireframe** — Research UX trends and generate wireframes using Pencil

## Project Structure

```
wireframe-skills/
├── .claude/
│   ├── CLAUDE.md          ← this file
│   └── skills/
│       └── wireframe/
│           └── SKILL.md   ← main skill file
├── scripts/
│   ├── fetch_reddit.py    ← Reddit UX/wireframe research
│   ├── fetch_hn.py        ← Hacker News design research
│   └── fetch_qiita.py     ← Qiita JP design research
├── references/
│   ├── wireframe-principles.md   ← Core wireframe theory
│   ├── ui-patterns.md            ← UI patterns & screen templates
│   ├── pencil-guide.md           ← Pencil MCP usage guide
│   └── research-methodology.md  ← How to interpret research data
├── reports/               ← Generated reports (auto-created)
│   └── {year}/{yyyymmdd}/{hhmmss}/
│       ├── report.md
│       └── {name}.pen
└── .env                   ← QIITA_TOKEN (not committed to git)
```

## Usage

Invoke the wireframe skill by asking:
- "ワイヤーフレームを作りたい"
- "このアプリのUI設計をしてほしい"
- "Create a wireframe for a [type] app"
- "画面設計をして"

The skill will ask you questions in Japanese before starting research and design.
