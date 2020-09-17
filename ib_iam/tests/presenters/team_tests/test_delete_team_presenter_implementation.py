import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestDeleteTeamPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_iam.presenters.delete_team_presenter_implementation import \
            DeleteTeamPresenterImplementation
        return DeleteTeamPresenterImplementation()

    def test_get_success_response_for_delete_team_returns_empty_dict_response(
            self, presenter
    ):
        # Arrange
        expected_response = {}

        # Act
        result = presenter.get_success_response_for_delete_team()

        # Assert
        actual_response = json.loads(result.content)
        assert actual_response == expected_response

    def test_response_for_user_has_no_access_exception_returns_user_has_no_access_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            USER_HAS_NO_ACCESS_FOR_DELETE_TEAM
        expected_response = USER_HAS_NO_ACCESS_FOR_DELETE_TEAM[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_DELETE_TEAM[1]
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

    def test_response_for_invalid_team_id_exception_returns_invalid_team_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            INVALID_TEAM_ID_FOR_DELETE_TEAM
        expected_response = INVALID_TEAM_ID_FOR_DELETE_TEAM[0]
        expected_res_status = INVALID_TEAM_ID_FOR_DELETE_TEAM[1]
        expected_http_status_code = StatusCode.NOT_FOUND.value

        # Act
        result = presenter.response_for_invalid_team_id_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
