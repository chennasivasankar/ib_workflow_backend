from mock import create_autospec, Mock

from ib_iam.interactors.presenter_interfaces.update_team_presenter_interface \
    import UpdateTeamPresenterInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from ib_iam.interactors.team_interactor import TeamInteractor
from ib_iam.tests.factories.storage_dtos import \
    TeamWithTeamIdAndUserIdsDTOFactory


class TestUpdateTeamDetails:

    # TODO: write repeated lines in a fixtures.
    def test_if_user_not_admin_returns_unauthorized_exception_response(self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        user_id = "1"
        team_with_team_id_and_user_ids_dto = \
            TeamWithTeamIdAndUserIdsDTOFactory(team_id="1")
        user_storage.is_user_admin.return_value = False
        presenter.get_user_has_no_access_response_for_update_team \
            .return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_team_id_and_user_ids_dto=
            team_with_team_id_and_user_ids_dto,
            presenter=presenter)

        user_storage.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_update_team \
            .assert_called_once()

    def test_if_invalid_team_id_raises_not_found_exception_response(self):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        user_id = "1"
        team_id = "2"
        team_with_team_id_and_user_ids_dto = \
            TeamWithTeamIdAndUserIdsDTOFactory(team_id="2")
        team_storage.raise_exception_if_team_not_exists.side_effect = \
            InvalidTeamId
        presenter.get_invalid_team_response_for_update_team \
            .return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_team_id_and_user_ids_dto=
            team_with_team_id_and_user_ids_dto,
            presenter=presenter)

        team_storage.raise_exception_if_team_not_exists \
            .assert_called_once_with(team_id=team_id)
        presenter.get_invalid_team_response_for_update_team \
            .assert_called_once()

    def test_given_duplicate_users_returns_duplicate_users_response(self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        user_id = "1"
        user_ids = ["2", "2", "3", "1"]
        team_with_team_id_and_user_ids_dto = \
            TeamWithTeamIdAndUserIdsDTOFactory(team_id="3", user_ids=user_ids)
        team_storage.raise_exception_if_team_not_exists.return_value = None
        presenter.get_duplicate_users_response_for_update_team \
            .return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_team_id_and_user_ids_dto=
            team_with_team_id_and_user_ids_dto,
            presenter=presenter)

        presenter.get_duplicate_users_response_for_update_team \
            .assert_called_once()

    def test_given_invalid_users_returns_invalid_users_response(self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        user_id = "1"
        user_ids = ["2", "3", "1"]
        valid_user_ids = ["2", "3"]
        team_with_team_id_and_user_ids_dto = \
            TeamWithTeamIdAndUserIdsDTOFactory(team_id="3", user_ids=user_ids)
        team_storage.raise_exception_if_team_not_exists.return_value = None
        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = valid_user_ids
        presenter.get_invalid_users_response_for_update_team \
            .return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_team_id_and_user_ids_dto=
            team_with_team_id_and_user_ids_dto,
            presenter=presenter)

        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .assert_called_once_with(user_ids=user_ids)
        presenter.get_invalid_users_response_for_update_team \
            .assert_called_once()

    def test_if_team_name_already_exists_raises_bad_request_exception_response(
            self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        user_id = "1"
        team_name = "team4"
        expected_team_name_from_error = team_name
        user_ids = ["2", "3", "1"]
        team_with_team_id_and_user_ids_dto = TeamWithTeamIdAndUserIdsDTOFactory(
            team_id="3", name=team_name, user_ids=user_ids)
        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        team_storage.get_team_id_if_team_name_already_exists.return_value = "2"
        presenter.get_team_name_already_exists_response_for_update_team \
            .return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_team_id_and_user_ids_dto=
            team_with_team_id_and_user_ids_dto,
            presenter=presenter)

        team_storage.get_team_id_if_team_name_already_exists \
            .assert_called_once_with(name=team_name)
        call_args = presenter \
            .get_team_name_already_exists_response_for_update_team.call_args
        error_obj = call_args[0][0]
        actual_team_name_from_error = error_obj.team_name
        assert actual_team_name_from_error == expected_team_name_from_error

    def test_given_team_name_not_belongs_to_other_teams_updation_will_be_done(
            self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateTeamPresenterInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        user_id = "1"
        existing_user_ids = ["1", "3", "4"]
        user_ids = ["2", "3", "1"]
        new_user_ids = ["2"]
        delete_user_ids = ["4"]
        team_with_team_id_and_user_ids_dto = \
            TeamWithTeamIdAndUserIdsDTOFactory(user_ids=user_ids)
        from ib_iam.interactors.storage_interfaces.dtos import TeamDTO
        team_dto = TeamDTO(
            team_id=team_with_team_id_and_user_ids_dto.team_id,
            name=team_with_team_id_and_user_ids_dto.name,
            description=team_with_team_id_and_user_ids_dto.description)
        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        team_storage.get_team_id_if_team_name_already_exists \
            .return_value = None
        team_storage.get_member_ids_of_team.return_value = existing_user_ids
        presenter.get_success_response_for_update_team.return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            team_with_team_id_and_user_ids_dto=
            team_with_team_id_and_user_ids_dto,
            presenter=presenter)

        team_storage.update_team_details.assert_called_once_with(
            team_dto=team_dto)
        team_storage.add_users_to_team.assert_called_once_with(
            team_id=team_dto.team_id, user_ids=new_user_ids)
        team_storage.delete_members_from_team.assert_called_once_with(
            team_id=team_dto.team_id, user_ids=delete_user_ids)
        presenter.get_success_response_for_update_team.assert_called_once()
