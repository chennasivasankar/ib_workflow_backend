from unittest.mock import Mock

import pytest


class TestGetTeamMemberLevelsInteractor:

    @pytest.fixture()
    def team_member_level_storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
            TeamMemberLevelStorageInterface
        storage = create_autospec(TeamMemberLevelStorageInterface)
        return storage

    @pytest.fixture()
    def user_storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
            GetTeamMemberLevelsPresenterInterface
        presenter = create_autospec(GetTeamMemberLevelsPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, team_member_level_storage_mock, user_storage_mock):
        from ib_iam.interactors.levels.get_team_member_levels_interactor import \
            GetTeamMemberLevelsInteractor
        interactor = GetTeamMemberLevelsInteractor(
            team_member_level_storage=team_member_level_storage_mock,
            user_storage=user_storage_mock
        )
        return interactor

    def test_with_user_not_admin_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_presenter_response_for_invalid_project_id_mock = Mock()
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        user_storage_mock.is_user_admin.return_value = False

        presenter_mock.response_for_user_is_not_admin_exception.return_value \
            = expected_presenter_response_for_invalid_project_id_mock

        # Act
        response = interactor.get_team_member_levels_wrapper(
            team_id=team_id, presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_project_id_mock
        user_storage_mock.is_user_admin.assert_called_with(user_id=user_id)
        presenter_mock.response_for_user_is_not_admin_exception.assert_called_once()

    def test_with_invalid_team_id_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_presenter_response_for_invalid_team_id_mock = Mock()
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        team_member_level_storage_mock.validate_team_id.side_effect = InvalidTeamId
        user_storage_mock.is_user_admin.return_value = True

        presenter_mock.response_for_invalid_team_id_exception.return_value \
            = expected_presenter_response_for_invalid_team_id_mock

        # Act
        response = interactor.get_team_member_levels_wrapper(
            team_id=team_id, presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_team_id_mock
        team_member_level_storage_mock.validate_team_id.assert_called_with(team_id=team_id)
        presenter_mock.response_for_invalid_team_id_exception.assert_called_once()

    def test_with_valid_details_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_level_details_dtos_mock = Mock()

        presenter_mock.response_for_team_member_level_details_dtos.return_value = \
            expected_presenter_response_for_level_details_dtos_mock

        user_storage_mock.is_user_admin.return_value = True

        # Act
        response = interactor.get_team_member_levels_wrapper(
            team_id=team_id, presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_response_for_level_details_dtos_mock

        presenter_mock.response_for_team_member_level_details_dtos. \
            assert_called_once()
        team_member_level_storage_mock.get_team_member_level_details_dtos.assert_called_once_with(
            team_id=team_id
        )
