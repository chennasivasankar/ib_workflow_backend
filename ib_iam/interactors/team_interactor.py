from ib_iam.exceptions import UserHasNoAccess
from ib_iam.exceptions.custom_exceptions import (
    InvalidTeamId, TeamNameAlreadyExists
)
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface
)
from ib_iam.interactors.storage_interfaces.dtos import UpdateTeamParametersDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)


class TeamInteractor:

    def __init__(self, storage: TeamStorageInterface):
        self.storage = storage

    def update_team_details_wrapper(
            self,
            user_id: str,
            update_team_parameters_dto: UpdateTeamParametersDTO,
            presenter: TeamPresenterInterface
    ):
        try:
            self.update_team_details(
                user_id=user_id,
                update_team_parameters_dto=update_team_parameters_dto
            )
            response = presenter.make_empty_http_success_response()
        except UserHasNoAccess:
            response = presenter.raise_exception_for_user_has_no_access()
        except InvalidTeamId:
            response = presenter.raise_exception_for_invalid_team_id()
        except TeamNameAlreadyExists as exception:
            response = presenter.raise_exception_if_team_name_already_exists(
                exception
            )
        return response

    def update_team_details(self, user_id: str, update_team_parameters_dto: UpdateTeamParametersDTO):

        self.storage.raise_exception_if_user_is_not_admin(user_id=user_id)
        self.storage.raise_exception_if_team_not_exists(
            team_id=update_team_parameters_dto.team_id
        )

        team_id = self.storage.get_team_id_if_team_name_already_exists(
            name=update_team_parameters_dto.name
        )
        is_team_name_exists = team_id is not None
        if is_team_name_exists:
            is_team_requested_name_already_assigned_to_other = \
                team_id != update_team_parameters_dto.team_id
            if is_team_requested_name_already_assigned_to_other:
                raise TeamNameAlreadyExists(
                    team_name=update_team_parameters_dto.name
                )

        self.storage.update_team_details(
            update_team_parameters_dto=update_team_parameters_dto
        )

    def delete_team_wrapper(
            self, user_id: str, team_id: str, presenter: TeamPresenterInterface
    ):
        try:
            self.delete_team(user_id=user_id, team_id=team_id)
            response = presenter.make_empty_http_success_response()
        except UserHasNoAccess:
            response = presenter.raise_exception_for_user_has_no_access()
        except InvalidTeamId:
            response = presenter.raise_exception_for_invalid_team_id()
        return response

    def delete_team(self, user_id: str, team_id: str):
        self.storage.raise_exception_if_user_is_not_admin(user_id=user_id)
        self.storage.raise_exception_if_team_not_exists(team_id=team_id)
        self.storage.delete_team(team_id=team_id)
