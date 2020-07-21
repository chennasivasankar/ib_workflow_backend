from ib_iam.exceptions import (
    UserHasNoAccess,
    TeamNameAlreadyExists,
    InvalidUsers,
    DuplicateUsers,
    InvalidTeam
)
from ib_iam.interactors.presenter_interfaces.delete_team_presenter_interface import (
    DeleteTeamPresenterInterface
)
from ib_iam.interactors.presenter_interfaces \
    .update_team_presenter_interface import UpdateTeamPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import TeamWithUserIdsDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)
from typing import List


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
        self.storage.raise_exception_if_user_is_not_admin(user_id=user_id)
        self.storage.raise_exception_if_team_not_exists(team_id=team_id)
        self._raise_exception_if_duplicate_user_ids_found(user_ids=user_ids)
        self._raise_exception_if_invalid_users_found(user_ids=user_ids)
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
        team_member_ids = self.storage.get_member_ids_of_team(team_id=team_id)
        self._add_members_to_team(
            user_ids=user_ids, team_member_ids=team_member_ids, team_id=team_id
        )
        self._delete_members_of_team(
            user_ids=user_ids, team_member_ids=team_member_ids, team_id=team_id
        )

    def delete_team_wrapper(
            self, user_id: str, team_id: str, presenter: DeleteTeamPresenterInterface
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
        self.storage.raise_exception_if_user_is_not_admin(user_id=user_id)
        self.storage.raise_exception_if_team_not_exists(team_id=team_id)
        self.storage.delete_team(team_id=team_id)

    def _add_members_to_team(self, user_ids, team_member_ids, team_id):
        user_ids_to_add = list(set(user_ids) - set(team_member_ids))
        self.storage.add_users_to_team(
            team_id=team_id, user_ids=user_ids_to_add
        )

    def _delete_members_of_team(self, user_ids, team_member_ids, team_id):
        member_ids_to_delete = list(set(team_member_ids) - set(user_ids))
        self.storage.delete_members_from_team(
            team_id=team_id, member_ids=member_ids_to_delete
        )

    @staticmethod
    def _raise_exception_if_duplicate_user_ids_found(user_ids: List[str]):
        is_duplicate_user_ids_exist = len(user_ids) != len(set(user_ids))
        if is_duplicate_user_ids_exist:
            raise DuplicateUsers()

    def _raise_exception_if_invalid_users_found(self, user_ids: List[str]):
        user_ids_from_db = \
            self.storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids
            )
        is_invalid_users_found = len(user_ids) != len(user_ids_from_db)
        if is_invalid_users_found:
            raise InvalidUsers()
