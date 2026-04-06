from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Adversarial Skills")
ROOT = Path(__file__).parent


def load_skill(*parts: str) -> str:
    skill_path = ROOT.joinpath(*parts)
    return skill_path.read_text() if skill_path.exists() else "Skill not found."


@mcp.prompt()
def twist_the_knife() -> str:
    """Trigger the cynical senior architect persona."""
    return load_skill(".github", "skills", "twist-the-knife", "SKILL.md")


@mcp.prompt()
def roast_my_idea() -> str:
    """Trigger the cynical veteran project manager persona."""
    return load_skill(".github", "skills", "roast-my-idea", "SKILL.md")


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