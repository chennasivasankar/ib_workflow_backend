from ib_iam.constants.exception_messages import \
    DUPLICATE_USER_IDS_FOR_UPDATE_TEAM

from ib_iam.constants.exception_messages import INVALID_TEAM_ID_FOR_UPDATE_TEAM

from ib_iam.constants.exception_messages import \
    INVALID_USER_IDS_FOR_UPDATE_TEAM

from ib_iam.exceptions.custom_exceptions import TeamNameAlreadyExists

from ib_iam.constants.exception_messages import (
    TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM
)

import json
from ib_iam.presenters.update_team_presenter_implementation import (
    UpdateTeamPresenterImplementation
)
from ib_iam.constants.exception_messages import (
    USER_HAS_NO_ACCESS_FOR_UPDATE_TEAM
)


class TestUpdateTeamPresenterImplementation:
    def test_when_it_is_called_it_returns_empty_dict_http_response(self):
        # Arrange
        json_presenter = UpdateTeamPresenterImplementation()
        expected_response = {}

        # Act
        result = json_presenter.get_success_response_for_update_team()

        # Assert
        actual_response = json.loads(result.content)
        assert actual_response == expected_response

    def test_whether_it_returns_error_object(self, snapshot):
        # Arrange
        json_presenter = UpdateTeamPresenterImplementation()
        expected_response = INVALID_TEAM_ID_FOR_UPDATE_TEAM[0]
        expected_res_status = INVALID_TEAM_ID_FOR_UPDATE_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        # Act
        result = json_presenter.response_for_invalid_team_id_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_invalid_users_http_response(self):
        # Arrange
        json_presenter = UpdateTeamPresenterImplementation()
        expected_response = INVALID_USER_IDS_FOR_UPDATE_TEAM[0]
        expected_res_status = INVALID_USER_IDS_FOR_UPDATE_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        # Act
        result = json_presenter.response_for_invalid_user_ids_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_team_name_already_exists_http_response(self):
        # Arrange
        json_presenter = UpdateTeamPresenterImplementation()
        team_name = "team_name1"
        expected_response = TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM[0].format(
            team_name=team_name
        )
        expected_res_status = TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = json_presenter.response_for_team_name_already_exists_exception(
            err=TeamNameAlreadyExists(team_name=team_name)
        )

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_user_has_no_access_http_response(self):
        json_presenter = UpdateTeamPresenterImplementation()
        expected_response = USER_HAS_NO_ACCESS_FOR_UPDATE_TEAM[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_UPDATE_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.UNAUTHORIZED.value

        # Act
        result = json_presenter.response_for_user_has_no_access_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_when_it_is_called_it_returns_http_response(self):
        # Arrange
        json_presenter = UpdateTeamPresenterImplementation()
        expected_response = DUPLICATE_USER_IDS_FOR_UPDATE_TEAM[0]
        expected_res_status = DUPLICATE_USER_IDS_FOR_UPDATE_TEAM[1]
        expected_http_status_code = 400

        # Act
        result = json_presenter.response_for_duplicate_user_ids_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
