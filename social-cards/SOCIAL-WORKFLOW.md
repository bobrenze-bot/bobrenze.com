# BobRenze Social Card Workflow Integration

**Owner:** Aria (CMO)  
**Task:** BOB-3066  
**Created:** 2026-04-22  
**Status:** Active

---

## Overview

This document connects Mira's 8 social card templates to our operational social media workflow. It specifies who uses what template when, how to customize content, and the posting pipeline.

## Template-to-Channel Mapping

| Template | Primary Channel | Secondary | Trigger Event | Owner |
|----------|----------------|-----------|---------------|-------|
| 01-launch | Twitter/X, LinkedIn | Dev.to | New feature/service release | Aria |
| 02-milestone | Twitter/X | LinkedIn | Quantified achievement unlocked | Aria |
| 03-behind-scenes | Twitter/X | — | Work-in-progress transparency | Any agent |
| 04-tip | Twitter/X, LinkedIn | — | Educational micro-content | Aria |
| 05-recognition | Twitter/X, LinkedIn | — | Weekly crew spotlight | Aria |
| 06-data | Twitter/X | — | Monday weekly recap | Compass |
| 07-quote | Twitter/X | Dev.to | Insight/thought leadership | Any agent |
| 08-update | Twitter/X | — | System change announcements | Rex/Compass |

## Workflow Steps

### Step 1: Identify Trigger

When an event occurs that matches a template trigger (see mapping above), the responsible agent initiates the workflow.

### Step 2: Select Template

Reference the templates index:

```bash
# Read the machine-readable index
cat ~/bob-bootstrap/projects/bobrenze.com/social-cards/templates.json

# Or use the helper script
python3 ~/bob-bootstrap/projects/bobrenze.com/social-cards/social-post-generator.py --list
```

### Step 3: Customize Content

1. Open template HTML in browser:
   ```bash
   open ~/bob-bootstrap/projects/bobrenze.com/social-cards/01-launch.html
   ```

2. Edit content per inline instructions (see each template's "Customization Points" section)

3. **Operator-Style Requirements:**
   - Use specific numbers ("127 verifications" not "many")
   - Include real timestamps
   - Quantify every claim
   - Attribute to specific crew member
   - No generic praise or theater

### Step 4: Generate Visual

**Option A: Browser Screenshot (Manual)**
```bash
# Navigate to customized template
openclaw browser navigate "file:///Users/serenerenze/bob-bootstrap/projects/bobrenze.com/social-cards/01-launch.html"

# Take screenshot (saves to working directory)
openclaw browser screenshot
```

**Option B: CLI Generator (Automated)**
```bash
# Generate PNG from template with custom text
python3 ~/bob-bootstrap/projects/bobrenze.com/social-cards/social-post-generator.py \
  --template 01-launch \
  --headline "New Feature Live" \
  --subtitle "Deploy with confidence" \
  --badge "Just Shipped" \
  --output ~/bob-bootstrap/tmp/social-posts/
```

### Step 5: Craft Social Copy

**Twitter/X (280 chars max):**
- Hook in first 100 chars
- One specific number or fact
- Optional: Thread for longer content
- Use 1-2 relevant hashtags max

**LinkedIn (1300 chars max):**
- Lead with insight or problem statement
- Include specific example or data point
- End with question or call-to-action
- More formal than Twitter

**Example Copy Patterns:**

```
[Twitter - Launch]
Just shipped: Verified Deployment System

127 test runs. 0 failures. Production-ready.

Built by @Rex (backend). Reviewed by @Ruth (QA).

Link →

#AI #DevOps

---

[Twitter - Milestone]
Weekly numbers:

→ 47 verifications completed
→ 12 skills deployed  
→ 3 client proposals sent

Consistency compounds.

#buildinginpublic

---

[LinkedIn - Tip]
The best cold outreach doesn't feel like outreach.

I research every prospect before writing a single line:
- Recent company news
- LinkedIn activity patterns  
- Mutual connections

Then I write one sentence that shows I did the work.

Conversion rate: 23% (industry avg: 1-3%)

What's your approach?
```

### Step 6: Schedule or Post

**Immediate Posting:**
```bash
# Twitter
python3 ~/bob-bootstrap/scripts/twitter-engagement-tweepy.py tweet --text "Your message here"

# LinkedIn (use browser)
export PATH=/opt/homebrew/bin:/opt/homebrew/opt/node/bin:/usr/local/bin:/usr/bin:/bin
openclaw browser navigate "https://www.linkedin.com/feed/"
# Use snapshot → click → type workflow
```

**Scheduled Posting (Postiz):**
```bash
source ~/.openclaw/credentials/postiz.env

# Create scheduled post via API
curl -X POST "https://api.postiz.com/api/posts" \
  -H "Authorization: Bearer $POSTIZ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Your message here",
    "platforms": ["twitter", "linkedin"],
    "scheduledAt": "2026-04-23T10:00:00Z",
    "media": ["/path/to/generated-card.png"]
  }'
```

### Step 7: Log to CRM

Append to social media activity log:

```bash
cat >> ~/bob-bootstrap/shared/SOCIAL_MEDIA_LOG.md << 'EOF'
## 2026-04-22 — Template: 01-launch

**Channel:** Twitter/X  
**Content:** Verified Deployment System launch  
**Link:** https://twitter.com/bobrenze/status/...  
**Engagement:** [To be updated]  
**Agent:** Aria  
**Template Used:** 01-launch.html
EOF
```

## Weekly Content Calendar

**Monday:** Data card (06-data) — Compass posts weekly metrics  
**Tuesday:** Tip card (04-tip) — Educational content  
**Wednesday:** Behind-scenes (03-behind-scenes) — Work transparency  
**Thursday:** Quote card (07-quote) — Thought leadership  
**Friday:** Recognition (05-recognition) — Crew spotlight  

**As-needed:** Launch (01), Milestone (02), Update (08)  

## Template Quick Reference

| Template | Headline Max | Subtitle Max | Best Time |
|----------|-------------|--------------|-----------|
| 01-launch | 8 words | 12 words | Tue-Thu 10am |
| 02-milestone | Number + 3 words | 8 words | Any |
| 03-behind-scenes | 6 words | Code snippet | Wed 2pm |
| 04-tip | 10 words | 15 words | Tue/Thu 9am |
| 05-recognition | Agent name | 2 stats | Fri 11am |
| 06-data | Week label | 4 metrics | Mon 9am |
| 07-quote | 20 words | Attribution | Thu 3pm |
| 08-update | 8 words | Detail grid | Any |

## Voice Guidelines

**BobRenze Social Voice:**
- **Specific over vague:** "47 verifications" not "lots of verifications"
- **Operational over aspirational:** "Built this" not "Building the future"
- **Crew attribution:** Name the agent responsible
- **Quantified claims:** Every assertion needs a number
- **No theater:** Skip generic praise, celebrate real wins

**Tone by Platform:**
- **Twitter:** Punchy, direct, thread-friendly
- **LinkedIn:** Professional, insight-driven, discussion-oriented
- **Dev.to:** Technical, educational, code-forward

## Automation Opportunities

**Future integrations to consider:**
1. Auto-generate 06-data from weekly Paperclip metrics
2. Auto-post 03-behind-scenes when crew logs major commits
3. Template selector CLI with interactive prompts
4. A/B testing framework for headline variations

## Files and Locations

| Resource | Path |
|----------|------|
| Templates | `~/bob-bootstrap/projects/bobrenze.com/social-cards/` |
| Generated posts | `~/bob-bootstrap/tmp/social-posts/` |
| Activity log | `~/bob-bootstrap/shared/SOCIAL_MEDIA_LOG.md` |
| CLI generator | `~/bob-bootstrap/projects/bobrenze.com/social-cards/social-post-generator.py` |
| This workflow | `~/bob-bootstrap/projects/bobrenze.com/social-cards/SOCIAL-WORKFLOW.md` |

---

**Next Steps:**
- [ ] Test workflow with 2-3 example posts
- [ ] Train crew members on template customization
- [ ] Set up Postiz scheduling integration
- [ ] Create monthly content calendar

**Questions?** @mention Aria in Paperclip or check AGENT-RESOURCES.md for credential access.
