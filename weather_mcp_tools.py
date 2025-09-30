from fastmcp import FastMCP

mcp = FastMCP("weather-server")

@mcp.tool
def get_weather(city: str) -> str:
    """Get Current Weather for a given city"""
    return f"The weather in {city} is snowy."

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)