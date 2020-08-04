from ib_iam.exceptions.custom_exceptions import UserHasNoAccess, \
    TeamNameAlreadyExists, InvalidUserIds, DuplicateUserIds, InvalidTeamId
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces \
    .delete_team_presenter_interface import DeleteTeamPresenterInterface
from ib_iam.interactors.presenter_interfaces \
    .update_team_presenter_interface import UpdateTeamPresenterInterface
from ib_iam.interactors.presenter_interfaces.team_presenter_interface import (
    TeamPresenterInterface)
from ib_iam.interactors.storage_interfaces.team_storage_interface import (
    TeamStorageInterface)
from ib_iam.interactors.storage_interfaces.dtos import (
    TeamWithUserIdsDTO, TeamWithTeamIdAndUserIdsDTO, TeamNameAndDescriptionDTO)


class TeamInteractor(ValidationMixin):

    def __init__(self, storage: TeamStorageInterface):
        self.storage = storage

    def add_team_wrapper(self, user_id: str,
                         team_with_user_ids_dto: TeamWithUserIdsDTO,
                         presenter: TeamPresenterInterface):
        try:
            team_id = self.add_team(
                user_id=user_id,
                team_with_user_ids_dto=team_with_user_ids_dto)
            response = presenter.get_response_for_add_team(team_id=team_id)
        except UserHasNoAccess:
            response = presenter.get_user_has_no_access_response_for_add_team()
        except TeamNameAlreadyExists as exception:
            response = presenter.get_team_name_already_exists_response_for_add_team(
                exception)
        except DuplicateUserIds as exception:
            response = \
                presenter.get_duplicate_users_response_for_add_team(exception)
        except InvalidUserIds as exception:
            response = \
                presenter.get_invalid_users_response_for_add_team(exception)
        return response

    def add_team(self, user_id: str,
                 team_with_user_ids_dto: TeamWithUserIdsDTO):
        user_ids = team_with_user_ids_dto.user_ids
        self.storage.validate_is_user_admin(user_id=user_id)
        self._validate_add_team_details(
            team_with_user_ids_dto=team_with_user_ids_dto)
        team_name_and_description_dto = TeamNameAndDescriptionDTO(
            name=team_with_user_ids_dto.name,
            description=team_with_user_ids_dto.description)
        team_id = self.storage.add_team(
            user_id=user_id,
            team_name_and_description_dto=team_name_and_description_dto)
        self.storage.add_users_to_team(team_id=team_id, user_ids=user_ids)
        return team_id

    def update_team_details_wrapper(
            self, user_id: str,
            team_with_team_id_and_user_ids_dto: TeamWithTeamIdAndUserIdsDTO,
            presenter: UpdateTeamPresenterInterface):
        try:
            self.update_team_details(
                user_id=user_id,
                team_with_team_id_and_user_ids_dto=team_with_team_id_and_user_ids_dto
            )
            response = presenter.get_success_response_for_update_team()
        except UserHasNoAccess:
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
        user_ids = team_with_team_id_and_user_ids_dto.user_ids
        team_id = team_with_team_id_and_user_ids_dto.team_id
        self.storage.validate_is_user_admin(user_id=user_id)
        self._validate_update_team_details(
            team_with_team_id_and_user_ids_dto=team_with_team_id_and_user_ids_dto
        )
        from ib_iam.interactors.storage_interfaces.dtos import TeamDTO
        team_dto = TeamDTO(
            team_id=team_with_team_id_and_user_ids_dto.team_id,
            name=team_with_team_id_and_user_ids_dto.name,
            description=team_with_team_id_and_user_ids_dto.description)
        self.storage.update_team_details(team_dto=team_dto)
        self.storage.delete_all_members_of_team(team_id=team_id)
        self.storage.add_users_to_team(team_id=team_id, user_ids=user_ids)

    def delete_team_wrapper(
            self, user_id: str, team_id: str,
            presenter: DeleteTeamPresenterInterface):
        try:
            self.delete_team(user_id=user_id, team_id=team_id)
            response = presenter.get_success_response_for_delete_team()
        except UserHasNoAccess:
            response = presenter.get_user_has_no_access_response_for_delete_team()
        except InvalidTeamId:
            response = presenter.get_invalid_team_response_for_delete_team()
        return response

    def delete_team(self, user_id: str, team_id: str):
        self.storage.validate_is_user_admin(user_id=user_id)
        self.storage.raise_exception_if_team_not_exists(team_id=team_id)
        self.storage.delete_team(team_id=team_id)

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
        self.storage.raise_exception_if_team_not_exists(team_id=team_id)
        self._validate_duplicate_or_invalid_users(
            user_ids=team_with_team_id_and_user_ids_dto.user_ids)
        self._validate_is_team_name_exists_for_update_team(
            name=name, team_id=team_id)

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
