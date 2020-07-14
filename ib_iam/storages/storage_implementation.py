from typing import List

from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_iam.models.role import Role


class StorageImplementation(StorageInterface):
    def create_roles(self, role_dtos: List[RoleDTO]):
        role_objects = [
            Role(role_id=role_dto.role_id, role_name=role_dto.role_name,
                 role_description=role_dto.role_description)
            for role_dto in role_dtos]
        Role.objects.bulk_create(role_objects)
