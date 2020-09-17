import json
import pytest


class TestGetTeamsPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_iam.presenters.team_presenter_implementation import (
            GetTeamsPresenterImplementation
        )
        return GetTeamsPresenterImplementation()

    def test_whether_it_returns_user_has_no_access_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            USER_HAS_NO_ACCESS_FOR_GET_LIST_OF_TEAMS
        )
        expected_response = USER_HAS_NO_ACCESS_FOR_GET_LIST_OF_TEAMS[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_GET_LIST_OF_TEAMS[1]
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

    @pytest.fixture
    def teams_set_up(self):
        team_ids = [
            "f2c02d98-f311-4ab2-8673-3daa00757002",
            "aa66c40f-6d93-484a-b418-984716514c7b",
            "c982032b-53a7-4dfa-a627-4701a5230765"
        ]
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        TeamDTOFactory.reset_sequence(1)
        team_dtos = [
            TeamDTOFactory(team_id=team_id) for team_id in team_ids
        ]
        return team_dtos

    @pytest.fixture
    def team_users_set_up(self):
        team_ids = [
            "f2c02d98-f311-4ab2-8673-3daa00757002",
            "aa66c40f-6d93-484a-b418-984716514c7b",
            "c982032b-53a7-4dfa-a627-4701a5230765"
        ]
        from ib_iam.tests.factories.storage_dtos import TeamUserIdsDTOFactory
        TeamUserIdsDTOFactory.reset_sequence(1)
        team_user_ids_dtos = [
            TeamUserIdsDTOFactory(team_id=team_id) for team_id in team_ids
        ]
        return team_user_ids_dtos

    @pytest.fixture
    def users_set_up(self):
        user_ids = [
            '2bdb417e-4632-419a-8ddd-085ea272c6eb',
            '548a803c-7b48-47ba-a700-24f2ea0d1280',
            '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
            '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
        ]
        from ib_iam.tests.factories.storage_dtos import \
            BasicUserDetailsDTOFactory
        BasicUserDetailsDTOFactory.reset_sequence(1)
        user_dtos = [
            BasicUserDetailsDTOFactory(user_id=user_id) for user_id in user_ids
        ]
        return user_dtos

    @pytest.fixture()
    def teams_with_users_set_up(self, teams_set_up, team_users_set_up,
                                users_set_up):
        from ib_iam.tests.factories.presenter_dtos import \
            TeamWithMembersDetailsDTOFactory
        teams_with_members_dto = TeamWithMembersDetailsDTOFactory(
            total_teams_count=3, team_dtos=teams_set_up,
            team_user_ids_dtos=team_users_set_up, user_dtos=users_set_up
        )
        return teams_with_members_dto

    def test_given_valid_team_with_members_details_dto_returns_http_response(
            self, snapshot, teams_with_users_set_up, presenter
    ):
        # Act
        http_response = presenter.get_response_for_get_list_of_teams(
            team_details_dtos=teams_with_users_set_up
        )

        # Assert
        response = json.loads(http_response.content)
        snapshot.assert_match(response, "response")

    def test_given_zero_teams_exists_returns_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.interactors.presenter_interfaces.dtos import \
            TeamWithUsersDetailsDTO
        team_details_dtos = TeamWithUsersDetailsDTO(
            total_teams_count=0, team_dtos=[], team_user_ids_dtos=[],
            user_dtos=[]
        )

        # Act
        http_response = presenter.get_response_for_get_list_of_teams(
            team_details_dtos=team_details_dtos
        )

        # Assert
        response = json.loads(http_response.content)
        assert response == {'teams': [], 'total_teams_count': 0}

    def test_whether_it_returns_invalid_limit_exception_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            INVALID_LIMIT_FOR_GET_LIST_OF_TEAMS
        )
        expected_response = INVALID_LIMIT_FOR_GET_LIST_OF_TEAMS[0]
        expected_res_status = INVALID_LIMIT_FOR_GET_LIST_OF_TEAMS[1]
        expected_http_status_code = 400

        # Act
        result = presenter.response_for_invalid_limit_value_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_invalid_offset_exception_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            INVALID_OFFSET_FOR_GET_LIST_OF_TEAMS
        )
        expected_response = INVALID_OFFSET_FOR_GET_LIST_OF_TEAMS[0]
        expected_res_status = INVALID_OFFSET_FOR_GET_LIST_OF_TEAMS[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.response_for_invalid_offset_value_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
