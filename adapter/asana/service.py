import asana 
from typing import Dict, List

import logging
logger = logging.getLogger(__name__)

class AsanaService:
    """
        AsanaService class is used for interacting with Asana API.
    """
    def __init__(self, config: Dict):
        self.api_client = asana.ApiClient(configuration=config)
        logger.info("AsanaService initialized")
         

    def create_tasks(self, tasks: List[Dict]) -> List[Dict]:
        """
            Create a multiple tasks in the project management tool.

        Args:
            tasks (List[Dict]): List of tasks to be created.
        
        Returns:
            List[Dict]: List of created tasks.
        """
        pass 