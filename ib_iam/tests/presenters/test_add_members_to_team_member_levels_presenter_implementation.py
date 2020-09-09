import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestAddMembersToTeamMemberLevelsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.add_members_to_team_member_levels_presenter_implementation import \
            AddMembersToTeamMemberLevelsPresenterImplementation
        presenter = AddMembersToTeamMemberLevelsPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_add_members_to_levels(
            self, presenter):
        # Act
        response_object = presenter. \
            prepare_success_response_for_add_members_to_team_member_levels()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS_CREATE.value

    def test_response_for_invalid_team_id(self, presenter):
        # Arrange
        from ib_iam.presenters.add_members_to_team_member_levels_presenter_implementation import \
            INVALID_TEAM_ID
        expected_response = INVALID_TEAM_ID[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_TEAM_ID[1]

        # Act
        response_obj = presenter.response_for_invalid_team_id()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_team_member_level_ids_not_found(self, presenter):
        # Arrange
        team_member_level_ids = ["1", "2"]
        from ib_iam.presenters.add_members_to_team_member_levels_presenter_implementation import \
            TEAM_MEMBER_LEVEL_IDS_NOT_FOUND
        expected_response = TEAM_MEMBER_LEVEL_IDS_NOT_FOUND[0].format(
            team_member_level_ids=team_member_level_ids
        )
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = TEAM_MEMBER_LEVEL_IDS_NOT_FOUND[1]

        from ib_iam.interactors.add_members_to_team_member_levels_interactor import \
            TeamMemberLevelIdsNotFound
        error_object = TeamMemberLevelIdsNotFound(
            team_member_level_ids=team_member_level_ids
        )

        # Act
        response_obj = presenter.response_for_team_member_level_ids_not_found(
            err=error_object
        )

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_team_member_ids_not_found(self, presenter):
        # Arrange
        team_member_ids = ["1", "2"]
        from ib_iam.presenters.add_members_to_team_member_levels_presenter_implementation import \
            TEAM_MEMBER_IDS_NOT_FOUND
        expected_response = TEAM_MEMBER_IDS_NOT_FOUND[0].format(
            team_member_ids=team_member_ids
        )
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = TEAM_MEMBER_IDS_NOT_FOUND[1]

        from ib_iam.exceptions.custom_exceptions import MemberIdsNotFoundInTeam
        error_object = MemberIdsNotFoundInTeam(
            team_member_ids=team_member_ids
        )

        # Act
        response_obj = presenter.response_for_team_member_ids_not_found(
            err=error_object
        )

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status
