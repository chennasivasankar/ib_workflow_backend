from ib_iam.exceptions import UserHasNoAccess, TeamNameAlreadyExists
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import TeamPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import TeamNameAndDescriptionDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface


class AddTeamInteractor:

    def __init__(self, storage: TeamStorageInterface):
        self.storage = storage

    def add_team_wrapper(
            self,
            user_id: str,
            team_name_and_description_dto: TeamNameAndDescriptionDTO,
            presenter: TeamPresenterInterface
    ):
        try:
            team_id = self.add_team(
                user_id=user_id,
                team_name_and_description_dto=team_name_and_description_dto
            )
            response = presenter.get_response_for_add_team(team_id=team_id)
        except UserHasNoAccess:
            response = presenter.raise_exception_for_user_has_no_access()
        except TeamNameAlreadyExists as exception:
            response = presenter.raise_exception_if_team_name_already_exists(exception)
        return response

    def add_team(self, user_id: str, team_name_and_description_dto: TeamNameAndDescriptionDTO):

        self.storage.raise_exception_if_user_is_not_admin(user_id=user_id)
        team_id = self.storage.get_team_id_if_team_name_already_exists(
            name=team_name_and_description_dto.name
        )
        is_team_name_already_exists = team_id is not None
        if is_team_name_already_exists:
            raise TeamNameAlreadyExists(
                team_name=team_name_and_description_dto.name
            )
        team_id = self.storage.add_team(
            user_id=user_id,
            team_name_and_description_dto=team_name_and_description_dto)
        return team_id
