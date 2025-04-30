from langchain.tools import Tool
from tools.calendar_tools import create_event, get_events

calendar_tools = [
    Tool.from_function(create_event, name="create_event", description="Create a calendar event"),
    Tool.from_function(get_events, name="get_events", description="Get upcoming events for a user"),
]
