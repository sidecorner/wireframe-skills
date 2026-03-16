# Pencil Wireframe Creation Guide

## Overview

This guide explains how to create wireframes using the Pencil MCP tool within the wireframe-skills project. All wireframes are output as `.pen` files inside `reports/{year}/{yyyymmdd}/{hhmmss}/`.

---

## Pencil Tool Workflow

### 1. Initialize the Document

Always start by opening a new `.pen` file in the correct reports directory:

```
mcp__pencil__open_document("reports/{year}/{yyyymmdd}/{hhmmss}/{filename}.pen")
```

Example:
```
mcp__pencil__open_document("reports/2026/20260316/143022/todo-app.pen")
```

### 2. Load Guidelines

Before designing, load the appropriate guideline for the platform:

```
mcp__pencil__get_guidelines("mobile-app")   # for iOS/Android apps
mcp__pencil__get_guidelines("web-app")      # for web applications
mcp__pencil__get_guidelines("landing-page") # for marketing pages
```

### 3. Get a Style Guide

For wireframes, use a clean/minimal style:

```
mcp__pencil__get_style_guide_tags()
mcp__pencil__get_style_guide(["minimal", "wireframe", "clean"], "wireframe")
```

### 4. Design Screens

Use `batch_design` to create wireframe screens. For wireframes:
- Use grayscale colors only (#F5F5F5, #E0E0E0, #9E9E9E, #424242, #000000)
- Use placeholder boxes for images (fill with gray + "Image" label)
- Use real content for text when possible (not Lorem Ipsum)
- Label every screen with its name

---

## Wireframe Design Principles in Pencil

### Screen Layout Template (Mobile, 390×844px)

```
[Status Bar: 44px]
[Navigation Bar: 56px]
  - Back button (left)
  - Title (center)
  - Primary action (right)
[Content Area: flexible]
[Tab Bar: 83px] (if applicable)
[Home Indicator: 34px]
```

### Screen Layout Template (Web, 1440×900px)

```
[Top Navigation: 64px]
  - Logo (left)
  - Nav links (center)
  - CTA button (right)
[Hero / Main Content: flexible]
[Footer: 200px]
```

---

## batch_design Operation Examples

### Creating a Mobile Screen Frame

```
screen=I("canvas", {
  "type": "frame",
  "name": "01_Home Screen",
  "width": 390,
  "height": 844,
  "fill": "#FFFFFF"
})
```

### Creating a Navigation Bar

```
navbar=I(screen+"/", {
  "type": "rectangle",
  "name": "Navigation Bar",
  "x": 0, "y": 44,
  "width": 390, "height": 56,
  "fill": "#FFFFFF",
  "borderBottom": "1px solid #E0E0E0"
})
title=I(navbar+"/", {
  "type": "text",
  "name": "Nav Title",
  "content": "Screen Title",
  "x": 0, "y": 0,
  "width": 390, "height": 56,
  "textAlign": "center",
  "fontSize": 17,
  "fontWeight": "600",
  "fill": "#000000"
})
```

### Creating a Card Component

```
card=I(screen+"/", {
  "type": "rectangle",
  "name": "Card",
  "x": 16, "y": 120,
  "width": 358, "height": 96,
  "fill": "#F5F5F5",
  "borderRadius": 12
})
card_title=I(card+"/", {
  "type": "text",
  "name": "Card Title",
  "content": "Item Title",
  "x": 16, "y": 16,
  "width": 280, "height": 24,
  "fontSize": 16,
  "fontWeight": "600"
})
card_subtitle=I(card+"/", {
  "type": "text",
  "name": "Card Subtitle",
  "content": "Supporting text here",
  "x": 16, "y": 44,
  "width": 280, "height": 20,
  "fontSize": 14,
  "fill": "#757575"
})
```

### Creating a Tab Bar (Mobile)

```
tabbar=I(screen+"/", {
  "type": "rectangle",
  "name": "Tab Bar",
  "x": 0, "y": 727,
  "width": 390, "height": 83,
  "fill": "#FFFFFF",
  "borderTop": "1px solid #E0E0E0"
})
```

### Creating a Button

```
btn=I(screen+"/", {
  "type": "rectangle",
  "name": "Primary Button",
  "x": 16, "y": 740,
  "width": 358, "height": 52,
  "fill": "#000000",
  "borderRadius": 12
})
btn_label=I(btn+"/", {
  "type": "text",
  "name": "Button Label",
  "content": "Get Started",
  "x": 0, "y": 0,
  "width": 358, "height": 52,
  "textAlign": "center",
  "verticalAlign": "middle",
  "fontSize": 16,
  "fontWeight": "600",
  "fill": "#FFFFFF"
})
```

### Image Placeholder

```
img_placeholder=I(screen+"/", {
  "type": "rectangle",
  "name": "Image Placeholder",
  "x": 16, "y": 100,
  "width": 358, "height": 200,
  "fill": "#E0E0E0",
  "borderRadius": 8
})
img_label=I(img_placeholder+"/", {
  "type": "text",
  "name": "Image Label",
  "content": "[ Image ]",
  "x": 0, "y": 0,
  "width": 358, "height": 200,
  "textAlign": "center",
  "verticalAlign": "middle",
  "fontSize": 14,
  "fill": "#9E9E9E"
})
```

---

## Arranging Multiple Screens

For multi-screen wireframes, arrange screens horizontally with consistent gaps:

```
Screen 1: x=0,   y=0
Screen 2: x=430, y=0  (390px + 40px gap)
Screen 3: x=860, y=0
Screen 4: x=0,   y=900 (start new row after 3 screens)
```

Always label each screen prominently:
```
label=I("canvas", {
  "type": "text",
  "name": "Screen Label",
  "content": "01 - Home Screen",
  "x": 0, "y": -30,
  "width": 390,
  "fontSize": 14,
  "fontWeight": "700",
  "fill": "#424242"
})
```

---

## Flow Arrows

Connect screens with annotated arrows to show navigation:

```
arrow=I("canvas", {
  "type": "arrow",
  "name": "Tap → Detail",
  "from": {"nodeId": "card_node_id", "side": "right"},
  "to": {"nodeId": "detail_screen_id", "side": "left"},
  "label": "Tap card"
})
```

---

## Screenshot Validation

After creating each section of the wireframe, validate it:

```
mcp__pencil__get_screenshot()
```

Review the screenshot and adjust layout if elements overlap or spacing is off.

---

## Output Checklist

Before finalizing the wireframe, verify:
- [ ] All screens are labeled with number and name
- [ ] Navigation paths between screens are shown
- [ ] Each screen has: navigation bar, content area, appropriate bottom element
- [ ] Empty states are included for all list screens
- [ ] Error states are included for critical flows
- [ ] Primary action on each screen is visually prominent
- [ ] Annotations explain non-obvious interactions
