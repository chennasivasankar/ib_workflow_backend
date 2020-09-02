from typing import List

from ib_iam.exceptions.custom_exceptions import MemberIdsNotFoundInTeam
from ib_iam.interactors.dtos.dtos import TeamMemberLevelIdWithMemberIdsDTO
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddMembersToLevelPresenterInterface
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
    TeamMemberLevelStorageInterface


class TeamMemberLevelIdsNotFound(Exception):
    def __init__(self, team_member_level_ids: List[str]):
        self.team_member_level_ids = team_member_level_ids


class AddMembersToLevelsInteractor:

    def __init__(self,
                 team_member_level_storage: TeamMemberLevelStorageInterface):
        self.team_member_level_storage = team_member_level_storage

    def add_members_to_levels_wrapper(
            self, presenter: AddMembersToLevelPresenterInterface, team_id: str,
            team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO]
    ):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        try:
            response = self._add_members_to_levels_response(
                team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
                presenter=presenter, team_id=team_id
            )
        except InvalidTeamId:
            response = presenter.response_for_invalid_team_id()
        except TeamMemberLevelIdsNotFound as err:
            response = presenter.response_for_team_member_level_ids_not_found(
                err)
        except MemberIdsNotFoundInTeam as err:
            response = presenter.response_for_team_member_ids_not_found(err)
        return response

    def _add_members_to_levels_response(
            self, presenter: AddMembersToLevelPresenterInterface,
            team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO],
            team_id: str
    ):
        self.add_members_to_levels(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
            team_id=team_id
        )
        response = \
            presenter.prepare_success_response_for_add_members_to_levels()
        return response

    def add_members_to_levels(
            self, team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO],
            team_id: str
    ):
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
        team_member_ids_in_database = self.team_member_level_storage.get_team_member_ids(
            team_id=team_id)
        team_member_ids = []
        for team_member_level_id_with_member_ids_dto in team_member_level_id_with_member_ids_dtos:
            team_member_ids.extend(
                team_member_level_id_with_member_ids_dto.member_ids)
        member_ids_not_found_in_team = [
            team_member_id
            for team_member_id in team_member_ids
            if team_member_id not in team_member_ids_in_database
        ]
        if member_ids_not_found_in_team:
            raise MemberIdsNotFoundInTeam(
                team_member_ids=member_ids_not_found_in_team)

    def _validate_team_member_level_ids(
            self, team_id: str,
            team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO]
    ):
        team_member_level_ids_in_database = \
            self.team_member_level_storage.get_team_member_level_ids(
                team_id=team_id)
        team_member_level_ids = [
            team_member_level_id_with_member_ids_dto.team_member_level_id
            for team_member_level_id_with_member_ids_dto in
            team_member_level_id_with_member_ids_dtos
        ]
        team_member_level_ids_not_found = [
            team_member_level_id
            for team_member_level_id in team_member_level_ids
            if team_member_level_id not in team_member_level_ids_in_database
        ]
        if team_member_level_ids_not_found:
            raise TeamMemberLevelIdsNotFound(
                team_member_level_ids=team_member_level_ids_not_found)
