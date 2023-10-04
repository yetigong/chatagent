from fastapi import FastAPI
# from langcorn import create_service
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.chatagent import chat_agent_api

class Input(BaseModel):
    human_input: str

class Output(BaseModel):
    output: str

app=FastAPI()

@app.get("/")
def get():
  return {"Hello": "World"}

@app.get("/test")
def get():
  return {"Hello": "World, test endpoint"}

@app.post("/chatagent", response_model=Output)
async def input(input: Input):
    output = Output(output=chat_agent_api(input.human_input))
    return output

origins = [
    "<http://localhost>",
    "<http://localhost:5173>",
        "...Your Domains..."
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)