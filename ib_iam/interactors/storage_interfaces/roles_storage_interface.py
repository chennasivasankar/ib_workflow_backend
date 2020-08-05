from abc import ABC, abstractmethod
from typing import List, Optional

from ib_iam.exceptions.custom_exceptions import InvalidUserId, InvalidUserIds
from ib_iam.interactors.DTOs.common_dtos import UserIdWithRoleIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import RoleDTO


class RolesStorageInterface(ABC):

    @abstractmethod
    def create_roles(self, role_dtos: List[RoleDTO]):
        pass

    @abstractmethod
    def get_valid_role_ids(self, role_ids: List[str]):
        pass

    @abstractmethod
    def validate_user_id(self, user_id) -> Optional[InvalidUserId]:
        pass

    @abstractmethod
    def get_user_role_ids(self, user_id: str) -> List[str]:
        pass

    @abstractmethod
    def validate_user_ids(self, user_ids: List[str]) \
            -> Optional[InvalidUserIds]:
        pass

    @abstractmethod
    def get_user_id_with_role_ids_dtos(self, user_ids: List[str]) \
            -> List[UserIdWithRoleIdsDTO]:
        pass
