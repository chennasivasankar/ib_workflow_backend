from typing import List
from ib_iam.exceptions.custom_exceptions import UserHasNoAccess, \
    TeamNameAlreadyExists, InvalidUsers, DuplicateUsers, InvalidTeam
from ib_iam.interactors.presenter_interfaces \
    .delete_team_presenter_interface import DeleteTeamPresenterInterface
from ib_iam.interactors.presenter_interfaces \
    .update_team_presenter_interface import UpdateTeamPresenterInterface
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface
)
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)
from ib_iam.interactors.storage_interfaces.dtos import (
    TeamDetailsWithUserIdsDTO, TeamWithUserIdsDTO
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
            response = presenter.get_team_name_already_exists_response_for_add_team(
                exception)
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
            response = presenter.get_success_response_for_update_team()
        except UserHasNoAccess:
            response = \
                presenter.get_user_has_no_access_response_for_update_team()
        except InvalidTeam:
            response = presenter.get_invalid_team_response_for_update_team()
        except DuplicateUsers:
            response = presenter.get_duplicate_users_response_for_update_team()
        except InvalidUsers:
            response = presenter.get_invalid_users_response_for_update_team()
        except TeamNameAlreadyExists as exception:
            response = presenter \
                .get_team_name_already_exists_response_for_update_team(
                exception
            )
        return response

    def update_team_details(
            self, user_id: str, team_with_user_ids_dto: TeamWithUserIdsDTO
    ):
        user_ids = team_with_user_ids_dto.user_ids
        team_id = team_with_user_ids_dto.team_id
        self.storage.validate_is_user_admin(user_id=user_id)
        self._validate_update_team_details(
            team_with_user_ids_dto=team_with_user_ids_dto
        )
        self.storage.update_team_details(
            team_with_user_ids_dto=team_with_user_ids_dto
        )
        team_user_ids = self.storage.get_member_ids_of_team(team_id=team_id)
        self._add_members_to_team(
            user_ids=user_ids, team_user_ids=team_user_ids, team_id=team_id
        )
        self._delete_members_of_team(
            user_ids=user_ids, team_user_ids=team_user_ids, team_id=team_id
        )

    def delete_team_wrapper(
            self, user_id: str, team_id: str,
            presenter: DeleteTeamPresenterInterface
    ):
        try:
            self.delete_team(user_id=user_id, team_id=team_id)
            response = presenter.get_success_response_for_delete_team()
        except UserHasNoAccess:
            response = presenter.get_user_has_no_access_response_for_delete_team()
        except InvalidTeam:
            response = presenter.get_invalid_team_response_for_delete_team()
        return response

    def delete_team(self, user_id: str, team_id: str):
        self.storage.validate_is_user_admin(user_id=user_id)
        self.storage.raise_exception_if_team_not_exists(team_id=team_id)
        self.storage.delete_team(team_id=team_id)

    def _validate_add_team_details(
            self, team_details_with_user_ids_dto: TeamDetailsWithUserIdsDTO
    ):
        name = team_details_with_user_ids_dto.name
        self._validate_users(user_ids=team_details_with_user_ids_dto.user_ids)
        self._validate_is_team_name_already_exists(name=name)

    def _validate_update_team_details(
            self, team_with_user_ids_dto: TeamWithUserIdsDTO
    ):
        name = team_with_user_ids_dto.name
        team_id = team_with_user_ids_dto.team_id
        self.storage.raise_exception_if_team_not_exists(team_id=team_id)
        self._validate_users(user_ids=team_with_user_ids_dto.user_ids)
        self._validate_is_team_name_exists_for_update_team(
            name=name, team_id=team_id)

    def _add_members_to_team(self, user_ids, team_user_ids, team_id):
        user_ids_to_add = list(set(user_ids) - set(team_user_ids))
        self.storage.add_users_to_team(
            team_id=team_id, user_ids=user_ids_to_add)

    def _delete_members_of_team(self, user_ids, team_user_ids, team_id):
        member_ids_to_delete = list(set(team_user_ids) - set(user_ids))
        self.storage.delete_members_from_team(
            team_id=team_id, user_ids=member_ids_to_delete)

    def _validate_users(self, user_ids):
        self._validate_is_duplicate_users_exists(user_ids=user_ids)
        self._validate_is_invalid_users_exists(user_ids=user_ids)

    @staticmethod
    def _validate_is_duplicate_users_exists(user_ids: List[str]):
        is_duplicate_user_ids_exist = len(user_ids) != len(set(user_ids))
        if is_duplicate_user_ids_exist:
            raise DuplicateUsers()

    def _validate_is_invalid_users_exists(self, user_ids: List[str]):
        user_ids_from_db = \
            self.storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids)
        is_invalid_users_found = len(user_ids) != len(user_ids_from_db)
        if is_invalid_users_found:
            raise InvalidUsers()

    def _validate_is_team_name_already_exists(self, name: str):
        team_id = \
            self.storage.get_team_id_if_team_name_already_exists(name=name)
        is_team_name_already_exists = team_id is not None
        if is_team_name_already_exists:
            raise TeamNameAlreadyExists(team_name=name)

    def _validate_is_team_name_exists_for_update_team(self, name, team_id):
        team_id_from_db = \
            self.storage.get_team_id_if_team_name_already_exists(name=name)
        is_team_name_exists = team_id_from_db is not None
        if is_team_name_exists:
            is_team_requested_name_already_assigned_to_other = \
                team_id_from_db != team_id
            if is_team_requested_name_already_assigned_to_other:
                raise TeamNameAlreadyExists(team_name=name)
