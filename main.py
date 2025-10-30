from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, List
from tools.prd_generator_tool import prd_generator_tool, project_planner_tool, task_pusher_tool
from adapter.types import Task
from dotenv import load_dotenv

import os
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY_9")
model = os.getenv("GOOGLE_GEMINI_MODEL")

llm = ChatGoogleGenerativeAI(model=model, api_key=google_api_key)

class OrchestrAIState(TypedDict):
    user_input: str 
    prd_text: str 
    tasks: List[Task] 
    asana_result: str

def prd_architect(state: OrchestrAIState):
    """
        Convert a user input into a strcutured PRD text.
    """
    print("\n📝 Generating PRD...")
    result = prd_generator_tool(state)
    print("✅ PRD Generated Successfully")
    return result

def project_planner(state: OrchestrAIState):
    """
        Convert a PRD text into a project plan.
    """
    print("\n📋 Planning Tasks...")
    result = project_planner_tool(state)
    if "tasks" in result and result["tasks"]:
        print(f"✅ Generated {len(result['tasks'])} Tasks Successfully")
    return result

def task_pusher(state: OrchestrAIState):
    """
        Push generated tasks to Asana.
    """
    print("\n🚀 Pushing Tasks to Asana...")
    result = task_pusher_tool(state)
    return result


workflow = StateGraph(state_schema=OrchestrAIState)

workflow.add_node("prd_architect", prd_architect)
workflow.add_node('project_planner', project_planner)
workflow.add_node('task_pusher', task_pusher)
workflow.add_edge(START, "prd_architect")
workflow.add_edge("prd_architect", "project_planner")
workflow.add_edge("project_planner", "task_pusher")
workflow.add_edge("task_pusher", END)


app = workflow.compile()

input = {"user_input": "create a basic todo application"}

print("=" * 60)
print("🎯 OrchestrAI Workflow Started")
print("=" * 60)

final_output = app.invoke(input)

print("\n" + "=" * 60)
asana_result = final_output.get("asana_result", "N/A")
print(f"✅ {asana_result}")
print("=" * 60)




