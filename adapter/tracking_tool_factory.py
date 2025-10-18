from adapter.asana.asana import AsanaAdapter
from adapter.base_adapter import BaseProjectManagementAdapter
from adapter.project_management_tool_name import ProjectManagementToolName
import os

class TaskTrackingToolFactory:

    def __init__(self):
        """
            Initialize the factory with the project management tool.
        """
        self.project_management_tool = os.getenv("PROJECT_MANAGEMENT_TOOL") 

    def get_tracking_tool(self) -> BaseProjectManagementAdapter:
        """
            Get the tracking tool adapter based on the project management tool.
        """

        try:
            if self.project_management_tool.lower() == ProjectManagementToolName.ASANA.value:
                config = {}
                config["access_token"] = os.getenv("ASANA_ACCESS_TOKEN")
                return AsanaAdapter(config)
        
            raise ValueError("Invalid project management tool")
        except Exception as e:
            raise ValueError(f"Invalid project management tool {e}")