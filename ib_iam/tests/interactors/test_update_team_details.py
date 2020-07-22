from mock import create_autospec, Mock
from ib_iam.interactors.presenter_interfaces.update_team_presenter_interface import (
    UpdateTeamPresenterInterface
)
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface
from ib_iam.interactors.team_interactor import TeamInteractor
from ib_iam.tests.factories import TeamWithUserIdsDTOFactory


class TestUpdateTeamDetails:

    def test_if_user_not_admin_returns_unauthorized_exception_response(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_with_user_ids_dto = \
            TeamWithUserIdsDTOFactory(team_id="1")
        storage.validate_is_user_admin.side_effect = UserHasNoAccess
        presenter.get_user_has_no_access_response_for_update_team.side_effect = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        storage.validate_is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_update_team \
                 .assert_called_once()

    def test_if_invalid_team_id_raises_not_found_exception_response(self):
        from ib_iam.exceptions.custom_exceptions import InvalidTeam
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_id = "2"
        team_with_user_ids_dto = \
            TeamWithUserIdsDTOFactory(team_id="2")
        storage.raise_exception_if_team_not_exists.side_effect = InvalidTeam
        presenter.get_invalid_team_response_for_update_team.side_effect = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        storage.raise_exception_if_team_not_exists \
            .assert_called_once_with(team_id=team_id)
        presenter.get_invalid_team_response_for_update_team.assert_called_once()

    def test_given_duplicate_users_returns_duplicate_users_response(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_name = "team1"
        user_ids = ["2", "2", "3", "1"]
        team_with_user_ids_dto = \
            TeamWithUserIdsDTOFactory(team_id="3", user_ids=user_ids)
        storage.raise_exception_if_team_not_exists.return_value = None
        presenter.get_duplicate_users_response_for_update_team \
            .return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        presenter.get_duplicate_users_response_for_update_team \
                 .assert_called_once()

    def test_given_invalid_users_returns_invalid_users_response(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_name = "team1"
        user_ids = ["2", "3", "1"]
        valid_user_ids = ["2", "3"]
        team_with_user_ids_dto = \
            TeamWithUserIdsDTOFactory(team_id="3", user_ids=user_ids)
        storage.raise_exception_if_team_not_exists.return_value = None
        storage.get_valid_user_ids_among_the_given_user_ids \
               .return_value = valid_user_ids
        presenter.get_invalid_users_response_for_update_team \
            .return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        storage.get_valid_user_ids_among_the_given_user_ids \
               .assert_called_once_with(user_ids=user_ids)
        presenter.get_invalid_users_response_for_update_team \
                 .assert_called_once()

    def test_if_team_name_already_exists_raises_bad_request_exception_response(
            self
    ):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_name = "team4"
        expected_team_name_from_error = team_name
        user_ids = ["2", "3", "1"]
        team_with_user_ids_dto = TeamWithUserIdsDTOFactory(
                team_id="3", name=team_name, user_ids=user_ids
        )
        storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        storage.get_team_id_if_team_name_already_exists.return_value = "2"
        presenter.get_team_name_already_exists_response_for_update_team \
                 .side_effect = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        storage.get_team_id_if_team_name_already_exists \
            .assert_called_once_with(name=team_name)
        call_obj = presenter \
            .get_team_name_already_exists_response_for_update_team.call_args
        error_obj = call_obj.args[0]
        actual_team_name_from_error = error_obj.team_name
        assert actual_team_name_from_error == expected_team_name_from_error

    def test_team_requested_for_its_own_name_then_updation_will_be_done(
            self
    ):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        user_ids = ["2", "3", "1"]
        team_with_user_ids_dto = \
            TeamWithUserIdsDTOFactory(team_id="3", user_ids=user_ids)
        storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        storage.get_team_id_if_team_name_already_exists.return_value = None
        presenter.get_success_response_for_update_team.return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        storage.update_team_details.assert_called_once_with(
            team_with_user_ids_dto=team_with_user_ids_dto
        )
        presenter.get_success_response_for_update_team.assert_called_once()

    def test_given_team_name_not_exists_then_updation_will_be_done(
                self
    ):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_ids = ["2", "3", "1"]
        team_with_user_ids_dto = \
            TeamWithUserIdsDTOFactory(team_id="3", user_ids=user_ids)
        storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        storage.get_team_id_if_team_name_already_exists.return_value = None
        presenter.get_success_response_for_update_team.return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id="1",
            team_with_user_ids_dto=team_with_user_ids_dto,
            presenter=presenter
        )

        storage.update_team_details.assert_called_once_with(
            team_with_user_ids_dto=team_with_user_ids_dto
        )
        presenter.get_success_response_for_update_team.assert_called_once()
