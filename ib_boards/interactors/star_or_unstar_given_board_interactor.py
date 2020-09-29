from ib_boards.constants.enum import StartAction
from ib_boards.exceptions.custom_exceptions import InvalidBoardId
from ib_boards.interactors.dtos import StarOrUnstarParametersDTO
from ib_boards.interactors.mixins.validation_mixins import ValidationMixin
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class StarOrUnstarBoardInteractor(ValidationMixin):
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def star_or_unstar_board_wrapper(self,
                                     parameters: StarOrUnstarParametersDTO,
                                     presenter: PresenterInterface):
        try:
            self.star_or_unstar_board(parameters)
        except InvalidBoardId:
            return presenter.response_for_invalid_board_id()

    def star_or_unstar_board(self, parameters):
        board_id = parameters.board_id
        action = parameters.action
        self.validate_board_id(board_id)

        if action == StartAction.STAR.value:
            self.storage.star_given_board(parameters)

        elif action == StartAction.UNSTAR.value:
            self.storage.unstar_given_board(parameters)
