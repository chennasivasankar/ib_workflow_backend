from ib_iam.adapters.services import get_service_adapter
from ib_iam.interactors.presenter_interfaces \
    .team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces \
    .team_storage_interface import TeamStorageInterface
from ib_iam.interactors.presenter_interfaces.dtos import (
    TeamWithMembersDetailsDTO
)
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamDTO, TeamMemberIdsDTO, MemberDTO
)
from ib_iam.adapters.dtos import UserProfileDTO
from typing import List
from ib_iam.exceptions.custom_exceptions import (
    UserHasNoAccess, InvalidLimit, InvalidOffset
)


class GetListOfTeamsInteractor:

    def __init__(self, storage: TeamStorageInterface):
        self.storage = storage

    def get_list_of_teams_wrapper(
            self,
            user_id: str,
            pagination_dto: PaginationDTO,
            presenter: TeamPresenterInterface
    ):
        try:
            team_details_dtos = self.get_list_of_teams(
                user_id=user_id, pagination_dto=pagination_dto
            )
            response = presenter.get_response_for_get_list_of_teams(
                team_details_dtos=team_details_dtos
            )
        except UserHasNoAccess:
            response = presenter \
                .get_user_has_no_access_response_for_get_list_of_teams()
        except InvalidLimit:
            response = \
                presenter.get_invalid_limit_response_for_get_list_of_teams()
        except InvalidOffset:
            response = \
                presenter.get_invalid_offset_response_for_get_list_of_teams()
        return response

    def get_list_of_teams(self, user_id: str, pagination_dto: PaginationDTO):
        self._validate_pagination_details(pagination_dto=pagination_dto)
        self.storage.raise_exception_if_user_is_not_admin(user_id=user_id)
        teams_with_total_teams_count = \
            self.storage.get_teams_with_total_teams_count_dto(
                pagination_dto=pagination_dto
            )
        team_ids = self._get_team_ids_from_team_dtos(
            team_dtos=teams_with_total_teams_count.teams
        )

        team_member_ids_dtos = self.storage.get_team_member_ids_dtos(
            team_ids=team_ids
        )
        member_ids = self._get_all_member_ids_from_team_member_ids_dtos(
            team_member_ids_dtos=team_member_ids_dtos
        )
        member_dtos = self._get_members_dtos_from_service(
            member_ids=member_ids
        )
        team_with_memebers_dtos = TeamWithMembersDetailsDTO(
            total_teams_count=teams_with_total_teams_count.total_teams_count,
            team_dtos=teams_with_total_teams_count.teams,
            team_member_ids_dtos=team_member_ids_dtos,
            member_dtos=member_dtos
        )
        return team_with_memebers_dtos

    @staticmethod
    def _validate_pagination_details(pagination_dto: PaginationDTO):
        if pagination_dto.limit <= 0:
            raise InvalidLimit()
        if pagination_dto.offset < 0:
            raise InvalidOffset()

    @staticmethod
    def _get_team_ids_from_team_dtos(
            team_dtos: List[TeamDTO]
    ) -> List[str]:
        team_ids = [
            team_dto.team_id for team_dto in team_dtos
        ]
        return team_ids

    @staticmethod
    def _get_all_member_ids_from_team_member_ids_dtos(
            team_member_ids_dtos: List[TeamMemberIdsDTO]
    ):
        member_ids = []
        for team_member_ids_dto in team_member_ids_dtos:
            member_ids.extend(team_member_ids_dto.member_ids)
        unique_member_ids = list(set(member_ids))
        return unique_member_ids

    def _get_members_dtos_from_service(self, member_ids: List[str]):
        service = get_service_adapter()
        user_dtos = service.user_service.get_basic_user_dtos(
            user_ids=member_ids
        )
        member_dtos = self._convert_user_dtos_to_member_dtos(
            user_dtos=user_dtos
        )
        return member_dtos

    @staticmethod
    def _convert_user_dtos_to_member_dtos(
            user_dtos: List[UserProfileDTO]
    ) -> List[MemberDTO]:
        member_dtos = [
            MemberDTO(member_id=user_dto.user_id,
                      name=user_dto.name,
                      profile_pic_url=user_dto.profile_pic_url
                      ) for user_dto in user_dtos
        ]
        return member_dtos
