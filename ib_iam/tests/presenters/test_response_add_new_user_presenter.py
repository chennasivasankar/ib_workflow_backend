import json

from ib_iam.constants.enums import StatusCode
from ib_iam.presenters.presenter_implementation import PresenterImplementation


class TestResponseAddNewUser:
    def test_raise_invalid_name_exception(self):
        # Arrange
        presenter = PresenterImplementation()
        from ib_iam.constants.exception_messages import EMPTY_NAME_IS_INVALID
        expected_response = EMPTY_NAME_IS_INVALID[0]
        response_status_code = EMPTY_NAME_IS_INVALID[1]

        # Act
        response_object = presenter.raise_invalid_name_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_name_should_not_contain_special_characters_exception(self):
        # Arrange
        presenter = PresenterImplementation()
        from ib_iam.constants.exception_messages \
            import NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS
        expected_response = \
            NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[0]
        response_status_code = \
            NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[1]

        # Act
        response_object = presenter. \
            raise_name_should_not_contain_special_characters_exception()

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
        response_object = presenter. \
            raise_user_account_already_exist_with_this_email_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_create_user_accout_response_returns_response(self):
        # Arrange
        presenter = PresenterImplementation()
        from ib_iam.constants.exception_messages \
            import CREATE_USER_SUCCESSFULLY
        expected_response = CREATE_USER_SUCCESSFULLY[0]
        response_status_code = CREATE_USER_SUCCESSFULLY[1]

        # Act
        response_object = presenter.user_created_response()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.SUCCESS_CREATE.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response
