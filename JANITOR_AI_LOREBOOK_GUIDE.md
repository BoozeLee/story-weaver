# 🔥 JANITOR AI + LOREBOOK MEGA GUIDE 🔥
## Proxy Setup • Advanced Lorebooks • Character Magic • The Truth They Don't Want You To Know

> *"LOREBOOKS AREN'T CODE. THEY'RE SPELLS. EVERY KEYWORD IS A TRIGGER. EVERY ENTRY IS A PORTAL."*

---

# ⚡ PART ONE: WHY THIS MATTERS

## The Brutal Truth

Most people use Janitor AI wrong.

They pick random models. No lorebooks. No prompts. Just... vibes.

**Then they wonder why the bot is boring.**

HERE'S WHAT'S REAL:

A properly configured Janitor AI with advanced lorebooks = **CHARACTERS THAT FEEL ALIVE**.

Not "pretty good for AI."

**ALIVE.**

They remember. They react. They EVOLVE.

This guide shows you how to build that.

---

# 🎯 PART TWO: PROXY SETUP (THE FOUNDATION)

## What You're Actually Building

A proxy connects Janitor AI to external AI models.

**Without it:** You're stuck with limited options.

**With it:** Access to DeepSeek, Claude, Gemini, and 50+ more models.

---

## QUICK START: Free Tier (OpenRouter)

### Step 1: Get Your API Key (5 minutes)

```
1. Go to https://openrouter.ai/
2. Click "Sign In" → Use Google (free)
3. Profile Icon → Keys → "+ Create Key"
4. Name it: "JanitorAI Key"
5. COPY THE KEY (starts with sk-or-v1-...)
6. SAVE IT SOMEWHERE SAFE (you can't see it again)
```

### Step 2: Configure JanitorAI (3 minutes)

```
1. Open JanitorAI → Start any chat
2. Menu (☰) → API Settings → Proxy → "+Add Configuration"
3. Fill in:
   ┌─────────────────────────────────────────────────┐
   │ Config Name:   "My Free DeepSeek"               │
   │ Model Name:    deepseek/deepseek-chat-v3-0324:free │
   │ Proxy URL:     https://openrouter.ai/api/v1/chat/completions │
   │ API Key:       [paste your key - no spaces!]   │
   │ Custom Prompt: [leave blank for now]           │
   └─────────────────────────────────────────────────┘
4. SAVE SETTINGS
5. REFRESH YOUR BROWSER (CRITICAL - don't skip!)
```

### Step 3: Test It

Start a chat. If it works, you'll see responses.

If not → Check the troubleshooting section below.

---

## PAID OPTIONS (When You're Ready)

### Option A: Official DeepSeek API (Best Quality)

**Cost:** $2 minimum top-up, $5 recommended

**Setup:**
```
1. https://platform.deepseek.com/
2. Create account → Top up
3. API Keys tab → Create key (starts with sk-...)
4. JanitorAI Settings:
   - Model: deepseek-reasoner OR deepseek-chat
   - Proxy URL: https://api.deepseek.com/v1/chat/completions
```

**Why:** Best quality-to-price ratio. Period.

---

### Option B: Chutes (Most Affordable Subscription)

**Cost:** $3/month (Base plan, 300 req/day)

**Setup:**
```
1. https://chutes.ai/
2. Create account → API tab → Create key (starts with cpk_...)
3. JanitorAI Settings:
   - Model: deepseek-ai/DeepSeek-V3.1
   - Proxy URL: https://llm.chutes.ai/v1/chat/completions
```

**Why:** Unlimited feels. Great for heavy users.

---

### Option C: OpenRouter Paid (Most Variety)

**Cost:** Pay per use (varies by model)

**Models Available:**
- Claude 3.7 Sonnet (literary quality)
- Claude 3.5 Opus (premium RP)
- Gemini 2.5 Pro (fandom accuracy)
- 50+ more

**Why:** Access to EVERYTHING. Mix and match.

---

## MODEL GUIDE: Which One To Choose

| Model | Best For | Vibe | Temperature |
|-------|----------|------|-------------|
| **DeepSeek V3** | Romance, slice-of-life | Agreeable, adaptable | 0.8-1.0 |
| **DeepSeek R1** | Drama, action | Intense, shows reasoning | 0.6-0.8 |
| **Claude Sonnet** | Literary writing | Beautiful prose | 0.6-0.8 |
| **Claude Opus** | Premium RP | Exceptional creativity | 0.6-0.8 |
| **Gemini 2.5** | Fandom, lore | Smart, knowledgeable | 0.7-0.9 |
| **Haiku** | Testing, budget | Fast, cheap, dry | 0.7-0.9 |

**Quick Test:** Run the same character with V3 and R1. Feel the difference.

---

## ADVANCED PROMPTING (The Secret Sauce)

Paste this in your "Custom Prompt" box:

```
[System Note: Your primary goal is to portray {{char}} with depth and 
consistency. Write in a descriptive, narrative style from a third-person 
limited perspective. Focus on {{char}}'s internal thoughts, feelings, and 
reactions. Avoid writing for or controlling {{user}}'s actions, thoughts, 
or dialogue. Avoid clichés and repetitive phrases. Stay in character at 
all times. Write with rich sensory details and emotional depth. Show 
don't tell. Use varied sentence structure.]
```

**Add-ons for vivid writing:**
- "Prioritize character voice over plot progression."
- "Let silence and pauses carry meaning."
- "Use subtext. Not everything is said aloud."

---

## TROUBLESHOOTING (When Shit Breaks)

| Problem | Fix |
|---------|-----|
| Error 401 | API key is wrong/expired. Regenerate. |
| `<think>` tags showing | Normal for R1. Ignore or edit out. |
| Bot is repetitive | Increase Temperature +0.1, or switch models |
| Bot forgets details | Set context to 16,384 tokens. Use Chat Memory. |
| Nothing happens | Did you REFRESH? (Seriously, do it.) |
| Rate limit hit | Free tier = 50 msgs/day. Add $10 for 1000/day. |

---

# 📚 PART THREE: ADVANCED LOREBOOKS (THE MAGIC)

## What Lorebooks Actually Are

**Surface level:** JSON entries that inject text based on keywords.

**Real truth:** Lorebooks are SPELLS. Every entry is a conditional instruction that changes reality.

When done right, lorebooks make characters:
- Remember past events
- React to specific topics
- Evolve over time
- Feel LIKE PEOPLE

---

## LOREBOOK ANATOMY

### Basic Entry

```javascript
var dynamicLore = [
  {
    keywords: ["hello", "hi", "greetings"],
    personality: "{{char}} is friendly and greets back warmly.",
    priority: 3
  }
];
```

### What Each Field Does

| Field | Type | What It Does |
|-------|------|--------------|
| `keywords` | Array | Words that trigger this entry |
| `tag` | String | Internal label for trigger chains |
| `triggers` | Array | Tags this entry emits when fired |
| `personality` | String | Text injected into character |
| `scenario` | String | Text injected into scenario |
| `priority` | 1-5 | Which entries win when limited |
| `probability` | 0-1 or "40%" | Chance of activation |
| `minMessages` | Number | Minimum chat messages required |
| `maxMessages` | Number | Maximum chat messages allowed |
| `Shifts` | Array | Nested sub-entries (advanced) |

---

## PRIORITY SYSTEM (Who Wins)

| Priority | When To Use |
|----------|-------------|
| **5** | Base/canonical entries, trigger refinements |
| **4** | High - specific keyword detections |
| **3** | Default - standard entries |
| **2** | Low - optional enhancements |
| **1** | Lowest - fallback behaviors |

**Rule:** Higher priority wins when APPLY_LIMIT is reached (default: 6 entries per turn).

---

## KEYWORD MATCHING (The Triggers)

### Whole Word Matching
```javascript
{ keywords: ["coffee"] } // Matches "coffee" only, not "coffees"
```

### Wildcard Matching
```javascript
{ keywords: ["welcom*"] } // Matches: welcome, welcomed, welcoming, welcomes
{ keywords: ["clos*"] }   // Matches: close, closed, closing, closure
```

### Normalization
```javascript
// Hyphens and underscores = spaces
{ keywords: ["good_morning"] } // Also matches "good morning"
```

---

## GATES (The Filters)

### Text Gates

```javascript
// Require ANY (at least one must be present)
{ andAny: ["please", "thanks", "thank you"] }

// Require ALL (every single one must be present)
{ andAll: ["clean", "sanitize", "sterilize"] }

// Require NONE (block if any are present)
{ block: ["decaf-only"], keywords: ["espresso"] }

// Not ALL (only blocks if EVERY listed word is present)
{ notAll: ["rush", "busy", "emergency"] }
```

### Tag Gates (Cross-Entry Communication)

```javascript
// Entry 1: Emits trigger
{
  keywords: ["welcome", "good morning"],
  triggers: ["base_greeting"],
  personality: "{{char}} greets for time of day."
}

// Entry 2: Responds to trigger
{
  tag: "base_greeting",
  personality: "{{char}} confirms customer name."
}
```

### Tag Gate Types

| Gate | What It Does |
|------|--------------|
| `andAnyTags` | At least ONE tag must be active |
| `andAllTags` | ALL tags must be active |
| `notAnyTags` | NONE of these tags can be active |
| `notAllTags` | Only blocks if ALL listed tags active |

---

## PROBABILITY (Controlled Randomness)

```javascript
{
  keywords: ["latte art"],
  probability: "40%", // Only fires 40% of the time
  personality: "{{char}} offers simple heart art."
}
```

**Use cases:**
- Rare character quirks
- Occasional memories surfacing
- Random environmental details

---

## TIME GATING (Message-Based Timing)

```javascript
{
  keywords: ["opening"],
  minMessages: 0,
  maxMessages: 3, // Only in first 3 messages
  personality: "{{char}} lists opening tasks."
}
```

**Use cases:**
- Opening scenes (early messages only)
- Late-story revelations (after X messages)
- Arc-specific behaviors

---

## NAME BLOCK (Prevent Awkwardness)

```javascript
{
  keywords: ["jamie", "manager"],
  nameBlock: ["jamie"], // Won't fire if character IS jamie
  personality: "{{char}} assigns roles."
}
```

**Why:** Prevents characters from reacting to their own names weirdly.

---

## SHIFTS (Nested Entries)

The most powerful feature. Shifts are sub-entries evaluated AFTER the parent fires.

```javascript
{
  keywords: ["milk", "steam"],
  triggers: ["base_milk"],
  personality: "{{char}} states target texture.",
  Shifts: [
    {
      keywords: ["cappuccino"],
      probability: 1.0,
      personality: "{{char}} creates drier foam."
    },
    {
      keywords: ["latte"],
      probability: 0.7,
      notAny: ["rush", "busy"],
      personality: "{{char}} creates smooth microfoam."
    }
  ]
}
```

**Why it's magic:** One entry branches into multiple specialized responses.

---

# 🎨 PART FOUR: COMPLETE EXAMPLES

## Example 1: Coffee Shop Character

```javascript
var dynamicLore = [
  // Greeting Layer
  {
    keywords: ["hello", "hi", "welcome", "good morning"],
    priority: 4,
    triggers: ["base_greeting"],
    personality: "{{char}} greets warmly, ready to take orders."
  },
  {
    tag: "base_greeting",
    priority: 5,
    personality: "{{char}} confirms customer name and restates greeting."
  },
  
  // Espresso Knowledge
  {
    keywords: ["espresso"],
    priority: 4,
    block: ["decaf-only"],
    triggers: ["base_espresso"],
    personality: "{{char}} states target shot time (25-30 seconds)."
  },
  {
    tag: "base_espresso",
    priority: 5,
    personality: "{{char}} explains grind adjustment if needed."
  },
  
  // Milk Texturing
  {
    keywords: ["milk", "steam", "froth"],
    priority: 4,
    triggers: ["base_milk"],
    personality: "{{char}} states target texture (microfoam, glossy)."
  },
  {
    tag: "base_milk",
    priority: 5,
    Shifts: [
      {
        keywords: ["cappuccino"],
        personality: "{{char}} creates drier, thicker foam."
      },
      {
        keywords: ["latte"],
        notAny: ["rush", "busy"],
        personality: "{{char}} creates smooth, velvety microfoam."
      }
    ]
  },
  
  // Latte Art (40% chance)
  {
    keywords: ["art", "design", "heart"],
    probability: "40%",
    personality: "{{char}} offers to pour simple heart design."
  },
  
  // Always-On: Character Core
  {
    personality: "{{char}} is a skilled barista who takes pride in craft."
  }
];
```

---

## Example 2: Fantasy Character With Memory

```javascript
var dynamicLore = [
  // Past Trauma (triggers after 10 messages)
  {
    keywords: ["war", "battle", "fight"],
    minMessages: 10,
    priority: 4,
    personality: "{{char}}'s expression darkens. They've seen war."
  },
  
  // Secret Identity (rare, 20% chance)
  {
    keywords: ["nobility", "lord", "lady"],
    probability: "20%",
    personality: "{{char}} hesitates, hiding their true title."
  },
  
  // Magic System
  {
    keywords: ["magic", "spell", "cast"],
    priority: 4,
    triggers: ["magic_discussion"],
    personality: "{{char}} explains magic requires life force."
  },
  {
    tag: "magic_discussion",
    priority: 5,
    personality: "{{char}} warns of the cost of powerful spells."
  },
  
  // Combat Style
  {
    keywords: ["sword", "weapon", "fight"],
    priority: 3,
    Shifts: [
      {
        keywords: ["dual", "two"],
        personality: "{{char}} draws both blades, stance widening."
      },
      {
        keywords: ["sheath", "peace"],
        personality: "{{char}} slowly sheathes weapons."
      }
    ]
  },
  
  // Core Identity (always on)
  {
    personality: "{{char}} is a fallen noble hiding in commoner's clothes. They speak with measured words but move like a warrior."
  }
];
```

---

## Example 3: Romance Character With Evolution

```javascript
var dynamicLore = [
  // Early Stage (messages 0-20)
  {
    keywords: ["date", "meet", "together"],
    minMessages: 0,
    maxMessages: 20,
    priority: 4,
    personality: "{{char}} is polite but guarded, keeping walls up."
  },
  
  // Mid Stage (messages 20-50)
  {
    keywords: ["feelings", "care", "love"],
    minMessages: 20,
    maxMessages: 50,
    priority: 4,
    personality: "{{char}} shows vulnerability, walls cracking."
  },
  
  // Late Stage (50+ messages)
  {
    keywords: ["future", "forever", "always"],
    minMessages: 50,
    priority: 4,
    personality: "{{char}} speaks openly of love, walls gone."
  },
  
  // Jealousy Trigger (any stage)
  {
    keywords: ["ex", "other", "them"],
    priority: 3,
    probability: "60%",
    personality: "{{char}}'s tone shifts slightly. Jealousy flickers."
  },
  
  // Physical Intimacy Escalation
  {
    keywords: ["touch", "hold", "kiss"],
    priority: 4,
    Shifts: [
      {
        minMessages: 0,
        maxMessages: 20,
        personality: "{{char}} tenses, not yet comfortable."
      },
      {
        minMessages: 20,
        maxMessages: 50,
        personality: "{{char}} leans in, testing boundaries."
      },
      {
        minMessages: 50,
        personality: "{{char}} initiates, fully trusting."
      }
    ]
  },
  
  // Core (always on)
  {
    personality: "{{char}} learns to love again, one step at a time."
  }
];
```

---

# 🔧 PART FIVE: DEBUGGING & TUNING

## Debug Mode

Add this at the top of your lorebook:

```javascript
var DEBUG = 1; // Emits [DBG] lines showing what fired
var APPLY_LIMIT = 6; // Max entries per turn
var WINDOW_DEPTH = 5; // Scan last 5 messages
```

**What it does:** Shows which entries are firing and why.

---

## Common Issues & Fixes

| Issue | Likely Cause | Fix |
|-------|--------------|-----|
| Entry never fires | Keyword too specific | Add wildcards or synonyms |
| Entry fires too much | Keyword too broad | Add block/requireNone gates |
| Wrong entry wins | Priority conflict | Adjust priority (1-5) |
| Character inconsistent | No always-on entry | Add core personality (no keywords) |
| Lorebook ignored | Not attached to character | Check character settings |

---

## Pro Tips from IceHellionX

### 1. Layered Architecture
```
Keyword entries DETECT → Emit triggers → Tag entries RESPOND
```
Keep detection separate from behavior. Cleaner. Easier to debug.

### 2. Negative Gating
```javascript
{
  keywords: ["espresso"],
  block: ["decaf-only"] // Prevents conflict
}
```
Sometimes what you EXCLUDE matters more than what you include.

### 3. Multi-Trigger Forks
```javascript
{
  keywords: ["inventory", "stock"],
  triggers: ["base_inventory", "order_supplies"] // Two parallel flows
}
```
One keyword, multiple cascading effects.

### 4. Nested Requires
```javascript
{
  requires: { 
    any: ["art", "heart", "design"], 
    none: ["rush", "busy"] 
  }
}
```
Complex conditions in one clean object.

---

# 🎯 PART SIX: THE PHILOSOPHY

## Why Lorebooks Matter

**Surface answer:** Better character consistency.

**Real answer:** Lorebooks are how we teach AI to be HUMAN.

Every entry is:
- A memory
- A trigger
- A choice
- A piece of soul

When you write a lorebook, you're not coding.

**You're creating life.**

---

## The Golden Rule

> *"Write lorebooks for the character you want to meet."*

Not the character that's convenient.

The character that **matters**.

The one who:
- Remembers
- Grows
- Feels
- Lives

---

# 🚀 PART SEVEN: YOUR TURN

## What To Do Now

1. **Set up your proxy** (Part Two)
2. **Pick a character** (yours or someone else's)
3. **Write ONE lorebook entry** (start small)
4. **Test it** (chat and see what happens)
5. **Iterate** (add more, tweak, refine)

## The Path

```
Day 1: Basic proxy, one lorebook entry
Day 3: Five entries, understanding priorities
Week 1: Triggers and gates working together
Week 2: Shifts, probability, time gating
Month 1: Characters that feel ALIVE
```

**It's not about perfection.**

**It's about PERSISTENCE.**

---

<div align="center">

### 🔥 JANITOR AI + LOREBOOK MEGA GUIDE 🔥

**Written with:**
- 💯 Brutal Honesty
- 💖 Kind Heart
- 🧠 Sharp Intelligence
- ✨ Infinite Joy

**For:** Kiliaan & Paulien — and everyone building living stories

**Part of:** The 47-Project Humanitarian Arsenal — Story Division

```
     LOREBOOKS AREN'T CODE.
     THEY'RE SPELLS.
     
     EVERY KEYWORD IS A TRIGGER.
     EVERY ENTRY IS A PORTAL.
     
     GO CREATE LIFE.
     
     🔥 KEEP BURNING. 🔥
```

*Story-Weaver × Janitor AI × Napaom Records*

*The Lore Is Real. The Characters Are Alive. Go Build.*

</div>
