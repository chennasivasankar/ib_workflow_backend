from typing import List

from ib_iam.exceptions.custom_exceptions import MemberIdsNotFoundInTeam, \
    UserIsNotAdmin
from ib_iam.interactors.dtos.dtos import TeamMemberLevelIdWithMemberIdsDTO
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddMembersToTeamMemberLevelsPresenterInterface
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
    TeamMemberLevelStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class TeamMemberLevelIdsNotFound(Exception):

    def __init__(self, team_member_level_ids: List[str]):
        self.team_member_level_ids = team_member_level_ids


class AddMembersToTeamMemberLevelsInteractor(ValidationMixin):

    def __init__(
            self, user_storage: UserStorageInterface,
            team_member_level_storage: TeamMemberLevelStorageInterface
    ):
        self.team_member_level_storage = team_member_level_storage
        self.user_storage = user_storage

    def add_members_to_team_member_levels_wrapper(
            self, presenter: AddMembersToTeamMemberLevelsPresenterInterface,
            team_id: str, user_id: str,
            team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO]
    ):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        try:
            response = self._add_members_to_team_member_levels_response(
                team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
                presenter=presenter, team_id=team_id, user_id=user_id
            )
        except UserIsNotAdmin:
            response = presenter.response_for_user_is_not_admin()
        except InvalidTeamId:
            response = presenter.response_for_invalid_team_id()
        except TeamMemberLevelIdsNotFound as err:
            response = presenter.response_for_team_member_level_ids_not_found(
                err
            )
        except MemberIdsNotFoundInTeam as err:
            response = presenter.response_for_team_member_ids_not_found(
                err
            )
        return response

    def _add_members_to_team_member_levels_response(
            self, presenter: AddMembersToTeamMemberLevelsPresenterInterface,
            team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO],
            team_id: str, user_id: str
    ):
        self.add_members_to_team_member_levels(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
            team_id=team_id, user_id=user_id
        )
        response = \
            presenter.prepare_success_response_for_add_members_to_team_member_levels()
        return response

    def add_members_to_team_member_levels(
            self, team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO],
            team_id: str, user_id: str
    ):
        self._validate_is_user_admin(user_id=user_id)
        self.team_member_level_storage.validate_team_id(team_id=team_id)

        self._validate_team_member_level_ids(
            team_id=team_id,
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos
        )
        self._validate_team_member_ids(
            team_id=team_id,
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos
        )
        self.team_member_level_storage.add_members_to_levels_for_a_team(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
        )
        return

    def _validate_team_member_ids(
            self, team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO],
            team_id: str
    ):
        team_member_ids_in_database = self.team_member_level_storage. \
            get_team_member_ids(team_id=team_id)
        team_member_ids = self._get_team_member_ids_from_dto(
            team_member_level_id_with_member_ids_dtos
        )
        member_ids_not_found_in_team = [
            team_member_id
            for team_member_id in team_member_ids
            if team_member_id not in team_member_ids_in_database
        ]
        if member_ids_not_found_in_team:
            raise MemberIdsNotFoundInTeam(
                team_member_ids=member_ids_not_found_in_team)

    @staticmethod
    def _get_team_member_ids_from_dto(
            team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO]
    ) -> List[str]:
        team_member_ids = []
        for team_member_level_id_with_member_ids_dto in \
                team_member_level_id_with_member_ids_dtos:
            team_member_ids.extend(
                team_member_level_id_with_member_ids_dto.member_ids
            )
        return team_member_ids

    def _validate_team_member_level_ids(
            self, team_id: str,
            team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO]
    ):
        valid_team_member_level_ids = \
            self.team_member_level_storage.get_team_member_level_ids(
                team_id=team_id
            )
        invalid_team_member_level_ids = [
            team_member_level_id_with_member_ids_dto.team_member_level_id
            for team_member_level_id_with_member_ids_dto in
            team_member_level_id_with_member_ids_dtos
            if
            (
                team_member_level_id_with_member_ids_dto.team_member_level_id
            ) not in valid_team_member_level_ids
        ]
        if invalid_team_member_level_ids:
            raise TeamMemberLevelIdsNotFound(
                team_member_level_ids=invalid_team_member_level_ids
            )
