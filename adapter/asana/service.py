import asana 
from typing import Dict, List

import logging

from adapter.asana.helper import get_user_info
logger = logging.getLogger(__name__)

class AsanaService:
    """
        AsanaService class is used for interacting with Asana API.
    """
    def __init__(self, config: Dict):

        configuration = asana.Configuration()
        configuration.access_token = config["access_token"]
        self.api_client = asana.ApiClient(configuration=configuration)
        self.task_api = asana.TasksApi(api_client=self.api_client)
        self.workspace_api = asana.WorkspacesApi(api_client=self.api_client)
        self.project_api = asana.ProjectsApi(api_client=self.api_client)
        logger.info("AsanaService initialized")

    def get_default_workspace_gid(self):
        """Fetch the user's first workspace GID"""
        workspaces = self.workspace_api.get_workspaces()
        return workspaces.data[0].gid if workspaces.data else None

    def create_project(self, asana_project):
        pass 

    def create_task(self, asana_task):
        pass
 
    def create_subtask(self, asana_subtask):
        pass 