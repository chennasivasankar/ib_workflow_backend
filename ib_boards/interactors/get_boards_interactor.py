"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Tuple

from ib_boards.adapters.iam_service import InvalidProjectIdsException, \
    UserIsNotInProjectException
from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, UserDoNotHaveAccessToBoards, \
    OffsetValueExceedsTotalTasksCount
from ib_boards.interactors.dtos import GetBoardsDTO, StarredAndOtherBoardsDTO
from ib_boards.interactors.mixins.validation_mixins import ValidationMixin
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetBoardsPresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import BoardDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetBoardsInteractor(ValidationMixin):

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_boards_wrapper(
            self, get_boards_dto: GetBoardsDTO,
            presenter: GetBoardsPresenterInterface):
        try:
            starred_and_other_boards_dto, total_boards = self.get_boards(
                get_boards_dto=get_boards_dto
            )
        except UserDoNotHaveAccessToBoards:
            return presenter.get_response_for_user_have_no_access_for_boards()
        except InvalidOffsetValue:
            return presenter.get_response_for_invalid_offset()
        except InvalidLimitValue:
            return presenter.get_response_for_invalid_limit()
        except OffsetValueExceedsTotalTasksCount:
            return presenter.get_response_for_offset_exceeds_total_tasks()
        except InvalidProjectIdsException as err:
            return presenter.get_response_for_invalid_project_id(error=err)
        except UserIsNotInProjectException:
            return presenter.get_response_for_user_is_not_in_project()

        return presenter.get_response_for_get_boards(
            starred_and_other_boards_dto=starred_and_other_boards_dto,
            total_boards=total_boards
        )

    def get_boards(self, get_boards_dto: GetBoardsDTO):
        project_id = get_boards_dto.project_id
        project_ids = [project_id]
        user_id = get_boards_dto.user_id
        self.validate_given_project_ids(project_ids=project_ids)

        self.validate_if_user_is_in_project(project_id=project_id,
                                            user_id=user_id)

        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = get_boards_dto.user_id
        user_role = service_adapter.user_service.get_user_roles(
            user_id=user_id)
        self.storage.validate_user_role_with_boards_roles(user_role=user_role)

        limit, offset = self._pagination_validations(get_boards_dto)

        all_boards_details_dtos, total_boards = self._get_all_boards_details_dtos(
            limit, offset, project_id, user_id)
        return all_boards_details_dtos, total_boards

    def _get_all_boards_details_dtos(self, limit: int, offset: int,
                                     project_id: str, user_id: str) -> \
            Tuple[StarredAndOtherBoardsDTO, int]:
        other_boards_ids, starred_board_ids = self.storage.get_board_ids(
            user_id=user_id, project_id=project_id
        )
        all_board_ids = other_boards_ids + starred_board_ids
        total_boards = len(all_board_ids)
        if offset >= total_boards:
            raise OffsetValueExceedsTotalTasksCount

        board_ids = all_board_ids[offset:offset + limit]
        all_boards_details_dtos = self._get_board_details_dtos(
            board_ids, other_boards_ids, starred_board_ids)

        return all_boards_details_dtos, total_boards

    def _get_board_details_dtos(self, board_ids: List[str],
                                other_boards_ids: List[str],
                                starred_board_ids: List[str]) -> \
            StarredAndOtherBoardsDTO:
        from ib_boards.interactors.get_board_details_interactor \
            import GetBoardsDetailsInteractor
        board_details_interactor = GetBoardsDetailsInteractor(
            storage=self.storage
        )
        boards_details_dtos = board_details_interactor.get_boards_details(
            board_ids=board_ids
        )
        starred_board_dtos, other_boards_dtos = self._map_starred_boards_and_all_boards(
            boards_details_dtos, starred_board_ids, other_boards_ids)
        all_boards_details_dtos = StarredAndOtherBoardsDTO(
            starred_boards_dtos=starred_board_dtos,
            other_boards_dtos=other_boards_dtos
        )
        return all_boards_details_dtos

    @staticmethod
    def _pagination_validations(get_boards_dto):
        offset = get_boards_dto.offset
        limit = get_boards_dto.limit
        if offset < 0:
            raise InvalidOffsetValue
        if limit < 0:
            raise InvalidLimitValue
        return limit, offset

    @staticmethod
    def _map_starred_boards_and_all_boards(
            boards_details_dtos: List[BoardDTO],
            starred_board_ids: List[str], other_board_ids: List[str]):
        starred_boards_dtos = []
        other_boards_dtos = []
        for board in boards_details_dtos:
            if board.board_id in starred_board_ids:
                starred_boards_dtos.append(board)
            if board.board_id in other_board_ids:
                other_boards_dtos.append(board)

        return starred_boards_dtos, other_boards_dtos
