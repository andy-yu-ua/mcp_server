# server.py
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.responses import JSONResponse
import uvicorn
import os

mcp = FastMCP("weather-server")

# Define your tool
@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is snowy."

# Route for OpenAI to fetch tool list
async def tool_list_endpoint(request):
    return JSONResponse(mcp.tool_list())  # returns the JSON OpenAI expects

# Build ASGI app
app = Starlette(
    routes=[
        Mount("/", app=mcp.streamable_http_app()),        # MCP HTTP app for tool calls
        Route("/.well-known/mcp.json", tool_list_endpoint)  # Tool list endpoint
    ]
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)