import json
from ib_iam.presenters.add_company_presenter_implementation import (
    AddCompanyPresenterImplementation
)
from ib_iam.constants.exception_messages import (
    DUPLICATE_USERS_FOR_ADD_COMPANY
)


class TestRaiseExceptionForDuplicateUsersForAddCompany:
    def test_whether_it_returns_duplicate_users_exception_http_response(self):
        json_presenter = AddCompanyPresenterImplementation()
        expected_response = DUPLICATE_USERS_FOR_ADD_COMPANY[0]
        expected_res_status = DUPLICATE_USERS_FOR_ADD_COMPANY[1]
        expected_http_status_code = 400

        result = json_presenter.get_duplicate_users_response_for_add_company()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
