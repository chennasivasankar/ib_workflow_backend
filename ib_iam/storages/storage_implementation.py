from typing import List

from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_iam.models.role import Role


class StorageImplementation(StorageInterface):
    def create_roles(self, role_dtos: List[RoleDTO]):
        role_objects = [
            Role(role_id=role_dto.role_id, name=role_dto.name,
                 description=role_dto.description)
            for role_dto in role_dtos]
        Role.objects.bulk_create(role_objects)

    def get_valid_role_ids(self, role_ids: List[str]):
        valid_role_ids = Role.objects.filter(role_id__in=role_ids).values_list(
            "role_id", flat=True
        )
        return list(valid_role_ids)
