from abc import ABC
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import BasicUserDetailsDTO, \
    UserRoleDTO


class GetSpecificTeamDetailsPresenterInterface(ABC):

    def prepare_success_response_for_get_specific_team_details(
            self, basic_user_details_dtos: List[BasicUserDetailsDTO],
            user_role_dtos: List[UserRoleDTO]
    ):
        pass
