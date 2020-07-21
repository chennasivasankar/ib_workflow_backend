"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""


def get_board_details_mock(mocker):
    mock = mocker.patch(
        'ib_boards.interactors.get_board_details_interactor.GetBoardsDetailsInteractor.get_boards_details'
    )
    from ib_boards.tests.factories.storage_dtos import BoardDTOFactory
    mock.return_value = BoardDTOFactory.create_batch(3)
    return mock
