# tools/mcp_tools.py
from langchain.tools import Tool
import requests

# 🌍 1. Geolocation tool using OpenStreetMap Nominatim
def get_geo_location(address: str) -> str:
    try:
        url = f"https://nominatim.openstreetmap.org/search"
        params = {
            "q": address,
            "format": "json",
            "limit": 1
        }
        headers = {
            "User-Agent": "LangChain-Agent/1.0"
        }

        res = requests.get(url, params=params, headers=headers)
        data = res.json()

        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            return f"Coordinates for '{address}':\nLatitude: {lat}, Longitude: {lon}"
        else:
            return f"No coordinates found for '{address}'."

    except Exception as e:
        return f"Error: {str(e)}"

geo_lookup_tool = Tool.from_function(
    get_geo_location,
    name="get_geo_location",
    description="Get GPS coordinates (lat/lon) for any given address using OpenStreetMap"
)

# (Optional) 📝 Also add blog search tool here if not already
def search_blog(query: str) -> str:
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        res = requests.get(url)
        data = res.json()
        return data.get("AbstractText") or "No summary found."
    except Exception as e:
        return f"Error during blog search: {str(e)}"

blog_lookup_tool = Tool.from_function(
    search_blog,
    name="search_blog",
    description="Look up customer-related blog or topic summaries"
)

# Export as list for registration
mcp_tools = [geo_lookup_tool, blog_lookup_tool]
