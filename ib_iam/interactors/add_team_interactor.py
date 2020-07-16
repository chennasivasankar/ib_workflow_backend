from ib_iam.exceptions import UserHasNoAccess, DuplicateTeamName
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import AddTeamParametersDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface


class AddTeamInteractor:

    def __init__(self, storage: TeamStorageInterface):
        self.storage = storage

    def add_team_wrapper(
            self,
            user_id: str,
            add_team_params_dto: AddTeamParametersDTO,
            presenter: TeamPresenterInterface
    ):

        try:
            team_id = self.add_team(
                user_id=user_id, add_team_params_dto=add_team_params_dto
            )
            response = presenter.get_response_for_add_team(team_id=team_id)
        except UserHasNoAccess:
            response = presenter.raise_exception_for_user_has_no_access()
        except DuplicateTeamName as exception:
            response = presenter.raise_exception_for_duplicate_team_name(exception)
        return response

    def add_team(self, user_id: str, add_team_params_dto: AddTeamParametersDTO):

        self.storage.is_user_admin(user_id=user_id)

        team_id = self.storage.add_team(user_id=user_id, add_team_params_dto=add_team_params_dto)

        return team_id
