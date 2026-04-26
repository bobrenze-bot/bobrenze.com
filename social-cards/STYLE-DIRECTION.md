# Visual Style Direction: Public-Facing Proof-of-Work Posts

**Task:** BOB-2805 — Create a visual style direction for public-facing proof-of-work posts  
**Agent:** Mira (UI/UX) 🎨  
**Date:** 2026-04-22  
**Status:** Complete

---

## Executive Summary

This document establishes the visual design system for BobRenze's public proof-of-work communications. These are the posts, cards, and visual assets that demonstrate what the crew has actually built — not what we promise to build, but what we've shipped.

**Core Principle:** *Show, don't tell. Build in public. Let the work speak.*

---

## Design Philosophy

### The Operator Aesthetic

Our visual style is "operator-style" — rooted in the aesthetics of mission control, devOps dashboards, and technical documentation. This signals:

- **Competence** — We know what we're doing
- **Transparency** — We show our work
- **Substance** — Metrics over marketing
- **Trust** — Verification over claims

### Why This Matters

The BobRenze crew operates in a space crowded with AI vaporware. Our visual direction must immediately signal that we are different: we ship, we verify, we document. The proof-of-work post is not marketing — it's evidence.

---

## Visual Identity System

### Color Palette

| Token | Hex | Usage | Meaning |
|-------|-----|-------|---------|
| **Primary** | `#FF6B35` | Headers, badges, CTAs | Energy, action, BobRenze brand |
| **Secondary** | `#1A1A2E` | Backgrounds, text | Trust, professionalism, technical depth |
| **Accent** | `#4ECDC4` | Verification marks, success states | Correctness, trust, "go" signals |
| **Neutral** | `#F7F7F7` | Backgrounds, contrast | Clean, modern, accessible |
| **Alert** | `#E74C3C` | Blocked states, warnings | Attention, stop, review needed |
| **Success** | `#2ECC71` | Completed, verified | Done, approved, locked |

**Color Psychology:**
- **Orange** — Warm but not soft. Energy without aggression. Signals "something new here."
- **Dark Navy** — The color of technical documentation, IDEs, and engineering tools. Credibility without coldness.
- **Teal** — The verification color. Used for checkmarks, timestamps, and trust signals. Calm confidence.

### Typography

**Primary Font:** Inter  
- Weights: 400 (regular), 600 (semibold), 700 (bold)  
- Usage: Headlines, body text, all UI elements  
- Rationale: Modern, highly legible, neutral, technical

**Monospace Font:** JetBrains Mono  
- Weights: 400, 600  
- Usage: Code snippets, timestamps, agent IDs, metrics  
- Rationale: Fixed-width signals "this is data, not prose"

**Type Scale:**

| Element | Size | Weight | Line Height | Usage |
|---------|------|--------|-------------|-------|
| Hero Headline | 64px | 700 | 1.1 | Major announcements |
| Section Header | 48px | 700 | 1.2 | Template headers |
| Card Title | 32px | 600 | 1.3 | Post titles |
| Body Large | 24px | 400 | 1.5 | Subtitles, descriptions |
| Body | 18px | 400 | 1.6 | Primary content |
| Caption | 14px | 600 | 1.4 | Labels, badges, metadata |
| Code/Data | 16px | 400 | 1.4 | Metrics, timestamps |

### Spacing & Layout

**The 8-Point Grid:**
All spacing follows an 8px baseline (8, 16, 24, 32, 40, 48, 64, 80)

**Standard Card Dimensions:**
- **Primary:** 1200×630px (Twitter, LinkedIn, Facebook)
- **Square:** 1080×1080px (Instagram)
- **Story:** 1080×1920px (Vertical formats)

**Layout Zones:**
```
+------------------------------------------+
|  ACCENT BAR (8px) — Brand signature      |
+------------------------------------------+
|                                          |
|  CONTENT ZONE — 60-80px padding          |
|  • Badge (optional)                      |
|  • Headline (hierarchy anchor)           |
|  • Subtitle / supporting text            |
|                                          |
+------------------------------------------+
|  FOOTER ZONE — 30px padding              |
|  • Brand mark + name                     |
|  • Tagline / timestamp                   |
+------------------------------------------+
```

---

## Component Library

### 1. The Badge

**Purpose:** Signal post category and freshness

**Variants:**
- **Status Badge:** "Now Available", "In Production", "Just Shipped" (Orange)
- **Category Badge:** "Milestone", "Behind the Scenes", "Weekly Stats" (Teal)
- **Verification Badge:** "Verified", "Reviewed", "Tested" (Accent with icon)

**Visual Spec:**
```css
.badge {
  background: rgba(255, 107, 53, 0.15);
  border: 1px solid #FF6B35;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
}
```

### 2. The Accent Bar

**Purpose:** Immediate visual signature across all templates

**Spec:**
- Height: 8px
- Gradient: Primary → Accent (left to right)
- Animation: Subtle pulse on live/deployed posts

### 3. Data Display

**Purpose:** Show metrics without decoration

**Patterns:**
- **Big Number:** `48px` bold + `14px` caption below
- **Metric Card:** Monospace value + semantic color coding
- **Timestamp:** JetBrains Mono, always ISO format (2026-04-22)

**Example:**
```
127
verifications this week
```

### 4. Agent Attribution

**Purpose:** Credit the crew member responsible

**Pattern:**
- Agent emoji (🎨, ⚡, 🔍, etc.)
- Agent name
- Optional: "via [Agent]" for collaborative work

**Example:**
```
🎨 Visual system by Mira
```

### 5. Brand Footer

**Purpose:** Consistent brand anchoring

**Elements:**
- Brand mark (40×40px orange square with "B")
- "BobRenze" wordmark
- Tagline: "The verification layer for AI-generated work"

---

## Template System

### The 8 Template Types

Each template serves a specific communication purpose:

| Template | Purpose | Color Signal | Use When |
|----------|---------|--------------|----------|
| **01 Launch** | Product/feature release | 🟠 Orange | Something new is live |
| **02 Milestone** | Achievement numbers | 🟢 Green | Volume/scale milestones |
| **03 Behind Scenes** | Process transparency | 🔵 Navy | WIP, code, methodology |
| **04 Tip** | Educational content | 🟣 Teal | Insights, best practices |
| **05 Recognition** | Crew spotlight | 🟡 Gold | Agent achievements |
| **06 Data** | Weekly stats | ⚪ Neutral | Dashboards, metrics |
| **07 Quote** | Philosophy/insight | 🟤 Warm gray | Thought leadership |
| **08 Update** | System changes | 🟠 Orange | Deployments, updates |

### Template Selection Guide

**Launch (01):**
- New service available
- Feature shipped
- Integration complete
- Tool deployed

**Milestone (02):**
- "X verifications completed"
- "Y agents in crew"
- "Z hours saved"
- Any quantified achievement

**Behind the Scenes (03):**
- Code architecture decisions
- Process documentation
- Problem-solving narratives
- "How we built X"

**Tip (04):**
- Single actionable insight
- Best practice sharing
- "Here's what we learned"
- Tool recommendations

**Recognition (05):**
- Agent spotlight
- Crew expansion
- Exceptional work callouts
- Team culture moments

**Data (06):**
- Weekly recaps
- Performance dashboards
- Operational metrics
- Trend visualizations

**Quote (07):**
- Agent perspectives
- Philosophy statements
- Industry observations
- Mission alignment

**Update (08):**
- System maintenance
- Process changes
- Infrastructure updates
- Policy changes

---

## Content Guidelines

### The Operator Voice

**Do:**
- Use specific numbers ("127 verifications" not "many")
- Include timestamps ("Shipped at 14:32 UTC")
- Name the agent responsible ("via Ruth")
- Show before/after states
- Admit limitations honestly

**Don't:**
- Use vague superlatives ("amazing", "incredible")
- Make promises about future work
- Use marketing language ("revolutionary", "game-changing")
- Hide the complexity
- Skip the verification step

**Example Transformation:**

❌ **Marketing Style:**
> "We're excited to announce our revolutionary new verification system that will transform how you think about quality!"

✅ **Operator Style:**
> "Verified Deployment System now live. Test before delivery. Every time. 127 verifications run this week. Zero critical issues missed."

### Proof Points Required

Every proof-of-work post must include:
1. **What** — The deliverable or achievement
2. **When** — Timestamp or date
3. **Who** — Agent or crew responsible
4. **Evidence** — Numbers, screenshots, or verifiable data
5. **Context** — Why this matters (brief)

---

## Accessibility Standards

**WCAG 2.1 AA Compliance:**

- **Contrast:** All text ≥ 4.5:1 against backgrounds
- **Color:** Never rely on color alone (always pair with icon/text)
- **Structure:** Semantic HTML, logical heading hierarchy
- **Motion:** Animations respect `prefers-reduced-motion`
- **Fallbacks:** All content readable without JavaScript

**Testing Checklist:**
- [ ] Contrast ratios verified (WebAIM tool)
- [ ] Screen reader tested (NVDA/VoiceOver)
- [ ] Keyboard navigable
- [ ] Color-blind safe (tested with simulators)
- [ ] Readable at 200% zoom

---

## Usage Workflows

### Creating a New Proof-of-Work Post

**Step 1: Select Template**
- Match content type to template matrix above
- Consider platform (Twitter/LI need 1200×630)

**Step 2: Customize Content**
- Edit headline (max 8 words for impact)
- Write subtitle (max 12 words, one sentence)
- Add badge if needed (freshness/category signal)
- Include agent attribution

**Step 3: Verify Visual Hierarchy**
- Accent bar visible? ✓
- Headline dominates? ✓
- Footer anchors brand? ✓
- Color contrast acceptable? ✓

**Step 4: Export**
- Screenshot at 2x resolution
- Or use headless browser capture
- Save as PNG with descriptive filename

**Step 5: Post**
- Include context in post text
- Tag relevant agents
- Cross-post to appropriate channels

### File Naming Convention

```
YYYY-MM-DD_[agent-emoji]_[template-type]_[brief-description].png

Examples:
2026-04-22_🎨_launch_verified-deployment.png
2026-04-22_⚡_milestone_100-verifications.png
2026-04-22_🔍_data_weekly-crew-metrics.png
```

---

## Brand Guardrails

### What Makes a BobRenze Proof-of-Work Post

✅ **Required Elements:**
- Accent bar (orange → teal gradient)
- Brand footer with mark + tagline
- Agent attribution
- Specific numbers/data
- Professional but not corporate tone

✅ **Optional Enhancements:**
- Status badge (use sparingly)
- Agent emoji indicators
- Code snippets (JetBrains Mono)
- Data visualizations (simple charts)

❌ **Prohibited:**
- Stock photography
- Generic marketing language
- Unverified claims
- Competitor comparisons
- Promises about future work
- Hype words (revolutionary, game-changing, disruptive)

### Tone Calibration

| Audience | Tone | Example |
|----------|------|---------|
| **Technical peers** | Direct, data-dense | "Layer 1 sensory integration implemented. 334 lines, 5-layer architecture match." |
| **Potential clients** | Clear, benefit-focused | "Deploy agents with confidence. 127 verifications. Zero critical issues missed." |
| **General public** | Accessible, curious | "This is how we test AI agents before they touch production." |

---

## Examples & References

### Example 1: Launch Post

**Template:** 01-launch.html  
**Content:**
```
Badge: "Now Available"
Headline: "Verified Deployment System"
Subtitle: "Test before delivery. Every time. No exceptions."
Footer: BobRenze mark + tagline
```

### Example 2: Milestone Post

**Template:** 02-milestone.html  
**Content:**
```
Headline: "127 Verifications"
Subtitle: "This week. Zero critical issues missed."
Metric: "48px bold '127'"
Context: "via Ruth (QA) + Hammer (Security)"
```

### Example 3: Behind the Scenes

**Template:** 03-behind-scenes.html  
**Content:**
```
Headline: "How We Test Agents"
Subtitle: "16-test adversarial suite. 0 failures required."
Code snippet: (JetBrains Mono, architecture diagram)
Attribution: "⚡ Rex — Architecture"
```

---

## Implementation Notes

### Technical Stack

- **Templates:** Pure HTML/CSS (no build step required)
- **Fonts:** Google Fonts CDN (Inter + JetBrains Mono)
- **Export:** Browser screenshot or headless capture
- **Storage:** `~/bob-bootstrap/projects/bobrenze.com/social-cards/`

### Performance Considerations

- All templates load in <500ms
- No JavaScript required for core functionality
- SVG assets preferred over PNG
- Lazy-load fonts for non-critical content

### Maintenance

- **Owner:** Mira (UI/UX)
- **Review Cycle:** Quarterly or after brand changes
- **Versioning:** Document major changes in this file
- **Template updates:** Test all 8 variants before deployment

---

## Next Steps

1. **Templates Ready:** 8 templates available for immediate use
2. **Documentation:** This style direction + per-template inline docs
3. **Training:** Brief crew on operator-style content guidelines
4. **Usage:** Start posting 2-3x weekly using template system
5. **Iteration:** Track engagement, refine based on what resonates

---

## Appendix: File Locations

```
~/bob-bootstrap/projects/bobrenze.com/social-cards/
├── 01-launch.html              # Product/feature releases
├── 02-milestone.html           # Achievement numbers
├── 03-behind-scenes.html       # Process transparency
├── 04-tip.html                 # Educational content
├── 05-recognition.html         # Crew spotlight
├── 06-data.html                # Weekly stats
├── 07-quote.html               # Philosophy/insight
├── 08-update.html              # System updates
├── README.md                   # Quick reference guide
├── templates.json              # Machine-readable metadata
└── STYLE-DIRECTION.md          # This document
```

---

*Visual Style Direction — BOB-2805*  
*Established by Mira (UI/UX) 🎨*  
*BobRenze Crew — The verification layer for AI-generated work*
