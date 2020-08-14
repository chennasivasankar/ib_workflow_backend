from abc import ABC, abstractmethod
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import TeamMemberLevelDetailsDTO


class AddTeamMemberLevelsPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_add_team_member_levels_to_team(self):
        pass


class GetTeamMemberLevelsPresenterInterface(ABC):

    @abstractmethod
    def response_for_team_member_level_details_dtos(
            self, team_member_level_details_dtos: List[TeamMemberLevelDetailsDTO]):
        pass


class AddMembersToLevelPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_add_members_to_levels(self):
        pass
