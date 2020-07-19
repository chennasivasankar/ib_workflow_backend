import pytest
from django_swagger_utils.drf_server.exceptions import Unauthorized, BadRequest
from mock import create_autospec, Mock
from ib_iam.interactors.get_list_of_teams_interactor import (
    GetListOfTeamsInteractor
)
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface
)
from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO, TeamsWithTotalTeamsCountDTO
from ib_iam.tests.factories.presenter_dtos import TeamWithMembersDetailsDTOFactory
from ib_iam.tests.factories.storage_dtos import TeamsWithTotalTeamsCountDTOFactory, PaginationDTOFactory


class TestGetListOfTeamsInteractor:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(storage=storage)
        user_id = "1"
        pagination_dto = PaginationDTO(limit=5, offset=0)
        storage.raise_exception_if_user_is_not_admin.side_effect = UserHasNoAccess
        presenter.raise_exception_for_user_has_no_access.side_effect = Unauthorized

        with pytest.raises(Unauthorized):
            interactor.get_list_of_teams_wrapper(
                user_id=user_id, pagination_dto=pagination_dto, presenter=presenter
            )

        storage.raise_exception_if_user_is_not_admin.assert_called_once_with(user_id=user_id)
        presenter.raise_exception_for_user_has_no_access.assert_called_once()

    @pytest.mark.parametrize("limit", [-1, 0])
    def test_if_limit_is_invalid_raises_invalid_limit_exception(self, limit):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(storage=storage)
        presenter.raise_exception_for_invalid_limit.side_effect = BadRequest
        pagination_dto = PaginationDTO(limit=limit, offset=5)

        with pytest.raises(BadRequest):
            interactor.get_list_of_teams_wrapper(
                user_id="1", pagination_dto=pagination_dto, presenter=presenter
            )

        presenter.raise_exception_for_invalid_limit.assert_called_once()

    def test_if_offset_is_invalid_raises_invalid_offset_exception(self):
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(storage=storage)
        pagination_dto = PaginationDTOFactory(offset=-1)
        presenter.raise_exception_for_invalid_offset.side_effect = BadRequest

        with pytest.raises(BadRequest):
            interactor.get_list_of_teams_wrapper(
                user_id="1", pagination_dto=pagination_dto, presenter=presenter
            )

        presenter.raise_exception_for_invalid_offset.assert_called_once()

    def test_whether_it_returns_list_of_teams(
            self,
            mocker,
            expected_list_of_teams_dtos,
            expected_team_member_ids_dtos,
            expected_list_of_user_dtos,
            expected_list_of_member_dtos
    ):
        # Arrange or Setup
        from ib_iam.tests.common_fixtures.adapters.user_service_mocks import (
            prepare_user_profile_dtos_mock
        )
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(storage=storage)
        pagination_dto = PaginationDTOFactory()
        user_id = "1"
        team_ids = ["1"]
        total_teams_count = 3
        expected_team_with_members_details_dtos = \
            TeamWithMembersDetailsDTOFactory(
                total_teams_count=total_teams_count,
                team_dtos=expected_list_of_teams_dtos,
                team_member_ids_dtos=expected_team_member_ids_dtos,
                member_dtos=expected_list_of_member_dtos
            )
        storage.get_teams_with_total_teams_count_dto.return_value = \
            TeamsWithTotalTeamsCountDTOFactory(
                teams=expected_list_of_teams_dtos,
                total_teams_count=total_teams_count
            )
        storage.get_team_member_ids_dtos.return_value = (
            expected_team_member_ids_dtos
        )
        presenter.get_response_for_get_list_of_teams.return_value = Mock()
        mock = prepare_user_profile_dtos_mock(mocker)
        mock.return_value = expected_list_of_user_dtos

        # Act
        interactor.get_list_of_teams_wrapper(
            user_id=user_id, pagination_dto=pagination_dto, presenter=presenter
        )

        # Assert
        storage.get_teams_with_total_teams_count_dto.assert_called_once_with(
            pagination_dto=pagination_dto
        )
        storage.get_team_member_ids_dtos.assert_called_once_with(
            team_ids=team_ids
        )
        presenter.get_response_for_get_list_of_teams.assert_called_once_with(
            team_details_dtos=expected_team_with_members_details_dtos
        )
