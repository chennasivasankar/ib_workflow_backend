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
