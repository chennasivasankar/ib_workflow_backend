
from abc import ABC
from abc import abstractmethod



class ActionStorageInterface(ABC):

    @abstractmethod
    def create_actions_to_stage(self):
        pass