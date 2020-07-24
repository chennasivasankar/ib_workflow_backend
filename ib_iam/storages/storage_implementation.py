from typing import List

from ib_iam.app_interfaces.dtos import UserDTO
from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_iam.models.role import Role


class StorageImplementation(StorageInterface):
    def create_roles(self, role_dtos: List[RoleDTO]):
        role_objects = [
            Role(role_id=role_dto.role_id,
                 name=role_dto.name,
                 description=role_dto.description) for role_dto in role_dtos
        ]
        Role.objects.bulk_create(role_objects)

    def get_valid_role_ids(self, role_ids: List[str]):
        role_ids_in_database = Role.objects.all().values_list("role_id",
                                                              flat=True)
        valid_roles_ids = [
            role_id for role_id in role_ids if role_id in role_ids_in_database
        ]
        return valid_roles_ids

    def get_user_dtos_based_on_limit_and_offset(
            self, limit: int, offset: int, search_query: str) -> List[UserDTO]:
        #use this query User.objects.filter(user_name__icontains=search_query)[offset:limit]
        pass

    def get_all_user_dtos_based_on_query(self,
                                         search_query: str) -> List[UserDTO]:
        #use this query User.objects.filter(user_name__icontains=search_query)
        pass
