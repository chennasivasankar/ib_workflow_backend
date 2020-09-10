from mock import create_autospec, Mock
from ib_iam.interactors.presenter_interfaces \
    .delete_team_presenter_interface import DeleteTeamPresenterInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from ib_iam.interactors.team_interactor import TeamInteractor


class TestDeleteTeam:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(DeleteTeamPresenterInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        user_id = "1"
        user_storage.is_user_admin.return_value = False
        presenter.get_user_has_no_access_response_for_delete_team \
                 .side_effect = Mock()

        interactor.delete_team_wrapper(
            user_id=user_id, team_id="1", presenter=presenter)

        user_storage.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_delete_team \
                 .assert_called_once()

    def test_if_invalid_team_id_raises_not_found_exception(self):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(DeleteTeamPresenterInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        user_id = "1"
        team_id = "1"
        team_storage.raise_exception_if_team_not_exists.side_effect = \
            InvalidTeamId
        presenter.get_invalid_team_response_for_delete_team \
                 .side_effect = Mock()

        interactor.delete_team_wrapper(
            user_id=user_id, team_id=team_id, presenter=presenter)

        team_storage.raise_exception_if_team_not_exists \
            .assert_called_once_with(team_id=team_id)
        presenter.get_invalid_team_response_for_delete_team \
                 .assert_called_once()

    def test_given_valid_details_deletion_will_happen(self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(DeleteTeamPresenterInterface)
        interactor = TeamInteractor(team_storage=team_storage,
                                    user_storage=user_storage)
        user_id = "1"
        team_id = "1"
        presenter.get_success_response_for_delete_team.return_value = Mock()

        interactor.delete_team_wrapper(
            user_id=user_id, team_id=team_id, presenter=presenter)

        team_storage.delete_team.assert_called_once_with(
            team_id=team_id)
        presenter.get_success_response_for_delete_team.assert_called_once()
