from langchain.agents import AgentExecutor, initialize_agent
# from langchain.chat_models import ChatOpenAI
from tools.summarizer import summarizer_tool
from tools.mcp_tools import mcp_tools
from agents.ticketing_agent import ticket_tools
from agents.customer_agent import customer_tools
from agents.calendar_agent import calendar_tools
from tools.utility_tools import date_tool
from tools.web_lookup import web_lookup_tool

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

tools = (
    ticket_tools +
    customer_tools +
    calendar_tools +
    mcp_tools +  # contains geo/blog tools
    [summarizer_tool, web_lookup_tool, date_tool]
)

agent_executor = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True, handle_parsing_errors=True
)

async def handle_orchestrator_query(query: str) -> str:
    return agent_executor.run(query)
