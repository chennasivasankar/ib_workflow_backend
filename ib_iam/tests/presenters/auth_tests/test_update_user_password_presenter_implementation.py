import json

from ib_iam.constants.enums import StatusCode
from ib_iam.presenters.update_user_password_presenter_implementation import \
    UpdateUserPasswordPresenterImplementation


class TestUpdateUserPasswordPresenterImplementation:
    def test_whether_it_returns_update_user_password_success_response(self):
        json_presenter = UpdateUserPasswordPresenterImplementation()
        expected_response = {}

        result = json_presenter.get_success_response_for_update_user_password()

        actual_response = json.loads(result.content)
        assert actual_response == expected_response

    def test_whether_it_returns_invalid_new_password_exception_response(self):
        json_presenter = UpdateUserPasswordPresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_NEW_PASSWORD
        expected_response = INVALID_NEW_PASSWORD[0]
        expected_res_status = INVALID_NEW_PASSWORD[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.response_for_invalid_new_password_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_invalid_current_password_exception_response(
            self):
        json_presenter = UpdateUserPasswordPresenterImplementation()
        from ib_iam.constants.exception_messages import \
            INVALID_CURRENT_PASSWORD
        expected_response = INVALID_CURRENT_PASSWORD[0]
        expected_res_status = INVALID_CURRENT_PASSWORD[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.response_for_invalid_current_password_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_current_password_mismatch_exception_response(
            self):
        json_presenter = UpdateUserPasswordPresenterImplementation()
        from ib_iam.constants.exception_messages import \
            CURRENT_PASSWORD_MISMATCH
        expected_response = CURRENT_PASSWORD_MISMATCH[0]
        expected_res_status = CURRENT_PASSWORD_MISMATCH[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.response_for_current_password_mismatch_exception()

        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
