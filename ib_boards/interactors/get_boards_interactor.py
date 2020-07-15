"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""
from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, UserDoNotHaveAccessToBoards
from ib_boards.interactors.dtos import GetBoardsDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetBoardsPresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetBoardsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_boards_wrapper(
            self, get_boards_dto: GetBoardsDTO,
            presenter: GetBoardsPresenterInterface):
        try:
            board_dtos = self.get_boards(
                get_boards_dto=get_boards_dto
            )
        except UserDoNotHaveAccessToBoards:
            return presenter.get_response_for_user_have_no_access_for_boards()
        except InvalidOffsetValue:
            return presenter.get_response_for_invalid_offset()
        except InvalidLimitValue:
            return presenter.get_response_for_invalid_limit()

    def get_boards(self, get_boards_dto: GetBoardsDTO):
        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()
        user_id = get_boards_dto.user_id
        user_role = service_adapter.user_service.get_user_role(
            user_id=user_id
        )
        self.storage.validate_user_role_with_boards_roles(
            user_role=user_role
        )
        offset = get_boards_dto.offset
        limit = get_boards_dto.limit
        if offset < 0:
            raise InvalidOffsetValue
        if limit < 1:
            raise InvalidLimitValue
        return 1
