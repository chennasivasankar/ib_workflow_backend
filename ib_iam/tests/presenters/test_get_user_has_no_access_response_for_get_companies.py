import json

from ib_iam.presenters.get_companies_presenter_implementation import GetCompaniesPresenterImplementation


class TestGetUserHasNoAccessResponseForGetCompanies:
    def test_it_returns_user_has_no_access_for_get_comapnies_response(self):
        from ib_iam.constants.exception_messages import USER_HAS_NO_ACCESS_FOR_GET_COMPANIES

        json_presenter = GetCompaniesPresenterImplementation()
        expected_response = USER_HAS_NO_ACCESS_FOR_GET_COMPANIES[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_GET_COMPANIES[1]
        expected_http_status_code = 401

        result = \
            json_presenter.get_user_has_no_access_response_for_get_companies()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
