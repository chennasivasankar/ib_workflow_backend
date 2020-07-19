from typing import List

from ib_iam.exceptions import (
    UserHasNoAccess, TeamNameAlreadyExists, InvalidMembers, DuplicateMembers
)
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface
)
from ib_iam.interactors.storage_interfaces.dtos import AddTeamParametersDTO
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface
)


class AddTeamInteractor:

    def __init__(self, storage: TeamStorageInterface):
        self.storage = storage

    def add_team_wrapper(
            self,
            user_id: str,
            add_team_parameters_dto: AddTeamParametersDTO,
            presenter: TeamPresenterInterface
    ):
        try:
            team_id = self.add_team(
                user_id=user_id,
                add_team_parameters_dto=add_team_parameters_dto
            )
            response = presenter.get_response_for_add_team(team_id=team_id)
        except UserHasNoAccess:
            response = presenter.raise_exception_for_user_has_no_access()
        except TeamNameAlreadyExists as exception:
            response = presenter.raise_exception_if_team_name_already_exists(exception)
        except DuplicateMembers:
            response = presenter.raise_exception_for_duplicate_members()
        except InvalidMembers:
            response = presenter.raise_exception_for_invalid_members()
        return response

    def add_team(self, user_id: str, add_team_parameters_dto: AddTeamParametersDTO):
        member_ids = add_team_parameters_dto.member_ids
        self.storage.raise_exception_if_user_is_not_admin(user_id=user_id)
        team_id = self.storage.get_team_id_if_team_name_already_exists(
            name=add_team_parameters_dto.name
        )
        is_team_name_already_exists = team_id is not None
        if is_team_name_already_exists:
            raise TeamNameAlreadyExists(
                team_name=add_team_parameters_dto.name
            )
        self._raise_exception_if_duplicate_member_ids_found(
            member_ids=member_ids
        )
        self._raise_exception_if_invalid_members_found(member_ids=member_ids)
        team_id = self.storage.add_team(
            user_id=user_id,
            add_team_parameters_dto=add_team_parameters_dto
        )
        self.storage.add_members_to_team(
            team_id=team_id, member_ids=member_ids
        )
        return team_id

    def _raise_exception_if_duplicate_member_ids_found(
        self, member_ids: List[str]
    ):
        is_duplicate_member_ids_exist = len(member_ids) != len(set(member_ids))
        if is_duplicate_member_ids_exist:
            raise DuplicateMembers()

    def _raise_exception_if_invalid_members_found(self, member_ids: List[str]):
        member_ids_from_db = \
            self.storage.get_valid_member_ids_among_the_given_member_ids(
                member_ids=member_ids
            )
        is_invalid_members_found = len(member_ids) != len(member_ids_from_db)
        if is_invalid_members_found:
            raise InvalidMembers()
