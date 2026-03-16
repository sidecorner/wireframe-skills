# UI Patterns & Trends Reference

## Table of Contents
1. [Current UX Trends](#current-ux-trends)
2. [Common App Screen Patterns](#common-app-screen-patterns)
3. [Common Web Screen Patterns](#common-web-screen-patterns)
4. [Navigation Patterns](#navigation-patterns)
5. [Pain Points Observed from Community Research](#pain-points-observed)
6. [Screen Inventory Templates](#screen-inventory-templates)

---

## Current UX Trends

### AI-Integrated Workflows (2024–2026)
- **Inline AI suggestions**: Autocomplete, smart defaults in forms
- **Conversational interfaces** alongside traditional UI (not replacing it)
- **AI onboarding**: Personalized setup via short Q&A instead of settings screens
- **Contextual AI actions**: "Summarize", "Improve", "Generate" buttons near content

### Simplified Navigation
- Trend toward **bottom tab bars** replacing hamburger menus on mobile
- **Progressive navigation**: Fewer top-level items, more contextual sub-navigation
- **Search-first patterns**: Search as the primary navigation method (Notion, Linear)

### Content-First Design
- **Skeleton screens** preferred over spinners — reduces perceived load time
- **Inline editing** instead of modal forms
- **Persistent context**: Users don't lose their place during actions

### Accessibility as Default
- **Large touch targets** (48dp minimum)
- **High contrast modes** baked in
- **Voice/keyboard navigation** planned from the start, not retrofitted

### Mobile-First Web Design
- **Single-column layouts** that scale up vs. multi-column that shrink
- **Thumb-friendly zones** even on desktop (bottom sheet patterns on web)

---

## Common App Screen Patterns

### Onboarding Screens
```
[Splash/Logo]
    ↓
[Value Proposition (3-5 slides or scroll)]
    ↓
[Sign Up / Log In]
    ↓
[Permissions (location, notifications, etc.)]
    ↓
[Personalization / Setup (optional)]
    ↓
[Home / Main Screen]
```

**Elements per onboarding screen:**
- 1 illustration or visual
- 1 headline (max 6 words)
- 1 supporting sentence
- Progress indicator
- Primary CTA + skip option

---

### Feed / List Screen
- Header: Title + search/filter icon
- Filter tabs (optional, horizontal scroll)
- Card list (infinite scroll or paginated)
- FAB for primary creation action
- Empty state with CTA when no items

---

### Detail Screen
- Hero image or icon
- Title + key metadata
- Primary action (Follow, Buy, Start, etc.)
- Content body
- Related items / recommendations

---

### Form / Input Screen
- Section headers grouping related fields
- Inline validation (not just on submit)
- Progress bar for multi-step
- Back + Next/Save navigation
- Sticky submit button at bottom

---

### Dashboard / Home Screen
- Greeting / context header
- Summary cards (key metrics or status)
- Quick action shortcuts
- Activity feed or recent items
- Navigation (tab bar or sidebar)

---

### Settings Screen
- Grouped sections with section headers
- Toggle switches for on/off preferences
- Chevron (>) for sub-settings pages
- Destructive section last (Log Out, Delete Account)

---

## Common Web Screen Patterns

### Landing Page
```
[Navigation bar: Logo | Links | CTA button]
[Hero: Headline + subtext + primary CTA + visual]
[Social proof: Logos or testimonials]
[Features/Benefits: 3-column grid]
[How it works: Step-by-step]
[Pricing section]
[Final CTA]
[Footer]
```

### SaaS Dashboard
```
[Left sidebar: Navigation links + workspace switcher]
[Top bar: Page title + search + user menu]
[Main content area: Metrics cards + charts + tables]
[Right panel (optional): Context or filters]
```

### E-commerce Product Page
```
[Breadcrumb navigation]
[Product images (gallery)]
[Title + rating + price]
[Variant selectors (color, size)]
[Add to cart + wishlist]
[Description tabs]
[Reviews]
[Related products]
```

### Blog / Article Page
```
[Header with category + date]
[Title + author + reading time]
[Feature image]
[Table of contents (for long articles)]
[Article body with inline CTAs]
[Share + save actions]
[Related posts]
[Comments (optional)]
```

---

## Navigation Patterns

### Mobile Navigation
| Pattern | Best For | Pros | Cons |
|---|---|---|---|
| Bottom Tab Bar | 3–5 primary sections | Always visible, thumb-friendly | Takes vertical space |
| Hamburger Drawer | 5+ sections or secondary nav | Maximizes content space | Hidden, lower discoverability |
| Top Tab Bar | Content categories (horizontal scroll) | Quick category switching | Reaches limit at 5 tabs |
| FAB + Modal | Creation-focused apps | Clear primary action | Only works with one main CTA |

### Web Navigation
| Pattern | Best For | Pros | Cons |
|---|---|---|---|
| Top Navigation Bar | Marketing / content sites | Familiar, visible | Collapses to hamburger on mobile |
| Left Sidebar | App dashboards, admin panels | Always visible, scalable | Uses horizontal space |
| Mega Menu | Large catalogs (e-commerce) | Deep navigation in one place | Complex to implement |
| Breadcrumbs | Deep hierarchies | Shows user's position | Only useful in deep navigation |

---

## Pain Points Observed

*Synthesized from community research across Reddit, HN, and Qiita:*

### For Non-Designer Founders & Indie Hackers
- **"I don't know where to start"** — Lack of a systematic approach to screen planning
- **"It looks bad but I can't explain why"** — Unable to identify specific design issues
- **"I keep redesigning the same screen"** — No wireframe phase → jumping to pixels
- **"My navigation is confusing but I don't know how to fix it"** — IA problems

### For Developers Building UIs
- **Inconsistent spacing and layout** — No grid or spacing system
- **Too many competing CTAs** — No clear primary action hierarchy
- **Navigation feels buried** — Hamburger menus for things users need constantly
- **Forms with no feedback** — Only showing errors on submit

### For UX Designers
- **Stakeholders skip wireframes** — Want to see "the real design" immediately
- **Wireframe tools are either too simple or too complex** — Gap between Figma and paper
- **Screen flows not documented** — Only individual screens, no connections
- **No empty/error states in wireframes** — Edge cases missed until development

### For Product Teams
- **Screen scope creep** — No defined screen inventory before design starts
- **Inconsistent patterns across screens** — No reusable component thinking
- **User flows not shared with engineers** — Dev re-implements logic differently

---

## Screen Inventory Templates

### Minimum Viable Screen Set (Mobile App)
1. Onboarding / Welcome
2. Sign Up / Log In
3. Home / Dashboard
4. [Core Feature] List
5. [Core Feature] Detail
6. Create / Edit Form
7. Profile / Account
8. Settings
9. Notifications (if applicable)
10. Empty State (for each major list)
11. Error / Offline State
12. Paywall / Upgrade (if applicable)

### Minimum Viable Screen Set (Web App / SaaS)
1. Landing / Marketing page
2. Sign Up
3. Log In
4. Onboarding wizard
5. Dashboard / Home
6. [Core Feature] List view
7. [Core Feature] Detail / Edit view
8. Settings
9. User Profile
10. Billing / Plan management
11. Error (404, 500)
12. Empty States
