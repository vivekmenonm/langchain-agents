from datetime import datetime
from langchain.tools import Tool

# ✅ Tool to return current date
def get_current_date(_: str) -> str:
    return datetime.now().strftime("Today is %A, %d %B %Y")


# ✅ Tool wrapper
date_tool = Tool.from_function(
    func=get_current_date,
    name="get_current_date",
    description="Get the current date. Use this to answer questions about the current day, month, or year."
)
