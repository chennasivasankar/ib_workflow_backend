import pytest
from mock import create_autospec, Mock


class TestDeleteTeam:

    @pytest.fixture
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        return create_autospec(UserStorageInterface)

    @pytest.fixture
    def team_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.team_storage_interface import (
            TeamStorageInterface)
        return create_autospec(TeamStorageInterface)

    @pytest.fixture
    def presenter(self):
        from ib_iam.interactors.presenter_interfaces.delete_team_presenter_interface import (
            DeleteTeamPresenterInterface)
        return create_autospec(DeleteTeamPresenterInterface)

    @pytest.fixture
    def interactor(self, team_storage_mock, user_storage_mock):
        from ib_iam.interactors.team_interactor import TeamInteractor
        return TeamInteractor(
            team_storage=team_storage_mock,
            user_storage=user_storage_mock
        )

    def test_if_user_not_admin_raises_unauthorized_exception(
            self, interactor, team_storage_mock, user_storage_mock, presenter
    ):
        # Arrange
        user_id = "1"
        user_storage_mock.is_user_admin.return_value = False
        presenter.response_for_user_has_no_access_exception \
            .side_effect = Mock()

        # Act
        interactor.delete_team_wrapper(
            user_id=user_id, team_id="1", presenter=presenter
        )

        # Assert
        user_storage_mock.is_user_admin.assert_called_once_with(
            user_id=user_id)
        presenter.response_for_user_has_no_access_exception \
            .assert_called_once()

    def test_if_invalid_team_id_raises_not_found_exception(
            self, interactor, team_storage_mock, user_storage_mock, presenter
    ):
        # Arrange
        user_id = "1"
        team_id = "1"
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        team_storage_mock.raise_exception_if_team_not_exists.side_effect = \
            InvalidTeamId
        presenter.response_for_invalid_team_id_exception \
            .side_effect = Mock()

        # Act
        interactor.delete_team_wrapper(
            user_id=user_id, team_id=team_id, presenter=presenter
        )

        # Assert
        team_storage_mock.raise_exception_if_team_not_exists \
            .assert_called_once_with(team_id=team_id)
        presenter.response_for_invalid_team_id_exception \
            .assert_called_once()

    def test_given_valid_details_deletion_will_happen(
            self, interactor, team_storage_mock, user_storage_mock, presenter
    ):
        # Arrange
        user_id = "1"
        team_id = "1"
        presenter.get_success_response_for_delete_team.return_value = Mock()

        # Act
        interactor.delete_team_wrapper(
            user_id=user_id, team_id=team_id, presenter=presenter
        )

        # Assert
        team_storage_mock.delete_team.assert_called_once_with(
            team_id=team_id)
        presenter.get_success_response_for_delete_team.assert_called_once()
