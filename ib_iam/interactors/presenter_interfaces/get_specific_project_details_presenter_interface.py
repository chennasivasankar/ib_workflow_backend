from abc import ABC, abstractmethod
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import BasicUserDetailsDTO, \
    UserRoleDTO


class GetSpecificProjectDetailsPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_get_specific_team_details(
            self, basic_user_details_dtos: List[BasicUserDetailsDTO],
            user_role_dtos: List[UserRoleDTO]
    ):
        pass

    @abstractmethod
    def response_for_invalid_project_id(self):
        pass
