from dataclasses import dataclass

from ib_tasks.exceptions.action_custom_exceptions import (
    InvalidActionException, InvalidKeyError, InvalidCustomLogicException,
    InvalidPresentStageAction
)
from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
from ib_tasks.exceptions.datetime_custom_exceptions import (
    StartDateIsAheadOfDueDate, DueDateTimeHasExpired, DueDateTimeIsRequired,
    DueDateTimeWithoutStartDateTimeIsNotValid, StartDateTimeIsRequired
)
from ib_tasks.exceptions.field_values_custom_exceptions import (
    EmptyValueForRequiredField, InvalidPhoneNumberValue,
    InvalidEmailFieldValue, InvalidURLValue, NotAStrongPassword,
    InvalidNumberValue, InvalidFloatValue, InvalidValueForDropdownField,
    IncorrectNameInGoFSelectorField, IncorrectRadioGroupChoice,
    IncorrectCheckBoxOptionsSelected, IncorrectMultiSelectOptionsSelected,
    IncorrectMultiSelectLabelsSelected, InvalidDateFormat, InvalidTimeFormat,
    InvalidUrlForImage, InvalidImageFormat, InvalidUrlForFile,
    InvalidFileFormat
)
from ib_tasks.exceptions.fields_custom_exceptions import (
    InvalidFieldIds, DuplicateFieldIdsToGoF, UserDidNotFillRequiredFields
)
from ib_tasks.exceptions.gofs_custom_exceptions import (
    InvalidGoFIds, DuplicateSameGoFOrderForAGoF, UserDidNotFillRequiredGoFs
)
from ib_tasks.exceptions.permission_custom_exceptions import (
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission,
    UserActionPermissionDenied
)
from ib_tasks.exceptions.stage_custom_exceptions import (
    DuplicateStageIds, InvalidDbStageIdsListException,
    StageIdsWithInvalidPermissionForAssignee, StageIdsListEmptyException,
    InvalidStageIdsListException
)
from ib_tasks.exceptions.task_custom_exceptions import (
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF, InvalidTaskTemplateDBId,
    InvalidTaskTemplateOfProject, PriorityIsRequired, InvalidTaskJson
)
from ib_tasks.interactors \
    .call_action_logic_function_and_update_task_status_variables_interactor \
    import InvalidMethodFound
from ib_tasks.interactors.create_or_update_task \
    .task_crud_operations_interactor import TaskCrudOperationsInteractor
from ib_tasks.interactors.create_or_update_task \
    .task_details_validations_interactor import \
    TaskDetailsValidationsInteractor, TaskDetailsValidationsStorages
from ib_tasks.interactors \
    .get_next_stages_random_assignees_of_a_task_interactor import \
    InvalidModulePathFound
from ib_tasks.interactors.mixins.task_operations_utilities_mixin import \
    TaskOperationsUtilitiesMixin
from ib_tasks.interactors.presenter_interfaces.create_task_presenter import \
    CreateTaskPresenterInterface
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface \
    import ElasticSearchStorageInterface
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
    import TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import (
    CreateTaskDTO, CreateTaskLogDTO, TaskCurrentStageDetailsDTO
)
from ib_tasks.interactors.user_action_on_task_interactor import \
    UserActionOnTaskInteractor


@dataclass
class CompleteTaskDetailsDTO:
    task_id: int
    task_current_stages_details_dto: TaskCurrentStageDetailsDTO
    all_tasks_overview_details_dto: AllTasksOverviewDetailsDTO


class CreateTaskInteractor(TaskOperationsUtilitiesMixin):

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

    def create_task_wrapper(
            self, presenter: CreateTaskPresenterInterface,
            task_dto: CreateTaskDTO, task_request_json: str
    ):
        try:
            return self._prepare_create_task_response(
                task_dto, presenter, task_request_json)
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
            return presenter.raise_invalid_custom_logic_function()
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

    def _prepare_create_task_response(
            self, task_dto: CreateTaskDTO,
            presenter: CreateTaskPresenterInterface,
            task_request_json: str
    ):
        complete_task_details_dto = self.create_task(task_dto)
        task_id = complete_task_details_dto.task_id
        user_id = task_dto.basic_task_details_dto.created_by_id
        action_id = task_dto.basic_task_details_dto.action_id

        self._create_task_log(task_id, user_id, action_id, task_request_json)
        response = presenter.get_create_task_response(
            complete_task_details_dto.task_current_stages_details_dto,
            complete_task_details_dto.all_tasks_overview_details_dto)
        return response

    def _create_task_log(
            self, task_id: int, user_id: str, action_id: int,
            task_request_json: str):
        from ib_tasks.interactors.task_log_interactor import TaskLogInteractor
        task_log_interactor = TaskLogInteractor(
            storage=self.storage, task_storage=self.task_storage)
        create_task_log_dto = CreateTaskLogDTO(
            task_json=task_request_json, task_id=task_id, user_id=user_id,
            action_id=action_id)
        task_log_interactor.create_task_log(create_task_log_dto)

    def create_task(self, task_dto: CreateTaskDTO) -> CompleteTaskDetailsDTO:
        project_id = task_dto.basic_task_details_dto.project_id
        user_id = task_dto.basic_task_details_dto.created_by_id
        action_id = task_dto.basic_task_details_dto.action_id
        task_template_id = task_dto.basic_task_details_dto.task_template_id

        self._validate_task_details(task_dto)
        task_id = self._create_task_gofs_and_fields(task_dto)
        self._set_status_variables_and_create_initial_task_stages(
            task_id, task_template_id)
        self._perform_user_action_on_task(task_id, action_id, user_id)
        task_current_stages_details_dto = \
            self._get_task_current_stages_information(task_id, user_id)
        all_tasks_overview_details_dto = self._get_task_overview_details_dto(
            task_id, user_id, project_id)
        complete_task_details_dto = CompleteTaskDetailsDTO(
            task_id=task_id,
            task_current_stages_details_dto=task_current_stages_details_dto,
            all_tasks_overview_details_dto=all_tasks_overview_details_dto)
        return complete_task_details_dto

    def _validate_task_details(self, task_dto: CreateTaskDTO):
        storages_dto = TaskDetailsValidationsStorages(
            task_template_storage=self.task_template_storage,
            storage=self.storage, action_storage=self.action_storage,
            task_storage=self.task_storage, gof_storage=self.gof_storage,
            create_task_storage=self.create_task_storage,
            field_storage=self.field_storage
        )
        task_details_validation_interactor = TaskDetailsValidationsInteractor(
            storages_dto)
        task_details_validation_interactor.perform_task_details_validations(
            task_dto)

    def _create_task_gofs_and_fields(self, task_dto: CreateTaskDTO) -> int:
        task_crud_interactor = TaskCrudOperationsInteractor(
            create_task_storage=self.create_task_storage)
        task_id = task_crud_interactor.create_task(
            task_dto.basic_task_details_dto)
        gof_field_dtos = task_dto.gof_fields_dtos
        task_gof_dtos = self._prepare_task_gof_dtos(task_id, gof_field_dtos)
        task_gof_details_dtos = task_crud_interactor.create_task_gofs(
            task_gof_dtos)
        task_gof_field_dtos = self._prepare_task_gof_fields_dtos(
            task_dto.gof_fields_dtos, task_gof_details_dtos)
        task_crud_interactor.create_task_gof_fields(task_gof_field_dtos)
        return task_id

    def _set_status_variables_and_create_initial_task_stages(
            self, task_id: int, task_template_id: str):
        self.create_task_storage.set_status_variables_for_template_and_task(
            task_id=task_id, task_template_id=task_template_id)
        self.create_task_storage.create_initial_task_stage(
            task_id=task_id, template_id=task_template_id)

    def _perform_user_action_on_task(
            self, task_id: int, action_id: int, user_id: str):
        act_on_task_interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=None, action_id=action_id,
            storage=self.storage, gof_storage=self.gof_storage,
            field_storage=self.field_storage, stage_storage=self.stage_storage,
            task_storage=self.task_storage, action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage,
            elasticsearch_storage=self.elastic_storage,
            create_task_storage=self.create_task_storage,
            task_template_storage=self.task_template_storage
        )
        act_on_task_interactor.user_action_on_task_and_set_random_assignees(
            task_id=task_id)

    def _get_task_current_stages_information(
            self, task_id: int, user_id: str) -> TaskCurrentStageDetailsDTO:
        from ib_tasks.interactors.get_task_current_stages_interactor import \
            GetTaskCurrentStagesInteractor
        get_task_current_stages_interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=self.task_stage_storage)
        task_current_stages_details_dto = \
            get_task_current_stages_interactor.get_task_current_stages_details(
                task_id=task_id, user_id=user_id)
        return task_current_stages_details_dto
