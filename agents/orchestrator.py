from langchain.agents import AgentExecutor, initialize_agent
from langchain.chat_models import ChatOpenAI
from tools.summarizer import summarizer_tool
from tools.web_lookup import web_lookup_tool
from agents.ticketing_agent import ticket_tools
from agents.customer_agent import customer_tools
from agents.calendar_agent import calendar_tools



llm = ChatOpenAI(temperature=0)


tools = ticket_tools + customer_tools + calendar_tools + [summarizer_tool, web_lookup_tool]


agent_executor = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

async def handle_orchestrator_query(query: str) -> str:
    return agent_executor.run(query)
