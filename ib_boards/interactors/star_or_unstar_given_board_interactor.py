from ib_boards.exceptions.custom_exceptions import InvalidBoardId
from ib_boards.interactors.dtos import StarOrUnstarParametersDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class StarOrUnstarBoardInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def star_or_unstar_board_wrapper(self,
                                     parameters: StarOrUnstarParametersDTO,
                                     presenter: PresenterInterface):
        try:
            self.star_or_unstar_board(parameters)
        except InvalidBoardId:
            presenter.response_for_invalid_board_id()

    def star_or_unstar_board(self, parameters):
        board_id = parameters.board_id
        is_starred = parameters.is_starred
        is_exists = self.storage.validate_board_id(board_id)
        does_not_exists = not is_exists
        if does_not_exists:
            raise InvalidBoardId

        if is_starred:
            self.storage.unstar_given_board(parameters)
        else:
            self.storage.star_given_board(parameters)
