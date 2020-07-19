from mock import create_autospec, Mock
from ib_iam.interactors.add_team_interactor import AddTeamInteractor
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface
)
from ib_iam.tests.factories import AddTeamParametersDTOFactory
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)


class TestAddTeamInteractor:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        add_team_parameters_dto = AddTeamParametersDTOFactory()
        storage.raise_exception_if_user_is_not_admin \
            .side_effect = UserHasNoAccess
        presenter.raise_exception_for_user_has_no_access.return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            add_team_parameters_dto=add_team_parameters_dto,
            presenter=presenter
        )

        storage.raise_exception_if_user_is_not_admin \
            .assert_called_once_with(user_id=user_id)
        presenter.raise_exception_for_user_has_no_access.assert_called_once()

    def test_given_name_exists_raises_team_name_already_exists_exception(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_name = "team1"
        expected_team_name_from_team_name_already_exists_error = team_name
        add_team_parameters_dto = AddTeamParametersDTOFactory(name="team1")
        storage.get_team_id_if_team_name_already_exists.return_value = "1"
        presenter.raise_exception_if_team_name_already_exists \
                 .return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            add_team_parameters_dto=add_team_parameters_dto,
            presenter=presenter
        )

        storage.get_team_id_if_team_name_already_exists \
            .assert_called_once_with(name=add_team_parameters_dto.name)
        call_obj = \
            presenter.raise_exception_if_team_name_already_exists.call_args
        error_obj = call_obj.args[0]
        actual_team_name_from_team_name_already_exists_error = \
            error_obj.team_name
        assert actual_team_name_from_team_name_already_exists_error == \
               expected_team_name_from_team_name_already_exists_error

    def test_given_duplicate_members_raises_duplicate_members_exception(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        member_ids = ["2", "2", "3", "1"]
        add_team_parameters_dto = AddTeamParametersDTOFactory(
            name="team1", member_ids=member_ids
        )
        storage.get_team_id_if_team_name_already_exists.return_value = None
        presenter.raise_exception_for_duplicate_members.return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            add_team_parameters_dto=add_team_parameters_dto,
            presenter=presenter
        )

        presenter.raise_exception_for_duplicate_members.assert_called_once()

    def test_given_invalid_members_raises_invalid_members_exception(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        valid_member_ids = ["2", "3"]
        invalid_member_ids = ["2", "3", "4"]
        add_team_parameters_dto = AddTeamParametersDTOFactory(
            name="team1", member_ids=invalid_member_ids
        )
        storage.get_team_id_if_team_name_already_exists.return_value = None
        storage.get_valid_member_ids_among_the_given_member_ids \
               .return_value = valid_member_ids
        presenter.raise_exception_for_invalid_members.return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            add_team_parameters_dto=add_team_parameters_dto,
            presenter=presenter
        )

        storage.get_valid_member_ids_among_the_given_member_ids \
            .assert_called_once_with(member_ids=invalid_member_ids)
        presenter.raise_exception_for_invalid_members.assert_called_once()

    def test_given_valid_details_then_returns_team_id(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = AddTeamInteractor(storage=storage)
        user_id = "1"
        team_id = "1"
        member_ids = ["2", "3"]
        add_team_parameters_dto = AddTeamParametersDTOFactory()
        storage.get_team_id_if_team_name_already_exists.return_value = None
        storage.get_valid_member_ids_among_the_given_member_ids \
               .return_value = member_ids
        storage.add_team.return_value = team_id
        presenter.get_response_for_add_team.return_value = Mock()

        interactor.add_team_wrapper(
            user_id=user_id,
            add_team_parameters_dto=add_team_parameters_dto,
            presenter=presenter
        )

        storage.add_team.assert_called_once_with(
            user_id=user_id,
            add_team_parameters_dto=add_team_parameters_dto
        )
        storage.add_members_to_team(team_id=team_id, member_ids=member_ids)
        presenter.get_response_for_add_team \
                 .assert_called_once_with(team_id=team_id)
