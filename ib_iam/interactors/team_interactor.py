from typing import List

from ib_iam.app_interfaces.dtos import UserTeamsDTO
from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin, \
    TeamNameAlreadyExists, InvalidUserIds, DuplicateUserIds, InvalidTeamId, \
    InvalidTeamIds
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces \
    .delete_team_presenter_interface import DeleteTeamPresenterInterface
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface)
from ib_iam.interactors.presenter_interfaces \
    .update_team_presenter_interface import UpdateTeamPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import (
    TeamWithUserIdsDTO, TeamWithTeamIdAndUserIdsDTO, TeamNameAndDescriptionDTO,
    TeamIdAndNameDTO, UserTeamDTO)
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface)
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class TeamInteractor(ValidationMixin):

    def __init__(self,
                 team_storage: TeamStorageInterface,
                 user_storage: UserStorageInterface):
        self.user_storage = user_storage
        self.team_storage = team_storage

    def add_team_wrapper(self, user_id: str,
                         team_with_user_ids_dto: TeamWithUserIdsDTO,
                         presenter: TeamPresenterInterface):
        try:
            team_id = self.add_team(
                user_id=user_id,
                team_with_user_ids_dto=team_with_user_ids_dto)
            response = presenter.get_response_for_add_team(team_id=team_id)
        except UserIsNotAdmin:
            response = presenter.get_user_has_no_access_response_for_add_team()
        except TeamNameAlreadyExists as exception:
            response = presenter \
                .get_team_name_already_exists_response_for_add_team(exception)
        except DuplicateUserIds as exception:
            response = \
                presenter.get_duplicate_users_response_for_add_team(exception)
        except InvalidUserIds as exception:
            response = \
                presenter.get_invalid_users_response_for_add_team(exception)
        return response

    def add_team(self, user_id: str,
                 team_with_user_ids_dto: TeamWithUserIdsDTO):
        self._validate_is_user_admin(user_id=user_id)
        self._validate_add_team_details(
            team_with_user_ids_dto=team_with_user_ids_dto)
        team_name_and_description_dto = TeamNameAndDescriptionDTO(
            name=team_with_user_ids_dto.name,
            description=team_with_user_ids_dto.description)
        team_id = self.team_storage.add_team(
            user_id=user_id,
            team_name_and_description_dto=team_name_and_description_dto)
        self.team_storage.add_users_to_team(
            team_id=team_id, user_ids=team_with_user_ids_dto.user_ids)
        return team_id

    def update_team_details_wrapper(
            self, user_id: str,
            team_with_team_id_and_user_ids_dto: TeamWithTeamIdAndUserIdsDTO,
            presenter: UpdateTeamPresenterInterface):
        try:
            self.update_team_details(user_id=user_id,
                                     team_with_team_id_and_user_ids_dto=
                                     team_with_team_id_and_user_ids_dto)
            response = presenter.get_success_response_for_update_team()
        except UserIsNotAdmin:
            response = \
                presenter.get_user_has_no_access_response_for_update_team()
        except InvalidTeamId:
            response = presenter.get_invalid_team_response_for_update_team()
        except DuplicateUserIds as exception:
            response = \
                presenter.get_duplicate_users_response_for_update_team(
                    exception)
        except InvalidUserIds as exception:
            response = \
                presenter.get_invalid_users_response_for_update_team(exception)
        except TeamNameAlreadyExists as exception:
            response = presenter \
                .get_team_name_already_exists_response_for_update_team(
                exception)
        return response

    def update_team_details(
            self, user_id: str,
            team_with_team_id_and_user_ids_dto: TeamWithTeamIdAndUserIdsDTO):
        self._validate_is_user_admin(user_id=user_id)
        self._validate_update_team_details(team_with_team_id_and_user_ids_dto=
                                           team_with_team_id_and_user_ids_dto)
        user_ids = team_with_team_id_and_user_ids_dto.user_ids
        team_id = team_with_team_id_and_user_ids_dto.team_id
        from ib_iam.interactors.storage_interfaces.dtos import TeamDTO
        team_dto = TeamDTO(
            team_id=team_with_team_id_and_user_ids_dto.team_id,
            name=team_with_team_id_and_user_ids_dto.name,
            description=team_with_team_id_and_user_ids_dto.description)
        self.team_storage.update_team_details(team_dto=team_dto)
        team_user_ids = self.team_storage.get_member_ids_of_team(
            team_id=team_id)
        self._add_members_to_team(
            user_ids=user_ids, team_user_ids=team_user_ids, team_id=team_id)
        self._delete_members_of_team(
            user_ids=user_ids, team_user_ids=team_user_ids, team_id=team_id)

    def delete_team_wrapper(
            self, user_id: str, team_id: str,
            presenter: DeleteTeamPresenterInterface):
        try:
            self.delete_team(user_id=user_id, team_id=team_id)
            response = presenter.get_success_response_for_delete_team()
        except UserIsNotAdmin:
            response = presenter \
                .get_user_has_no_access_response_for_delete_team()
        except InvalidTeamId:
            response = presenter.get_invalid_team_response_for_delete_team()
        return response

    def delete_team(self, user_id: str, team_id: str):
        self._validate_is_user_admin(user_id=user_id)
        self.team_storage.raise_exception_if_team_not_exists(team_id=team_id)
        self.team_storage.delete_team(team_id=team_id)

    def _validate_add_team_details(
            self, team_with_user_ids_dto: TeamWithUserIdsDTO):
        name = team_with_user_ids_dto.name
        self._validate_duplicate_or_invalid_users(
            user_ids=team_with_user_ids_dto.user_ids)
        self._validate_is_team_name_already_exists(name=name)

    def _validate_update_team_details(
            self,
            team_with_team_id_and_user_ids_dto: TeamWithTeamIdAndUserIdsDTO):
        name = team_with_team_id_and_user_ids_dto.name
        team_id = team_with_team_id_and_user_ids_dto.team_id
        self.team_storage.raise_exception_if_team_not_exists(team_id=team_id)
        self._validate_duplicate_or_invalid_users(
            user_ids=team_with_team_id_and_user_ids_dto.user_ids)
        self._validate_is_team_name_exists_for_update_team(
            name=name, team_id=team_id)

    def _add_members_to_team(self, user_ids, team_user_ids, team_id):
        user_ids_to_add = list(set(user_ids) - set(team_user_ids))
        self.team_storage.add_users_to_team(
            team_id=team_id, user_ids=user_ids_to_add)

    def _delete_members_of_team(self, user_ids, team_user_ids, team_id):
        member_ids_to_delete = list(set(team_user_ids) - set(user_ids))
        self.team_storage.delete_members_from_team(
            team_id=team_id, user_ids=member_ids_to_delete)

    def _validate_is_team_name_already_exists(self, name: str):
        team_id = \
            self.team_storage.get_team_id_if_team_name_already_exists(
                name=name)
        is_team_name_already_exists = team_id is not None
        if is_team_name_already_exists:
            raise TeamNameAlreadyExists(team_name=name)

    def _validate_is_team_name_exists_for_update_team(self, name, team_id):
        team_id_from_db = \
            self.team_storage.get_team_id_if_team_name_already_exists(
                name=name)
        is_team_name_exists = team_id_from_db is not None
        if is_team_name_exists:
            is_team_requested_name_already_assigned_to_other = \
                team_id_from_db != team_id
            if is_team_requested_name_already_assigned_to_other:
                raise TeamNameAlreadyExists(team_name=name)

    def get_valid_team_ids(self, team_ids: List[str]) -> List[str]:
        # todo check for duplicate team_ids and raise exception
        valid_team_ids = self.team_storage.get_valid_team_ids(
            team_ids=team_ids)
        return valid_team_ids

    def get_teams(self, team_ids: List[str]) -> List[TeamIdAndNameDTO]:
        team_id_and_name_dtos = self.team_storage.get_team_id_and_name_dtos(
            team_ids=team_ids)
        if len(team_ids) != len(team_id_and_name_dtos):
            raise InvalidTeamIds
        return team_id_and_name_dtos

    def get_user_teams_for_each_user(
            self, user_ids: List[str]) -> List[UserTeamsDTO]:
        valid_user_ids = self.user_storage.get_valid_user_ids(
            user_ids=user_ids)
        if len(valid_user_ids) != len(user_ids):
            invalid_user_ids = set(user_ids) - set(valid_user_ids)
            raise InvalidUserIds(invalid_user_ids)
        user_team_dtos = self.user_storage.get_team_details_of_users_bulk(
            user_ids=user_ids)
        return self._fetch_user_teams_for_each_user(
            user_team_dtos=user_team_dtos)

    def _fetch_user_teams_for_each_user(
            self, user_team_dtos: List[UserTeamDTO]
    ) -> List[UserTeamsDTO]:
        user_teams_dict = {}
        for user_team_dto in user_team_dtos:
            try:
                user_teams_dict[
                    user_team_dto.user_id
                ].user_teams.append(
                    self._convert_to_team_id_and_name_dto(
                        user_team_dto=user_team_dto)
                )
            except KeyError:
                user_teams_dict[user_team_dto.user_id] = UserTeamsDTO(
                    user_id=user_team_dto.user_id, user_teams=[
                        self._convert_to_team_id_and_name_dto(
                            user_team_dto=user_team_dto)
                    ]
                )
        return list(user_teams_dict.values())

    @staticmethod
    def _convert_to_team_id_and_name_dto(
            user_team_dto: UserTeamDTO) -> TeamIdAndNameDTO:
        return TeamIdAndNameDTO(
            team_id=user_team_dto.team_id, team_name=user_team_dto.team_name)
