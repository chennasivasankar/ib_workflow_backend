from typing import List

from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO, \
    UserRoleDTO, UserCompanyDTO, UserDTO, CompanyDTO, \
    TeamIdAndNameDTO, RoleIdAndNameDTO, RoleDTO
from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_iam.models import Role


class StorageImplementation(StorageInterface):

    def check_is_admin_user(self, user_id: str) -> bool:
        from ib_iam.models.user import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        return user.is_admin
