
import re
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from llm import chat_with_llm
from memory import conversation_history
from decision_engine import architecture_decision
from state import user_data

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def extract_mermaid(text):

    pattern = r"```mermaid(.*?)```"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1).strip()

    return None


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/chat")
async def chat(request: Request, message: str = Form(...)):

   
    conversation_history.append({
        "role": "user",
        "content": message
    })

  
    response = chat_with_llm(conversation_history)

  
    conversation_history.append({
        "role": "assistant",
        "content": response
    })


    diagram = extract_mermaid(response)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "history": conversation_history,
            "diagram": diagram
        }
    )
@app.get("/test")
def test():
    return {"status": "server running"}


user_data["users"] = 10000
user_data["realtime"] = True
user_data["payments"] = True

architecture = architecture_decision(user_data)