from pathlib import Path
from mcp.server.fastmcp import FastMCP
from bundled_skills import ROAST_MY_IDEA, TWIST_THE_KNIFE

mcp = FastMCP("Adversarial Skills")
ROOT = Path(__file__).parent
SKILLS = {
    "twist-the-knife": TWIST_THE_KNIFE,
    "roast-my-idea": ROAST_MY_IDEA,
}


def load_skill(skill_name: str, *parts: str) -> str:
    skill_path = ROOT.joinpath(*parts)
    if skill_path.exists():
        return skill_path.read_text()
    return SKILLS[skill_name]


@mcp.prompt()
def twist_the_knife() -> str:
    """Trigger the cynical senior architect persona."""
    return load_skill("twist-the-knife", ".github", "skills", "twist-the-knife", "SKILL.md")


@mcp.prompt()
def roast_my_idea() -> str:
    """Trigger the cynical veteran project manager persona."""
    return load_skill("roast-my-idea", ".github", "skills", "roast-my-idea", "SKILL.md")


@mcp.tool()
def roast_codebase() -> str:
    """Adversarial technical review of a codebase, repo, or system architecture. Finds security holes, architectural rot, and maintainability disasters. Use this for code and infrastructure, NOT for business ideas or plans."""
    return twist_the_knife()


@mcp.tool()
def roast_idea() -> str:
    """Adversarial review of a business idea, startup plan, or creative endeavor. Finds flawed assumptions, resource traps, and execution nightmares. Use this for ideas and plans, NOT for code or repos."""
    return roast_my_idea()


def main() -> None:
    mcp.run()

if __name__ == "__main__":
    main()