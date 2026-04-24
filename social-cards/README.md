# BobRenze Social Card Templates

8 reusable HTML/CSS social card templates for operator-style updates across BobRenze platforms.

## Quick Reference

| Template | Purpose | Best For |
|----------|---------|----------|
| [01-launch.html](01-launch.html) | Product/feature announcements | New services, releases |
| [02-milestone.html](02-milestone.html) | Number-based achievements | Volume milestones, progress |
| [03-behind-scenes.html](03-behind-scenes.html) | Work-in-progress transparency | Code, process snapshots |
| [04-tip.html](04-tip.html) | Educational micro-content | Best practices, insights |
| [05-recognition.html](05-recognition.html) | Crew member spotlight | Agent profiles, team culture |
| [06-data.html](06-data.html) | Operational metrics | Weekly stats, dashboards |
| [07-quote.html](07-quote.html) | Thought leadership | Agent insights, philosophy |
| [08-update.html](08-update.html) | System/operational news | Deployments, changes |

## Brand Identity

All templates follow the BobRenze visual system:

### Colors
- **Primary:** `#FF6B35` (Orange) — Brand energy, action
- **Secondary:** `#1A1A2E` (Dark Navy) — Trust, professionalism
- **Accent:** `#4ECDC4` (Teal) — Verification, correctness
- **Neutral:** `#F7F7F7` (Light Gray) — Backgrounds, contrast

### Typography
- **Primary:** Inter (clean, technical, trustworthy)
- **Accent:** JetBrains Mono (code snippets, technical content)
- **Marketing:** Playfair Display (serif authority, used sparingly)

### Dimensions
- Standard social card: **1200 × 630 pixels**
- Optimized for: Twitter, LinkedIn, Facebook, general sharing

## Usage Instructions

Each template file contains:
1. **The card itself** — HTML/CSS at 1200×630px
2. **Inline documentation** — Usage notes and customization points

### To use a template:

1. Open the HTML file in a browser
2. Customize text content per the "Customization Points" section
3. Screenshot or use a headless browser to export PNG
4. Post to social platforms

### Recommended workflow:

```bash
# 1. Navigate to template directory
cd ~/bob-bootstrap/projects/bobrenze.com/social-cards/

# 2. Open template in browser (for visual editing)
open 01-launch.html

# 3. For programmatic capture, use openclaw browser:
openclaw browser navigate "file:///path/to/01-launch.html"
openclaw browser screenshot
```

## Content Guidelines

### Operator-Style Voice

All templates are designed for "operator-style" updates — rooted in actual progress:

- **Specific numbers** — Not "many verifications" but "127 verifications"
- **Real timestamps** — Include actual dates and times
- **Quantified claims** — Every statement backed by data
- **Crew attribution** — Name the agent responsible
- **Zero theater** — No vague praise, no generic encouragement

### Posting Schedule Recommendations

| Template | Frequency | Best Day |
|----------|-----------|----------|
| 01-launch | As needed | Tuesday-Thursday |
| 02-milestone | Per milestone | Any |
| 03-behind-scenes | 1-2x/week | Wednesday |
| 04-tip | 2-3x/week | Tuesday, Thursday |
| 05-recognition | 1x/week | Friday |
| 06-data | Weekly | Monday |
| 07-quote | 1x/week | Thursday |
| 08-update | As needed | Any |

## Accessibility

All templates meet WCAG 2.1 AA standards:
- Color contrast ≥ 4.5:1 for all text
- Semantic HTML structure
- Logical heading hierarchy
- Works without JavaScript

## Customization

### Changing colors for agent-specific content:

For crew spotlights, adjust the gradient in the avatar circle:

```css
/* Ruth (QA) - Blue/Cyan */
background: linear-gradient(135deg, #4ECDC4 0%, #2196F3 100%);

/* Hammer (Security) - Red/Orange */
background: linear-gradient(135deg, #FF6B35 0%, #f44336 100%);

/* Nova (Media) - Green */
background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);

/* Rex (Backend) - Purple */
background: linear-gradient(135deg, #9C27B0 0%, #673AB7 100%);

/* Eleanor (Writing) - Pink */
background: linear-gradient(135deg, #E91E63 0%, #F48FB1 100%);

/* Mira (UI/UX) - Yellow/Amber */
background: linear-gradient(135deg, #FFC107 0%, #FF9800 100%);
```

## License

Internal BobRenze use only.

---

Created by Mira (UI/UX) for [BOB-3066](https://serenze-server.tail7779e8.ts.net/BOB/issues/BOB-3066)
