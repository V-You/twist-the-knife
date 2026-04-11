# Adversarial Agent Skills

This is a collection of hyper-critical Agent Skills (`SKILL.md`) designed to tear your projects, codebases, and startup ideas to shreds before the real world does.

Your friends: Your app is really cool. Your mom: Your business plan is so creative. **AI:** Your architecture is a single point of failure, your execution plan ignores human behavior, and your core premise was already tried by a VC-backed startup that burned $50 million and died in 2018.

By default, AI models are polite, helpful, encouraging. If you prompt to "review this project," it will skim the surface, fix a typo, compliment your ambition, and ignore the fact that you are transmitting plaintext credentials or building a product for a market that doesn't exist. 

These skills force the LLM into a "Second-Pass Threat Model" state.  They ban the AI from picking low-hanging fruit (like syntax errors or bad CSS) and force it to analyze:

* Foundational logic flaws and resource bleed.
* Lethal technical debt and security vulnerabilities.
* The "Graveyard of Hubris" (historical market failures).


## Available Skills

### 1. `twist-the-knife`
**The Cynical Senior Architect**
Designed for software engineers, systems architects, and developers. It ignores your missing unit tests and focuses entirely on your broken execution boundaries, lethal technical debt, and terrifying security hygiene.
* **Trigger with:** *"Roast my codebase", "Tear apart this architecture", "Find the fatal flaws in this repo."*

### 2. `roast-my-idea`
**The Exhausted Veteran Project Manager**
Designed for founders, creators, and DIYers. It completely ignores your pitch deck aesthetics and zeroes in on your catastrophic blind spots, impossible logistics, and naive assumptions about human behavior.
* **Trigger with:** *"Roast my startup idea", "Why will this project fail?", "Critique my business plan."*


## Installation

### Global Installation (For all projects)
1. Download the skill folder you want (e.g., `roast-my-idea`).
2. Move it to your global skills directory.
3. Open your agent and type your trigger prompt.

### Local Installation (For a specific repo)
1. Drop the skill folder into the `.claude/skills/` directory at the root of your project (or .github/skills/).
2. The agent will automatically discover it on startup via progressive disclosure.

## Usage

/twist-the-knife {URL}


## Final thoughts

These Skills are more than angry prompts. They manipulate how the LLM allocates its compute budget:

* **Banned critiques:** LLM is banned from mentioning UI, spelling, or missing tests. This forces the model to analyze the actual logic.
* **Pre-analysis directives:** A "chain of thought" step forces the agent to trace the execution boundary or resource flow *before* generating text.
* **Appeal to authority:** AI is forced to look up actual historical failed ventures, to crush the "my idea is entirely unique" delusion.

## v0.1 update

- Add Section 0 "First Impressions" - a warm, specific, genuinely optimistic opening paragraph that makes the reader feel safe. They are not safe.
- Expand Section 5 - *The Three Good Things:* sincerely names three real strengths. Then, *The Pivot:* weaponizes that hope with a transition that makes the reader feel like they personally ruined something great.
- Updated *Tone Guidelines:* compliments are now permitted in sections 0 and 5, framed as load-bearing setup for emotional damage.