from abc import ABC, abstractmethod
from ib_tasks.interactors.storage_interfaces.dtos import GOFDTO
from typing import List


class StorageInterface(ABC):

    @abstractmethod
    def create_gofs(self, gof_dtos: List[GOFDTO]):
        pass