from abc import ABC, abstractmethod
from ib_tasks.interactors.storage_interfaces.dtos import GOFDTO
from typing import List


class StorageInterface(ABC):

    @abstractmethod
    def create_gofs(self, gof_dtos: List[GOFDTO]):
        pass

    @abstractmethod
    def get_valid_read_permission_roles(self) -> List[str]:
        pass

    @abstractmethod
    def get_valid_write_permission_roles(self) -> List[str]:
        pass
