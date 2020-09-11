from typing import List

from ib_iam.adapters.service_adapter import get_service_adapter
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces \
    .team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces \
    .team_storage_interface import TeamStorageInterface
from ib_iam.interactors.presenter_interfaces.dtos import (
    TeamWithUsersDetailsDTO)
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamUserIdsDTO, TeamDTO, BasicUserDetailsDTO)
from ib_iam.exceptions.custom_exceptions import (
    UserIsNotAdmin, InvalidLimitValue, InvalidOffsetValue)
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetListOfTeamsInteractor(ValidationMixin):

    def __init__(
            self, team_storage: TeamStorageInterface,
            user_storage: UserStorageInterface):
        self.user_storage = user_storage
        self.team_storage = team_storage

    def get_list_of_teams_wrapper(
            self, user_id: str, pagination_dto: PaginationDTO,
            presenter: TeamPresenterInterface):
        try:
            team_details_dtos = self.get_list_of_teams(
                user_id=user_id, pagination_dto=pagination_dto)
            response = presenter.get_response_for_get_list_of_teams(
                team_details_dtos=team_details_dtos)
        except UserIsNotAdmin:
            response = presenter \
                .get_user_has_no_access_response_for_get_list_of_teams()
        except InvalidLimitValue:
            response = \
                presenter.get_invalid_limit_response_for_get_list_of_teams()
        except InvalidOffsetValue:
            response = \
                presenter.get_invalid_offset_response_for_get_list_of_teams()
        return response

    def get_list_of_teams(self, user_id: str, pagination_dto: PaginationDTO):
        self._validate_pagination_details(
            limit=pagination_dto.limit, offset=pagination_dto.offset)
        self._validate_is_user_admin(user_id=user_id)
        teams_with_total_teams_count = \
            self.team_storage.get_teams_with_total_teams_count_dto(
                pagination_dto=pagination_dto)
        team_ids = self._get_team_ids_from_team_dtos(
            team_dtos=teams_with_total_teams_count.teams)

        team_user_ids_dtos = self.team_storage.get_team_user_ids_dtos(
            team_ids=team_ids)
        member_ids = self._get_all_member_ids_from_team_user_ids_dtos(
            team_user_ids_dtos=team_user_ids_dtos)
        member_dtos = self._get_basic_user_details_dtos_from_service(
            user_ids=member_ids)
        team_with_members_dtos = TeamWithUsersDetailsDTO(
            total_teams_count=teams_with_total_teams_count.total_teams_count,
            team_dtos=teams_with_total_teams_count.teams,
            team_user_ids_dtos=team_user_ids_dtos,
            user_dtos=member_dtos)
        return team_with_members_dtos

    @staticmethod
    def _get_team_ids_from_team_dtos(team_dtos: List[TeamDTO]) -> List[str]:
        team_ids = [team_dto.team_id for team_dto in team_dtos]
        return team_ids

    @staticmethod
    def _get_all_member_ids_from_team_user_ids_dtos(
            team_user_ids_dtos: List[TeamUserIdsDTO]) -> List[str]:
        member_ids = []
        for team_user_ids_dto in team_user_ids_dtos:
            member_ids.extend(team_user_ids_dto.user_ids)
        unique_member_ids = list(set(member_ids))
        return unique_member_ids

    @staticmethod
    def _get_basic_user_details_dtos_from_service(
            user_ids: List[str]) -> List[BasicUserDetailsDTO]:
        service = get_service_adapter()
        user_dtos = service.user_service.get_basic_user_dtos(
            user_ids=user_ids)
        return user_dtos
