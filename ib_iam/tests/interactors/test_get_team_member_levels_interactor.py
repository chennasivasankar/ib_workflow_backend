from unittest.mock import Mock

import pytest


class TestGetTeamMemberLevelsInteractor:

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

        from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
            GetTeamMemberLevelsPresenterInterface
        presenter = create_autospec(GetTeamMemberLevelsPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_iam.interactors.get_team_member_levels_interactor import \
            GetTeamMemberLevelsInteractor
        interactor = GetTeamMemberLevelsInteractor(
            team_member_level_storage=storage_mock)
        return interactor

    def test_with_invalid_team_id_return_response(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_presenter_response_for_invalid_team_id_mock = Mock()

        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        storage_mock.validate_team_id.side_effect = InvalidTeamId

        presenter_mock.response_for_invalid_team_id.return_value \
            = expected_presenter_response_for_invalid_team_id_mock

        # Act
        response = interactor.get_team_member_levels_wrapper(
            team_id=team_id, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_team_id_mock
        storage_mock.validate_team_id.assert_called_with(team_id=team_id)
        presenter_mock.response_for_invalid_team_id.assert_called_once()

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_level_details_dtos_mock = Mock()

        presenter_mock.response_for_team_member_level_details_dtos.return_value = \
            expected_presenter_response_for_level_details_dtos_mock

        # Act
        response = interactor.get_team_member_levels_wrapper(
            team_id=team_id, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_level_details_dtos_mock

        presenter_mock.response_for_team_member_level_details_dtos. \
            assert_called_once()
        storage_mock.get_team_member_level_details_dtos.assert_called_once_with(
            team_id=team_id
        )
