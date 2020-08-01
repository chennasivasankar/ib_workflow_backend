from ib_iam.presenters.update_company_presenter_implementation import \
    UpdateCompanyPresenterImplementation
from ib_iam.constants.exception_messages import INVALID_USERS_FOR_UPDATE_COMPANY


class TestRaiseExceptionForInvalidUsers:
    def test_whether_it_returns_invalid_users_http_response(self):
        json_presenter = UpdateCompanyPresenterImplementation()
        import json
        expected_response = INVALID_USERS_FOR_UPDATE_COMPANY[0]
        expected_res_status = INVALID_USERS_FOR_UPDATE_COMPANY[1]
        expected_http_status_code = 404

        result = json_presenter.get_invalid_users_response_for_update_company()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code