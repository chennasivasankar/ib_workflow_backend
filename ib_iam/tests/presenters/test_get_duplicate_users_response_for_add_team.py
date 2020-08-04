import json
from ib_iam.presenters.team_presenter_implementation import (
    TeamPresenterImplementation
)
from ib_iam.constants.exception_messages import (
    DUPLICATE_USER_IDS_FOR_ADD_TEAM
)


class TestRaiseExceptionForDuplicateUserIdsForAddTeam:
    def test_whether_it_returns_duplicate_users_exception_http_response(self):
        json_presenter = TeamPresenterImplementation()
        user_ids = ["1", "2"]
        expected_response = DUPLICATE_USER_IDS_FOR_ADD_TEAM[0] % user_ids
        expected_res_status = DUPLICATE_USER_IDS_FOR_ADD_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        from ib_iam.exceptions.custom_exceptions import DuplicateUserIds
        result = json_presenter.get_duplicate_users_response_for_add_team(
            exception=DuplicateUserIds(user_ids=user_ids)
        )
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
