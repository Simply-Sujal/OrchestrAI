import asana

from typing import Dict, List
from adapter.asana.service import AsanaService
from adapter.base_adapter import BaseProjectManagementAdapter

import logging

from adapter.types import Task
logger = logging.getLogger(__name__)


class AsanaAdapter(BaseProjectManagementAdapter):
    """
        AsanaAdapter is a class that implements the BaseProjectManagementAdapter interface.
        This adapter is used to perform CRUD operations on tasks in Asana.
    """

    def __init__(self, config: Dict):
        """
            Initialize the AsanaAdapter with the configuration.
        """
        configuration = asana.Configuration()
        configuration.access_token = config["access_token"]
        self.api_client = asana.ApiClient(configuration=configuration)  
        self.config = config
        logger.info("AsanaAdapter initialized")

    def create(self, tasks: List[Task]) -> List[Task]:
        """
            Create multiple tasks in the project management tool.

        Args:
            tasks (List[Task]): List of tasks to be created.
        
        Returns:
            List[Task]: List of created tasks.
        """
        try:
            asana_service = AsanaService(config=self.config)
            return asana_service.create_tasks(tasks)
        except Exception as e:
            logger.error(f"Failed to create tasks: {e}")
            raise e