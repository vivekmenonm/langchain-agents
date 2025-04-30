from fastapi import FastAPI, Request
from agents.orchestrator import handle_orchestrator_query

app = FastAPI()

@app.post("/orchestrate")
async def orchestrate(request: Request):
    body = await request.json()
    query = body.get("query")
    response = await handle_orchestrator_query(query)
    return {"response": response}
