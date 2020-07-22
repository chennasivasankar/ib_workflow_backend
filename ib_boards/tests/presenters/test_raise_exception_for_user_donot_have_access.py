from ib_boards.constants.exception_messages import USER_DONOT_HAVE_ACCESS
from ib_boards.presenters.presenter_implementation import PresenterImplementation


class TestUserDonotHaveAccess:

    def test_raise_exception_for_user_donot_have_access_to_the_board_raises_exception(self):
        # Arrange
        presenter = PresenterImplementation()
        exception_message: str = USER_DONOT_HAVE_ACCESS[0]
        exception_res_status = USER_DONOT_HAVE_ACCESS[1]

        # Act
        response_object = presenter.response_for_user_donot_have_access_for_board()

        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 403
        assert response['res_status'] == exception_res_status
        assert response['response'] == exception_message
