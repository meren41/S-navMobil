from mcp.server.fastmcp import FastMCP
from app import get_joke

# MCP adını istediğin gibi değiştirebilirsin
mcp = FastMCP("joke-api-mcp")

@mcp.tool()
async def get_random_joke() -> str:
    """
    JokeAPI'yi kullanarak rastgele şaka döner.
    """
    joke = get_joke()
    return joke

if __name__ == "__main__":
    print("MCP Server başlatılıyor...")
    mcp.run(transport="stdio")
    print("MCP Server çalışıyor!")
