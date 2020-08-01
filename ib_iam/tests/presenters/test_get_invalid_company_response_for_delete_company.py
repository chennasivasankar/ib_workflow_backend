from ib_iam.presenters.delete_company_presenter_implementation import (
    DeleteCompanyPresenterImplementation
)
from ib_iam.constants.exception_messages import INVALID_COMPANY_FOR_DELETE_COMPANY


class TestRaiseExceptionForInvalidCompanyId:
    def test_whether_it_returns_invalid_company_exception_response(self):
        json_presenter = DeleteCompanyPresenterImplementation()
        import json
        expected_response = INVALID_COMPANY_FOR_DELETE_COMPANY[0]
        expected_res_status = INVALID_COMPANY_FOR_DELETE_COMPANY[1]
        expected_http_status_code = 404

        result = json_presenter.get_invalid_company_response_for_delete_company()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
