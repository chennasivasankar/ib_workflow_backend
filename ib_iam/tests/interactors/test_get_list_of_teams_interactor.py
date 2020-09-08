import pytest
from mock import create_autospec, Mock

from ib_iam.interactors.get_list_of_teams_interactor import \
    GetListOfTeamsInteractor
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import \
    TeamPresenterInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from ib_iam.tests.factories.presenter_dtos import \
    TeamWithMembersDetailsDTOFactory
from ib_iam.tests.factories.storage_dtos import (
    TeamsWithTotalTeamsCountDTOFactory, PaginationDTOFactory)


class TestGetListOfTeamsInteractor:

    @pytest.fixture
    def expected_list_of_teams_dtos(self):
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        TeamDTOFactory.reset_sequence(1)
        team_dtos = [TeamDTOFactory(team_id="1")]
        return team_dtos

    @pytest.fixture()
    def expected_team_user_ids_dtos(self):
        from ib_iam.tests.factories.storage_dtos import TeamUserIdsDTOFactory
        team_user_ids_dtos = [
            TeamUserIdsDTOFactory(team_id="1", user_ids=["2", "3"])
        ]
        return team_user_ids_dtos

    @pytest.fixture
    def expected_list_of_user_dtos(self):
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(2)
        user_profile_dtos = [
            UserProfileDTOFactory() for _ in range(2)
        ]
        return user_profile_dtos

    # TODO: Repeated lines write in a fixtures
    def test_if_user_not_admin_returns_unauthorized_response(self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(team_storage=team_storage,
                                              user_storage=user_storage)
        user_id = "1"
        pagination_dto = PaginationDTOFactory()
        user_storage.is_user_admin.return_value = False
        presenter.get_user_has_no_access_response_for_get_list_of_teams \
            .return_value = Mock()

        interactor.get_list_of_teams_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter)

        user_storage.is_user_admin.assert_called_once_with(
            user_id=user_id)
        presenter.get_user_has_no_access_response_for_get_list_of_teams \
            .assert_called_once()

    def test_invalid_limit_returns_invalid_limit_response(self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(team_storage=team_storage,
                                              user_storage=user_storage)
        presenter.get_invalid_limit_response_for_get_list_of_teams \
            .return_value = Mock()
        pagination_dto = PaginationDTOFactory(limit=-1)

        interactor.get_list_of_teams_wrapper(
            user_id="1", pagination_dto=pagination_dto, presenter=presenter)

        presenter.get_invalid_limit_response_for_get_list_of_teams \
            .assert_called_once()

    def test_invalid_offset_returns_invalid_offset_response(self):
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(team_storage=team_storage,
                                              user_storage=user_storage)
        pagination_dto = PaginationDTOFactory(offset=-1)
        presenter.get_invalid_offset_response_for_get_list_of_teams \
            .return_value = Mock()

        interactor.get_list_of_teams_wrapper(
            user_id="1", pagination_dto=pagination_dto, presenter=presenter)

        presenter.get_invalid_offset_response_for_get_list_of_teams \
            .assert_called_once()

    def test_given_valid_details_returns_list_of_teams(
            self,
            mocker, expected_list_of_teams_dtos, expected_team_user_ids_dtos,
            expected_list_of_user_dtos):
        # Arrange or Setup
        from ib_iam.tests.common_fixtures.adapters.user_service_mocks import \
            prepare_user_profile_dtos_mock
        team_storage = create_autospec(TeamStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(team_storage=team_storage,
                                              user_storage=user_storage)
        pagination_dto = PaginationDTOFactory()
        user_id = "1"
        team_ids = ["1"]
        total_teams_count = 3
        expected_team_with_members_details_dtos = \
            TeamWithMembersDetailsDTOFactory(
                total_teams_count=total_teams_count,
                team_dtos=expected_list_of_teams_dtos,
                team_user_ids_dtos=expected_team_user_ids_dtos,
                user_dtos=expected_list_of_user_dtos)
        team_storage.get_teams_with_total_teams_count_dto.return_value = \
            TeamsWithTotalTeamsCountDTOFactory(
                teams=expected_list_of_teams_dtos,
                total_teams_count=total_teams_count)
        team_storage.get_team_user_ids_dtos.return_value = \
            expected_team_user_ids_dtos
        presenter.get_response_for_get_list_of_teams.return_value = Mock()
        mock = prepare_user_profile_dtos_mock(mocker)
        mock.return_value = expected_list_of_user_dtos

        # Act
        interactor.get_list_of_teams_wrapper(
            user_id=user_id, pagination_dto=pagination_dto, presenter=presenter
        )

        # Assert
        team_storage.get_teams_with_total_teams_count_dto \
            .assert_called_once_with(pagination_dto=pagination_dto)
        team_storage.get_team_user_ids_dtos.assert_called_once_with(
            team_ids=team_ids)
        presenter.get_response_for_get_list_of_teams.assert_called_once_with(
            team_details_dtos=expected_team_with_members_details_dtos)
