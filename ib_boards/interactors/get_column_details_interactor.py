from ib_boards.exceptions.custom_exceptions import InvalidBoardId, InvalidOffsetValue, InvalidLimitValue, \
    UserDonotHaveAccess
from ib_boards.interactors.dtos import ColumnParametersDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import StorageInterface


class GetColumnDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_details_wrapper(self, presenter: PresenterInterface,
                                   columns_parameters: ColumnParametersDTO):
        try:
            self.get_column_details(columns_parameters=columns_parameters)
        except InvalidBoardId:
            presenter.raise_exception_for_invalid_board_id()
        except InvalidOffsetValue:
            presenter.raise_exception_for_invalid_offset_value()
        except InvalidLimitValue:
            presenter.raise_exception_for_invalid_limit_value()
        except UserDonotHaveAccess:
            presenter.raise_exception_for_user_donot_have_access_for_board()

    def get_column_details(self, columns_parameters: ColumnParametersDTO):
        board_id = columns_parameters.board_id
        offset = columns_parameters.offset
        limit = columns_parameters.limit
        user_id = columns_parameters.user_id

        self._validate_offset_value(offset=offset)
        self._validate_limit_value(limit=limit)
        self._validate_board_id(board_id=board_id)
        self._validate_if_user_has_permissions_for_given_board_id(
            board_id=board_id, user_id=user_id)

        column_ids = self.storage.get_column_ids_for_board(
            board_id=board_id, user_id=user_id)
        column_dtos = self.storage.get_columns_details(column_ids=column_ids)

    def _validate_if_user_has_permissions_for_given_board_id(self,
                                                             board_id: str,
                                                             user_id: str):
        is_permitted = self.storage.check_if_user_has_permissions_for_board_id(
            board_id=board_id, user_id=user_id
        )
        is_not_permitted = not is_permitted
        if is_not_permitted:
            raise UserDonotHaveAccess

    @staticmethod
    def _validate_offset_value(offset: int):
        if offset < 0:
            raise InvalidOffsetValue
        return

    @staticmethod
    def _validate_limit_value(limit: int):
        if limit <= 0:
            raise InvalidLimitValue

    def _validate_board_id(self, board_id: str):
        is_valid = self.storage.validate_board_id(board_id=board_id)
        is_invalid = not is_valid

        if is_invalid:
            raise InvalidBoardId
