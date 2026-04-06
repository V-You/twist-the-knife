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
def get_twist_the_knife_skill() -> str:
    """Return the twist-the-knife skill instructions."""
    return twist_the_knife()


@mcp.tool()
def get_roast_my_idea_skill() -> str:
    """Return the roast-my-idea skill instructions."""
    return roast_my_idea()


def main() -> None:
    mcp.run()

if __name__ == "__main__":
    main()