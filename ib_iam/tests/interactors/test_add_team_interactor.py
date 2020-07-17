import pytest
from mock import create_autospec

from ib_iam.interactors.add_team_interactor import AddTeamInteractor
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import AddTeamParametersDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface


class TestAddTeamInteractor:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        from django_swagger_utils.drf_server.exceptions import Unauthorized
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        add_team_params_dto = AddTeamParametersDTO(
            name="team1", description="team1_description"
        )
        storage.is_user_admin.side_effect = UserHasNoAccess
        presenter.raise_exception_for_user_has_no_access.side_effect = (
            Unauthorized
        )

        with pytest.raises(Unauthorized):
            interactor.add_team_wrapper(
                user_id=user_id,
                add_team_params_dto=add_team_params_dto,
                presenter=presenter
            )

        storage.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.raise_exception_for_user_has_no_access.assert_called_once()

    def test_duplicated_team_name_raises_duplicate_team_name_exception(self):
        from ib_iam.exceptions.custom_exceptions import DuplicateTeamName
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_name = "team1"
        expected_team_name_from_error = team_name
        add_team_params_dto = AddTeamParametersDTO(
            name=team_name, description="team1_description"
        )
        storage.add_team.side_effect = DuplicateTeamName(team_name=team_name)
        from django_swagger_utils.drf_server.exceptions import BadRequest
        presenter.raise_exception_for_duplicate_team_name.side_effect = (
            BadRequest
        )

        with pytest.raises(BadRequest):
            interactor.add_team_wrapper(
                user_id=user_id,
                add_team_params_dto=add_team_params_dto,
                presenter=presenter
            )

        storage.add_team.assert_called_once_with(
            user_id=user_id, add_team_params_dto=add_team_params_dto
        )
        call_obj = presenter.raise_exception_for_duplicate_team_name.call_args
        error_obj = call_obj.args[0]
        actual_team_name_from_error = error_obj.team_name
        assert actual_team_name_from_error == expected_team_name_from_error

    def test_given_correct_details_returns_team_id(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_id = "1"
        team_name = "team1"
        expected_team_id = team_id
        add_team_params_dto = AddTeamParametersDTO(
            name=team_name, description="team1_description"
        )
        storage.add_team.return_value = team_id
        presenter.get_response_for_add_team.return_value = expected_team_id

        actual_team_id = interactor.add_team_wrapper(
                user_id=user_id,
                add_team_params_dto=add_team_params_dto,
                presenter=presenter
            )

        storage.add_team.assert_called_once_with(
            user_id=user_id, add_team_params_dto=add_team_params_dto
        )
        presenter.get_response_for_add_team.assert_called_once_with(team_id=team_id)
        assert actual_team_id == expected_team_id
