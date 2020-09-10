from typing import Optional, List

from ib_tasks.adapters.roles_service import UserNotAMemberOfAProjectException
from ib_tasks.constants.enum import ViewType
from ib_tasks.exceptions.action_custom_exceptions import InvalidKeyError, \
    InvalidCustomLogicException, InvalidActionException, \
    InvalidPresentStageAction
from ib_tasks.exceptions.adapter_exceptions import UserIsNotInProjectException
from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import \
    UserDidNotFillRequiredGoFs
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserActionPermissionDenied, UserBoardPermissionDenied
from ib_tasks.exceptions.stage_custom_exceptions import DuplicateStageIds, \
    InvalidDbStageIdsListException, StageIdsWithInvalidPermissionForAssignee, \
    StageIdsListEmptyException, InvalidStageIdsListException, \
    VirtualStageIdsException
from ib_tasks.exceptions.task_custom_exceptions import (
    InvalidTaskException, InvalidTaskDisplayId, TaskDelayReasonIsNotUpdated)
from ib_tasks.interactors \
    .call_action_logic_function_and_update_task_status_variables_interactor \
    import InvalidMethodFound
from ib_tasks.interactors \
    .get_next_stages_random_assignees_of_a_task_interactor import \
    InvalidModulePathFound
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces.act_on_task_and_upadte_task_stage_assignees_presenter_interface import \
    ActOnTaskAndUpdateTaskStageAssigneesPresenterInterface
from ib_tasks.interactors.stages_dtos import \
    TaskIdWithStageAssigneesDTO, \
    StageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces \
    .create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.user_action_on_task_interactor import \
    InvalidBoardIdException


class ActOnTaskAndUpdateTaskStageAssigneesInteractor(
    GetTaskIdForTaskDisplayIdMixin, ValidationMixin):
    def __init__(self, user_id: str, action_id: int, storage: StorageInterface,
                 create_task_storage: CreateOrUpdateTaskStorageInterface,
                 board_id: Optional[str],
                 field_storage: FieldsStorageInterface,
                 stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 action_storage: ActionStorageInterface,
                 elasticsearch_storage: ElasticSearchStorageInterface,
                 task_stage_storage: Optional[TaskStageStorageInterface],
                 task_template_storage: TaskTemplateStorageInterface,
                 gof_storage: GoFStorageInterface,
                 view_type: ViewType = ViewType.KANBAN.value
                 ):
        self.task_stage_storage = task_stage_storage
        self.elasticsearch_storage = elasticsearch_storage
        self.user_id = user_id
        self.board_id = board_id
        self.action_id = action_id
        self.storage = storage
        self.create_task_storage = create_task_storage
        self.gof_storage = gof_storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.action_storage = action_storage
        self.view_type = view_type
        self.task_template_storage = task_template_storage

    def act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            self,
            presenter: ActOnTaskAndUpdateTaskStageAssigneesPresenterInterface,
            task_display_id: str,
            stage_assignee_dtos: List[StageAssigneeDTO]):

        try:
            task_id = self.get_task_id_for_task_display_id(task_display_id)
            task_complete_details_dto, task_current_stage_details_dto, \
            all_tasks_overview_dto = self. \
                act_on_task_interactor_and_update_task_stage_assignees(
                task_id=task_id, stage_assignee_dtos=stage_assignee_dtos)
            return presenter.get_response_for_user_action_on_task(
                task_complete_details_dto=task_complete_details_dto,
                task_current_stage_details_dto=task_current_stage_details_dto,
                all_tasks_overview_dto=all_tasks_overview_dto
            )
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id(err)
        except InvalidTaskException as err:
            return presenter.raise_exception_for_invalid_task(error_obj=err)
        except InvalidBoardIdException as err:
            return presenter.raise_exception_for_invalid_board(error_obj=err)
        except InvalidActionException as err:
            return presenter.raise_exception_for_invalid_action(error_obj=err)
        except UserDidNotFillRequiredGoFs as err:
            return presenter.raise_user_did_not_fill_required_gofs(err)
        except UserDidNotFillRequiredFields as err:
            return presenter.raise_user_did_not_fill_required_fields(err)
        except UserActionPermissionDenied as err:
            return presenter.raise_exception_for_user_action_permission_denied(
                error_obj=err)
        except InvalidPresentStageAction as err:
            return presenter.raise_exception_for_invalid_present_actions(
                error_obj=err)
        except UserBoardPermissionDenied as err:
            return presenter.raise_exception_for_user_board_permission_denied(
                error_obj=err)
        except InvalidKeyError:
            return presenter.raise_invalid_key_error()
        except InvalidCustomLogicException:
            return presenter.raise_invalid_custom_logic_function_exception()
        except InvalidModulePathFound as exception:
            return presenter.raise_invalid_path_not_found_exception(
                path_name=exception.path_name)
        except UserIsNotInProjectException:
            return presenter.get_response_for_user_not_in_project()
        except InvalidMethodFound as exception:
            return presenter.raise_invalid_method_not_found_exception(
                method_name=exception.method_name)
        except DuplicateStageIds as exception:
            return presenter.raise_duplicate_stage_ids_not_valid(
                duplicate_stage_ids=exception.duplicate_stage_ids)
        except InvalidDbStageIdsListException as exception:
            return presenter.raise_invalid_stage_ids_exception(
                invalid_stage_ids=exception.invalid_stage_ids)
        except VirtualStageIdsException as exception:
            return presenter.raise_virtual_stage_ids_exception(
                virtual_stage_ids=exception.virtual_stage_ids)
        except UserNotAMemberOfAProjectException:
            return presenter.raise_invalid_user_id_exception()
        except StageIdsWithInvalidPermissionForAssignee as exception:
            return presenter. \
                raise_stage_ids_with_invalid_permission_for_assignee_exception(
                invalid_stage_ids=exception.invalid_stage_ids)
        except StageIdsListEmptyException as err:
            return presenter.raise_stage_ids_list_empty_exception(err)
        except InvalidStageIdsListException as err:
            return presenter.raise_invalid_stage_ids_list_exception(err)
        except TaskDelayReasonIsNotUpdated as err:
            return presenter.get_response_for_task_delay_reason_not_updated(
                err)

    def act_on_task_interactor_and_update_task_stage_assignees(
            self, task_id: int, stage_assignee_dtos: List[StageAssigneeDTO]):
        task_complete_details_dto, task_current_stage_details_dto, \
        all_tasks_overview_details_dto, stage_ids = self._act_on_task_and_get_required_dtos(
            task_id=task_id)
        stage_ids_excluding_virtual_stages = self.stage_storage. \
            get_stage_ids_excluding_virtual_stages(stage_ids)
        self._create_task_stage_history_records_for_virtual_stages(
            task_id=task_id, stage_ids_excluding_virtual_stages=
            stage_ids_excluding_virtual_stages, stage_ids=stage_ids)
        task_id_with_stage_assignees_dto = TaskIdWithStageAssigneesDTO(
            task_id=task_id,
            stage_assignees=stage_assignee_dtos)
        self._update_task_stage_assignees(
            task_id_with_stage_assignees_dto=task_id_with_stage_assignees_dto)
        return (task_complete_details_dto, task_current_stage_details_dto,
                all_tasks_overview_details_dto)

    def _update_task_stage_assignees(self,
                                     task_id_with_stage_assignees_dto:
                                     TaskIdWithStageAssigneesDTO):
        from ib_tasks.interactors.update_task_stage_assignees_interactor import \
            UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=self.stage_storage,
                task_storage=self.task_storage)
        update_task_stage_assignees_interactor. \
            validate_and_update_task_stage_assignees(
            task_id_with_stage_assignees_dto=task_id_with_stage_assignees_dto)
        return

    def _act_on_task_and_get_required_dtos(self, task_id: int):

        from ib_tasks.interactors.user_action_on_task_interactor import \
            UserActionOnTaskInteractor
        act_on_task_interactor = UserActionOnTaskInteractor(
            action_id=self.action_id, board_id=self.board_id,
            user_id=self.user_id, action_storage=self.action_storage,
            create_task_storage=self.create_task_storage,
            elasticsearch_storage=self.elasticsearch_storage,
            field_storage=self.field_storage, gof_storage=self.gof_storage,
            stage_storage=self.stage_storage, storage=self.storage,
            view_type=self.view_type,
            task_stage_storage=self.task_stage_storage,
            task_storage=self.task_storage,
            task_template_storage=self.task_template_storage)
        task_complete_details_dto, task_current_stage_details_dto, \
        all_tasks_overview_details_dto, stage_ids = act_on_task_interactor.\
            user_action_on_task(task_id=task_id)
        return (
            task_complete_details_dto, task_current_stage_details_dto,
            all_tasks_overview_details_dto, stage_ids)

    def _create_task_stage_history_records_for_virtual_stages(
            self, task_id: int, stage_ids_excluding_virtual_stages: List[str],
            stage_ids: List[str]):
        stage_ids_having_virtual_stages = \
            [stage_id for stage_id in stage_ids
             if stage_id not in stage_ids_excluding_virtual_stages]
        virtual_stages_already_having_task = self.stage_storage. \
            get_virtual_stages_already_having_in_task(
            task_id, stage_ids_having_virtual_stages)
        virtual_stages_not_in_task = [stage_id for stage_id in
                                      stage_ids_having_virtual_stages if
                                      stage_id not in
                                      virtual_stages_already_having_task]
        virtual_stage_db_stage_ids_not_in_task = self.stage_storage. \
            get_db_stage_ids_for_given_stage_ids(virtual_stages_not_in_task)
        self.task_stage_storage. \
            create_task_stage_history_records_for_virtual_stages(
            stage_ids=virtual_stage_db_stage_ids_not_in_task, task_id=task_id)
        return