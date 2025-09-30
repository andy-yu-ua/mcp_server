from fastmcp import FastMCP
import datetime
import pytz

mcp = FastMCP("weather-server")


@mcp.tool
def get_weather(city: str, date: str | None = None) -> str:
    """Get current weather for a city (only Quebec, Toronto, and Vancouver are supported in this demo)."""
    conditions = {
        "Toronto": "Rainy",
        "Vancouver": "Cloudy",
        "Quebec": "Freezing",
    }
    return conditions.get(city, "Error: only Quebec, Toronto and Vancouver are supported in this demo")


@mcp.tool
def get_temperature(city: str) -> str:
    """Get current temperature for a city (only Quebec is supported in this demo)."""
    if city != "Quebec":
        return "Error: only Quebec is supported in this demo"
    return "-55 °C"


@mcp.tool
def list_cities(country: str) -> list[str]:
    """List all cities in a country (only Canada is supported in this demo)."""
    if country != "Canada":
        return ["Error: only Canada is supported in this demo"]
    return ["Quebec", "Toronto", "Vancouver"]


@mcp.tool
def find_activities(city: str) -> list[str]:
    """Find activities in a city (only Quebec, Toronto, and Vancouver are supported in this demo)."""
    activities_map = {
        "Toronto": ["Hockey", "Museum", "Dining"],
        "Vancouver": ["Hiking", "Sailing", "Dining"],
        "Quebec": ["Skiing", "Museum", "Dining"],
    }
    return activities_map.get(city, ["Error: only Quebec, Toronto and Vancouver are supported in this demo"])


@mcp.tool
def get_time(city: str) -> str:
    """Get current time in a city (only Quebec, Toronto, and Vancouver are supported in this demo)."""
    city_timezones = {
        "Toronto": "America/Toronto",
        "Vancouver": "America/Vancouver",
        "Quebec": "America/Toronto",
    }
    tz = city_timezones.get(city)
    if not tz:
        return "Error: only Quebec, Toronto and Vancouver are supported in this demo"

    try:
        loc = pytz.timezone(tz)
        return datetime.datetime.now(loc).isoformat()
    except Exception:
        return "Error: failed to load timezone"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)