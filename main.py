from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator import handle_orchestrator_query

app = FastAPI()

# Define request schema
class OrchestrateRequest(BaseModel):
    query: str

# POST endpoint using the schema
@app.post("/orchestrate")
async def orchestrate(request: OrchestrateRequest):
    response = await handle_orchestrator_query(request.query)
    return {"response": response}
