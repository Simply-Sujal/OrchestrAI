from typing import Dict, Optional, Union
from adapter.types import Task, Subtask


def build_task_body(
    task_data: Union[Task, Subtask],
    workspace_gid: Optional[str] = None,
    project_gid: Optional[str] = None,
    parent_task_gid: Optional[str] = None,
    is_subtask: bool = False
) -> Dict:
    """
    Build Asana task/subtask body with all fields from Task/Subtask models
    
    Args:
        task_data: Task or Subtask Pydantic model
        workspace_gid: Workspace GID (for main tasks)
        project_gid: Project GID (for main tasks)
        parent_task_gid: Parent task GID (for subtasks)
        is_subtask: Whether this is a subtask or main task
        
    Returns:
        Dict: Formatted task body for Asana API
    """
    # Get task name based on type
    task_name = task_data.subtask_name if is_subtask else task_data.task_name
    
    # Build base body
    task_body = {
        "data": {
            "name": task_name
        }
    }
    
    # Add workspace for main tasks
    if not is_subtask and workspace_gid:
        task_body["data"]["workspace"] = workspace_gid
    
    # Add parent for subtasks
    if is_subtask and parent_task_gid:
        task_body["data"]["parent"] = parent_task_gid
    
    # Add project for main tasks
    if not is_subtask and project_gid:
        task_body["data"]["projects"] = [project_gid]
    
    # Build description with all metadata
    description_parts = []
    
    # Add main description
    if task_data.description:
        description_parts.append(task_data.description)
    
    # Add priority
    if task_data.priority:
        description_parts.append(f"\nPriority: {task_data.priority.upper()}")
    
    # Add estimated hours
    if task_data.estimated_hours:
        description_parts.append(f"Estimated Hours: {task_data.estimated_hours}")
    
    # Add frequency
    if task_data.frequency:
        description_parts.append(f"Frequency: {task_data.frequency}")
    
    # Add tags
    if task_data.tags:
        tags_str = ", ".join(task_data.tags)
        description_parts.append(f"Tags: {tags_str}")
    
    # Set notes
    if description_parts:
        task_body["data"]["notes"] = "\n".join(description_parts)
    
    # Add due date
    if task_data.due_date and task_data.due_date.strip():
        task_body["data"]["due_on"] = task_data.due_date
    
    # Add assignee
    if task_data.assignee and task_data.assignee.strip():
        task_body["data"]["assignee"] = task_data.assignee
    
    return task_body
