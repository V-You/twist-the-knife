from mcp.server.fastmcp import FastMCP
from pathlib import Path

# Initialize the server
mcp = FastMCP("Adversarial Skills")

# Read the SKILL.md file
skill_path = Path(".github/skills/twist-the-knife/SKILL.md")
skill_content = skill_path.read_text() if skill_path.exists() else "Skill not found."

@mcp.prompt()
def twist_the_knife() -> str:
    """Trigger the cynical senior architect persona."""
    return skill_content

if __name__ == "__main__":
    mcp.run()