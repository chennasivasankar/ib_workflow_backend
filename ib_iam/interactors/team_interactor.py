from ib_iam.exceptions import UserHasNoAccess
from ib_iam.exceptions.custom_exceptions import InvalidTeamId, DuplicateTeamName
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import UpdateTeamParametersDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface


class TeamInteractor:

    def __init__(self, storage: TeamStorageInterface):
        self.storage = storage

    def update_team_details_wrapper(self, user_id: str, update_team_parameters_dto: UpdateTeamParametersDTO,
                                    presenter: TeamPresenterInterface):
        try:
            self.update_team_details(
                user_id=user_id, update_team_parameters_dto=update_team_parameters_dto
            )
            response = presenter.make_empty_http_success_response()
        except UserHasNoAccess:
            response = presenter.raise_exception_for_user_has_no_access()
        except InvalidTeamId:
            response = presenter.raise_exception_for_invalid_team_id()
        except DuplicateTeamName as exception:
            response = presenter.raise_exception_for_duplicate_team_name(
                exception
            )
        return response

    def update_team_details(self, user_id: str, update_team_parameters_dto: UpdateTeamParametersDTO):

        self.storage.is_user_admin(user_id=user_id)
        self.storage.is_valid_team(
            team_id=update_team_parameters_dto.team_id
        )
        self.storage.is_duplicate_name(
            team_id=update_team_parameters_dto.team_id,
            name=update_team_parameters_dto.name
        )
        self.storage.update_team_details(
            update_team_parameters_dto=update_team_parameters_dto
        )
