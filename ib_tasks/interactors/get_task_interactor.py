from typing import List

from ib_tasks.adapters.assignees_details_service import InvalidUserIdException
from ib_tasks.adapters.auth_service import InvalidProjectIdsException, \
    TeamsNotExistForGivenProjectException, UsersNotExistsForGivenTeamsException
from ib_tasks.adapters.roles_service import UserNotAMemberOfAProjectException
from ib_tasks.adapters.searchable_details_service import \
    InvalidUserIdsException, InvalidStateIdsException, \
    InvalidCountryIdsException, InvalidCityIdsException
from ib_tasks.exceptions.task_custom_exceptions \
    import InvalidTaskIdException, InvalidStageIdsForTask, \
    InvalidTaskDisplayId, UserPermissionDenied
from ib_tasks.interactors.get_task_base_interactor \
    import GetTaskBaseInteractor
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import \
    GetTaskPresenterInterface, TaskCompleteDetailsDTO
from ib_tasks.interactors.stages_dtos import StageAssigneeWithTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces \
    .create_or_update_task_storage_interface \
    import CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface \
    import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import (
    TaskGoFDTO,
    TaskGoFFieldDTO,
    TaskDetailsDTO, FieldSearchableDTO
)
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO


class GetTaskInteractor(GetTaskIdForTaskDisplayIdMixin):

    def __init__(
            self, task_crud_storage: CreateOrUpdateTaskStorageInterface,
            fields_storage: FieldsStorageInterface,
            storage: StorageInterface,
            stage_storage: StageStorageInterface,
            task_storage: TaskStorageInterface,
            action_storage: ActionStorageInterface,
            task_stage_storage: TaskStageStorageInterface,
            gof_storage: GoFStorageInterface
    ):
        self.storage = storage
        self.task_stage_storage = task_stage_storage
        self.action_storage = action_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.task_crud_storage = task_crud_storage
        self.fields_storage = fields_storage
        self.gof_storage = gof_storage

    def get_task_details_wrapper(
            self, user_id: str, task_display_id: str,
            presenter: GetTaskPresenterInterface
    ):
        try:
            return self.get_task_details_response(user_id, task_display_id,
                                                  presenter)
        except InvalidTaskIdException as err:
            response = presenter.raise_exception_for_invalid_task_id(err)
            return response
        except InvalidStageIdsForTask as err:
            response = presenter.raise_invalid_stage_ids_for_task(err)
            return response
        except InvalidTaskDisplayId as err:
            response = presenter.raise_invalid_task_display_id(err)
            return response
        except UserPermissionDenied:
            response = presenter.raise_user_permission_denied()
            return response
        except InvalidCityIdsException as err:
            response = presenter.raise_invalid_searchable_records_found()
            return response
        except InvalidStateIdsException:
            response = presenter.raise_invalid_searchable_records_found()
            return response
        except InvalidCountryIdsException:
            response = presenter.raise_invalid_searchable_records_found()
            return response
        except InvalidUserIdsException:
            response = presenter.raise_invalid_searchable_records_found()
            return response
        except InvalidProjectIdsException as err:
            response = presenter.raise_invalid_project_id(err)
            return response
        except TeamsNotExistForGivenProjectException as err:
            response = presenter.raise_teams_does_not_exists_for_project(err)
            return response
        except UsersNotExistsForGivenTeamsException as err:
            response = presenter.raise_users_not_exist_for_given_teams(err)
            return response
        except InvalidUserIdException:
            response = presenter.raise_invalid_user()
            return response
        except UserNotAMemberOfAProjectException:
            response = presenter.raise_user_not_a_member_of_project()
            return response

    def get_task_details_response(
            self, user_id: str, task_display_id: str,
            presenter: GetTaskPresenterInterface
    ):
        task_id = self.get_task_id_for_task_display_id(
            task_display_id=task_display_id)
        task_complete_details_dto = self.get_task_details(user_id, task_id)
        response = presenter.get_task_response(task_complete_details_dto)
        return response

    def get_task_details(
            self, user_id: str, task_id: int
    ) -> TaskCompleteDetailsDTO:

        task_details_dto = self._get_task_details_dto(task_id)
        project_details_dto = task_details_dto.project_details_dto
        project_id = project_details_dto.project_id
        user_roles = self._get_user_roles_for_the_project(user_id, project_id)
        stages_and_actions_details_dtos = \
            self._get_stages_and_actions_details_dtos(
                task_id, user_id, user_roles)
        stage_ids = self._get_stage_ids(stages_and_actions_details_dtos)
        task_details_dto = \
            self._get_task_details_dto_based_on_stages_and_user_roles(
                task_details_dto, user_roles, stage_ids
            )

        stage_assignee_details_dtos = \
            self._stage_assignee_with_team_details_dtos(
                task_id, stage_ids, project_id
            )

        task_complete_details_dto = TaskCompleteDetailsDTO(
            task_details_dto=task_details_dto,
            stages_and_actions_details_dtos=stages_and_actions_details_dtos,
            stage_assignee_with_team_details_dtos=stage_assignee_details_dtos
        )
        return task_complete_details_dto

    def _get_task_details_dto(self, task_id: int) -> TaskDetailsDTO:
        get_task_base_interactor = GetTaskBaseInteractor(
            storage=self.task_crud_storage,
            gof_storage=self.gof_storage,
        )
        task_details_dto = get_task_base_interactor.get_task(task_id)
        return task_details_dto

    @staticmethod
    def _get_user_roles_for_the_project(
            user_id: str, project_id: str
    ) -> List[str]:
        from ib_tasks.interactors.user_role_validation_interactor import \
            UserRoleValidationInteractor
        user_role_validation_interactor = UserRoleValidationInteractor()
        user_roles = \
            user_role_validation_interactor.get_user_role_ids_for_project(
                user_id, project_id)
        return user_roles

    def _validate_user_have_permission_for_at_least_one_stage(
            self, stage_ids: List[int], user_roles: List[str]) -> bool:
        is_user_has_permission = \
            self.task_stage_storage \
                .is_user_has_permission_for_at_least_one_stage(
                    stage_ids=stage_ids, user_roles=user_roles
                )
        is_user_permission_denied = not is_user_has_permission
        if is_user_permission_denied:
            raise UserPermissionDenied()

    def _stage_assignee_with_team_details_dtos(
            self, task_id: int, stage_ids: List[int], project_id: str
    ) -> List[StageAssigneeWithTeamDetailsDTO]:
        from ib_tasks.interactors.get_stages_assignees_details_interactor \
            import \
            GetStagesAssigneesDetailsInteractor
        interactor = GetStagesAssigneesDetailsInteractor(
            task_stage_storage=self.task_stage_storage
        )
        stage_assignee_with_details_dtos = \
            interactor.get_stages_assignee_details_dtos(
                task_id=task_id,
                stage_ids=stage_ids,
                project_id=project_id
            )
        return stage_assignee_with_details_dtos

    @staticmethod
    def _get_stage_ids(stages_and_actions_details_dtos) -> List[int]:
        stage_ids = [
            stages_and_actions_details_dto.db_stage_id
            for stages_and_actions_details_dto in
            stages_and_actions_details_dtos
        ]
        return stage_ids

    def _get_task_details_dto_based_on_stages_and_user_roles(
            self, task_details_dto: TaskDetailsDTO, user_roles: List[str],
            stage_ids: List[str]
    ) -> TaskDetailsDTO:

        task_gof_dtos = task_details_dto.task_gof_dtos
        all_task_gof_field_dtos = task_details_dto.task_gof_field_dtos
        permission_task_gof_dtos = self._get_permission_task_gof_dtos(
            task_gof_dtos, user_roles, stage_ids
        )
        task_gof_field_dtos = self._get_task_gof_field_dtos(
            permission_task_gof_dtos, all_task_gof_field_dtos
        )
        permission_task_gof_field_dtos = \
            self._get_permission_task_gof_field_dtos(
                task_gof_field_dtos, user_roles
            )
        task_gof_field_dtos = \
            self._get_task_gof_field_dtos_when_some_fields_are_searchable_type(
                permission_task_gof_field_dtos
            )
        task_details_dto = TaskDetailsDTO(
            task_base_details_dto=task_details_dto.task_base_details_dto,
            project_details_dto=task_details_dto.project_details_dto,
            task_gof_dtos=permission_task_gof_dtos,
            task_gof_field_dtos=task_gof_field_dtos
        )
        return task_details_dto

    def _get_task_gof_field_dtos_when_some_fields_are_searchable_type(
            self, permission_task_gof_field_dtos: List[TaskGoFFieldDTO]
    ) -> List[TaskGoFFieldDTO]:

        field_ids = [
            permission_task_gof_field_dto.field_id
            for permission_task_gof_field_dto in permission_task_gof_field_dtos
        ]
        task_gof_ids = [
            permission_task_gof_field_dto.task_gof_id
            for permission_task_gof_field_dto in permission_task_gof_field_dtos
        ]
        field_searchable_dtos = \
            self.task_crud_storage.get_field_searchable_dtos(
                field_ids, task_gof_ids)
        is_field_searchable_dtos_empty = not field_searchable_dtos

        if is_field_searchable_dtos_empty:
            return permission_task_gof_field_dtos
        task_gof_field_dtos = \
            self._get_task_gof_field_dtos_with_modified_field_response(
                permission_task_gof_field_dtos, field_searchable_dtos)
        return task_gof_field_dtos

    def _get_task_gof_field_dtos_with_modified_field_response(
            self, permission_task_gof_field_dtos: List[TaskGoFFieldDTO],
            field_searchable_dtos: List[FieldSearchableDTO]
    ):
        from ib_tasks.interactors.get_searchable_field_details import \
            GetSearchableFieldDetails
        interactor = GetSearchableFieldDetails()
        field_searchable_dtos = interactor.get_searchable_fields_details(
            field_searchable_dtos)
        task_gof_field_dtos = self._get_modified_task_gof_field_dtos(
            permission_task_gof_field_dtos, field_searchable_dtos
        )
        return task_gof_field_dtos

    def _get_modified_task_gof_field_dtos(
            self, permission_task_gof_field_dtos: List[TaskGoFFieldDTO],
            field_searchable_dtos: List[FieldSearchableDTO]
    ) -> List[TaskGoFFieldDTO]:

        for permission_task_gof_field_dto in permission_task_gof_field_dtos:
            field_response = self._get_field_response(
                permission_task_gof_field_dto, field_searchable_dtos)
            if field_response:
                permission_task_gof_field_dto.field_response = field_response
        return permission_task_gof_field_dtos

    @staticmethod
    def _get_field_response(
            permission_task_gof_field_dto: TaskGoFFieldDTO,
            field_searchable_dtos: List[FieldSearchableDTO]
    ) -> str:
        field_response = None
        field_id = permission_task_gof_field_dto.field_id
        task_gof_id = permission_task_gof_field_dto.task_gof_id
        for field_searchable_dto in field_searchable_dtos:
            is_field_matches = field_id == field_searchable_dto.field_id and \
                               task_gof_id == field_searchable_dto.task_gof_id
            if is_field_matches:
                return field_searchable_dto.field_response

        return field_response

    def _get_stages_and_actions_details_dtos(
            self, task_id: int, user_id: str, user_roles: str
    ) -> List[StageAndActionsDetailsDTO]:
        from ib_tasks.interactors.get_task_stages_and_actions \
            import GetTaskStagesAndActions
        interactor = GetTaskStagesAndActions(
            field_storage=self.fields_storage,
            task_storage=self.task_storage,
            storage=self.storage,
            stage_storage=self.stage_storage,
            action_storage=self.action_storage
        )
        stages_and_actions_details_dtos = \
            interactor.get_task_stages_and_actions(task_id, user_id)

        stage_ids = self._get_stage_ids(stages_and_actions_details_dtos)
        self._validate_user_have_permission_for_at_least_one_stage(stage_ids,
                                                                   user_roles)
        return stages_and_actions_details_dtos

    @staticmethod
    def _get_task_gof_field_dtos(
            permission_task_gof_dtos: List[TaskGoFDTO],
            all_task_gof_field_dtos: List[TaskGoFFieldDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_ids = [
            permission_task_gof_dto.task_gof_id
            for permission_task_gof_dto in permission_task_gof_dtos
        ]
        task_gof_field_dtos = [
            task_gof_field_dto
            for task_gof_field_dto in all_task_gof_field_dtos
            if task_gof_field_dto.task_gof_id in task_gof_ids
        ]
        return task_gof_field_dtos

    def _get_permission_task_gof_field_dtos(
            self, task_gof_field_dtos: List[TaskGoFFieldDTO],
            user_roles: List[str]
    ) -> List[TaskGoFFieldDTO]:
        field_ids = [
            task_gof_field_dto.field_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        from ib_tasks.interactors.user_role_validation_interactor import \
            UserRoleValidationInteractor
        user_role_validation_interactor = UserRoleValidationInteractor()
        permission_field_ids = \
            user_role_validation_interactor \
                .get_field_ids_having_read_permission_for_user(
                user_roles=user_roles, field_ids=field_ids,
                field_storage=self.fields_storage
            )
        permission_task_gof_field_dtos = [
            task_gof_field_dto
            for task_gof_field_dto in task_gof_field_dtos
            if task_gof_field_dto.field_id in permission_field_ids
        ]
        return permission_task_gof_field_dtos

    def _get_permission_task_gof_dtos(
            self, task_gof_dtos: List[TaskGoFDTO], user_roles: List[str],
            stage_ids: List[str]
    ) -> List[TaskGoFDTO]:
        gof_ids = [
            task_gof_dto.gof_id
            for task_gof_dto in task_gof_dtos
        ]
        stage_gof_ids = self.stage_storage.get_stages_permitted_gof_ids(
            stage_ids, gof_ids)
        from ib_tasks.interactors.user_role_validation_interactor import \
            UserRoleValidationInteractor
        user_role_validation_interactor = UserRoleValidationInteractor()
        permission_gof_ids = \
            user_role_validation_interactor \
                .get_gof_ids_having_read_permission_for_user(
                user_roles=user_roles, gof_ids=stage_gof_ids,
                gof_storage=self.gof_storage
            )
        permission_task_gof_dtos = [
            task_gof_dto
            for task_gof_dto in task_gof_dtos
            if task_gof_dto.gof_id in permission_gof_ids
        ]
        return permission_task_gof_dtos
