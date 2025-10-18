from abc import ABC, abstractmethod
from typing import Dict, List

class BaseProjectManagementAdapter(ABC):
    
    @abstractmethod
    def create(self, tasks: List[Dict]) -> List[Dict]:
        """
            Create a multiple tasks in the project management tool.

            Args:
                tasks (List[Dict]): List of tasks to be created.
            
            Returns:
                List[Dict]: List of created tasks.
        """
        pass 
