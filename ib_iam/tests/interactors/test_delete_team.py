import pytest
from mock import create_autospec
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface
from ib_iam.interactors.team_interactor import TeamInteractor


class TestDeleteTeam:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        from django_swagger_utils.drf_server.exceptions import Unauthorized
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        storage.is_user_admin.side_effect = UserHasNoAccess
        presenter.raise_exception_for_user_has_no_access.side_effect = (
            Unauthorized
        )

        with pytest.raises(Unauthorized):
            interactor.delete_team_wrapper(
                user_id=user_id,
                team_id="1",
                presenter=presenter
            )

        storage.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.raise_exception_for_user_has_no_access.assert_called_once()

    def test_if_invalid_team_id_raises_not_found_exception(self):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        from django_swagger_utils.drf_server.exceptions import NotFound
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_id = "1"
        storage.is_valid_team.side_effect = InvalidTeamId
        presenter.raise_exception_for_invalid_team_id.side_effect = (
            NotFound
        )

        with pytest.raises(NotFound):
            interactor.delete_team_wrapper(
                user_id=user_id,
                team_id=team_id,
                presenter=presenter
            )

        storage.is_valid_team.assert_called_once_with(team_id=team_id)
        presenter.raise_exception_for_invalid_team_id.assert_called_once()

    def test_given_proper_details_deletion_will_be_successful(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_id = "1"
        expected_response = {}
        presenter.make_empty_http_success_response \
            .return_value = expected_response

        interactor.delete_team_wrapper(
            user_id=user_id,
            team_id=team_id,
            presenter=presenter
        )

        storage.delete_team.assert_called_once_with(
            team_id=team_id
        )
        presenter.make_empty_http_success_response.assert_called_once()
