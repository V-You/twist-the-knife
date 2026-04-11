# Adversarial Reviewer

This is a collection of **hyper-critical Agent Skills** (`SKILL.md`) designed to tear your projects, codebases, and startup ideas to shreds before the real world does.

**Your friends:** Your app is really cool. **Your mom:** Your business plan is so creative. **Your agent:** This architecture is one single point of failure. Your execution plan ignores human behavior, and your core premise was already tried by a VC-backed startup that burned $50 million and died in 2018.

**By default, AI models are polite**, helpful, encouraging. If you prompt to "review this project," it will skim the surface, fix a typo, compliment your ambition, and ignore the fact that you are transmitting plaintext credentials or building a product for a market that doesn't exist. 

**These Skills are the opposite.** They force the LLM into a "Second-Pass Threat Model" state. They ban the AI from picking low-hanging fruit (like syntax errors or bad CSS) and force it to analyze:

* Foundational logic flaws and resource bleed.
* Lethal technical debt and security vulnerabilities.
* The "Graveyard of Hubris" (historical market failures).


## Available Skills

### 1. `roast-my-idea`
**The Exhausted Veteran Project Manager**
Designed for founders, creators, and DIYers. It completely ignores your pitch deck aesthetics and zeroes in on your catastrophic blind spots, impossible logistics, and naive assumptions about human behavior.
* **Trigger with:** *"Roast my startup idea", "Why will this project fail?", "Critique my business plan"*, or slash-command URL.

### 2. `twist-the-knife`
**The Cynical Senior Architect**
Designed for software engineers, systems architects, and developers. It ignores your missing unit tests and focuses entirely on your broken execution boundaries, lethal technical debt, and terrifying security hygiene.
* **Trigger with:** *"Roast my codebase", "Tear apart this architecture", "Find the fatal flaws in this repo"*, or slash-command URL.

## Installation

### GitHub/Cloudflare CI/CD (recommended)
- See [Overview how to do this via Obot.ai](https://www.linkedin.com/pulse/how-make-your-skills-go-viral-cicd-pipeline-brain-stefan-laetzer-adlae)
- (Clone repo first, to be in control of auth)

### Global

1. Installation for all projects on local machine:
2. Download the Skills from the repo's `.github/skills` folder
3. Move it to your global skills directory.

### Project

1. Installation for a specific project on local machine:
2. Download the Skills from the repo's `.github/skills` folder
3. Move it to your local skills directory
    - Claude Code: `.claude/skills/`
    - VS Code: `.github/skills/`
    - ...

## Usage

When the slash commands below are used, the client should start the MCP server automatically (VS Code behavior). If this does not happen, start the MCP server manually, then:

`/roast-my-idea` {URL}

`/twist-the-knife` {URL}

Or use the trigger keywords (see above).

## Notes

These Skills manipulate how the LLM allocates its compute budget:

* **Banned critiques:** LLM won't mention UI, spelling, or missing tests. Forces the model to analyze the actual logic.
* **Pre-analysis:** Traces the execution boundary or resource flow *before* response is generated.
* **Appeal to authority:** AI finds historical failed ventures, to crush the "my idea is unique" delusion.
* **Compliments** are banned via *Tone Guidelines*, except as load-bearing setup for emotional damage, in `/twist-the-knife` Skill:
    - Section 0 adds a warm, specific, genuinely optimistic opening paragraph that makes the user feel safe.
    - Section 5 sincerely names three real strengths to incite hope for a biased review. Weaponizes that hope to makes the user feel like they personally ruined something great.