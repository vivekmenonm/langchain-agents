from langchain.tools import Tool
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.chat_models import ChatOpenAI

def summarize_ticket(history: str) -> str:
    llm = ChatOpenAI()
    docs = [Document(page_content=history)]
    chain = load_summarize_chain(llm, chain_type="stuff")
    return chain.run(docs)

summarizer_tool = Tool.from_function(
    summarize_ticket,
    name="summarize_ticket",
    description="Summarize long ticket history into a short version"
)
