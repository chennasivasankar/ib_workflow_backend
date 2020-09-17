import pytest
import json


class TestAddTeamPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_iam.presenters.add_team_presenter_implementation import \
            AddTeamPresenterImplementation
        return AddTeamPresenterImplementation()

    def test_given_team_id_it_return_http_response_with_team_id(
            self, presenter
    ):
        # Arrange
        team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        expected_json_response = {"team_id": team_id}

        # Act
        http_response = presenter.get_response_for_add_team(
            team_id=team_id
        )

        # Assert
        actual_json_response = json.loads(http_response.content)
        assert actual_json_response == expected_json_response

    def test_whether_it_returns_team_name_already_exists_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            TEAM_NAME_ALREADY_EXISTS_FOR_ADD_TEAM
        )
        from ib_iam.exceptions.custom_exceptions import TeamNameAlreadyExists
        team_name = "team_name1"
        expected_response = TEAM_NAME_ALREADY_EXISTS_FOR_ADD_TEAM[
            0].format(team_name=team_name)
        expected_res_status = TEAM_NAME_ALREADY_EXISTS_FOR_ADD_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.response_for_team_name_already_exists_exception(
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

    def test_whether_it_returns_user_has_no_access_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            USER_HAS_NO_ACCESS_FOR_ADD_TEAM
        )
        expected_response = USER_HAS_NO_ACCESS_FOR_ADD_TEAM[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_ADD_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.UNAUTHORIZED.value

        # Act
        result = presenter.response_for_user_has_no_access_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_invalid_users_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            INVALID_USER_IDS_FOR_ADD_TEAM
        expected_response = INVALID_USER_IDS_FOR_ADD_TEAM[0]
        expected_res_status = INVALID_USER_IDS_FOR_ADD_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        # Act
        result = presenter.response_for_invalid_user_ids_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_duplicate_users_exception_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            DUPLICATE_USER_IDS_FOR_ADD_TEAM
        expected_response = DUPLICATE_USER_IDS_FOR_ADD_TEAM[0]
        expected_res_status = DUPLICATE_USER_IDS_FOR_ADD_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.response_for_duplicate_user_ids_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
