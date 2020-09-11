import json
from ib_iam.presenters.update_team_presenter_implementation import (
    UpdateTeamPresenterImplementation)
from ib_iam.constants.exception_messages import DUPLICATE_USER_IDS_FOR_UPDATE_TEAM


class TestRaiseExceptionForDuplicateUserIdsForUpdateTeam:
    def test_when_it_is_called_it_returns_http_response(self):
        json_presenter = UpdateTeamPresenterImplementation()
        user_ids = ["1", "2"]
        expected_response = DUPLICATE_USER_IDS_FOR_UPDATE_TEAM[0] % user_ids
        expected_res_status = DUPLICATE_USER_IDS_FOR_UPDATE_TEAM[1]
        expected_http_status_code = 400

        from ib_iam.exceptions.custom_exceptions import DuplicateUserIds
        result = json_presenter.response_for_duplicate_user_ids_exception(
            err=DuplicateUserIds(user_ids=user_ids)
        )
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
