import json

from ib_iam.constants.enums import StatusCode
from ib_iam.presenters.update_user_profile_presenter_implementation import \
    UpdateUserProfilePresenterImplementation


class TestUpdateUserProfilePresenterImplementation:
    def test_whether_it_returns_update_user_profile_success_response(self):
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = {}

        result = json_presenter.get_success_response_for_update_user_profile()

        actual_response = json.loads(result.content)
        assert actual_response == expected_response

    def test_whether_it_returns_empty_name_exception_response(self):
        from ib_iam.constants.exception_messages import EMPTY_NAME_IS_INVALID
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = EMPTY_NAME_IS_INVALID[0]
        expected_res_status = EMPTY_NAME_IS_INVALID[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.get_response_for_empty_name_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_minimum_name_length_exception_response(self):
        from ib_iam.constants.exception_messages import \
            NAME_MINIMUM_LENGTH_SHOULD_BE_FIVE_OR_MORE
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = NAME_MINIMUM_LENGTH_SHOULD_BE_FIVE_OR_MORE[0]
        expected_res_status = NAME_MINIMUM_LENGTH_SHOULD_BE_FIVE_OR_MORE[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.get_response_for_minimum_name_length()

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
            NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS
        json_presenter = UpdateUserProfilePresenterImplementation()
        expected_response = \
            NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[0]
        expected_res_status = \
            NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter \
            .get_response_for_name_contains_special_chars_and_numbers_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
