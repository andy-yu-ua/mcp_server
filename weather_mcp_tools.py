# server.py
from mcp.server.fastmcp import FastMCP
from mcp.server.websocket import websocket_server
mcp = FastMCP("weather-server")

# Define a tool
@mcp.tool()
def get_weather(city: str) -> str:
    """Return fake weather info for a city."""
    return f"The weather in {city} is sunny."

if __name__ == "__main__":
    mcp.run(transport="sse", mount_path="/mcp")
