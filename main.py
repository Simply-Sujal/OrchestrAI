from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from tools.prd_generator_tool import prd_generator_tool, project_planner_tool
from dotenv import load_dotenv

import os
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY_9")
model = os.getenv("GOOGLE_GEMINI_MODEL")

llm = ChatGoogleGenerativeAI(model=model, api_key=google_api_key)

class OrchestrAIState(TypedDict):
    user_input: str 
    prd_text: str 
    project_plan: str

def prd_architect(state: OrchestrAIState):
    """
        Convert a user input into a strcutured PRD text.
    """
    return prd_generator_tool(state)

def project_planner(state: OrchestrAIState):
    """
        Convert a PRD text into a project plan.
    """
    return project_planner_tool(state)


workflow = StateGraph(state_schema=OrchestrAIState)

workflow.add_node("prd_architect", prd_architect)
workflow.add_node('project_planner', project_planner)
workflow.add_edge(START, "prd_architect")
workflow.add_edge("prd_architect", "project_planner")
workflow.add_edge("project_planner", END)


app = workflow.compile()

input = {"user_input": "create a basic todo list application"}

final_output = app.invoke(input)

print(final_output["project_plan"])




