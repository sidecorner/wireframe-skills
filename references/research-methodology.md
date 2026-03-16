# Research Methodology: Interpreting Community Data for Wireframe Design

## Overview

This guide explains how to interpret the raw data from Reddit, Hacker News, and Qiita to extract actionable wireframe design decisions.

---

## Data Sources & What They Tell You

### Reddit (r/UXDesign, r/UI_Design, r/userexperience, etc.)
**What it reveals:**
- Real user pain points in plain language ("I hate when apps...")
- Common usability patterns that frustrate users
- What users wish existed but doesn't
- Critique of specific apps/patterns (learn from named examples)

**How to weight:** High-engagement posts (score + comments × 3) indicate widespread sentiment. Look for repeated complaints across multiple posts.

**Key signals:**
- Posts tagged as "Rant" or "Frustration" → pain points to avoid
- Posts tagged as "Feedback Request" → what users need from designers
- Posts with links to specific apps → real-world examples to study

### Hacker News (HN)
**What it reveals:**
- Technical perspective on design tools and patterns
- What experienced developers/founders think about UX
- Tool trends (what's gaining traction in the builder community)
- Accessibility and performance discussions

**How to weight:** High-point stories (100+) + comment threads = strong community signal. The comments often have more insight than the story itself.

**Key signals:**
- "Show HN" posts about design tools → what people are building
- Ask HN about design decisions → community consensus on patterns
- High-comment posts → controversial topic with multiple valid perspectives

### Qiita
**What it reveals:**
- Japanese developer/designer perspective on UI/UX
- Practical tutorials indicating what people find hard to implement
- Stock count = "saved for reference" = highly practical content
- Tool comparisons from a practical implementation perspective

**How to weight:** stocks_count × 2 + likes_count = practical value signal. High-stock articles are reference material, not just interesting reads.

**Key signals:**
- "〇〇の作り方" (how to make X) → people are actively trying to build this pattern
- "比較" (comparison) → people are choosing between approaches
- "改善" (improvement) → existing implementations need fixing

---

## Synthesis Framework

### Step 1: Extract Pain Points
From `top_pain_points` (Reddit) and high-engagement posts, list the top 10 complaints related to the target app category. Group by theme:
- Navigation confusion
- Unclear information hierarchy
- Too many steps to complete core task
- Missing feedback states
- Onboarding friction

### Step 2: Extract Desired Patterns
From all sources, list what users explicitly ask for or admire:
- "I love how [App X] does..."
- "I wish this app would..."
- Articles titled "Best practices for..."

### Step 3: Extract Tool Trends
From HN and Qiita, identify what tools/patterns are gaining adoption:
- New interaction patterns (e.g., bottom sheets becoming standard)
- Emerging UI conventions (e.g., AI-first onboarding)
- Tools the target audience uses (affects design expectations)

### Step 4: Competitive Landscape
Identify apps/services mentioned repeatedly in the data:
- **Praised for UX**: Study their patterns and incorporate
- **Criticized for UX**: Explicitly avoid their mistakes
- **Industry standards**: Users expect these patterns to be followed

### Step 5: Map to Wireframe Decisions
Transform each finding into a specific wireframe decision:

| Research Finding | Wireframe Decision |
|---|---|
| "Navigation is buried in hamburger menu" | Use bottom tab bar for primary navigation |
| "Too many steps to [core action]" | Reduce [core action] to max 2 taps from home |
| "No feedback after submitting form" | Add loading state + success confirmation screen |
| "Hard to find search" | Make search bar persistent in top navigation |
| "Onboarding is too long" | Max 3 onboarding screens + skip option |

---

## Reporting Format

When writing `report.md`, structure it as:

```markdown
# Wireframe Research Report: {Service Name}
**Research Period:** {start_date} to {end_date}
**Target Platform:** {iOS / Android / Web / All}
**Target Users:** {persona description}

## Executive Summary
{2-3 sentences on key findings that drove wireframe decisions}

## Research Data Summary

### Reddit Insights
- Total posts analyzed: {n}
- Pain points identified: {n}
- Top themes: ...

### Hacker News Insights
- Total posts analyzed: {n}
- Key discussions: ...

### Qiita Insights
- Total articles analyzed: {n}
- Top practical references: ...

## Key Findings

### Pain Points (What to Avoid)
1. ...

### Desired Patterns (What to Include)
1. ...

### Trend-Based Decisions
1. ...

## Wireframe Decisions

| Screen | Decision | Based On |
|---|---|---|
| Home | Bottom tab navigation | Reddit: hamburger menus frustrate users |
| Onboarding | Max 3 screens + skip | HN: long onboarding → user drop-off |
| ... | ... | ... |

## Screen Inventory
{List of all screens in the wireframe with brief description}

## Wireframe File
See: `{filename}.pen` in this directory
```

---

## Quality Gates

Before finalizing the wireframe, verify these are addressed:

1. **Every major pain point** from research maps to a wireframe decision
2. **Onboarding flow** is clearly defined
3. **Empty and error states** are included for all data-driven screens
4. **Navigation pattern** is consistent across all screens
5. **Primary action** on each screen is clear and prominent
6. **Screen count** is realistic for MVP (avoid scope creep)
