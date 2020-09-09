import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestAddLevelsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.add_team_member_levels_presenter_implementation import \
            AddTeamMemberLevelsPresenterImplementation
        presenter = AddTeamMemberLevelsPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_add_levels_to_team(self, presenter):
        # Act
        response_object = presenter. \
            prepare_success_response_for_add_team_member_levels_to_team()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS_CREATE.value

    def test_response_for_invalid_team_id(self, presenter):
        # Arrange
        from ib_iam.presenters.add_team_member_levels_presenter_implementation import \
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

    def test_response_for_duplicate_level_hierarchies(self, presenter):
        # Arrange
        duplicate_level_hierarchies = [1, 2]
        from ib_iam.presenters.add_team_member_levels_presenter_implementation import \
            DUPLICATE_LEVEL_HIERARCHIES
        expected_response = DUPLICATE_LEVEL_HIERARCHIES[0].format(
            level_hierarchies=duplicate_level_hierarchies
        )
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = DUPLICATE_LEVEL_HIERARCHIES[1]

        from ib_iam.interactors.add_team_member_levels_interactor import \
            DuplicateLevelHierarchies
        error_object = DuplicateLevelHierarchies(
            level_hierarchies=duplicate_level_hierarchies
        )

        # Act
        response_obj = presenter.response_for_duplicate_level_hierarchies(
            err=error_object
        )

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_negative_level_hierarchies(self, presenter):
        # Arrange
        negative_level_hierarchies = [-1, -2]
        from ib_iam.presenters.add_team_member_levels_presenter_implementation import \
            NEGATIVE_LEVEL_HIERARCHIES
        expected_response = NEGATIVE_LEVEL_HIERARCHIES[0].format(
            level_hierarchies=negative_level_hierarchies
        )
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = NEGATIVE_LEVEL_HIERARCHIES[1]

        from ib_iam.interactors.add_team_member_levels_interactor import \
            NegativeLevelHierarchy
        error_object = NegativeLevelHierarchy(
            level_hierarchies=negative_level_hierarchies
        )

        # Act
        response_obj = presenter.response_for_negative_level_hierarchies(
            err=error_object
        )

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_duplicate_team_member_level_names(self, presenter):
        # Arrange
        duplicate_team_member_level_names = ["L0", "L1"]
        from ib_iam.presenters.add_team_member_levels_presenter_implementation import \
            DUPLICATE_TEAM_MEMBER_LEVEL_NAMES
        expected_response = DUPLICATE_TEAM_MEMBER_LEVEL_NAMES[0].format(
            team_member_level_names=duplicate_team_member_level_names
        )
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = DUPLICATE_TEAM_MEMBER_LEVEL_NAMES[1]

        from ib_iam.interactors.add_team_member_levels_interactor import \
            DuplicateTeamMemberLevelNames
        error_object = DuplicateTeamMemberLevelNames(
            team_member_level_names=duplicate_team_member_level_names
        )

        # Act
        response_obj = presenter.response_for_duplicate_team_member_level_names(
            err=error_object
        )

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status
