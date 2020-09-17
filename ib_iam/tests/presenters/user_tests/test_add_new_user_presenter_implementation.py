import json
import pytest

from ib_iam.constants.enums import StatusCode


class TestResponseAddNewUser:

    @pytest.fixture
    def presenter(self):
        from ib_iam.presenters.add_new_user_presenter_implementation \
            import AddUserPresenterImplementation
        return AddUserPresenterImplementation()

    def test_raise_name_should_not_contain_special_characters_exception(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages \
            import NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS
        expected_response = \
            NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[0]
        response_status_code = \
            NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[1]

        # Act
        response_object = presenter. \
            response_for_name_contains_special_character_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_name_length_should_be_exception_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import INVALID_NAME_LENGTH
        from ib_iam.constants.config import MINIMUM_USER_NAME_LENGTH
        expected_response = INVALID_NAME_LENGTH[0].format(
            minimum_name_length=MINIMUM_USER_NAME_LENGTH)
        response_status_code = INVALID_NAME_LENGTH[1]

        # Act
        response_object = presenter.response_for_invalid_name_length_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_email_exception(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import INVALID_EMAIL
        expected_response = INVALID_EMAIL[0]
        response_status_code = INVALID_EMAIL[1]

        # Act
        response_object = presenter.response_for_invalid_email_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_user_account_already_exist_with_this_email_exception(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages \
            import USER_ALREADY_EXIST_WITH_THIS_EMAIL
        expected_response = USER_ALREADY_EXIST_WITH_THIS_EMAIL[0]
        response_status_code = USER_ALREADY_EXIST_WITH_THIS_EMAIL[1]

        # Act
        response_object = presenter. \
            response_for_user_account_already_exists_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_create_user_account_response_returns_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            CREATE_USER_SUCCESSFULLY
        expected_response = CREATE_USER_SUCCESSFULLY[0]
        response_status_code = CREATE_USER_SUCCESSFULLY[1]

        # Act
        response_object = presenter.response_for_add_user_response()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.SUCCESS_CREATE.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response
