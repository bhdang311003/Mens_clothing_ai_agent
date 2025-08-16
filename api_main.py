from fastapi import FastAPI
from pydantic import BaseModel
from agent import answer_query

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Men's Clothing AI Agent API is running!"}

@app.post("/ask")
def ask_question(request: QueryRequest):
    answer = answer_query(request.query)
    return {"query": request.query, "answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_main:app", host="127.0.0.1", port=8000, reload=True)