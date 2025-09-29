# weather_mcp_server.py
from mcp.server.fastmcp import FastMCP
import os

# Create MCP server
mcp = FastMCP("weather-server")

# Define your tool
@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is snowy."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="streamable-http") # built-in HTTP server

