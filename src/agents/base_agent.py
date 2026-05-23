from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the agent logic.
        """
        pass
