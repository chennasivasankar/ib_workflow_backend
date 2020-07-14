from abc import ABC
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import RoleDto


class StorageInterface(ABC):
    def create_roles(self, roles_dto_list: List[RoleDto]):
        pass