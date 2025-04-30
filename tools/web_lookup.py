from langchain.tools import Tool
import requests

def web_search_duckduckgo(query: str) -> str:
    """
    Perform a web search using DuckDuckGo's Instant Answer API and return
    either the direct abstract or a related topic summary.
    """
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1"
        res = requests.get(url)
        data = res.json()

        # Primary summary if available
        abstract = data.get("AbstractText")
        if abstract:
            return f"📝 {abstract}"

        # Try related topic summaries
        related = data.get("RelatedTopics")
        if related and isinstance(related, list):
            for item in related:
                if isinstance(item, dict) and item.get("Text"):
                    return f"🔗 Related: {item['Text']}"
                # Some items may be nested in a "Topics" list
                if isinstance(item, dict) and "Topics" in item:
                    for sub in item["Topics"]:
                        if sub.get("Text"):
                            return f"🔗 Related: {sub['Text']}"

        return "❌ No relevant summary found. Try a more specific query."
    
    except Exception as e:
        return f"🚨 Error during DuckDuckGo lookup: {str(e)}"

# Register tool
web_lookup_tool = Tool.from_function(
    web_search_duckduckgo,
    name="web_lookup",
    description="Search any topic using DuckDuckGo and return a concise summary or related information"
)