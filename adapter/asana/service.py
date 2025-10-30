import asana 
from typing import Dict, List

import logging
from adapter.asana.helper import build_task_body
from adapter.types import Task, Subtask

logger = logging.getLogger(__name__)

class AsanaService:
    """
        AsanaService class is used for interacting with Asana API.
    """
    def __init__(self, config: Dict):

        configuration = asana.Configuration()
        configuration.access_token = config["access_token"]
        self.api_client = asana.ApiClient(configuration=configuration)
        self.workspace_gid = config["workspace_gid"]
        self.project_gid = config["project_gid"]
        self.task_api = asana.TasksApi(api_client=self.api_client)
        logger.info("AsanaService initialized")

    def create_task(self, task_data: Task) -> Dict:
        """Create a task in Asana with all fields"""
        try:
            # Use helper function to build task body
            task_body = build_task_body(
                task_data=task_data,
                workspace_gid=self.workspace_gid,
                project_gid=self.project_gid,
                is_subtask=False
            )
            
            result = self.task_api.create_task(body=task_body, opts={})
            logger.info(f"Task created: {result['gid']} - {result['name']}")
            return {"gid": result['gid'], "name": result['name']}
        except Exception as e:
            logger.error(f"Failed to create task: {e}")
            raise
 
    def create_subtask(self, subtask_data: Subtask, parent_task_gid: str) -> Dict:
        """Create a subtask in Asana with all fields"""
        try:
            # Use helper function to build subtask body
            subtask_body = build_task_body(
                task_data=subtask_data,
                parent_task_gid=parent_task_gid,
                is_subtask=True
            )
            
            result = self.task_api.create_task(body=subtask_body, opts={})
            logger.info(f"Subtask created: {result['gid']} - {result['name']}")
            return {"gid": result['gid'], "name": result['name']}
        except Exception as e:
            logger.error(f"Failed to create subtask: {e}")
            raise

    def create_tasks(self, tasks: List[Task]) -> List[Task]:
        """Create multiple tasks with subtasks in Asana"""
        created_tasks = []
        
        for task in tasks:
            try:
                # Create main task
                created_task = self.create_task(task)
                parent_task_gid = created_task["gid"]
                created_tasks.append(created_task)  
                
                # Create subtasks if any
                subtasks = task.subtasks or []
                for subtask in subtasks:
                    try:
                        created_subtask = self.create_subtask(subtask, parent_task_gid)
                        created_tasks.append(created_subtask)
                    except Exception as e:
                        logger.error(f"Failed to create subtask '{subtask.subtask_name}': {e}")
                        continue

            except Exception as e:
                logger.error(f"Failed to create task '{task.task_name}': {e}")
                continue
        
        return created_tasks 