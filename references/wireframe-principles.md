# Wireframe Design Principles

## What is a Wireframe?

A wireframe is a schematic or blueprint that represents the skeletal framework of an app or website. It defines:
- **Layout structure** — where elements sit on the page
- **Information hierarchy** — what matters most
- **User flows** — how screens connect and how users move through the product
- **Functionality** — what each element does (without visual design)

Wireframes intentionally avoid colors, fonts, and imagery to keep focus on structure and function.

---

## Fidelity Levels

| Fidelity | When to Use | What It Shows |
|---|---|---|
| **Lo-fi** (sketch/boxes) | Early ideation, stakeholder alignment | Layout, flow, rough content areas |
| **Mid-fi** (grayscale, real content) | Design validation, user testing | Interaction patterns, content hierarchy |
| **Hi-fi** (near-final UI) | Developer handoff, final sign-off | Exact spacing, real content, interactions |

**Recommendation for AI-generated wireframes:** Start with mid-fi — enough detail to be meaningful, enough ambiguity to allow iteration.

---

## Core Wireframe Components

### 1. Navigation Patterns
- **Tab bar** (mobile): Bottom navigation for 3–5 primary sections
- **Hamburger / drawer**: Secondary or overflow navigation
- **Top navigation bar**: Context title, back button, primary action
- **Breadcrumbs**: Hierarchical position indicator (web)
- **Bottom sheet**: Contextual actions without leaving current screen

### 2. Content Blocks
- **Hero / above-the-fold**: Primary value proposition or content
- **Cards**: Repeatable content items (feed, grid, list)
- **Empty states**: What the user sees before content exists
- **Loading skeletons**: Placeholder while data fetches
- **Error states**: When something goes wrong

### 3. Input & Forms
- **Text fields**: Single-line and multi-line
- **Dropdowns / selects**: Constrained choice
- **Toggle / switch**: Binary preference
- **Date/time pickers**: Specialized input
- **Search bar**: Query input with optional filters

### 4. Actions & CTAs
- **Primary button**: One per screen — the main action
- **Secondary button**: Supporting action
- **Floating action button (FAB)**: Mobile primary action
- **Inline actions**: Within list items or cards
- **Destructive actions**: Delete, remove — always secondary or confirming

### 5. Feedback & Status
- **Toast / snackbar**: Non-blocking temporary feedback
- **Modal / dialog**: Blocking confirmation or input
- **Progress indicators**: Linear or circular
- **Badges / indicators**: Count or status signals

---

## Information Architecture Principles

### 1. Hierarchy First
Organize content from most important to least. Users scan before they read. Put the most important information where the eye lands first.

### 2. The 3-Click Rule (guideline, not gospel)
Critical information or actions should be reachable within 3 taps/clicks. More depth = more friction.

### 3. Progressive Disclosure
Show only what's needed for the current step. Reveal complexity gradually. Avoid overwhelming users with all options at once.

### 4. Consistent Patterns
Use the same interaction pattern for similar tasks. If swiping left deletes on one screen, it should delete everywhere.

### 5. Recognition over Recall
Users should recognize their options, not memorize them. Visible navigation beats hidden menus.

### 6. Forgiveness
Make it easy to undo. Destructive actions require confirmation. Navigation should allow going back.

---

## Screen Design Best Practices

### Mobile (iOS/Android)
- **Thumb zone**: Primary actions in the bottom 2/3 of the screen
- **Minimum tap target**: 44×44pt (iOS) / 48×48dp (Android)
- **One primary action per screen**: Avoid competing CTAs
- **Safe areas**: Respect notch, home indicator, and status bar
- **Gesture affordances**: Swipe, pinch, long press — make them discoverable

### Web / Responsive
- **Above-the-fold content**: The critical information visible without scrolling
- **F-pattern / Z-pattern reading**: Place key content along natural eye paths
- **Grid system**: 12-column or 4/8-column for consistent spacing
- **Breakpoints**: Design for mobile first, then expand to tablet and desktop
- **Hover states**: Every interactive element needs a hover state (web only)

---

## User Flow Design

### Flow Types
1. **Happy path**: The ideal, frictionless journey from entry to goal completion
2. **Edge cases**: Error states, empty states, permission denied, offline
3. **Onboarding flow**: First-time user experience — account creation, tutorial, permissions
4. **Conversion flow**: Sign-up, purchase, upgrade — minimize steps

### Flow Notation
- **Rectangle**: Screen / page
- **Diamond**: Decision point (yes/no, condition)
- **Arrow**: Navigation direction
- **Rounded rectangle**: Action / event
- **Cylinder**: Data store

### Common Flow Mistakes
- Missing back/cancel paths
- No empty states (what if the list is empty?)
- No error handling (what if the API fails?)
- Assuming all users complete onboarding
- Forgetting returning vs. first-time user differences

---

## Wireframe Annotation Standards

Annotations explain intent and behavior that visuals can't show:
- **Interaction notes**: "Tap to expand", "Swipe left to delete"
- **Conditional content**: "Shows only if user has completed profile"
- **Data notes**: "Pulled from user's location, defaults to 'Nearby'"
- **Error behavior**: "Shows inline error if email already registered"
- **Truncation rules**: "Max 2 lines, then '…'"
