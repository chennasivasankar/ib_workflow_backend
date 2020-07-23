from typing import List

from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class StorageImplementation(StorageInterface):

    def check_is_admin_user(self, user_id: str) -> bool:
        from ib_iam.models.user import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        return user.is_admin

    def create_roles(self, role_dtos: List[RoleDTO]):
        from ib_iam.models import Role
        role_objects = [
            Role(role_id=role_dto.role_id, name=role_dto.name,
                 description=role_dto.description)
            for role_dto in role_dtos]
        Role.objects.bulk_create(role_objects)

    def get_valid_role_ids(self, role_ids: List[str]):
        from ib_iam.models import Role
        valid_role_ids = Role.objects.filter(role_id__in=role_ids).\
            values_list("role_id", flat=True)
        return list(valid_role_ids)
