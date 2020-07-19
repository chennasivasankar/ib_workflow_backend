import pytest
from mock import create_autospec, Mock

from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import UpdateTeamParametersDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface
from ib_iam.interactors.team_interactor import TeamInteractor
from ib_iam.tests.factories import UpdateTeamParametersDTOFactory


class TestUpdateTeamDetails:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        update_team_parameters_dto = \
            UpdateTeamParametersDTOFactory(team_id="1")
        storage.raise_exception_if_user_is_not_admin \
            .side_effect = UserHasNoAccess
        presenter.raise_exception_for_user_has_no_access.side_effect = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            update_team_parameters_dto=update_team_parameters_dto,
            presenter=presenter
        )

        storage.raise_exception_if_user_is_not_admin \
            .assert_called_once_with(user_id=user_id)
        presenter.raise_exception_for_user_has_no_access.assert_called_once()

    def test_if_invalid_team_id_raises_not_found_exception(self):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_id = "2"
        update_team_parameters_dto = \
            UpdateTeamParametersDTOFactory(team_id="2")
        storage.raise_exception_if_team_not_exists.side_effect = InvalidTeamId
        presenter.raise_exception_for_invalid_team_id.side_effect = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            update_team_parameters_dto=update_team_parameters_dto,
            presenter=presenter
        )

        storage.raise_exception_if_team_not_exists \
            .assert_called_once_with(team_id=team_id)
        presenter.raise_exception_for_invalid_team_id.assert_called_once()

    def test_if_team_name_already_exists_raises_bad_request_exception(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        team_name = "team2"
        expected_team_name_from_error = team_name
        update_team_parameters_dto = \
            UpdateTeamParametersDTOFactory(team_id="3")
        storage.get_team_id_if_team_name_already_exists.return_value = "2"
        presenter.raise_exception_if_team_name_already_exists.side_effect = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            update_team_parameters_dto=update_team_parameters_dto,
            presenter=presenter
        )

        storage.get_team_id_if_team_name_already_exists \
            .assert_called_once_with(name=team_name)
        call_obj = presenter.raise_exception_if_team_name_already_exists \
                            .call_args
        error_obj = call_obj.args[0]
        actual_team_name_from_error = error_obj.team_name
        assert actual_team_name_from_error == expected_team_name_from_error

    def test_team_requested_for_its_own_name_then_updation_will_be_done(
            self
    ):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        user_id = "1"
        update_team_parameters_dto = \
            UpdateTeamParametersDTOFactory(team_id="4")
        storage.get_team_id_if_team_name_already_exists.return_value = None
        presenter.make_empty_http_success_response.return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id=user_id,
            update_team_parameters_dto=update_team_parameters_dto,
            presenter=presenter
        )

        storage.update_team_details.assert_called_once_with(
            update_team_parameters_dto=update_team_parameters_dto
        )
        presenter.make_empty_http_success_response.assert_called_once()

    def test_given_team_name_not_exists_then_updation_will_be_done(
                self
    ):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = TeamInteractor(storage=storage)
        update_team_parameters_dto = \
            UpdateTeamParametersDTOFactory(team_id="5")
        storage.get_team_id_if_team_name_already_exists.return_value = "5"
        presenter.make_empty_http_success_response.return_value = Mock()

        interactor.update_team_details_wrapper(
            user_id="1",
            update_team_parameters_dto=update_team_parameters_dto,
            presenter=presenter
        )

        storage.update_team_details.assert_called_once_with(
            update_team_parameters_dto=update_team_parameters_dto
        )
        presenter.make_empty_http_success_response.assert_called_once()
