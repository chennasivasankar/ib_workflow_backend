from typing import List, Tuple, Optional

from ib_iam.app_interfaces.dtos import (
    ProjectTeamUserDTO, UserIdWithTeamIDAndNameDTO, ProjectTeamsAndUsersDTO,
    UserTeamsDTO)
from ib_iam.exceptions.custom_exceptions import (
    ProjectNameAlreadyExists, ProjectDisplayIdAlreadyExists, DuplicateTeamIds,
    TeamIdsAreInvalid, UserIsNotAdmin, InvalidProjectId, RoleIdsAreDuplicated,
    RoleIdsAreInvalid, InvalidUserIds, InvalidUserId, InvalidProjectIds,
    DuplicateRoleNamesExists, RoleNamesAlreadyExists)
from ib_iam.interactors.dtos.dtos import (
    ProjectWithTeamIdsAndRolesDTO, CompleteProjectDetailsDTO,
    UserIdWithProjectIdAndStatusDTO)
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces \
    .add_project_presenter_interface import AddProjectPresenterInterface
from ib_iam.interactors.presenter_interfaces \
    .update_project_presenter_interface import UpdateProjectPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import (
    ProjectWithoutIdDTO, RoleDTO, RoleNameAndDescriptionDTO,
    ProjectWithDisplayIdDTO, ProjectDTO, TeamWithUserIdDTO, TeamIdAndNameDTO)
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class UsersNotExistsForGivenProject(Exception):
    def __init__(self, user_ids):
        self.user_ids = user_ids


class TeamsNotExistForGivenProject(Exception):
    def __init__(self, team_ids: List[str]):
        self.team_ids = team_ids


class UsersNotExistsForGivenTeams(Exception):
    def __init__(self, user_ids: List[str]):
        self.user_ids = user_ids


class ProjectInteractor(ValidationMixin):

    def __init__(
            self, project_storage: ProjectStorageInterface,
            team_storage: TeamStorageInterface,
            user_storage: UserStorageInterface
    ):
        self.project_storage = project_storage
        self.team_storage = team_storage
        self.user_storage = user_storage

    def add_projects(self, project_dtos: List[ProjectWithDisplayIdDTO]):
        # todo check for duplicate project_ids in dtos
        # todo get to know if any permissions has to apply
        # todo check if name or project_id is empty in any project dto
        self.project_storage.add_projects(project_dtos=project_dtos)

    def get_valid_project_ids(self, project_ids):
        # todo check for duplicate project_ids
        valid_project_ids = \
            self.project_storage.get_valid_project_ids_from_given_project_ids(
                project_ids=project_ids)
        return valid_project_ids

    def get_project_dtos_bulk(
            self, project_ids: List[str]) -> List[ProjectDTO]:
        project_dtos = self.project_storage. \
            get_project_dtos_for_given_project_ids(project_ids=project_ids)
        invalid_project_ids = self._get_invalid_project_ids(
            project_dtos=project_dtos, project_ids=project_ids)
        if invalid_project_ids:
            from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
            raise InvalidProjectIds(project_ids=project_ids)
        return project_dtos

    @staticmethod
    def _get_invalid_project_ids(
            project_dtos: List[ProjectDTO], project_ids: List[str]
    ) -> List[str]:
        for project_dto in project_dtos:
            if project_dto.project_id in project_ids:
                project_ids.remove(project_dto.project_id)
        return project_ids

    def get_team_details_for_given_project_team_user_details_dto(
            self, project_team_user_dto: ProjectTeamUserDTO
    ) -> UserIdWithTeamIDAndNameDTO:
        # todo confirm and add invalid team and user exceptions
        self._validate_project(project_id=project_team_user_dto.project_id)
        self._validate_team_existence_in_project(
            project_team_user_dto=project_team_user_dto)
        self._validate_user_existence_in_given_team(
            project_team_user_dto=project_team_user_dto)
        name = self.project_storage.get_team_name(
            team_id=project_team_user_dto.team_id)
        from ib_iam.app_interfaces.dtos import UserIdWithTeamIDAndNameDTO
        user_id_with_team_id_and_name_dto = UserIdWithTeamIDAndNameDTO(
            user_id=project_team_user_dto.user_id,
            team_id=project_team_user_dto.team_id,
            name=name)
        return user_id_with_team_id_and_name_dto

    def get_user_team_dtos_for_given_project_teams_and_users_details_dto(
            self, project_teams_and_users_dto: ProjectTeamsAndUsersDTO
    ) -> List[TeamWithUserIdDTO]:
        project_id = project_teams_and_users_dto.project_id
        user_ids, team_ids = self._fetch_user_ids_and_team_ids(
            project_teams_and_users_dto=project_teams_and_users_dto)
        user_ids = list(set(user_ids))
        team_ids = list(set(team_ids))
        self._validate_project(project_id=project_id)
        valid_team_ids = self.project_storage \
            .get_valid_team_ids_for_given_project(project_id=project_id,
                                                  team_ids=team_ids)
        invalid_team_ids = list(set(team_ids) - set(valid_team_ids))
        if invalid_team_ids:
            raise TeamsNotExistForGivenProject(team_ids=invalid_team_ids)
        team_user_dtos = self.team_storage.get_team_user_dtos(
            team_ids=valid_team_ids, user_ids=user_ids)
        invalid_user_ids = self._get_invalid_user_ids_for_given_team_ids(
            user_ids=user_ids, team_user_dtos=team_user_dtos)
        if invalid_user_ids:
            raise UsersNotExistsForGivenTeams(user_ids=invalid_user_ids)
        return team_user_dtos

    @staticmethod
    def _get_invalid_user_ids_for_given_team_ids(
            user_ids: List[str], team_user_dtos: List[TeamWithUserIdDTO]
    ) -> List[str]:
        for team_user_dto in team_user_dtos:
            if team_user_dto.user_id in user_ids:
                user_ids.remove(team_user_dto.user_id)
        return user_ids

    @staticmethod
    def _fetch_user_ids_and_team_ids(
            project_teams_and_users_dto: ProjectTeamsAndUsersDTO
    ) -> Tuple[List[str], List[str]]:
        user_ids = []
        team_ids = []
        user_and_team_id_dtos = project_teams_and_users_dto \
            .user_id_with_team_id_dtos
        for user_and_team_id_dto in user_and_team_id_dtos:
            user_ids.append(user_and_team_id_dto.user_id)
            team_ids.append(user_and_team_id_dto.team_id)
        return user_ids, team_ids

    def is_valid_user_id_for_given_project(
            self, user_id: str, project_id: str) -> bool:
        self._validate_user_id(user_id=user_id)
        self._validate_project(project_id=project_id)
        return self.project_storage.is_user_exist_given_project(
            user_id=user_id, project_id=project_id)

    def _validate_user_id(self, user_id: str):
        is_valid_user_id = self.user_storage.is_user_exist(user_id=user_id)
        if not is_valid_user_id:
            from ib_iam.exceptions.custom_exceptions import InvalidUserId
            raise InvalidUserId

    def _validate_project(self, project_id: str):
        valid_project_ids = self.project_storage \
            .get_valid_project_ids_from_given_project_ids(
            project_ids=[project_id])
        is_not_valid_project = not (
                len(valid_project_ids) == 1 and
                valid_project_ids[0] == project_id
        )
        if is_not_valid_project:
            from ib_iam.exceptions.custom_exceptions import InvalidProjectId
            raise InvalidProjectId

    def _validate_team_existence_in_project(
            self, project_team_user_dto: ProjectTeamUserDTO):
        is_team_exists_in_project = self.project_storage \
            .is_team_exists_in_project(
            project_id=project_team_user_dto.project_id,
            team_id=project_team_user_dto.team_id)
        is_team_not_exists_in_project = not is_team_exists_in_project
        if is_team_not_exists_in_project:
            from ib_iam.exceptions.custom_exceptions import \
                TeamNotExistsInGivenProject
            raise TeamNotExistsInGivenProject

    def _validate_user_existence_in_given_team(
            self, project_team_user_dto: ProjectTeamUserDTO):
        is_user_exists_in_team = self.project_storage \
            .is_user_exists_in_team(team_id=project_team_user_dto.team_id,
                                    user_id=project_team_user_dto.user_id)
        is_user_not_exists_in_team = not is_user_exists_in_team
        if is_user_not_exists_in_team:
            from ib_iam.exceptions.custom_exceptions import \
                UserNotExistsInGivenTeam
            raise UserNotExistsInGivenTeam

    def get_team_dtos(
            self, team_ids: List[str], project_id: str
    ) -> List[TeamIdAndNameDTO]:
        valid_team_ids = self.project_storage \
            .get_valid_team_ids_for_given_project(project_id=project_id,
                                                  team_ids=team_ids)
        return self.team_storage.get_team_id_and_name_dtos(
            team_ids=valid_team_ids)

    def get_user_teams_for_each_project_user(
            self, user_ids: List[str], project_id: str
    ) -> List[UserTeamsDTO]:
        self._validate_project(project_id=project_id)
        valid_user_ids = self.user_storage.get_valid_user_ids(
            user_ids=user_ids)
        if len(valid_user_ids) != len(user_ids):
            invalid_user_ids = list(set(user_ids) - set(valid_user_ids))
            raise InvalidUserIds(invalid_user_ids)
        user_team_dtos = \
            self._validate_user_ids_and_get_user_team_dtos_for_given_project(
                project_id=project_id, user_ids=valid_user_ids)
        return self._fetch_user_teams_for_each_user(
            user_team_dtos=user_team_dtos)

    def _validate_user_ids_and_get_user_team_dtos_for_given_project(
            self, project_id: str, user_ids: List[str]
    ) -> Optional[List[TeamWithUserIdDTO]]:
        team_ids = self.project_storage.get_valid_team_ids(
            project_id=project_id)
        user_team_dtos = self.team_storage.get_team_user_dtos(
            user_ids=user_ids, team_ids=team_ids)
        for user_team_dto in user_team_dtos:
            if user_team_dto.user_id in user_ids:
                user_ids.remove(user_team_dto.user_id)
        not_exists_users_in_given_project = user_ids
        if not_exists_users_in_given_project:
            raise UsersNotExistsForGivenProject(
                user_ids=not_exists_users_in_given_project)
        return user_team_dtos

    def _fetch_user_teams_for_each_user(
            self, user_team_dtos: List[TeamWithUserIdDTO]
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
            user_team_dto: TeamWithUserIdDTO) -> TeamIdAndNameDTO:
        return TeamIdAndNameDTO(
            team_id=user_team_dto.team_id, team_name=user_team_dto.team_name)

    def add_project_wrapper(
            self,
            user_id: str,
            project_with_team_ids_and_roles_dto: ProjectWithTeamIdsAndRolesDTO,
            presenter: AddProjectPresenterInterface):
        try:
            self.add_project(user_id=user_id,
                             project_with_team_ids_and_roles_dto=
                             project_with_team_ids_and_roles_dto)
            response = presenter.get_success_response_for_add_project()
        except UserIsNotAdmin:
            response = presenter.get_user_has_no_access_response()
        except ProjectNameAlreadyExists:
            response = presenter.get_project_name_already_exists_response()
        except ProjectDisplayIdAlreadyExists:
            response = presenter \
                .get_project_display_id_already_exists_response()
        except TeamIdsAreInvalid:
            response = presenter.get_invalid_team_ids_response()
        except DuplicateTeamIds:
            response = presenter.get_duplicate_team_ids_response()
        except DuplicateRoleNamesExists:
            response = presenter.get_duplicate_role_names_response()
        except RoleNamesAlreadyExists as exception:
            response = presenter.get_role_names_already_exists_response(
                exception)
        return response

    def add_project(
            self, user_id: str,
            project_with_team_ids_and_roles_dto: ProjectWithTeamIdsAndRolesDTO
    ):
        self._validate_is_user_admin(user_id=user_id)
        self._validate_add_project_details(project_with_team_ids_and_roles_dto=
                                           project_with_team_ids_and_roles_dto)
        project_without_id_dto = ProjectWithoutIdDTO(
            name=project_with_team_ids_and_roles_dto.name,
            display_id=project_with_team_ids_and_roles_dto.display_id,
            description=project_with_team_ids_and_roles_dto.description,
            logo_url=project_with_team_ids_and_roles_dto.logo_url)
        project_id = self.project_storage.add_project(
            project_without_id_dto=project_without_id_dto)
        self.project_storage.assign_teams_to_projects(
            project_id=project_id,
            team_ids=project_with_team_ids_and_roles_dto.team_ids)
        self.project_storage.add_project_roles(
            project_id=project_id,
            roles=project_with_team_ids_and_roles_dto.roles)

    def _validate_add_project_details(
            self,
            project_with_team_ids_and_roles_dto: ProjectWithTeamIdsAndRolesDTO
    ):
        self._validate_is_given_name_already_exists(
            name=project_with_team_ids_and_roles_dto.name)
        self._validate_is_given_display_id_already_exists(
            display_id=project_with_team_ids_and_roles_dto.display_id)
        self._validate_duplicate_team_ids(
            team_ids=project_with_team_ids_and_roles_dto.team_ids)
        self._validate_invalid_team_ids(
            team_ids=project_with_team_ids_and_roles_dto.team_ids)
        role_names = [
            role_dto.name
            for role_dto in project_with_team_ids_and_roles_dto.roles]
        self._validate_duplicate_role_names(role_names=role_names)
        self._validate_is_role_names_already_exists_for_add_project(
            role_names=role_names)

    def update_project_wrapper(
            self, user_id: str,
            complete_project_details_dto: CompleteProjectDetailsDTO,
            presenter: UpdateProjectPresenterInterface):
        try:
            self.update_project(
                user_id=user_id,
                complete_project_details_dto=complete_project_details_dto)
            response = presenter.get_success_response_for_update_project()
        except UserIsNotAdmin:
            response = presenter.get_user_has_no_access_response()
        except InvalidProjectId:
            response = presenter.get_invalid_project_response()
        except ProjectNameAlreadyExists:
            response = presenter.get_project_name_already_exists_response()
        except DuplicateTeamIds:
            response = presenter.get_duplicate_team_ids_response()
        except TeamIdsAreInvalid:
            response = presenter.get_invalid_team_ids_response()
        except RoleIdsAreDuplicated:
            response = presenter.get_duplicate_role_ids_response()
        except RoleIdsAreInvalid:
            response = presenter.get_invalid_role_ids_response()
        except DuplicateRoleNamesExists:
            response = presenter.get_duplicate_role_names_exists_response()
        except RoleNamesAlreadyExists as exception:
            response = presenter.get_role_names_already_exists_response(
                exception)
        return response

    def update_project(
            self, user_id: str,
            complete_project_details_dto: CompleteProjectDetailsDTO):
        self._validate_is_user_admin(user_id=user_id)
        # todo have to know whether we can do any better here
        project_role_ids = self.project_storage.get_project_role_ids(
            project_id=complete_project_details_dto.project_id)
        self._validate_update_project_details(
            complete_project_details_dto=complete_project_details_dto,
            project_role_ids=project_role_ids)
        project_dto = self._convert_to_project_dto(
            complete_project_details_dto=complete_project_details_dto,
            project_id=complete_project_details_dto.project_id)
        self.project_storage.update_project(project_dto=project_dto)
        project_team_ids = self.project_storage.get_valid_team_ids(
            project_id=complete_project_details_dto.project_id)
        self._assign_teams_to_project(
            project_id=complete_project_details_dto.project_id,
            project_team_ids=project_team_ids,
            team_ids=complete_project_details_dto.team_ids)
        self._remove_teams_from_project(
            project_id=complete_project_details_dto.project_id,
            project_team_ids=project_team_ids,
            team_ids=complete_project_details_dto.team_ids)
        self._project_roles_related_operations(
            project_id=complete_project_details_dto.project_id,
            project_role_ids=project_role_ids,
            roles=complete_project_details_dto.roles)

    def _validate_update_project_details(
            self, complete_project_details_dto: CompleteProjectDetailsDTO,
            project_role_ids: List[str]):
        self._validate_project_id(
            project_id=complete_project_details_dto.project_id)
        self._validate_is_given_name_already_exists_for_update_project(
            name=complete_project_details_dto.name,
            project_id=complete_project_details_dto.project_id)
        self._validate_duplicate_team_ids(
            team_ids=complete_project_details_dto.team_ids)
        self._validate_roles(roles=complete_project_details_dto.roles,
                             project_role_ids=project_role_ids)
        self._validate_invalid_team_ids(
            team_ids=complete_project_details_dto.team_ids)
        role_names = [role_dto.name
                      for role_dto in complete_project_details_dto.roles]
        self._validate_duplicate_role_names(role_names=role_names)
        self._validate_is_role_names_already_exists_for_update_project(
            roles=complete_project_details_dto.roles)

    def _validate_project_id(self, project_id: str):
        is_project_exist = self.user_storage.is_valid_project_id(
            project_id=project_id)
        if not is_project_exist:
            raise InvalidProjectId

    def _project_roles_related_operations(
            self, project_id: str, project_role_ids: List[str],
            roles: List[RoleDTO]):
        self._add_project_roles(project_id=project_id, roles=roles)
        self._update_project_roles(
            project_role_ids=project_role_ids, roles=roles)
        self._delete_project_roles(
            project_role_ids=project_role_ids, roles=roles)

    @staticmethod
    def _convert_to_project_dto(
            project_id: str,
            complete_project_details_dto: CompleteProjectDetailsDTO):
        project_dto = ProjectDTO(
            project_id=project_id,
            name=complete_project_details_dto.name,
            description=complete_project_details_dto.description,
            logo_url=complete_project_details_dto.logo_url)
        return project_dto

    def _assign_teams_to_project(self, project_id: str,
                                 project_team_ids: List[str],
                                 team_ids: List[str]):
        team_ids_to_assign = list(set(team_ids) - set(project_team_ids))
        self.project_storage.assign_teams_to_projects(
            project_id=project_id, team_ids=team_ids_to_assign)

    def _remove_teams_from_project(self, project_id: str,
                                   project_team_ids: List[str],
                                   team_ids: List[str]):
        team_ids_to_be_removed = list(set(project_team_ids) - set(team_ids))
        self.project_storage.remove_teams_from_project(
            project_id=project_id, team_ids=team_ids_to_be_removed)

    def _add_project_roles(self, project_id: str, roles: List[RoleDTO]):
        role_name_and_description_dtos = [
            RoleNameAndDescriptionDTO(name=role_dto.name,
                                      description=role_dto.description)
            for role_dto in roles
            if role_dto.role_id is None]
        self.project_storage.add_project_roles(
            project_id=project_id,
            roles=role_name_and_description_dtos)

    def _update_project_roles(self, project_role_ids, roles):
        roles_to_be_updated = [role_dto
                               for role_dto in roles
                               if role_dto.role_id in project_role_ids]
        self.project_storage.update_project_roles(roles=roles_to_be_updated)

    def _delete_project_roles(self, project_role_ids, roles):
        role_ids = [role_dto.role_id for role_dto in roles]
        role_ids_to_be_deleted = list(set(project_role_ids) - set(role_ids))
        self.project_storage.delete_project_roles(
            role_ids=role_ids_to_be_deleted)

    @staticmethod
    def _validate_duplicate_role_names(role_names: List[str]):
        is_duplicate_role_names_exists = len(role_names) != len(
            set(role_names))
        if is_duplicate_role_names_exists:
            raise DuplicateRoleNamesExists

    def _validate_is_role_names_already_exists_for_add_project(
            self, role_names: List[str]):
        role_names_that_already_exists = self.project_storage \
            .get_valid_role_names_from_given_role_names(role_names=role_names)
        if role_names_that_already_exists:
            raise RoleNamesAlreadyExists(
                role_names=role_names_that_already_exists)

    def _validate_is_role_names_already_exists_for_update_project(
            self, roles: List[RoleDTO]):
        role_id_and_name_dtos = self.user_storage.get_roles()
        role_names = [role.name for role in roles if role.role_id is None]
        roles_dictionary = {}
        for role in roles:
            roles_dictionary[role.role_id] = role.name
        for role_id_and_name_dto in role_id_and_name_dtos:
            roles_dictionary[role_id_and_name_dto.role_id] = \
                role_id_and_name_dto.name
            role_names.append(role_id_and_name_dto.name)
        import collections
        role_names_that_already_exists = [
            item for item, count in collections.Counter(role_names).items()
            if count > 1]
        if role_names_that_already_exists:
            raise RoleNamesAlreadyExists(
                role_names=role_names_that_already_exists)

    def _validate_is_given_name_already_exists(self, name: str):
        project_id = self.project_storage \
            .get_project_id_if_project_name_already_exists(name=name)
        if project_id:
            raise ProjectNameAlreadyExists

    def _validate_is_given_name_already_exists_for_update_project(
            self, project_id: str, name: str):
        project_id_from_db = self.project_storage \
            .get_project_id_if_project_name_already_exists(name=name)
        if project_id_from_db not in [None, project_id]:
            raise ProjectNameAlreadyExists

    def _validate_is_given_display_id_already_exists(self, display_id: str):
        project_id = self.project_storage \
            .get_project_id_if_display_id_already_exists(display_id=display_id)
        if project_id:
            raise ProjectDisplayIdAlreadyExists

    @staticmethod
    def _validate_duplicate_team_ids(team_ids: List[str]):
        is_duplicate_team_ids_exist = len(team_ids) != len(set(team_ids))
        if is_duplicate_team_ids_exist:
            raise DuplicateTeamIds

    def _validate_invalid_team_ids(self, team_ids: List[str]):
        valid_team_ids = self.team_storage.get_valid_team_ids(
            team_ids=team_ids)
        invalid_team_ids = list(set(team_ids) - set(valid_team_ids))
        if invalid_team_ids:
            raise TeamIdsAreInvalid

    def _validate_roles(self, roles: List[RoleDTO],
                        project_role_ids: List[str]):
        role_ids = [role_dto.role_id
                    for role_dto in roles if role_dto.role_id is not None]
        self._validate_duplicate_role_ids(role_ids=role_ids)
        self._validate_invalid_role_ids(role_ids=role_ids,
                                        project_role_ids=project_role_ids)

    @staticmethod
    def _validate_duplicate_role_ids(role_ids: List[str]):
        is_duplicate_role_ids_exist = len(role_ids) != len(set(role_ids))
        if is_duplicate_role_ids_exist:
            raise RoleIdsAreDuplicated

    @staticmethod
    def _validate_invalid_role_ids(role_ids: List[str],
                                   project_role_ids: List[str]):
        is_invalid_role_ids_exist = list(set(role_ids) - set(project_role_ids))
        if is_invalid_role_ids_exist:
            raise RoleIdsAreInvalid

    def get_user_status_for_given_projects(
            self, user_id: str, project_ids: List[str]
    ) -> List[UserIdWithProjectIdAndStatusDTO]:
        project_ids = list(set(project_ids))
        is_user_exist = self.user_storage.is_user_exist(user_id=user_id)
        if not is_user_exist:
            raise InvalidUserId
        self._validate_project_ids(project_ids=project_ids)
        return self.project_storage.get_user_status_for_given_projects(
            project_ids=project_ids, user_id=user_id)

    def _validate_project_ids(self, project_ids: List[str]):
        valid_project_ids = self.project_storage \
            .get_valid_project_ids_from_given_project_ids(
            project_ids=project_ids)
        invalid_project_ids = list(set(project_ids) - set(valid_project_ids))
        if invalid_project_ids:
            raise InvalidProjectIds(project_ids=invalid_project_ids)
