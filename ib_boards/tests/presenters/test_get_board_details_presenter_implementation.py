"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
import json

from ib_boards.presenters.presenter_implementation import \
    GetBoardsDetailsPresenterImplementation


class TestGetBoardsDetailsPresenterImplementation:

    def test_get_response_for_invalid_board_ids(self):
        # Arrange
        board_ids = ['BOARD_ID_1', 'BOARD_ID_1']
        from ib_boards.exceptions.custom_exceptions import InvalidBoardIds
        error = InvalidBoardIds(board_ids=board_ids)
        from ib_boards.constants.exception_messages import \
            INVALID_BOARD_IDS
        expected_response = INVALID_BOARD_IDS[0] + f': {board_ids}'
        expected_http_status_code = 404
        expected_res_status = INVALID_BOARD_IDS[1]
        presenter = GetBoardsDetailsPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_invalid_board_ids(
            error=error
        )

        # Assert
        actual_response_content = json.loads(actual_response.content)

        assert actual_response_content['response'] == expected_response
        assert actual_response_content[
                   'http_status_code'] == expected_http_status_code
        assert actual_response_content['res_status'] == expected_res_status

    def test_get_response_for_board_details(self, snapshot):
        # Arrange
        total_boards = 3
        from ib_boards.tests.factories.storage_dtos import BoardDTOFactory
        BoardDTOFactory.reset_sequence()
        board_dtos = BoardDTOFactory.create_batch(3)

        presenter = GetBoardsDetailsPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_board_details(
            board_dtos=board_dtos
        )

        # Assert
        actual_response_content = json.loads(actual_response.content)

        snapshot.assert_match(actual_response_content, 'board_details')
