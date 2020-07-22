from typing import List

from ib_iam.exceptions import (
    UserHasNoAccess,
    TeamNameAlreadyExists,
    InvalidUsers,
    DuplicateUsers
)
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface
)
from ib_iam.interactors.storage_interfaces.dtos import (
    TeamDetailsWithUserIdsDTO
)
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)


class TeamInteractor:

    def __init__(self, storage: TeamStorageInterface):
        self.storage = storage

    def add_team_wrapper(
            self,
            user_id: str,
            team_details_with_user_ids_dto: TeamDetailsWithUserIdsDTO,
            presenter: TeamPresenterInterface
    ):
        try:
            team_id = self.add_team(
                user_id=user_id,
                team_details_with_user_ids_dto=team_details_with_user_ids_dto
            )
            response = presenter.get_response_for_add_team(team_id=team_id)
        except UserHasNoAccess:
            response = presenter.get_user_has_no_access_response_for_add_team()
        except TeamNameAlreadyExists as exception:
            response = presenter.get_team_name_already_exists_response_for_add_team(exception)
        except DuplicateUsers:
            response = presenter.get_duplicate_users_response_for_add_team()
        except InvalidUsers:
            response = presenter.get_invalid_users_response_for_add_team()
        return response

    def add_team(
            self,
            user_id: str,
            team_details_with_user_ids_dto: TeamDetailsWithUserIdsDTO
    ):
        user_ids = team_details_with_user_ids_dto.user_ids
        self.storage.validate_is_user_admin(user_id=user_id)
        self._validate_add_team_details(
            team_details_with_user_ids_dto=team_details_with_user_ids_dto
        )
        team_id = self.storage.add_team(
            user_id=user_id,
            team_details_with_user_ids_dto=team_details_with_user_ids_dto
        )
        self.storage.add_users_to_team(
            team_id=team_id, user_ids=user_ids
        )
        return team_id

    def _validate_add_team_details(self, team_details_with_user_ids_dto):
        user_ids = team_details_with_user_ids_dto.user_ids
        name = team_details_with_user_ids_dto.name
        self._validate_is_duplicate_users_exists(user_ids=user_ids)
        self._validate_is_invalid_users_exists(user_ids=user_ids)
        self._validate_is_team_name_already_exists(name=name)

    @staticmethod
    def _validate_is_duplicate_users_exists(user_ids: List[str]):
        is_duplicate_user_ids_exist = len(user_ids) != len(set(user_ids))
        if is_duplicate_user_ids_exist:
            raise DuplicateUsers()

    def _validate_is_invalid_users_exists(self, user_ids: List[str]):
        user_ids_from_db = \
            self.storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids
            )
        is_invalid_users_found = len(user_ids) != len(user_ids_from_db)
        if is_invalid_users_found:
            raise InvalidUsers()

    def _validate_is_team_name_already_exists(self, name: str):
        team_id = \
            self.storage.get_team_id_if_team_name_already_exists(name=name)
        is_team_name_already_exists = team_id is not None
        if is_team_name_already_exists:
            raise TeamNameAlreadyExists(team_name=name)
