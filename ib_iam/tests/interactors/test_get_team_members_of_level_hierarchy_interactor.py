from unittest.mock import Mock

import pytest


class TestGetTeamMembersOfLevelHierarchyInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
            TeamMemberLevelStorageInterface
        storage = create_autospec(TeamMemberLevelStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.presenter_interfaces.level_presenter_interface \
            import GetTeamMembersOfLevelHierarchyPresenterInterface
        presenter = create_autospec(
            GetTeamMembersOfLevelHierarchyPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_iam.interactors.get_team_members_of_level_hierarchy_interactor import \
            GetTeamMembersOfLevelHierarchyInteractor
        interactor = GetTeamMembersOfLevelHierarchyInteractor(
            team_member_level_storage=storage_mock)
        return interactor

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 0

        expected_presenter_prepare_success_response_for_get_team_members_of_level_hierarchy = Mock()

        presenter_mock.prepare_success_response_for_get_team_members_of_level_hierarchy. \
            return_value = expected_presenter_prepare_success_response_for_get_team_members_of_level_hierarchy

        # Act
        response = interactor.get_team_members_of_level_hierarchy_wrapper(
            team_id=team_id, level_hierarchy=level_hierarchy,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_prepare_success_response_for_get_team_members_of_level_hierarchy

        presenter_mock.prepare_success_response_for_get_team_members_of_level_hierarchy. \
            assert_called_once()
        storage_mock.get_member_details.assert_called_once_with(
            team_id=team_id, level_hierarchy=level_hierarchy
        )
