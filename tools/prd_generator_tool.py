from typing import Dict, Any, List
from prompts.prd_generator_prompt import PRD_GENERATOR_PROMPT
from langchain_google_genai import ChatGoogleGenerativeAI
from google.ai.generativelanguage_v1beta.types import Tool as GenAITool
from dotenv import load_dotenv
import os
import json
import logging

from prompts.project_planner_prompt import PROJECT_PLANNER_PROMPT
from adapter.tracking_tool_factory import TaskTrackingToolFactory
from adapter.types import Task, ProjectPlan

logger = logging.getLogger(__name__)

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY_9")
model = os.getenv("GOOGLE_GEMINI_MODEL")

llm = ChatGoogleGenerativeAI(model=model, api_key=google_api_key)

def prd_generator_tool(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a PRD using online insights and return the response.
    """
    response = llm.invoke(
        input=PRD_GENERATOR_PROMPT.format(user_input=state["user_input"]),
        tools=[GenAITool(google_search={})],
    ).content

    with open("prd_text.txt", "w") as f:
        f.write(response)

    return {"prd_text": response}


def project_planner_tool(state: Dict[str, Any]):
    """
    Generate a project plan using the PRD text with structured output.
    """
    if "prd_text" not in state:
        return {"tasks": [], "error": "No PRD text available"}
    
    try:
        structured_llm = llm.with_structured_output(ProjectPlan)
        project_plan: ProjectPlan = structured_llm.invoke(
            input=PROJECT_PLANNER_PROMPT.format(prd_text=state["prd_text"])
        )
        
        with open("project_plan.json", "w") as f:
            f.write(project_plan.model_dump_json(indent=2))
        
        logger.info(f"Generated {len(project_plan.tasks)} tasks with structured output")
        
        return {"tasks": project_plan.tasks}
        
    except Exception as e:
        error_msg = f"Error generating project plan: {str(e)}"
        logger.error(error_msg)
        return {"tasks": [], "error": error_msg}


def task_pusher_tool(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Push generated tasks to Asana using typed Task models.
    """
    if "tasks" not in state:
        return {"asana_result": "Error: No tasks available"}
    
    try:
        tasks: List[Task] = state["tasks"]
        
        if not tasks:
            return {"asana_result": "No tasks found in project plan"}

        logger.info(f"Pushing {len(tasks)} typed tasks to Asana")

        factory = TaskTrackingToolFactory()
        adapter = factory.get_tracking_tool()
        created_tasks = adapter.create(tasks)

        logger.info(f"Successfully created {len(created_tasks)} tasks in Asana")
        
        return {
            "asana_result": f"Successfully created {len(created_tasks)} tasks in Asana"
        }
        
    except Exception as e:
        error_msg = f"Error pushing tasks to Asana: {str(e)}"
        logger.error(error_msg)
        return {"asana_result": error_msg}