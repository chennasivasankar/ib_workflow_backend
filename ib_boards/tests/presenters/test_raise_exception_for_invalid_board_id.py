from ib_boards.constants.exception_messages import INVALID_BOARD_ID
from ib_boards.presenters.presenter_implementation import PresenterImplementation


class TestInvalidBoardId:

    def test_raise_exception_for_invalid_board_id_raises_exception(self):
        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_BOARD_ID[0]
        exception_res_status = INVALID_BOARD_ID[1]

        # Act
        response_object = presenter.raise_exception_for_invalid_board_id()

        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 404
        assert response['res_status'] == exception_res_status
        assert response['response'] == exception_message
