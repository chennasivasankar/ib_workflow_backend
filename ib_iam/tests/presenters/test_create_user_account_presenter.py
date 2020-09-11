import pytest

from ib_iam.constants.enums import StatusCode


class TestCreateUserAccountPresenter:
    @pytest.fixture
    def presenter_mock(self):
        from ib_iam.presenters.auth_presenter_implementation import \
            CreateUserAccountPresenterImplementation
        presenter = CreateUserAccountPresenterImplementation()
        return presenter

    def test_raise_account_already_exists_exception(self, presenter_mock):
        import json
        from ib_iam.presenters.auth_presenter_implementation import \
            ACCOUNT_ALREADY_EXISTS
        response_dict = {
            "response": ACCOUNT_ALREADY_EXISTS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ACCOUNT_ALREADY_EXISTS[1]
        }

        response = presenter_mock.raise_account_already_exists_exception()

        actual_response_content = json.loads(response.content)
        assert response_dict == actual_response_content

    def test_raise_password_not_matched_with_criteria_exception(
            self, presenter_mock):
        import json
        from ib_iam.presenters.auth_presenter_implementation import \
            PASSWORD_DOES_NOT_MATCH_CRITERIA
        response_dict = {
            "response": PASSWORD_DOES_NOT_MATCH_CRITERIA[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": PASSWORD_DOES_NOT_MATCH_CRITERIA[1]
        }

        response = presenter_mock.raise_password_not_matched_with_criteria_exception()

        actual_response_content = json.loads(response.content)
        assert response_dict == actual_response_content

    def test_raise_invalid_email_exception(self, presenter_mock):
        import json
        from ib_iam.presenters.auth_presenter_implementation import \
            INVALID_EMAIL
        response_dict = {
            "response": INVALID_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_EMAIL[1]
        }

        response = presenter_mock.response_for_invalid_email_exception()

        actual_response_content = json.loads(response.content)
        assert response_dict == actual_response_content

    def test_raise_invalid_domain_exception(self, presenter_mock):
        import json
        from ib_iam.presenters.auth_presenter_implementation import \
            INVALID_DOMAIN
        response_dict = {
            "response": INVALID_DOMAIN[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_DOMAIN[1]
        }

        response = presenter_mock.raise_invalid_domain_exception()

        actual_response_content = json.loads(response.content)
        assert response_dict == actual_response_content

    def test_get_response_for_create_user_account(self, presenter_mock):
        response = presenter_mock.get_response_for_create_user_account()

        assert response.status_code == 200

    def test_raise_invalid_name_length_exception(self, presenter_mock):
        from ib_iam.constants.exception_messages import \
            INVALID_NAME_LENGTH
        from ib_iam.constants.config import MINIMUM_USER_NAME_LENGTH
        import json
        response_dict = {
            "response": INVALID_NAME_LENGTH[0].format(
                minimum_name_length=MINIMUM_USER_NAME_LENGTH
            ),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_NAME_LENGTH[1]
        }

        response = presenter_mock.response_for_invalid_name_length_exception()

        actual_response_content = json.loads(response.content)
        assert response_dict == actual_response_content

    def test_raise_name_should_not_contain_special_characters_exception(
            self, presenter_mock):
        import json
        from ib_iam.constants.exception_messages import \
            NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS
        response_dict = {
            "response":
                NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status":
                NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[1]
        }

        response = presenter_mock.response_for_name_contains_special_character_exception()

        actual_response_content = json.loads(response.content)
        assert response_dict == actual_response_content
