from mock import create_autospec, Mock
from ib_iam.interactors.add_team_interactor import AddTeamInteractor
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface
)
from ib_iam.tests.factories import TeamDetailsWithUserIdsDTOFactory
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)


class TestAddTeamInteractor:

    def test_if_user_not_admin_returns_unauthorized_exception_response(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_details_with_user_ids_dto = TeamDetailsWithUserIdsDTOFactory()
        storage.raise_exception_if_user_is_not_admin \
            .side_effect = UserHasNoAccess
        presenter.get_user_has_no_access_response_for_add_team \
                 .return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            team_details_with_user_ids_dto=team_details_with_user_ids_dto,
            presenter=presenter
        )

        storage.raise_exception_if_user_is_not_admin \
            .assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_add_team \
                 .assert_called_once()

    def test_team_name_exists_returns_team_name_already_exists_response(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_name = "team1"
        expected_team_name_from_team_name_already_exists_error = team_name
        team_details_with_user_ids_dto = TeamDetailsWithUserIdsDTOFactory(name="team1")
        storage.get_team_id_if_team_name_already_exists.return_value = "1"
        presenter.get_team_name_already_exists_response_for_add_team \
                 .return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            team_details_with_user_ids_dto=team_details_with_user_ids_dto,
            presenter=presenter
        )

        storage.get_team_id_if_team_name_already_exists \
            .assert_called_once_with(name=team_details_with_user_ids_dto.name)
        call_obj = \
            presenter.get_team_name_already_exists_response_for_add_team.call_args
        error_obj = call_obj.args[0]
        actual_team_name_from_team_name_already_exists_error = \
            error_obj.team_name
        assert actual_team_name_from_team_name_already_exists_error == \
               expected_team_name_from_team_name_already_exists_error

    def test_given_duplicate_users_returns_duplicate_users_response(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        user_ids = ["2", "2", "3", "1"]
        team_details_with_user_ids_dto = TeamDetailsWithUserIdsDTOFactory(
            name="team1", user_ids=user_ids
        )
        storage.get_team_id_if_team_name_already_exists.return_value = None
        presenter.get_duplicate_users_response_for_add_team \
                 .return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            team_details_with_user_ids_dto=team_details_with_user_ids_dto,
            presenter=presenter
        )

        presenter.get_duplicate_users_response_for_add_team.assert_called_once()

    def test_given_invalid_users_returns_invalid_users_response(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        valid_user_ids = ["2", "3"]
        invalid_user_ids = ["2", "3", "4"]
        team_details_with_user_ids_dto = TeamDetailsWithUserIdsDTOFactory(
            name="team1", user_ids=invalid_user_ids
        )
        storage.get_team_id_if_team_name_already_exists.return_value = None
        storage.get_valid_user_ids_among_the_given_user_ids \
               .return_value = valid_user_ids
        presenter.get_invalid_users_response_for_add_team.return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            team_details_with_user_ids_dto=team_details_with_user_ids_dto,
            presenter=presenter
        )

        storage.get_valid_user_ids_among_the_given_user_ids \
            .assert_called_once_with(user_ids=invalid_user_ids)
        presenter.get_invalid_users_response_for_add_team.assert_called_once()

    def test_given_valid_details_then_returns_team_id(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_id = "1"
        user_ids = ["2", "3"]
        team_details_with_user_ids_dto = TeamDetailsWithUserIdsDTOFactory()
        storage.get_team_id_if_team_name_already_exists.return_value = None
        storage.get_valid_user_ids_among_the_given_user_ids \
               .return_value = user_ids
        storage.add_team.return_value = team_id
        presenter.get_response_for_add_team.return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            team_details_with_user_ids_dto=team_details_with_user_ids_dto,
            presenter=presenter
        )

        storage.add_team.assert_called_once_with(
            user_id=user_id,
            team_details_with_user_ids_dto=team_details_with_user_ids_dto
        )
        storage.add_users_to_team(team_id=team_id, user_ids=user_ids)
        presenter.get_response_for_add_team \
                 .assert_called_once_with(team_id=team_id)
