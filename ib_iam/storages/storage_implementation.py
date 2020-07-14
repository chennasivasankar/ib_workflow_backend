from typing import List

from ib_iam.interactors.storage_interfaces.dtos import RoleDto
from ib_iam.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_iam.models.role import Role


class StorageImplementation(StorageInterface):
    def create_roles(self, roles_dto_list: List[RoleDto]):
        roles = [Role(role_id=role.role_id, role_name=role.role_name,
            role_description=role.role_description) for role in roles_dto_list]
        Role.objects.bulk_create(roles)