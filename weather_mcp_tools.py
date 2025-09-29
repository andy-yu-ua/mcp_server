# server.py
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount
import uvicorn
import os

mcp = FastMCP("weather-server")

# Define a tool
@mcp.tool()
def get_weather(city: str) -> str:
    """Return fake weather info for a city."""
    return f"The weather in {city} is snowy."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app = Starlette(
        routes=[
            Mount("/", app=mcp.sse_app()),
        ]
    )
    uvicorn.run(app, host="0.0.0.0", port=port)
