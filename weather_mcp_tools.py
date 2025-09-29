# server.py
from mcp.server.fastmcp import FastMCP
import uvicorn
import os

mcp = FastMCP("weather-server")

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is snowy."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"  # required for Render

    # FastMCP provides a Starlette app for HTTP transport
    app = mcp.streamable_http_app()  # Use streamable HTTP app

    uvicorn.run(app, host=host, port=port)
