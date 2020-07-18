import json

from ib_iam.constants.enums import StatusCode
from ib_iam.presenters.presenter_implementation import PresenterImplementation


class TestResponseAddNewUser:
    def test_raise_invalid_name_exception(self):
        # Arrange
        presenter = PresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_NAME
        expected_response = INVALID_NAME[0]
        response_status_code = INVALID_NAME[1]

        # Act
        response_object = presenter.raise_invalid_name_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_email_exception(self):
        # Arrange
        presenter = PresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_EMAIL
        expected_response = INVALID_EMAIL[0]
        response_status_code = INVALID_EMAIL[1]

        # Act
        response_object = presenter.raise_invalid_email_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_user_account_already_exist_with_this_email_exception(self):
        # Arrange
        presenter = PresenterImplementation()
        from ib_iam.constants.exception_messages \
            import USER_ACCOUNT_ALREADY_EXIST_FOR_THIS_EMAIL
        expected_response = USER_ACCOUNT_ALREADY_EXIST_FOR_THIS_EMAIL[0]
        response_status_code = USER_ACCOUNT_ALREADY_EXIST_FOR_THIS_EMAIL[1]

        # Act
        response_object = presenter.\
            raise_user_account_already_exist_with_this_email_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response
