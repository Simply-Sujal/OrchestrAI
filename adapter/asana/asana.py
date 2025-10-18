import asana

from typing import Dict, List
from adapter.base_adapter import BaseProjectManagementAdapter

import logging
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
        self.api_client = asana.ApiClient(configuration=config)
        logger.info("AsanaAdapter initialized")

    def create(self, tasks: List[Dict]) -> List[Dict]:
        """
            Create a multiple tasks in the project management tool.

        Args:
            tasks (List[Dict]): List of tasks to be created.
        
        Returns:
            List[Dict]: List of created tasks.
        """
        pass 