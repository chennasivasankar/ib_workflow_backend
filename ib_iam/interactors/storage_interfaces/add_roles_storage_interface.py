from abc import ABC, abstractmethod
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import RoleDTO


class AddRolesStorageInterface(ABC):
    @abstractmethod
    def check_is_admin_user(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def create_roles(self, role_dtos: List[RoleDTO]):
        pass

    @abstractmethod
    def get_valid_role_ids(self, role_ids: List[str]):
        pass


