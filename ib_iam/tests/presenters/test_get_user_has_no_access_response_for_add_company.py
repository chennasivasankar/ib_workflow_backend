import json
from ib_iam.presenters.add_company_presenter_implementation import (
    AddCompanyPresenterImplementation
)
from ib_iam.constants.exception_messages import (
    USER_HAS_NO_ACCESS_FOR_ADD_COMPANY
)


class TestRaiseExceptionForUserHasNoAccessForAddCompany:
    def test_when_it_is_called_it_returns_http_response(self):
        json_presenter = AddCompanyPresenterImplementation()
        expected_response = USER_HAS_NO_ACCESS_FOR_ADD_COMPANY[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_ADD_COMPANY[1]
        expected_http_status_code = 401

        result = \
            json_presenter.get_user_has_no_access_response_for_add_company()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
