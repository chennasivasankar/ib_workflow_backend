import pytest
from django_swagger_utils.drf_server.exceptions import Unauthorized, BadRequest
from mock import create_autospec, patch
from ib_iam.interactors.get_list_of_teams_interactor import (
    GetListOfTeamsInteractor
)
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface
)
from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
from ib_iam.interactors.presenter_interfaces.dtos import (
    TeamWithMembersDetailsDTO
)


class TestGetListOfTeamsInteractor:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(storage=storage)
        user_id = "1"
        pagination_dto = PaginationDTO(limit=5, offset=0)
        storage.is_user_admin.side_effect = UserHasNoAccess
        presenter.raise_exception_for_user_has_no_access.side_effect = Unauthorized

        with pytest.raises(Unauthorized):
            interactor.get_list_of_teams_wrapper(
                user_id=user_id, pagination_dto=pagination_dto, presenter=presenter
            )

        storage.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.raise_exception_for_user_has_no_access.assert_called_once()

    @pytest.mark.parametrize("limit", [(-1), (0)])
    def test_if_limit_is_invalid_raises_invalid_limit_exception(self, limit):
        from ib_iam.exceptions.custom_exceptions import InvalidLimit
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
        from ib_iam.exceptions.custom_exceptions import InvalidLimit
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(storage=storage)
        pagination_dto = PaginationDTO(limit=5, offset=-1)
        presenter.raise_exception_for_invalid_offset.side_effect = BadRequest

        with pytest.raises(BadRequest):
            interactor.get_list_of_teams_wrapper(
                user_id="1", pagination_dto=pagination_dto, presenter=presenter
            )

        presenter.raise_exception_for_invalid_offset.assert_called_once()

    @patch(
        "ib_iam.adapters.user_service.UserService.get_basic_user_dtos"
    )
    def test_returns_list_of_teams(
            self,
            get_basic_user_dtos_mock,
            expected_list_of_teams_dtos,
            expected_team_member_ids_dtos,
            expected_list_of_user_dtos,
            expected_get_list_of_teams_details,
            expected_list_of_member_dtos
    ):
        # Arrange or Setup
        storage = create_autospec(TeamStorageInterface)
        presenter = create_autospec(TeamPresenterInterface)
        interactor = GetListOfTeamsInteractor(storage=storage)
        pagination_dto = PaginationDTO(limit=5, offset=0)
        user_id = "1"
        team_ids = ["1"]
        member_ids = ["2", "3"]
        total_teams = 3
        expected_team_details_dtos = TeamWithMembersDetailsDTO(
            total_teams=total_teams,
            team_dtos=expected_list_of_teams_dtos,
            team_member_ids_dtos=expected_team_member_ids_dtos,
            member_dtos=expected_list_of_member_dtos
        )
        storage.get_team_dtos_along_with_count.return_value = (
            expected_list_of_teams_dtos, total_teams
        )
        storage.get_team_member_ids_dtos.return_value = (
            expected_team_member_ids_dtos
        )
        get_basic_user_dtos_mock.return_value = expected_list_of_user_dtos
        presenter.get_response_for_get_list_of_teams.return_value = (
            expected_get_list_of_teams_details
        )

        # Act
        actual_list_of_teams_details = interactor.get_list_of_teams_wrapper(
            user_id=user_id, pagination_dto=pagination_dto, presenter=presenter
        )

        # Assert
        assert actual_list_of_teams_details == \
               expected_get_list_of_teams_details
        storage.get_team_dtos_along_with_count.assert_called_once_with(
            user_id=user_id, pagination_dto=pagination_dto
        )
        storage.get_team_member_ids_dtos.assert_called_once_with(
            team_ids=team_ids
        )
        get_basic_user_dtos_mock.assert_called_once_with(user_ids=member_ids)

        presenter.get_response_for_get_list_of_teams.assert_called_once_with(
            team_details_dtos=expected_team_details_dtos
        )
