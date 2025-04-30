from langchain.tools import Tool
from tools.ticket_tools import (
    get_ticket, update_ticket, create_ticket, add_ticket_note, add_timelog
)

ticket_tools = [
    Tool.from_function(get_ticket, name="get_ticket", description="Get ticket by ID"),
    Tool.from_function(update_ticket, name="update_ticket", description="Update ticket details"),
    Tool.from_function(create_ticket, name="create_ticket", description="Create new ticket"),
    Tool.from_function(add_ticket_note, name="add_ticket_note", description="Add note to ticket"),
    Tool.from_function(add_timelog, name="add_timelog", description="Log time on ticket"),
]
