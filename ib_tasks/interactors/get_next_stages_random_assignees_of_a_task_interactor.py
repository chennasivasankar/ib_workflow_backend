from typing import List

from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.action_custom_exceptions \
    import InvalidKeyError
from ib_tasks.exceptions.custom_exceptions import InvalidModulePathFound, \
    InvalidMethodFound
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskDisplayId
from ib_tasks.interactors.get_users_with_less_tasks_for_stages import \
    GetUsersWithLessTasksInGivenStagesInteractor
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces. \
    get_next_stages_random_assignees_of_a_task_presenter import \
    GetNextStagesRandomAssigneesOfATaskPresenterInterface
from ib_tasks.interactors.stages_dtos import \
    StageWithUserDetailsAndTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetNextStagesRandomAssigneesOfATaskInteractor(
    ValidationMixin, GetTaskIdForTaskDisplayIdMixin):
    def __init__(self, storage: StorageInterface,
                 stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 action_storage: ActionStorageInterface,
                 task_stage_storage: TaskStageStorageInterface,
                 field_storage: FieldsStorageInterface,
                 create_task_storage: CreateOrUpdateTaskStorageInterface,
                 gof_storage: GoFStorageInterface
                 ):
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.action_storage = action_storage
        self.storage = storage
        self.create_task_storage = create_task_storage
        self.task_stage_storage = task_stage_storage
        self.field_storage = field_storage
        self.gof_storage = gof_storage

    def get_next_stages_random_assignees_of_a_task_wrapper(
            self, task_display_id: str, action_id: int,
            presenter: GetNextStagesRandomAssigneesOfATaskPresenterInterface):
        from ib_tasks.adapters.auth_service import \
            UsersNotExistsForGivenProjectException
        try:
            task_id = self.get_task_id_for_task_display_id(task_display_id)
            stage_with_user_details_and_team_details_dto = \
                self.get_next_stages_random_assignees_of_a_task(
                    task_id=task_id, action_id=action_id)
            return presenter. \
                get_next_stages_random_assignees_of_a_task_response(
                stage_with_user_details_and_team_details_dto)
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id(err)
        except InvalidActionException as exception:
            return presenter.raise_exception_for_invalid_action(
                action_id=exception.action_id)
        except UsersNotExistsForGivenProjectException as exception:
            return presenter.raise_users_not_exists_for_given_projects(
                user_ids=exception.user_ids)

        except InvalidKeyError:
            return presenter.raise_invalid_key_error()
        except InvalidModulePathFound as exception:
            return presenter.raise_invalid_path_not_found_exception(
                path_name=exception.path_name)
        except InvalidMethodFound as exception:
            return presenter.raise_invalid_method_not_found_exception(
                method_name=exception.method_name)

    def get_next_stages_random_assignees_of_a_task(
            self, task_id: int,
            action_id: int) -> StageWithUserDetailsAndTeamDetailsDTO:
        self.validate_action_id(action_id=action_id)
        project_id = self.task_storage.get_project_id_of_task(task_id)
        status_variable_dtos = self. \
            _get_status_variables_dtos_of_task_based_on_action(
            task_id=task_id, action_id=action_id)
        next_stage_ids_of_task = \
            self._get_next_stages_of_task(task_id=task_id,
                                          status_variable_dtos=
                                          status_variable_dtos)
        valid_next_stage_ids_of_task = self.stage_storage. \
            get_stage_ids_excluding_virtual_stages(
            next_stage_ids_of_task)
        stage_with_user_details_and_team_details_dto = self. \
            _get_users_with_less_tasks_in_given_stages(
            valid_next_stage_ids_of_task, project_id)

        return stage_with_user_details_and_team_details_dto

    def _get_users_with_less_tasks_in_given_stages(
            self, stage_ids: List[str], project_id: str) -> \
            StageWithUserDetailsAndTeamDetailsDTO:
        get_users_with_less_tasks_interactor = \
            GetUsersWithLessTasksInGivenStagesInteractor(
                action_storage=self.action_storage,
                stage_storage=self.stage_storage,
                task_stage_storage=self.task_stage_storage)
        stage_with_user_details_and_team_details_dto = \
            get_users_with_less_tasks_interactor. \
                get_users_with_less_tasks_in_given_stages(
                stage_ids=stage_ids, project_id=project_id)
        return stage_with_user_details_and_team_details_dto

    def _get_status_variables_dtos_of_task_based_on_action(self, task_id: int,
                                                           action_id: int) -> \
            List[StatusVariableDTO]:

        from ib_tasks.interactors.user_action_on_task.call_action_logic_function_and_get_or_update_task_status_variables_interactor import \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor
        call_action_logic_function_interactor = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                storage=self.storage,
                create_task_storage=self.create_task_storage, task_id=task_id,
                action_id=action_id, field_storage=self.field_storage,
                gof_storage=self.gof_storage
            )
        updated_status_variable_dtos = call_action_logic_function_interactor. \
            call_action_logic_function_and_get_status_variables_dtos_of_task()
        return updated_status_variable_dtos

    def _get_next_stages_of_task(self, task_id: int,
                                 status_variable_dtos) -> List[str]:

        from ib_tasks.interactors.user_action_on_task.get_task_stage_logic_satisfied_stages import \
            GetTaskStageLogicSatisfiedStagesInteractor
        get_task_stage_logic_satisfied_next_stages_interactor = \
            GetTaskStageLogicSatisfiedStagesInteractor(
                storage=self.storage, stage_storage=self.stage_storage,
                task_id=task_id)
        next_stage_ids = get_task_stage_logic_satisfied_next_stages_interactor. \
            get_task_stage_logic_satisfied_next_stages_given_status_variable_dtos(
            status_variable_dtos=status_variable_dtos)
        return next_stage_ids
