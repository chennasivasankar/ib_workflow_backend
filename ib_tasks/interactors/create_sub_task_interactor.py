from typing import Union

from ib_tasks.exceptions.action_custom_exceptions import \
    InvalidActionException, InvalidPresentStageAction, InvalidKeyError
from ib_tasks.exceptions.custom_exceptions import InvalidProjectId, \
    InvalidModulePathFound
from ib_tasks.exceptions.datetime_custom_exceptions import \
    DueDateTimeWithoutStartDateTimeIsNotValid, StartDateTimeIsRequired, \
    DueDateTimeIsRequired, StartDateIsAheadOfDueDate, DueDateTimeHasExpired
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
from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF, InvalidGoFIds, InvalidStagePermittedGoFs
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission, \
    UserActionPermissionDenied
from ib_tasks.exceptions.stage_custom_exceptions import DuplicateStageIds, \
    InvalidDbStageIdsListException, StageIdsWithInvalidPermissionForAssignee, \
    StageIdsListEmptyException, InvalidStageIdsListException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateDBId, \
    InvalidTaskTemplateOfProject, PriorityIsRequired, \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF, InvalidTaskJson, \
    InvalidTaskDisplayId
from ib_tasks.interactors.create_or_update_task.create_task_interactor import \
    CompleteTaskDetailsDTO
from ib_tasks.interactors.presenter_interfaces.create_sub_task_presenter import \
    CreateSubTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
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
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import CreateSubTaskDTO, CreateTaskLogDTO, \
    CreateTaskDTO
from ib_tasks.interactors.user_action_on_task\
    .call_action_logic_function_and_get_or_update_task_status_variables_interactor import \
    InvalidMethodFound


class CreateSubTaskInteractor:

    def __init__(
            self, task_storage: TaskStorageInterface,
            gof_storage: GoFStorageInterface,
            task_template_storage: TaskTemplateStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface,
            stage_storage: StageStorageInterface,
            action_storage: ActionStorageInterface,
            elastic_storage: ElasticSearchStorageInterface,
            task_stage_storage: TaskStageStorageInterface
    ):
        self.task_stage_storage = task_stage_storage
        self.task_template_storage = task_template_storage
        self.gof_storage = gof_storage
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.storage = storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.action_storage = action_storage
        self.elastic_storage = elastic_storage

    def create_sub_task_wrapper(
            self, presenter: CreateSubTaskPresenterInterface,
            task_dto: CreateSubTaskDTO, task_request_json: str
    ):
        try:
            return self._prepare_create_sub_task_response(
                task_dto, presenter, task_request_json)
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_parent_task_id(err)
        except InvalidProjectId as err:
            return presenter.raise_invalid_project_id(err)
        except InvalidTaskTemplateDBId as err:
            return presenter.raise_invalid_task_template_id(err)
        except InvalidTaskTemplateOfProject as err:
            return presenter.raise_invalid_task_template_of_project(err)
        except InvalidActionException as err:
            return presenter.raise_invalid_action_id(err)
        except DuplicateSameGoFOrderForAGoF as err:
            return presenter.raise_duplicate_same_gof_orders_for_a_gof(err)
        except PriorityIsRequired as err:
            return presenter.raise_priority_is_required(err)
        except DueDateTimeWithoutStartDateTimeIsNotValid as err:
            return presenter.raise_due_date_time_without_start_datetime(err)
        except StartDateTimeIsRequired as err:
            return presenter.raise_start_date_time_is_required(err)
        except DueDateTimeIsRequired as err:
            return presenter.raise_due_date_time_is_required(err)
        except StartDateIsAheadOfDueDate as err:
            return presenter.raise_start_date_is_ahead_of_due_date(err)
        except DueDateTimeHasExpired as err:
            return presenter.raise_due_date_time_has_expired(err)
        except InvalidGoFIds as err:
            return presenter.raise_invalid_gof_ids(err)
        except InvalidGoFsOfTaskTemplate as err:
            return presenter.raise_invalid_gofs_given_to_a_task_template(err)
        except InvalidFieldIds as err:
            return presenter.raise_invalid_field_ids(err)
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
        except InvalidModulePathFound as err:
            return presenter.raise_invalid_path_not_found(err)
        except InvalidMethodFound as err:
            return presenter.raise_invalid_method_not_found(err)
        except DuplicateStageIds as err:
            return presenter.raise_duplicate_stage_ids_not_valid(err)
        except InvalidDbStageIdsListException as err:
            return presenter.raise_invalid_stage_ids(err)
        except StageIdsWithInvalidPermissionForAssignee as err:
            return presenter.raise_invalid_stage_assignees(err)
        except StageIdsListEmptyException as err:
            return presenter.raise_stage_ids_list_empty(err)
        except InvalidStageIdsListException as err:
            return presenter.raise_invalid_stage_ids_list(err)
        except InvalidTaskJson as err:
            return presenter.raise_invalid_task_json(err)

    def _prepare_create_sub_task_response(
            self, task_dto: CreateSubTaskDTO,
            presenter: CreateSubTaskPresenterInterface,
            task_request_json: str
    ):
        complete_task_details = self.create_sub_task(task_dto)
        task_id = complete_task_details.task_id
        user_id = task_dto.basic_task_details_dto.created_by_id
        action_id = task_dto.basic_task_details_dto.action_id

        task_log_dto = CreateTaskLogDTO(
            task_id=task_id, user_id=user_id, action_id=action_id,
            task_json=task_request_json)
        self._create_task_log(task_log_dto)
        response = presenter.get_create_sub_task_response(complete_task_details)
        return response

    def _create_task_log(self, task_log_dto: CreateTaskLogDTO):
        from ib_tasks.interactors.task_log_interactor import TaskLogInteractor
        task_log_interactor = TaskLogInteractor(
            storage=self.storage, task_storage=self.task_storage,
            action_storage=self.action_storage)
        create_task_log_dto = CreateTaskLogDTO(
            task_json=task_log_dto.task_json,
            task_id=task_log_dto.task_id, user_id=task_log_dto.user_id,
            action_id=task_log_dto.action_id)
        task_log_interactor.create_task_log(create_task_log_dto)

    def create_sub_task(
            self, task_dto: CreateSubTaskDTO) -> CompleteTaskDetailsDTO:
        parent_task_id = self._validate_parent_task_id_and_get_db_id(
            task_dto.parent_task_id)
        complete_task_details = self.create_task(task_dto)
        self._add_task_as_sub_task_to_given_parent_task(
            parent_task_id, complete_task_details.task_id)
        return complete_task_details

    def _validate_parent_task_id_and_get_db_id(
            self, parent_task_id: str) -> Union[InvalidTaskDisplayId, int]:
        task_id = \
            self.task_storage.validate_task_display_id_and_return_task_id(
                parent_task_id)
        return task_id

    def create_task(self, task_dto: CreateSubTaskDTO) -> CompleteTaskDetailsDTO:
        from ib_tasks.interactors.create_or_update_task \
            .create_task_interactor import CreateTaskInteractor
        create_task_interactor = CreateTaskInteractor(
            task_storage=self.task_storage, gof_storage=self.gof_storage,
            task_template_storage=self.task_template_storage,
            create_task_storage=self.create_task_storage,
            storage=self.storage, field_storage=self.field_storage,
            stage_storage=self.stage_storage,
            action_storage=self.action_storage,
            elastic_storage=self.elastic_storage,
            task_stage_storage=self.task_stage_storage)
        create_task_dto = CreateTaskDTO(
            basic_task_details_dto=task_dto.basic_task_details_dto,
            gof_fields_dtos=task_dto.gof_fields_dtos)
        complete_task_details_dto = create_task_interactor.create_task(
            create_task_dto)
        return complete_task_details_dto

    def _add_task_as_sub_task_to_given_parent_task(
            self, parent_task_id, created_task_id):
        self.task_storage.add_sub_task(created_task_id, parent_task_id)
