import pytest
from mock import create_autospec

from ib_iam.interactors.add_team_interactor import AddTeamInteractor
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.tests.factories import TeamNameAndDescriptionDTOFactory
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface


class TestAddTeamInteractor:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        from django_swagger_utils.drf_server.exceptions import Unauthorized
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_name_and_description_dto = TeamNameAndDescriptionDTOFactory()
        storage.raise_exception_if_user_is_not_admin.side_effect = UserHasNoAccess
        presenter.raise_exception_for_user_has_no_access.side_effect = (
            Unauthorized
        )

        with pytest.raises(Unauthorized):
            interactor.add_team_wrapper(
                user_id=user_id,
                team_name_and_description_dto=team_name_and_description_dto,
                presenter=presenter
            )

        storage.raise_exception_if_user_is_not_admin.assert_called_once_with(user_id=user_id)
        presenter.raise_exception_for_user_has_no_access.assert_called_once()

    def test_given_name_exists_raises_team_name_already_exists_exception(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_name = "team1"
        expected_team_name_from_team_name_already_exists_error = team_name
        team_name_and_description_dto = TeamNameAndDescriptionDTOFactory(name="team1")
        storage.get_team_id_if_team_name_already_exists.return_value = "2"
        from django_swagger_utils.drf_server.exceptions import BadRequest
        presenter.raise_exception_if_team_name_already_exists.side_effect = (
            BadRequest
        )

        with pytest.raises(BadRequest):
            interactor.add_team_wrapper(
                user_id=user_id,
                team_name_and_description_dto=team_name_and_description_dto,
                presenter=presenter
            )

        storage.get_team_id_if_team_name_already_exists \
            .assert_called_once_with(name=team_name_and_description_dto.name)
        call_obj = \
            presenter.raise_exception_if_team_name_already_exists.call_args
        error_obj = call_obj.args[0]
        actual_team_name_from_team_name_already_exists_error = \
            error_obj.team_name
        assert actual_team_name_from_team_name_already_exists_error == \
               expected_team_name_from_team_name_already_exists_error

    def test_given_valid_details_then_returns_team_id(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_id = "1"
        team_name_and_description_dto = TeamNameAndDescriptionDTOFactory()
        storage.get_team_id_if_team_name_already_exists.return_value = None
        storage.add_team.return_value = team_id

        interactor.add_team_wrapper(
            user_id=user_id,
            team_name_and_description_dto=team_name_and_description_dto,
            presenter=presenter
        )

        storage.add_team.assert_called_once_with(
            user_id=user_id,
            team_name_and_description_dto=team_name_and_description_dto
        )
        presenter.get_response_for_add_team.assert_called_once_with(team_id=team_id)
