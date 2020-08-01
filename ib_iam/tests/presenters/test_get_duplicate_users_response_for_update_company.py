from ib_iam.presenters.update_company_presenter_implementation import (
    UpdateCompanyPresenterImplementation
)
from ib_iam.constants.exception_messages import DUPLICATE_USERS_FOR_UPDATE_COMPANY


class TestRaiseExceptionForDuplicateMembers:
    def test_when_it_is_called_it_returns_http_response(self):
        json_presenter = UpdateCompanyPresenterImplementation()
        import json
        expected_response = DUPLICATE_USERS_FOR_UPDATE_COMPANY[0]
        expected_res_status = DUPLICATE_USERS_FOR_UPDATE_COMPANY[1]
        expected_http_status_code = 400

        result = json_presenter.get_duplicate_users_response_for_update_company()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
