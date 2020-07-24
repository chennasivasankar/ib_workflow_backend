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

    def get_user_dtos_based_on_limit_and_offset(
            self, limit: int, offset: int, search_query: str) -> List[UserDTO]:
        #use this query User.objects.filter(user_name__icontains=search_query)[offset:limit]
        pass

    def get_all_user_dtos_based_on_query(self,
                                         search_query: str) -> List[UserDTO]:
        #use this query User.objects.filter(user_name__icontains=search_query)
        pass
