import requests
import os
from dotenv import load_dotenv
import requests

load_dotenv()

OPENROUTER_API_KEY =os.getenv("OPENROUTER_API_KEY")

MODEL = "deepseek/deepseek-chat"

SYSTEM_PROMPT = """
You are a senior distributed systems architect.

Your job is to design scalable backend architectures.

When the user describes an application:

1. First list architecture components:
Architecture Type
Core Services
Databases
Infrastructure

2. Then generate a Mermaid diagram.

The diagram MUST be returned exactly like this:

```mermaid
graph LR
User --> API_Gateway
API_Gateway --> Service
Service --> Database
"""
def chat_with_llm(messages):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            *messages
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    result = response.json()

    print(result)   # <-- important debug line

    if "choices" not in result:
        return f"API Error: {result}"

    return result["choices"][0]["message"]["content"]