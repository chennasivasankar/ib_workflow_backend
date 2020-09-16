from typing import List

from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    GetTeamMemberLevelsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamMemberLevelDetailsDTO
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
    TeamMemberLevelStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetTeamMemberLevelsInteractor(ValidationMixin):

    def __init__(
            self, user_storage: UserStorageInterface,
            team_member_level_storage: TeamMemberLevelStorageInterface
    ):
        self.team_member_level_storage = team_member_level_storage
        self.user_storage = user_storage

    def get_team_member_levels_wrapper(
            self, team_id: str, user_id: str,
            presenter: GetTeamMemberLevelsPresenterInterface
    ):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin

        try:
            response = self._get_team_member_levels_response(
                team_id=team_id, presenter=presenter, user_id=user_id)
        except UserIsNotAdmin:
            response = presenter.response_for_user_is_not_admin()
        except InvalidTeamId:
            response = presenter.response_for_invalid_team_id()
        return response

    def _get_team_member_levels_response(
            self, team_id: str, user_id: str,
            presenter: GetTeamMemberLevelsPresenterInterface
    ):
        team_member_level_details_dtos = self.get_team_member_levels(
            team_id=team_id, user_id=user_id)
        response = presenter.response_for_team_member_level_details_dtos(
            team_member_level_details_dtos=team_member_level_details_dtos
        )
        return response

    def get_team_member_levels(
            self, team_id: str, user_id: str
    ) -> List[TeamMemberLevelDetailsDTO]:
        self._validate_is_user_admin(user_id=user_id)
        self.team_member_level_storage.validate_team_id(team_id=team_id)
        team_member_level_details_dtos = \
            self.team_member_level_storage.get_team_member_level_details_dtos(
                team_id=team_id
            )
        return team_member_level_details_dtos
