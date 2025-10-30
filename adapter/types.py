from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class Priority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Frequency(str, Enum):
    ONCE = "Once"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"

class Subtask(BaseModel):
    subtask_name: str = Field(description="The name of the subtask")
    description: str = Field(description="The description of the subtask")
    assignee: Optional[str] = Field(default="", description="The assignee of the subtask")
    due_date: Optional[str] = Field(default="", description="The due date of the subtask")
    tags: Optional[List[str]] = Field(default_factory=list, description="The tags of the subtask")
    frequency: Optional[str] = Field(default=Frequency.ONCE, description="The frequency of the subtask")
    priority: Optional[str] = Field(default=Priority.MEDIUM, description="The priority of the subtask")
    estimated_hours: Optional[int] = Field(description="The estimated hours of the subtask")

class Task(BaseModel):
    task_name: str = Field(description="The name of the task")
    description: str = Field(description="The description of the task")
    assignee: Optional[str] = Field(default="", description="The assignee of the task")
    due_date: Optional[str] = Field(default="", description="The due date of the task")
    tags: Optional[List[str]] = Field(default_factory=list, description="The tags of the task")
    frequency: Optional[str] = Field(default=Frequency.ONCE, description="The frequency of the task")
    priority: Optional[str] = Field(default=Priority.MEDIUM, description="The priority of the task")
    estimated_hours: Optional[int] = Field(description="The estimated hours of the task")
    subtasks: Optional[List[Subtask]] = Field(default_factory=list, description="The subtasks of the task")

class ProjectPlan(BaseModel):
    """Project plan containing multiple tasks"""
    tasks: List[Task] = Field(description="List of tasks in the project plan")