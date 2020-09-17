from typing import Union, Optional

from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.action_custom_exceptions import \
    InvalidActionException, InvalidPresentStageAction, InvalidKeyError, \
    InvalidCustomLogicException
from ib_tasks.exceptions.custom_exceptions import InvalidModulePathFound, \
    InvalidMethodFound
from ib_tasks.exceptions.datetime_custom_exceptions import \
    StartDateIsAheadOfDueDate, \
    DueDateTimeHasExpired, DueDateTimeWithoutStartDateTimeIsNotValid, \
    StartDateTimeIsRequired, DueDateTimeIsRequired
from ib_tasks.exceptions.field_values_custom_exceptions import \
    EmptyValueForRequiredField, InvalidPhoneNumberValue, \
    InvalidEmailFieldValue, InvalidURLValue, NotAStrongPassword, \
    InvalidNumberValue, InvalidFloatValue, InvalidValueForDropdownField, \
    IncorrectNameInGoFSelectorField, IncorrectRadioGroupChoice, \
    IncorrectCheckBoxOptionsSelected, IncorrectMultiSelectOptionsSelected, \
    IncorrectMultiSelectLabelsSelected, InvalidDateFormat, InvalidTimeFormat, \
    InvalidUrlForImage, InvalidImageFormat, InvalidUrlForFile, \
    InvalidFileFormat
from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds, \
    DuplicateFieldIdsToGoF, UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds, \
    DuplicateSameGoFOrderForAGoF, UserDidNotFillRequiredGoFs, \
    InvalidStagePermittedGoFs
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission, \
    UserActionPermissionDenied
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsWithInvalidPermissionForAssignee, DuplicateStageIds, \
    InvalidDbStageIdsListException, InvalidStageId, \
    StageIdsListEmptyException, \
    InvalidStageIdsListException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException, \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF, InvalidTaskDisplayId, \
    TaskDelayReasonIsNotUpdated, PriorityIsRequired, InvalidTaskJson
from ib_tasks.interactors.create_or_update_task.update_task_interactor import \
    UpdateTaskInteractor
from ib_tasks.interactors.dtos.dtos import TaskOverallCompleteDetailsDTO
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.mixins.task_operations_utilities_mixin import \
    TaskOperationsUtilitiesMixin
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.presenter_interfaces \
    .save_and_act_on_task_presenter_interface import \
    SaveAndActOnATaskPresenterInterface
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
    import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import UpdateTaskDTO, \
    SaveAndActOnTaskDTO, \
    SaveAndActOnTaskWithTaskDisplayIdDTO, UpdateTaskBasicDetailsDTO, \
    CreateTaskLogDTO
from ib_tasks.interactors.user_action_on_task.user_action_on_task_interactor \
    import UserActionOnTaskInteractor


class SaveAndActOnATaskInteractor(
    GetTaskIdForTaskDisplayIdMixin, TaskOperationsUtilitiesMixin
):

    def __init__(
            self, task_storage: TaskStorageInterface,
            gof_storage: GoFStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface,
            stage_storage: StageStorageInterface,
            action_storage: ActionStorageInterface,
            elastic_storage: ElasticSearchStorageInterface,
            task_stage_storage: TaskStageStorageInterface,
            task_template_storage: TaskTemplateStorageInterface
    ):
        self.task_stage_storage = task_stage_storage
        self.elastic_storage = elastic_storage
        self.action_storage = action_storage
        self.gof_storage = gof_storage
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.storage = storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.task_template_storage = task_template_storage

    def save_and_act_on_task_wrapper(
            self, presenter: SaveAndActOnATaskPresenterInterface,
            task_dto: SaveAndActOnTaskWithTaskDisplayIdDTO,
            task_request_json: str, board_id: str):
        try:
            return self._prepare_save_and_act_response(
                presenter, task_dto, task_request_json, board_id)
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id(err)
        except InvalidActionException as err:
            return presenter.raise_invalid_action_id(err)
        except InvalidTaskException as err:
            return presenter.raise_invalid_task_id(err)
        except InvalidStageId as err:
            return presenter.raise_invalid_stage_id(err)
        except PriorityIsRequired as err:
            return presenter.raise_priority_is_required(err)
        except DueDateTimeWithoutStartDateTimeIsNotValid as err:
            return presenter.raise_due_date_time_without_start_datetime(err)
        except StartDateTimeIsRequired as err:
            return presenter.raise_start_date_time_is_required(err)
        except DueDateTimeIsRequired as err:
            return presenter.raise_due_date_time_is_required(err)
        except DueDateTimeHasExpired as err:
            return presenter.raise_due_date_time_has_expired(err)
        except StartDateIsAheadOfDueDate as err:
            return presenter.raise_start_date_is_ahead_of_due_date(err)
        except TaskDelayReasonIsNotUpdated as err:
            return presenter.raise_task_delay_reason_not_updated(err)
        except DuplicateSameGoFOrderForAGoF as err:
            return presenter.raise_duplicate_same_gof_orders_for_a_gof(err)
        except InvalidGoFIds as err:
            return presenter.raise_invalid_gof_ids(err)
        except InvalidFieldIds as err:
            return presenter.raise_invalid_field_ids(err)
        except InvalidGoFsOfTaskTemplate as err:
            return presenter.raise_invalid_gofs_given_to_a_task_template(err)
        except DuplicateFieldIdsToGoF as err:
            return presenter.raise_duplicate_field_ids_to_a_gof(err)
        except InvalidFieldsOfGoF as err:
            return presenter.raise_invalid_fields_given_to_a_gof(err)
        except InvalidStagePermittedGoFs as err:
            return presenter.raise_invalid_stage_permitted_gofs(err)
        except UserNeedsGoFWritablePermission as err:
            return presenter.raise_user_needs_gof_writable_permission(err)
        except UserNeedsFieldWritablePermission as err:
            return presenter.raise_user_needs_field_writable_permission(err)
        except UserDidNotFillRequiredGoFs as err:
            return presenter.raise_user_did_not_fill_required_gofs(err)
        except UserDidNotFillRequiredFields as err:
            return presenter.raise_user_did_not_fill_required_fields(err)
        except EmptyValueForRequiredField as err:
            return presenter.raise_empty_value_in_required_field(err)
        except InvalidPhoneNumberValue as err:
            return presenter.raise_invalid_phone_number_value(err)
        except InvalidEmailFieldValue as err:
            return presenter.raise_invalid_email_address(err)
        except InvalidURLValue as err:
            return presenter.raise_invalid_url_address(err)
        except NotAStrongPassword as err:
            return presenter.raise_weak_password(err)
        except InvalidNumberValue as err:
            return presenter.raise_invalid_number_value(err)
        except InvalidFloatValue as err:
            return presenter.raise_invalid_float_value(err)
        except InvalidValueForDropdownField as err:
            return presenter.raise_invalid_dropdown_value(err)
        except IncorrectNameInGoFSelectorField as err:
            return presenter.raise_invalid_name_in_gof_selector(err)
        except IncorrectRadioGroupChoice as err:
            return presenter.raise_invalid_choice_in_radio_group_field(err)
        except IncorrectCheckBoxOptionsSelected as err:
            return presenter.raise_invalid_checkbox_group_options_selected(err)
        except IncorrectMultiSelectOptionsSelected as err:
            return presenter.raise_invalid_multi_select_options_selected(err)
        except IncorrectMultiSelectLabelsSelected as err:
            return presenter.raise_invalid_multi_select_labels_selected(err)
        except InvalidDateFormat as err:
            return presenter.raise_invalid_date_format(err)
        except InvalidTimeFormat as err:
            return presenter.raise_invalid_time_format(err)
        except InvalidUrlForImage as err:
            return presenter.raise_invalid_image_url(err)
        except InvalidImageFormat as err:
            return presenter.raise_not_acceptable_image_format(err)
        except InvalidUrlForFile as err:
            return presenter.raise_invalid_file_url(err)
        except InvalidFileFormat as err:
            return presenter.raise_not_acceptable_file_format(err)
        except UserActionPermissionDenied as err:
            return presenter.raise_user_action_permission_denied(err)
        except InvalidPresentStageAction as err:
            return presenter.raise_invalid_present_stage_actions(err)
        except InvalidKeyError:
            return presenter.raise_invalid_key_error()
        except InvalidCustomLogicException:
            return presenter.raise_invalid_custom_logic_function_exception()
        except InvalidModulePathFound as err:
            return presenter.raise_path_not_found_exception(err)
        except InvalidMethodFound as err:
            return presenter.raise_method_not_found(err)
        except DuplicateStageIds as err:
            return presenter.raise_duplicate_stage_ids_not_valid(err)
        except InvalidDbStageIdsListException as err:
            return presenter.raise_invalid_stage_ids_exception(err)
        except StageIdsWithInvalidPermissionForAssignee as err:
            return presenter.raise_invalid_stage_assignees(err)
        except StageIdsListEmptyException as err:
            return presenter.raise_stage_ids_list_empty_exception(err)
        except InvalidStageIdsListException as err:
            return presenter.raise_invalid_stage_ids_list_exception(err)
        except InvalidTaskJson as err:
            return presenter.raise_invalid_task_json(err)

    def _prepare_save_and_act_response(
            self, presenter, task_dto: SaveAndActOnTaskWithTaskDisplayIdDTO,
            task_request_json: str, board_id: str):
        task_overview_dto = self.save_and_act_on_task_with_task_display_id(
            task_dto, task_request_json, board_id)
        return presenter.get_save_and_act_on_task_response(task_overview_dto)

    def save_and_act_on_task_with_task_display_id(
            self, task_dto: SaveAndActOnTaskWithTaskDisplayIdDTO,
            task_request_json: str, board_id: str
    ):

        task_db_id = self.get_task_id_for_task_display_id(
            task_dto.task_display_id)
        task_dto_with_db_task_id = SaveAndActOnTaskDTO(
            task_id=task_db_id, created_by_id=task_dto.created_by_id,
            action_id=task_dto.action_id, title=task_dto.title,
            description=task_dto.description,
            start_datetime=task_dto.start_datetime,
            due_datetime=task_dto.due_datetime,
            priority=task_dto.priority, stage_assignee=task_dto.stage_assignee,
            gof_fields_dtos=task_dto.gof_fields_dtos)
        task_overview_dto = self.save_and_act_on_task(task_dto_with_db_task_id,
                                                      board_id)
        task_log_dto = CreateTaskLogDTO(
            task_id=task_db_id, user_id=task_dto.created_by_id,
            action_id=task_dto.action_id, task_json=task_request_json)
        self._create_task_log(task_log_dto)
        return task_overview_dto

    def _create_task_log(self, task_log_dto: CreateTaskLogDTO):
        from ib_tasks.interactors.task_log_interactor import TaskLogInteractor
        task_log_interactor = TaskLogInteractor(
            storage=self.storage, task_storage=self.task_storage)
        create_task_log_dto = CreateTaskLogDTO(
            task_json=task_log_dto.task_json,
            task_id=task_log_dto.task_id, user_id=task_log_dto.user_id,
            action_id=task_log_dto.action_id)
        task_log_interactor.create_task_log(create_task_log_dto)

    def save_and_act_on_task(
            self, task_dto: SaveAndActOnTaskDTO, board_id: str):
        action_id = task_dto.action_id

        action_type = self._validate_action_id_and_get_action_type(action_id)
        self._update_task(task_dto, action_type)
        task_overview_dto = self._perform_user_action_on_task(
            task_dto.task_id, task_dto.action_id, task_dto.created_by_id,
            board_id)
        return task_overview_dto

    def _update_task(
            self, task_dto: SaveAndActOnTaskDTO, action_type: ActionTypes
    ) -> AllTasksOverviewDetailsDTO:
        update_task_interactor = UpdateTaskInteractor(
            task_storage=self.task_storage, gof_storage=self.gof_storage,
            create_task_storage=self.create_task_storage,
            storage=self.storage, field_storage=self.field_storage,
            stage_storage=self.stage_storage,
            elastic_storage=self.elastic_storage,
            action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage,
            task_template_storage=self.task_template_storage)
        task_basic_details = UpdateTaskBasicDetailsDTO(
            task_id=task_dto.task_id,
            created_by_id=task_dto.created_by_id,
            title=task_dto.title, description=task_dto.description,
            start_datetime=task_dto.start_datetime,
            due_datetime=task_dto.due_datetime, priority=task_dto.priority,
            action_type=action_type)
        update_task_dto = UpdateTaskDTO(
            task_basic_details=task_basic_details,
            stage_assignee=task_dto.stage_assignee,
            gof_fields_dtos=task_dto.gof_fields_dtos)
        return update_task_interactor.update_task(update_task_dto)

    def _perform_user_action_on_task(
            self, task_id: int, action_id: int, user_id: str,
            board_id: str
    ):
        act_on_task_interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, task_storage=self.task_storage,
            action_storage=self.action_storage, action_id=action_id,
            storage=self.storage, gof_storage=self.gof_storage,
            field_storage=self.field_storage, stage_storage=self.stage_storage,
            task_stage_storage=self.task_stage_storage,
            elasticsearch_storage=self.elastic_storage,
            create_task_storage=self.create_task_storage,
            task_template_storage=self.task_template_storage)
        task_complete_details_dto, task_current_stage_details_dto, \
        all_tasks_overview_dto = \
            act_on_task_interactor.user_action_on_task_and_set_random_assignees(
                task_id=task_id)
        task_overview_dto = TaskOverallCompleteDetailsDTO(
            task_complete_details_dto=task_complete_details_dto,
            task_current_stage_details_dto=task_current_stage_details_dto,
            all_tasks_overview_details_dto=all_tasks_overview_dto
        )
        return task_overview_dto

    def _validate_action_id_and_get_action_type(
            self, action_id: int
    ) -> Union[ActionTypes, InvalidActionException]:
        self._validate_action_id(action_id)
        action_type = \
            self.action_storage.get_action_type_for_given_action_id(action_id)
        return action_type

    def _validate_action_id(
            self, action_id: int) -> Optional[InvalidActionException]:
        is_valid_action_id = self.storage.validate_action(action_id)
        action_id_is_invalid = not is_valid_action_id
        if action_id_is_invalid:
            raise InvalidActionException(action_id)
        return None
