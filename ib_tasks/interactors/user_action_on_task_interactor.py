import datetime
from typing import List, Optional

from ib_tasks.constants.enum import ViewType, ActionTypes
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
    StageIdsListEmptyException, InvalidStageIdsListException
from ib_tasks.exceptions.task_custom_exceptions import (
    InvalidTaskException, InvalidTaskDisplayId, TaskDelayReasonIsNotUpdated)
from ib_tasks.interactors \
    .call_action_logic_function_and_get_or_update_task_status_variables_interactor \
    import CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor, \
    InvalidMethodFound
from ib_tasks.interactors \
    .get_all_task_overview_with_filters_and_searches_for_user import \
    GetTasksOverviewForUserInteractor
from ib_tasks.interactors \
    .get_and_update_assignees_having_less_tasks_counts_for_next_stages_interactor import \
    GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor
from ib_tasks.interactors \
    .get_next_stages_random_assignees_of_a_task_interactor import \
    InvalidModulePathFound
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO, AllTasksOverviewDetailsDTO
from ib_tasks.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces \
    .create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskDetailsDTO
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


class InvalidBoardIdException(Exception):

    def __init__(self, board_id: str):
        self.board_id = board_id


class UserActionOnTaskInteractor(GetTaskIdForTaskDisplayIdMixin,
                                 ValidationMixin):

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

    def user_action_on_task_wrapper(
            self, presenter: PresenterInterface, task_display_id: str):

        try:
            task_id = self.get_task_id_for_task_display_id(task_display_id)
            task_complete_details_dto, task_current_stage_details_dto, \
            all_tasks_overview_dto =\
                self.user_action_on_task_and_set_random_assignees(task_id=task_id)
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
        return presenter.get_response_for_user_action_on_task(
            task_complete_details_dto=task_complete_details_dto,
            task_current_stage_details_dto=task_current_stage_details_dto,
            all_tasks_overview_dto=all_tasks_overview_dto
        )

    def user_action_on_task_and_set_random_assignees(self, task_id: int):
        task_complete_details_dto, task_current_stage_details_dto, \
        all_tasks_overview_dto, stage_ids = self.user_action_on_task(
            task_id)
        self._set_next_stage_assignees_to_task_and_update_in_db(
            task_id=task_id, stage_ids=stage_ids
        )
        return (task_complete_details_dto, task_current_stage_details_dto,
                all_tasks_overview_dto)

    def user_action_on_task(self, task_id: int):
        self._validate_task_id(task_id)
        project_id = \
            self.task_storage.get_project_id_for_the_task_id(task_id=task_id)
        self.validate_if_user_is_in_project(
            project_id=project_id, user_id=self.user_id)
        self._validation_all_user_template_permitted_fields_are_filled_or_not(
            task_id=task_id, project_id=project_id
        )
        self._validations_for_task_action(task_id, project_id)
        self._validate_present_task_stage_actions(task_id=task_id)
        updated_task_dto = \
            self._call_logic_and_update_status_variables_and_get_stage_ids(
                task_id=task_id
            )
        stage_ids = self._get_task_stage_display_satisfied_stage_ids(task_id)
        self._update_task_stages(stage_ids=stage_ids, task_id=task_id)
        self._create_or_update_task_in_elasticsearch(
            task_dto=updated_task_dto, task_id=task_id, stage_ids=stage_ids
        )
        task_complete_details_dto = self._get_task_current_board_complete_details(
            task_id=task_id, stage_ids=stage_ids
        )
        task_current_stage_details_dto = \
            self._get_task_current_stage_details(task_id=task_id)
        all_tasks_overview_details_dto = self._get_tasks_overview_for_users(
            task_id=task_id, project_id=project_id
        )
        return (
            task_complete_details_dto, task_current_stage_details_dto,
            all_tasks_overview_details_dto, stage_ids
        )

    def _validation_all_user_template_permitted_fields_are_filled_or_not(
            self, task_id: int, project_id: str
    ):
        action_type = self.action_storage.get_action_type_for_given_action_id(
            self.action_id)
        action_type_is_not_no_validations = \
            action_type != ActionTypes.NO_VALIDATIONS.value
        if action_type_is_not_no_validations:
            self._validate_all_user_template_permitted_fields_are_filled_or_not(
                self.user_id, task_id, project_id)

    def _validate_task_delay_reason_updated_or_not(self, task_id):

        stage_id = self.action_storage.get_stage_id_for_given_action_id(
            self.action_id)
        due_date = self.create_task_storage.get_existing_task_due_date(
            task_id)
        due_date_is_none_when_action_type_is_no_validations = due_date is None
        if due_date_is_none_when_action_type_is_no_validations:
            return
        due_date_is_expired = (due_date < datetime.datetime.now())
        if due_date_is_expired:
            updated_due_date = due_date
            self._validate_task_delay_reason_is_added(
                task_id=task_id, updated_due_date=updated_due_date,
                stage_id=stage_id)

    def _get_tasks_overview_for_users(
            self, task_id: int, project_id: str
    ) -> AllTasksOverviewDetailsDTO:
        task_overview_interactor = GetTasksOverviewForUserInteractor(
            stage_storage=self.stage_storage, task_storage=self.task_storage,
            field_storage=self.field_storage,
            action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage
        )
        all_tasks_overview_details_dto = \
            task_overview_interactor.get_filtered_tasks_overview_for_user(
                user_id=self.user_id, task_ids=[task_id],
                view_type=self.view_type,
                project_id=project_id)
        return all_tasks_overview_details_dto

    def _get_task_current_board_complete_details(
            self, task_id: int, stage_ids: List[str]
    ) -> TaskCompleteDetailsDTO:
        from ib_tasks.interactors \
            .get_task_current_board_complete_details_interactor \
            import GetTaskCurrentBoardCompleteDetailsInteractor
        interactor = GetTaskCurrentBoardCompleteDetailsInteractor(
            task_stage_storage=self.task_stage_storage,
            user_id=self.user_id,
            board_id=self.board_id,
            field_storage=self.field_storage,
            stage_storage=self.stage_storage,
            task_storage=self.task_storage,
            action_storage=self.action_storage,
            view_type=self.view_type
        )
        return interactor.get_task_current_board_complete_details(
            task_id=task_id, stage_ids=stage_ids)

    def _get_task_current_stage_details(self, task_id: int):
        from ib_tasks.interactors.get_task_current_stages_interactor import \
            GetTaskCurrentStagesInteractor
        get_task_current_stages_interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=self.task_stage_storage)
        task_current_stage_details_dto = \
            get_task_current_stages_interactor.get_task_current_stages_details(
                task_id=task_id, user_id=self.user_id)
        return task_current_stage_details_dto

    def _set_next_stage_assignees_to_task_and_update_in_db(
            self, task_id: int, stage_ids: List[str]
    ):
        set_stage_assignees_interactor = \
            GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor(
                storage=self.storage, stage_storage=self.stage_storage,
                task_storage=self.task_storage,
                action_storage=self.action_storage,
                task_stage_storage=self.task_stage_storage
            )
        set_stage_assignees_interactor \
            .get_random_assignees_of_next_stages_and_update_in_db(
            task_id=task_id, stage_ids=stage_ids
        )

    def _update_task_stages(self, stage_ids: List[str], task_id: int):

        self.storage.update_task_stages(
            task_id=task_id, stage_ids=stage_ids
        )

    def _get_task_stage_display_satisfied_stage_ids(self, task_id: int) -> \
            List[str]:
        from ib_tasks.interactors.get_task_stage_logic_satisfied_stages \
            import GetTaskStageLogicSatisfiedStagesInteractor
        interactor = GetTaskStageLogicSatisfiedStagesInteractor(
            task_id=task_id, storage=self.storage,
            stage_storage=self.stage_storage)
        stage_ids = interactor.get_task_stage_logic_satisfied_stages()
        return stage_ids

    def _call_logic_and_update_status_variables_and_get_stage_ids(
            self, task_id: int) -> TaskDetailsDTO:
        update_status_variable_obj = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                action_id=self.action_id, storage=self.storage,
                task_id=task_id, create_task_storage=self.create_task_storage,
                field_storage=self.field_storage)
        task_dto = update_status_variable_obj \
            .call_action_logic_function_and_update_task_status_variables()
        return task_dto

    def _validations_for_task_action(self, task_id: int, project_id: str):

        if self.board_id:
            self._validate_board_id()
        valid_action = self.storage.validate_action(action_id=self.action_id)
        is_invalid_action = not valid_action
        if is_invalid_action:
            raise InvalidActionException(action_id=self.action_id)
        action_roles = self.storage.get_action_roles(action_id=self.action_id)
        self._validate_user_permission_to_user(
            self.user_id, action_roles, self.action_id, project_id=project_id
        )
        self._validate_task_delay_reason_updated_or_not(task_id)

    def _validate_present_task_stage_actions(self, task_id: int):

        action_id = self.action_id
        action_ids = self.storage.get_task_present_stage_actions(
            task_id=task_id)
        is_not_present_stage_actions = int(action_id) not in action_ids
        if is_not_present_stage_actions:
            raise InvalidPresentStageAction(action_id=action_id)

    def _validate_task_id(self, task_id: int):

        task_id = task_id
        valid_task = self.storage.validate_task_id(task_id=task_id)
        is_invalid_task = not valid_task
        if is_invalid_task:
            raise InvalidTaskException(task_id=task_id)

    def _validate_board_id(self):

        from ib_tasks.adapters.service_adapter import ServiceAdapter
        adapter = ServiceAdapter()
        board_id = self.board_id
        valid_board = \
            adapter.boards_service.validate_board_id(board_id=board_id)
        is_invalid_board = not valid_board
        if is_invalid_board:
            raise InvalidBoardIdException(board_id=board_id)

    @staticmethod
    def _validate_user_permission_to_user(user_id: str,
                                          action_roles: List[str],
                                          action_id: int, project_id: str):

        from ib_tasks.interactors.user_role_validation_interactor \
            import UserRoleValidationInteractor
        interactor = UserRoleValidationInteractor()
        permit = interactor.does_user_has_required_permission(
            user_id=user_id, role_ids=action_roles, project_id=project_id
        )
        is_permission_denied = not permit
        if is_permission_denied:
            raise UserActionPermissionDenied(action_id=action_id)

    def _create_or_update_task_in_elasticsearch(
            self, task_dto: TaskDetailsDTO, stage_ids: List[str],
            task_id: int):
        from ib_tasks.interactors \
            .create_or_update_data_in_elasticsearch_interactor import \
            CreateOrUpdateDataInElasticSearchInteractor
        elasticsearch_interactor = CreateOrUpdateDataInElasticSearchInteractor(
            elasticsearch_storage=self.elasticsearch_storage,
            field_storage=self.field_storage,
            task_storage=self.task_storage
        )
        elasticsearch_interactor.create_or_update_task_in_elasticsearch(
            task_dto=task_dto, stage_ids=stage_ids, task_id=task_id
        )

    def _validate_task_delay_reason_is_added(
            self, updated_due_date: datetime.datetime, task_id: int,
            stage_id: int
    ) -> Optional[TaskDelayReasonIsNotUpdated]:
        self._validate_delay_reason_is_updated_or_not(
            task_id, stage_id, updated_due_date)
        return

    def _validate_delay_reason_is_updated_or_not(
            self, task_id: int, stage_id: int,
            updated_due_date: datetime.datetime
    ) -> Optional[TaskDelayReasonIsNotUpdated]:
        is_task_delay_reason_updated = \
            self.create_task_storage.check_task_delay_reason_updated_or_not(
                task_id, stage_id, updated_due_date)
        task_delay_reason_is_not_updated = not is_task_delay_reason_updated
        if task_delay_reason_is_not_updated:
            task_display_id = \
                self.create_task_storage.get_task_display_id_for_task_id(task_id)
            stage_display_name = \
                self.stage_storage.get_stage_display_name_for_stage_id(stage_id)
            raise TaskDelayReasonIsNotUpdated(
                updated_due_date, task_display_id, stage_display_name)
        return

    def _validate_all_user_template_permitted_fields_are_filled_or_not(
            self, user_id: str, task_id: int, project_id: str
    ):
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service \
            .get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id)
        task_template_id = \
            self.create_task_storage.get_template_id_for_given_task(task_id)
        template_gof_ids = self.task_template_storage.get_gof_ids_of_template(
            template_id=task_template_id)
        gof_id_with_display_name_dtos = \
            self.gof_storage.get_user_write_permitted_gof_ids_in_given_gof_ids(
                user_roles, template_gof_ids)
        user_permitted_gof_ids = [
            dto.gof_id for dto in gof_id_with_display_name_dtos]
        field_id_with_display_name_dtos = \
            self.field_storage \
                .get_user_write_permitted_field_ids_for_given_gof_ids(
                user_roles, user_permitted_gof_ids)
        filled_gofs_with_task_gof_ids = \
            self.gof_storage.get_filled_task_gofs_with_gof_id(task_id)
        filled_gof_ids = [dto.gof_id for dto in filled_gofs_with_task_gof_ids]
        task_gof_ids = [
            dto.task_gof_id for dto in filled_gofs_with_task_gof_ids]
        filled_field_ids = \
            self.gof_storage.get_filled_field_ids_of_given_task_gof_ids(
                task_gof_ids)
        # self._validate_all_user_permitted_gof_ids_are_filled_or_not(
        #     gof_id_with_display_name_dtos, filled_gof_ids)
        self._validate_all_user_permitted_field_ids_are_filled_or_not(
            field_id_with_display_name_dtos, filled_field_ids)

    @staticmethod
    def _validate_all_user_permitted_gof_ids_are_filled_or_not(
            permitted_gofs, filled_gof_ids
    ) -> Optional[UserDidNotFillRequiredGoFs]:
        permitted_gof_ids = [
            permitted_gof.gof_id for permitted_gof in permitted_gofs]
        unfilled_gof_ids = list(sorted(
            set(permitted_gof_ids) - set(filled_gof_ids)))
        if unfilled_gof_ids:
            gof_display_names = [
                permitted_gof.gof_display_name
                for permitted_gof in permitted_gofs
                if permitted_gof.gof_id in unfilled_gof_ids
            ]
            raise UserDidNotFillRequiredGoFs(gof_display_names)
        return

    @staticmethod
    def _validate_all_user_permitted_field_ids_are_filled_or_not(
            permitted_fields, filled_field_ids
    ) -> Optional[UserDidNotFillRequiredFields]:
        permitted_field_ids = [
            permitted_field.field_id for permitted_field in permitted_fields]
        unfilled_field_ids = list(sorted(
            set(permitted_field_ids) - set(filled_field_ids)))
        if unfilled_field_ids:
            unfilled_field_dtos = [
                permitted_field
                for permitted_field in permitted_fields
                if permitted_field.field_id in unfilled_field_ids
            ]
            raise UserDidNotFillRequiredFields(unfilled_field_dtos)
        return
