import pytest
from mock import create_autospec, Mock

from ib_iam.tests.factories.storage_dtos import (
    TeamNameAndDescriptionDTOFactory, TeamWithUserIdsDTOFactory)


class TestAddTeamInteractor:

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
        from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
            TeamPresenterInterface)
        return create_autospec(TeamPresenterInterface)

    @pytest.fixture
    def interactor(self, team_storage_mock, user_storage_mock):
        from ib_iam.interactors.team_interactor import TeamInteractor
        return TeamInteractor(
            team_storage=team_storage_mock,
            user_storage=user_storage_mock
        )

    def test_if_user_not_admin_returns_unauthorized_exception_response(
            self, interactor, team_storage_mock, user_storage_mock, presenter
    ):
        # Arrange
        user_id = "1"
        team_with_user_ids_dto = TeamWithUserIdsDTOFactory()
        user_storage_mock.is_user_admin.return_value = False
        presenter.get_user_has_no_access_response_for_add_team \
            .return_value = Mock()

        # Act
        interactor.add_team_wrapper(
            user_id=user_id, team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        # Assert
        user_storage_mock.is_user_admin.assert_called_once_with(
            user_id=user_id)
        presenter.get_user_has_no_access_response_for_add_team \
            .assert_called_once()

    def test_given_duplicate_users_returns_duplicate_users_response(
            self, interactor, team_storage_mock, user_storage_mock, presenter
    ):
        # Arrange
        user_id = "1"
        user_ids = ["2", "2", "3", "1"]
        team_with_user_ids_dto = TeamWithUserIdsDTOFactory(
            name="team1", user_ids=user_ids)
        team_storage_mock.get_team_id_if_team_name_already_exists.return_value = None
        presenter.get_duplicate_users_response_for_add_team \
            .return_value = Mock()

        # Act
        interactor.add_team_wrapper(
            user_id=user_id, team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        # Assert
        presenter.get_duplicate_users_response_for_add_team.assert_called_once()

    def test_given_invalid_users_returns_invalid_users_response(
            self, interactor, team_storage_mock, user_storage_mock, presenter
    ):
        # Arrange
        user_id = "1"
        valid_user_ids = ["2", "3"]
        invalid_user_ids = ["2", "3", "4"]
        team_with_user_ids_dto = TeamWithUserIdsDTOFactory(
            name="team1", user_ids=invalid_user_ids)
        team_storage_mock.get_team_id_if_team_name_already_exists.return_value = None
        user_storage_mock.get_valid_user_ids_among_the_given_user_ids \
            .return_value = valid_user_ids
        presenter.get_invalid_users_response_for_add_team.return_value = Mock()

        # Act
        interactor.add_team_wrapper(
            user_id=user_id, team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        # Assert
        user_storage_mock.get_valid_user_ids_among_the_given_user_ids \
            .assert_called_once_with(user_ids=invalid_user_ids)
        presenter.get_invalid_users_response_for_add_team.assert_called_once()

    def test_team_name_exists_returns_team_name_already_exists_response(
            self, interactor, team_storage_mock, user_storage_mock, presenter
    ):
        # Arrange
        user_id = "1"
        team_name = "team1"
        user_ids = ["1"]
        expected_team_name_from_team_name_already_exists_error = team_name
        user_storage_mock.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        team_with_user_ids_dto = TeamWithUserIdsDTOFactory(
            name="team1", user_ids=user_ids
        )
        team_storage_mock.get_team_id_if_team_name_already_exists.return_value = "1"
        presenter.get_team_name_already_exists_response_for_add_team \
            .return_value = Mock()

        # Act
        interactor.add_team_wrapper(
            user_id=user_id, team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        # Assert
        team_storage_mock.get_team_id_if_team_name_already_exists \
            .assert_called_once_with(name=team_with_user_ids_dto.name)
        call_args = \
            presenter.get_team_name_already_exists_response_for_add_team.call_args
        error_obj = call_args[0][0]
        actual_team_name_from_team_name_already_exists_error = \
            error_obj.team_name
        assert actual_team_name_from_team_name_already_exists_error == \
               expected_team_name_from_team_name_already_exists_error

    def test_given_valid_details_then_returns_team_id(
            self, interactor, team_storage_mock, user_storage_mock, presenter
    ):
        # Arrange
        user_id = "1"
        team_id = "1"
        user_ids = ["2", "3"]
        TeamWithUserIdsDTOFactory.reset_sequence(1, force=True)
        team_with_user_ids_dto = TeamWithUserIdsDTOFactory()
        TeamNameAndDescriptionDTOFactory.reset_sequence(1)
        team_name_and_description_dto = TeamNameAndDescriptionDTOFactory()
        team_storage_mock.get_team_id_if_team_name_already_exists.return_value = None
        user_storage_mock.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        team_storage_mock.add_team.return_value = team_id
        presenter.get_response_for_add_team.return_value = Mock()

        # Act
        interactor.add_team_wrapper(
            user_id=user_id, team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        # Assert
        team_storage_mock.add_team.assert_called_once_with(
            user_id=user_id,
            team_name_and_description_dto=team_name_and_description_dto
        )
        team_storage_mock.add_users_to_team(team_id=team_id, user_ids=user_ids)
        presenter.get_response_for_add_team \
            .assert_called_once_with(team_id=team_id)
