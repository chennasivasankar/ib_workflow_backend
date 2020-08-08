import json
from ib_iam.presenters.update_company_presenter_implementation import \
    UpdateCompanyPresenterImplementation
from ib_iam.constants.exception_messages import INVALID_USER_IDS_FOR_UPDATE_COMPANY


class TestRaiseExceptionForInvalidUserIdsForUpdateCompany:
    def test_whether_it_returns_invalid_users_http_response(self):
        json_presenter = UpdateCompanyPresenterImplementation()
        user_ids = ["1"]
        expected_response = INVALID_USER_IDS_FOR_UPDATE_COMPANY[0] % user_ids
        expected_res_status = INVALID_USER_IDS_FOR_UPDATE_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        from ib_iam.exceptions.custom_exceptions import InvalidUserIds
        result = json_presenter.get_invalid_users_response_for_update_company(
            exception=InvalidUserIds(user_ids=user_ids)
        )
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
