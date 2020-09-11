import abc
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import BasicUserDetailsDTO, \
    UserRoleDTO


class GetListOfUserRolesForGivenProjectPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_users_with_roles(
            self, basic_user_details_dtos: List[BasicUserDetailsDTO],
            user_role_dtos: List[UserRoleDTO]
    ):
        pass

    @abc.abstractmethod
    def response_for_invalid_project_id_exception(self):
        pass

    @abc.abstractmethod
    def response_for_user_not_have_permission_exception(self):
        pass
