from unittest.mock import Mock

import pytest


class TestGetTeamMemberLevelsWithMembersInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.level_storage_interface import \
            TeamMemberLevelStorageInterface
        storage = create_autospec(TeamMemberLevelStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
            GetTeamMemberLevelsWithMembersPresenterInterface
        presenter = create_autospec(
            GetTeamMemberLevelsWithMembersPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_iam.interactors.get_team_member_levels_with_members_interactor import \
            GetTeamMemberLevelsWithMembersInteractor
        interactor = GetTeamMemberLevelsWithMembersInteractor(
            team_member_level_storage=storage_mock)
        return interactor

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor, mocker
    ):
        # Arrange
        # TODO: For all methods assert with proper parameters in assert
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_presenter_prepare_success_response_for_team_member_levels_with_members = \
            Mock()

        from ib_iam.tests.common_fixtures.interactors import \
            prepare_get_team_member_levels_mock
        from ib_iam.tests.common_fixtures.interactors import \
            prepare_get_team_members_of_level_hierarchy_mock
        get_team_member_levels_mock = \
            prepare_get_team_member_levels_mock(mocker)
        get_team_members_of_level_hierarchy_mock = \
            prepare_get_team_members_of_level_hierarchy_mock(mocker)

        presenter_mock.prepare_success_response_for_team_member_levels_with_members.return_value = \
            expected_presenter_prepare_success_response_for_team_member_levels_with_members

        # Act
        response = interactor.get_team_member_levels_with_members_wrapper(
            team_id=team_id, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_prepare_success_response_for_team_member_levels_with_members

        storage_mock.get_member_id_with_subordinate_member_ids_dtos. \
            assert_called_once()
        get_team_member_levels_mock.assert_called_once_with(
            team_id=team_id)
