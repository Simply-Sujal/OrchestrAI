from abc import ABC, abstractmethod
from typing import Dict, List

from adapter.types import Task

class BaseProjectManagementAdapter(ABC):
    
    @abstractmethod
    def create(self, tasks: List[Task]) -> List[Dict]:
        """
            Create a multiple tasks in the project management tool.

            Args:
                tasks (List[Task]): List of tasks to be created.
            
            Returns:
                List[Task]: List of created tasks.
        """
        pass 
