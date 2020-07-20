from ib_iam.exceptions import UserHasNoAccess
from ib_iam.exceptions.custom_exceptions import (
    InvalidTeam, TeamNameAlreadyExists
)
from ib_iam.interactors.presenter_interfaces \
    .update_team_presenter_interface import UpdateTeamPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import TeamWithUserIdsDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)


class TeamInteractor:

    def __init__(self, storage: TeamStorageInterface):
        self.storage = storage

    def update_team_details_wrapper(
            self,
            user_id: str,
            team_with_user_ids_dto: TeamWithUserIdsDTO,
            presenter: UpdateTeamPresenterInterface
    ):
        try:
            self.update_team_details(
                user_id=user_id,
                team_with_user_ids_dto=team_with_user_ids_dto
            )
            response = presenter.make_empty_http_success_response()
        except UserHasNoAccess:
            response = \
                presenter.get_user_has_no_access_response_for_update_team()
        except InvalidTeam:
            response = presenter.get_invalid_team_response_for_update_team()
        except TeamNameAlreadyExists as exception:
            response = presenter \
                        .get_team_name_already_exists_response_for_update_team(
                            exception
                        )
        return response

    def update_team_details(
            self, user_id: str, team_with_user_ids_dto: TeamWithUserIdsDTO
    ):

        self.storage.raise_exception_if_user_is_not_admin(user_id=user_id)
        self.storage.raise_exception_if_team_not_exists(
            team_id=team_with_user_ids_dto.team_id
        )

        team_id = self.storage.get_team_id_if_team_name_already_exists(
            name=team_with_user_ids_dto.name
        )
        is_team_name_exists = team_id is not None
        if is_team_name_exists:
            is_team_requested_name_already_assigned_to_other = \
                team_id != team_with_user_ids_dto.team_id
            if is_team_requested_name_already_assigned_to_other:
                raise TeamNameAlreadyExists(
                    team_name=team_with_user_ids_dto.name
                )

        self.storage.update_team_details(
            team_with_user_ids_dto=team_with_user_ids_dto
        )
