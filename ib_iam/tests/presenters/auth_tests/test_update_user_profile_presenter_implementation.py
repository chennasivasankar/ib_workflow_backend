import json

from ib_iam.constants.enums import StatusCode
from ib_iam.presenters.update_user_profile_presenter_implementation import \
    UpdateUserProfilePresenterImplementation


class TestUpdateUserProfilePresenterImplementation:
    def test_whether_it_returns_update_user_profile_success_response(self):
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = {}

        result = json_presenter.get_response_for_update_user_profile()

        actual_response = json.loads(result.content)
        assert actual_response == expected_response

    def test_whether_it_returns_minimum_name_length_exception_response(self):
        from ib_iam.constants.exception_messages import \
            INVALID_NAME_LENGTH
        from ib_iam.constants.enums import StatusCode
        json_presenter = UpdateUserProfilePresenterImplementation()
        from ib_iam.constants.config import MINIMUM_USER_NAME_LENGTH
        expected_response = INVALID_NAME_LENGTH[0].format(
            minimum_name_length=MINIMUM_USER_NAME_LENGTH)
        expected_res_status = INVALID_NAME_LENGTH[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.response_for_invalid_name_length_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_name_contains_numbers_or_special_chars_exception_response(
            self):
        from ib_iam.constants.exception_messages import \
            NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = \
            NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[0]
        expected_res_status = \
            NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter \
            .response_for_name_contains_special_character_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_invalid_email_exception_response(self):
        from ib_iam.constants.exception_messages import INVALID_EMAIL
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = INVALID_EMAIL[0]
        expected_res_status = INVALID_EMAIL[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.response_for_invalid_email_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_email_already_in_use_exception_response(self):
        from ib_iam.constants.exception_messages import EMAIL_ALREADY_IN_USE
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = EMAIL_ALREADY_IN_USE[0]
        expected_res_status = EMAIL_ALREADY_IN_USE[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.response_for_email_already_exists_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_invalid_role_ids_exception_response(self):
        from ib_iam.constants.exception_messages import INVALID_ROLE_IDS
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = INVALID_ROLE_IDS[0]
        expected_res_status = INVALID_ROLE_IDS[1]
        expected_http_status_code = StatusCode.NOT_FOUND.value

        result = json_presenter.response_for_invalid_role_ids_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_duplicate_role_ids_exception_response(self):
        from ib_iam.constants.exception_messages import \
            DUPLICATE_ROLE_IDS_FOR_UPDATE_USER_PROFILE as DUPLICATE_ROLE_IDS
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = DUPLICATE_ROLE_IDS[0]
        expected_res_status = DUPLICATE_ROLE_IDS[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.response_for_duplicate_role_ids_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code