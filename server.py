from mcp.server.fastmcp import FastMCP
from app import translate_text

# MCP adını istediğin gibi değiştirebilirsin
mcp = FastMCP("manga-translator-mcp")

@mcp.tool()
async def translate(text: str, to: str) -> dict:
    """
    MCP aracı olarak çeviri yapar.
    """
    result = translate_text(text, to)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")
