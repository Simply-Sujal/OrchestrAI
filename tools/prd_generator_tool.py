from typing import Dict, Any
from prompts.prd_generator_prompt import PRD_GENERATOR_PROMPT
from langchain_google_genai import ChatGoogleGenerativeAI
from google.ai.generativelanguage_v1beta.types import Tool as GenAITool
from dotenv import load_dotenv
import os

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY_9")
model = os.getenv("GOOGLE_GEMINI_MODEL")

llm = ChatGoogleGenerativeAI(model=model, api_key=google_api_key)

def prd_generator_tool(state: Dict[str, Any]):
    """
    Generate a PRD using online insights and return the response.
    """
    response = llm.invoke(
        input=PRD_GENERATOR_PROMPT.format(user_input=state["user_input"]),
        tools=[GenAITool(google_search={})],
    ).content

    # Save raw PRD
    with open("prd_text.txt", "w") as f:
        f.write(response)

    return {"prd_text": response}
