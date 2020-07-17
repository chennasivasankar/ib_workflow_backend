import pytest
from mock import create_autospec

from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import UpdateTeamParametersDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface
from ib_iam.interactors.team_interactor import TeamInteractor


class TestUpdateTeamDetails:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        from django_swagger_utils.drf_server.exceptions import Unauthorized
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        update_team_parameters_dto = UpdateTeamParametersDTO(
            team_id="1", name="team1", description="team1_description"
        )
        storage.is_user_admin.side_effect = UserHasNoAccess
        presenter.raise_exception_for_user_has_no_access.side_effect = (
            Unauthorized
        )

        with pytest.raises(Unauthorized):
            interactor.update_team_details_wrapper(
                user_id=user_id,
                update_team_parameters_dto=update_team_parameters_dto,
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
        update_team_parameters_dto = UpdateTeamParametersDTO(
            team_id=team_id, name="team1", description="team1_description"
        )
        storage.is_valid_team.side_effect = InvalidTeamId
        presenter.raise_exception_for_invalid_team_id.side_effect = (
            NotFound
        )

        with pytest.raises(NotFound):
            interactor.update_team_details_wrapper(
                user_id=user_id,
                update_team_parameters_dto=update_team_parameters_dto,
                presenter=presenter
            )

        storage.is_valid_team.assert_called_once_with(team_id=team_id)
        presenter.raise_exception_for_invalid_team_id.assert_called_once()

    def test_duplicate_team_name_raises_bad_request_exception(self):
        from ib_iam.exceptions.custom_exceptions import DuplicateTeamName
        from django_swagger_utils.drf_server.exceptions import BadRequest
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_id = "1"
        team_name = "team1"
        expected_team_name_from_error = team_name
        update_team_parameters_dto = UpdateTeamParametersDTO(
            team_id=team_id, name=team_name, description="team1_description"
        )
        storage.is_duplicate_team_name \
            .side_effect = DuplicateTeamName(team_name=team_name)
        presenter.raise_exception_for_duplicate_team_name.side_effect = (
            BadRequest
        )

        with pytest.raises(BadRequest):
            interactor.update_team_details_wrapper(
                user_id=user_id,
                update_team_parameters_dto=update_team_parameters_dto,
                presenter=presenter
            )

        storage.is_duplicate_team_name.assert_called_once_with(
            team_id=team_id, name=team_name
        )
        call_obj = presenter.raise_exception_for_duplicate_team_name.call_args
        print("*" * 80)
        print(call_obj)
        error_obj = call_obj.args[0]
        actual_team_name_from_error = error_obj.team_name
        assert actual_team_name_from_error == expected_team_name_from_error

    def test_given_proper_details_updation_will_be_successful(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        update_team_parameters_dto = UpdateTeamParametersDTO(
            team_id="1", name="team", description="team1_description"
        )
        expected_response = {}
        presenter.make_empty_http_success_response \
            .return_value = expected_response

        interactor.update_team_details_wrapper(
            user_id=user_id,
            update_team_parameters_dto=update_team_parameters_dto,
            presenter=presenter
        )

        storage.update_team_details.assert_called_once_with(
            update_team_parameters_dto=update_team_parameters_dto
        )
        presenter.make_empty_http_success_response.assert_called_once()
