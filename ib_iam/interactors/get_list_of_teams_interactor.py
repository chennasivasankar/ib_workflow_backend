from ib_iam.adapters.services import get_service_adapter
from ib_iam.interactors.presenter_interfaces \
    .team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces \
    .team_storage_interface import TeamStorageInterface
from ib_iam.interactors.presenter_interfaces.dtos import (
    TeamWithMembersDetailsDTO
)
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, BasicTeamDTO, TeamMembersDTO, MemberDTO
)
from ib_iam.adapters.dtos import BasicUserDTO
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
            response = presenter.raise_exception_for_user_has_no_access()
        except InvalidLimit:
            response = presenter.raise_exception_for_invalid_limit()
        except InvalidOffset:
            response = presenter.raise_exception_for_invalid_offset()
        return response

    def get_list_of_teams(self, user_id: str, pagination_dto: PaginationDTO):
        self.storage.is_user_admin(user_id=user_id)
        self._is_invalid_limit(pagination_dto.limit)
        self._is_invalid_offset(pagination_dto.offset)

        (team_dtos, total_teams) = self.storage.get_team_dtos_along_with_count(
            user_id=user_id,
            pagination_dto=pagination_dto
        )
        team_ids = self._get_team_ids_from_team_dtos(team_dtos=team_dtos)

        team_member_ids_dtos = self.storage.get_team_member_ids_dtos(
            team_ids=team_ids
        )
        member_ids = self._get_all_member_ids_from_team_member_ids_dtos(
            team_member_ids_dtos=team_member_ids_dtos
        )
        member_dtos = self._get_members_dtos_from_service(
            member_ids=member_ids
        )
        team_details_dtos = TeamWithMembersDetailsDTO(
            total_teams=total_teams,
            team_dtos=team_dtos,
            team_member_ids_dtos=team_member_ids_dtos,
            member_dtos=member_dtos
        )
        return team_details_dtos

    @staticmethod
    def _is_invalid_limit(limit: int):
        is_invalid_limit = limit <= 0
        if is_invalid_limit:
            raise InvalidLimit()

    @staticmethod
    def _is_invalid_offset(offset: int):
        is_invalid_offset = offset < 0
        if is_invalid_offset:
            raise InvalidOffset()

    @staticmethod
    def _get_team_ids_from_team_dtos(
            team_dtos: List[BasicTeamDTO]
    ) -> List[str]:
        team_ids = [
            team_dto.team_id for team_dto in team_dtos
        ]
        return team_ids

    @staticmethod
    def _get_all_member_ids_from_team_member_ids_dtos(
            team_member_ids_dtos: List[TeamMembersDTO]
    ):
        member_ids = []
        for team_member_ids_dto in team_member_ids_dtos:
            member_ids.extend(team_member_ids_dto.member_ids)
        unique_member_ids = list(set(member_ids))
        unique_member_ids.sort()
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
            user_dtos: List[BasicUserDTO]
    ) -> List[MemberDTO]:
        member_dtos = [
            MemberDTO(member_id=user_dto.user_id,
                      name=user_dto.name,
                      profile_pic_url=user_dto.profile_pic_url
                      ) for user_dto in user_dtos
        ]
        return member_dtos
