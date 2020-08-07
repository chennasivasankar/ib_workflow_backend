import json
from ib_iam.presenters.update_company_presenter_implementation import (
    UpdateCompanyPresenterImplementation
)
from ib_iam.constants.exception_messages import \
    INVALID_COMPANY_ID_FOR_UPDATE_COMPANY


class TestRaiseExceptionForInvalidCompanyIdForUpdateCompany:
    def test_whether_it_returns_error_object(self):
        json_presenter = UpdateCompanyPresenterImplementation()
        expected_response = INVALID_COMPANY_ID_FOR_UPDATE_COMPANY[0]
        expected_res_status = INVALID_COMPANY_ID_FOR_UPDATE_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        result = json_presenter.get_invalid_company_response_for_update_company()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
