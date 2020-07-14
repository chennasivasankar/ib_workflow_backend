from abc import ABC
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import RoleDTO


class StorageInterface(ABC):
    def create_roles(self, role_dtos: List[RoleDTO]):
        pass
