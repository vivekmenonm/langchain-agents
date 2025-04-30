
# 🧠 LangChain Multi-Agent System with FastAPI and Cosmos DB

This project implements a modular multi-agent architecture using [LangChain](https://www.langchain.com/), [FastAPI](https://fastapi.tiangolo.com/), and Azure Cosmos DB. It includes intelligent agents for managing customer tickets, calendars, and customer data, with an orchestrator agent that handles end-to-end workflows from natural language prompts.

## 📁 Folder Structure
```
langchain_agents/
├── main.py                  # FastAPI app with a single `/orchestrate` endpoint
├── agents/
│   ├── orchestrator.py      # Central agent that routes tasks to worker agents
│   ├── ticketing_agent.py   # Agent for ticket tools: create, update, note, log time
│   ├── customer_agent.py    # Agent for customer tools: CRUD operations, contacts
│   └── calendar_agent.py    # Agent for calendar tools: create and fetch events
├── tools/
│   ├── ticket_tools.py      # Cosmos DB queries for tickets
│   ├── customer_tools.py    # Cosmos DB queries for customers
│   ├── calendar_tools.py    # In-memory mock calendar tools
│   ├── summarizer.py        # LangChain summarizer tool for ticket summarization
│   └── web_lookup.py        # Tool for blog search or GPS coordinates
├── db/
│   └── cosmos_client.py     # Cosmos DB connection logic
├── vector_store/
│   └── chroma/              # (Optional) Vector store for embedding-based search
├── .env.example             # Environment variable template
├── .gitignore               # Ignoring secrets, cache, and build artifacts
└── requirements.txt         # All required Python packages
```

## 🚀 Features

- ✅ **Modular Agents**:
  - `TicketingAgent` for managing tickets
  - `CustomerAgent` for handling customer data
  - `CalendarAgent` for managing events
  - `OrchestratorAgent` for routing complex prompts

- ✨ **Stretch Tools**:
  - **Summarizer Tool**: Summarizes ticket history via LangChain
  - **Web Lookup Tool**: Fetches blogs or GPS coordinates

- 🌐 **FastAPI Endpoint**:
  - `/orchestrate`: Accepts natural language queries and returns structured responses

## 🛠️ Installation & Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/langchain-agents.git
cd langchain-agents
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

```bash
cp .env.example .env
# Then fill in your OpenAI key, Cosmos DB key, etc.
```

### 5. Run FastAPI App

```bash
uvicorn main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) to test in Swagger UI.

## 📡 Example Request

```json
POST /orchestrate
{
  "query": "Create a calendar event for Alice on Friday and a ticket for customer C123 with issue 'VPN Down'"
}
```

The orchestrator agent will route the intent to multiple tools and return a unified response.

## 📌 Acceptance Criteria

- ✅ Embedded in UI (Swagger UI provided)
- ✅ 3+ agents (Ticketing, Customer, Calendar, Orchestrator)
- ✅ 2+ APIs integrated (CosmosDB, OpenAI)
- ✅ One vector piece (Summarization)
- ✅ One MCP tool (web blog or GPS lookup)
