from langchain.tools import Tool
import requests

def lookup_blog_or_location(query: str) -> str:
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        res = requests.get(url)
        data = res.json()
        return data.get("AbstractText") or "No blog summary found, try another query."
    except Exception as e:
        return f"Error during lookup: {str(e)}"

# Register tool
web_lookup_tool = Tool.from_function(
    lookup_blog_or_location,
    name="web_lookup",
    description="Search for a customer's blog and summarize it"
)
