from ib_tasks.exceptions.action_custom_exceptions import \
    InvalidActionException, InvalidPresentStageAction, InvalidKeyError, \
    InvalidCustomLogicException
from ib_tasks.exceptions.custom_exceptions import InvalidModulePathFound, \
    InvalidMethodFound
from ib_tasks.exceptions.datetime_custom_exceptions import \
    InvalidDueTimeFormat, StartDateIsAheadOfDueDate, \
    DueTimeHasExpiredForToday, \
    DueDateHasExpired
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
    DuplicateFieldIdsToGoF
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds, \
    DuplicateSameGoFOrderForAGoF
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission, \
    UserActionPermissionDenied
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsWithInvalidPermissionForAssignee, DuplicateStageIds, \
    InvalidDbStageIdsListException, InvalidStageId
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException, \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF, InvalidTaskDisplayId
from ib_tasks.interactors.create_or_update_task.update_task_interactor import \
    UpdateTaskInteractor
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
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
from ib_tasks.interactors.task_dtos import UpdateTaskDTO, \
    SaveAndActOnTaskDTO, \
    SaveAndActOnTaskWithTaskDisplayIdDTO
from ib_tasks.interactors.user_action_on_task_interactor import \
    UserActionOnTaskInteractor


class SaveAndActOnATaskInteractor(GetTaskIdForTaskDisplayIdMixin):

    def __init__(
            self, task_storage: TaskStorageInterface,
            gof_storage: GoFStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface,
            stage_storage: StageStorageInterface,
            action_storage: ActionStorageInterface,
            elastic_storage: ElasticSearchStorageInterface,
            task_stage_storage: TaskStageStorageInterface
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

    def save_and_act_on_task_wrapper(
            self, presenter: SaveAndActOnATaskPresenterInterface,
            task_dto: SaveAndActOnTaskWithTaskDisplayIdDTO
    ):
        try:
            return self._prepare_save_and_act_response(presenter, task_dto)
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id(err)
        except InvalidActionException as err:
            return presenter.raise_invalid_action_id(err)
        except InvalidTaskException as err:
            return presenter.raise_invalid_task_id(err)
        except InvalidStageId as err:
            return presenter.raise_invalid_stage_id(err)
        except InvalidDueTimeFormat as err:
            return presenter.raise_invalid_due_time_format(err)
        except StartDateIsAheadOfDueDate as err:
            return presenter.raise_start_date_is_ahead_of_due_date(err)
        except DueDateHasExpired as err:
            return presenter.raise_due_date_has_expired(err)
        except DueTimeHasExpiredForToday as err:
            return presenter.raise_due_time_has_expired_for_today(err)
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
        except UserNeedsGoFWritablePermission as err:
            return presenter.raise_user_needs_gof_writable_permission(err)
        except UserNeedsFieldWritablePermission as err:
            return presenter.raise_user_needs_field_writable_permission(err)
        except EmptyValueForRequiredField as err:
            return presenter. \
                raise_exception_for_empty_value_in_required_field(err)
        except InvalidPhoneNumberValue as err:
            return presenter.raise_exception_for_invalid_phone_number_value(
                err)
        except InvalidEmailFieldValue as err:
            return presenter.raise_exception_for_invalid_email_address(err)
        except InvalidURLValue as err:
            return presenter.raise_exception_for_invalid_url_address(err)
        except NotAStrongPassword as err:
            return presenter.raise_exception_for_weak_password(err)
        except InvalidNumberValue as err:
            return presenter.raise_exception_for_invalid_number_value(err)
        except InvalidFloatValue as err:
            return presenter.raise_exception_for_invalid_float_value(err)
        except InvalidValueForDropdownField as err:
            return presenter.raise_exception_for_invalid_dropdown_value(err)
        except IncorrectNameInGoFSelectorField as err:
            return presenter. \
                raise_exception_for_invalid_name_in_gof_selector_field_value(
                err)
        except IncorrectRadioGroupChoice as err:
            return presenter. \
                raise_exception_for_invalid_choice_in_radio_group_field(err)
        except IncorrectCheckBoxOptionsSelected as err:
            return presenter. \
                raise_exception_for_invalid_checkbox_group_options_selected(
                err)
        except IncorrectMultiSelectOptionsSelected as err:
            return presenter. \
                raise_exception_for_invalid_multi_select_options_selected(err)
        except IncorrectMultiSelectLabelsSelected as err:
            return presenter. \
                raise_exception_for_invalid_multi_select_labels_selected(err)
        except InvalidDateFormat as err:
            return presenter.raise_exception_for_invalid_date_format(err)
        except InvalidTimeFormat as err:
            return presenter.raise_exception_for_invalid_time_format(err)
        except InvalidUrlForImage as err:
            return presenter.raise_exception_for_invalid_image_url(err)
        except InvalidImageFormat as err:
            return presenter.raise_exception_for_not_acceptable_image_format(
                err)
        except InvalidUrlForFile as err:
            return presenter.raise_exception_for_invalid_file_url(err)
        except InvalidFileFormat as err:
            return presenter.raise_exception_for_not_acceptable_file_format(
                err)
        except UserActionPermissionDenied as err:
            return presenter.raise_exception_for_user_action_permission_denied(
                error_obj=err)
        except InvalidPresentStageAction as err:
            return presenter.raise_exception_for_invalid_present_stage_actions(
                err)
        except InvalidKeyError:
            return presenter.raise_invalid_key_error()
        except InvalidCustomLogicException:
            return presenter.raise_invalid_custom_logic_function_exception()
        except InvalidModulePathFound as exception:
            return presenter.raise_invalid_path_not_found_exception(
                path_name=exception.path_name)
        except InvalidMethodFound as exception:
            return presenter.raise_invalid_method_not_found_exception(
                method_name=exception.method_name)
        except DuplicateStageIds as exception:
            return presenter.raise_duplicate_stage_ids_not_valid(
                duplicate_stage_ids=exception.duplicate_stage_ids)
        except InvalidDbStageIdsListException as exception:
            return presenter.raise_invalid_stage_ids_exception(
                invalid_stage_ids=exception.invalid_stage_ids)
        except StageIdsWithInvalidPermissionForAssignee as err:
            return presenter. \
                raise_stage_ids_with_invalid_permission_for_assignee_exception(
                err)

    def _prepare_save_and_act_response(
            self, presenter, task_dto: SaveAndActOnTaskWithTaskDisplayIdDTO):
        task_current_stage_details_dto, all_tasks_overview_details_dto = \
            self.save_and_act_on_task_with_task_display_id(task_dto)
        return presenter.get_save_and_act_on_task_response(
            task_current_stage_details_dto, all_tasks_overview_details_dto)

    def save_and_act_on_task_with_task_display_id(
            self, task_dto: SaveAndActOnTaskWithTaskDisplayIdDTO):
        task_db_id = self.get_task_id_for_task_display_id(
            task_dto.task_display_id)
        task_dto_with_db_task_id = SaveAndActOnTaskDTO(
            task_id=task_db_id, created_by_id=task_dto.created_by_id,
            action_id=task_dto.action_id, title=task_dto.title,
            description=task_dto.description, start_date=task_dto.start_date,
            due_date=task_dto.due_date, due_time=task_dto.due_time,
            priority=task_dto.priority, stage_assignee=task_dto.stage_assignee,
            gof_fields_dtos=task_dto.gof_fields_dtos
        )
        return self.save_and_act_on_task(task_dto_with_db_task_id)

    def save_and_act_on_task(self, task_dto: SaveAndActOnTaskDTO):
        is_valid_action_id = self.storage.validate_action(task_dto.action_id)
        if not is_valid_action_id:
            raise InvalidActionException(task_dto.action_id)
        action_type = self.action_storage.get_action_type_for_given_action_id(
            action_id=task_dto.action_id)
        update_task_interactor = UpdateTaskInteractor(
            task_storage=self.task_storage, gof_storage=self.gof_storage,
            create_task_storage=self.create_task_storage,
            storage=self.storage, field_storage=self.field_storage,
            stage_storage=self.stage_storage,
            elastic_storage=self.elastic_storage,
            action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage
        )
        update_task_dto = UpdateTaskDTO(
            task_id=task_dto.task_id, created_by_id=task_dto.created_by_id,
            title=task_dto.title, description=task_dto.description,
            start_date=task_dto.start_date, due_date=task_dto.due_date,
            due_time=task_dto.due_time, priority=task_dto.priority,
            stage_assignee=task_dto.stage_assignee,
            gof_fields_dtos=task_dto.gof_fields_dtos
        )
        all_tasks_overview_details_dto = \
            update_task_interactor.update_task(update_task_dto, action_type)
        act_on_task_interactor = UserActionOnTaskInteractor(
            user_id=task_dto.created_by_id, board_id=None,
            task_storage=self.task_storage,
            action_storage=self.action_storage, action_id=task_dto.action_id,
            storage=self.storage, gof_storage=self.create_task_storage,
            field_storage=self.field_storage, stage_storage=self.stage_storage,
            task_stage_storage=self.task_stage_storage,
            elasticsearch_storage=self.elastic_storage)
        act_on_task_interactor.user_action_on_task(task_id=task_dto.task_id)
        from ib_tasks.interactors.get_task_current_stages_interactor import \
            GetTaskCurrentStagesInteractor
        get_task_current_stages_interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=self.task_stage_storage)
        task_current_stage_details_dto = \
            get_task_current_stages_interactor.get_task_current_stages_details(
                task_id=task_dto.task_id, user_id=task_dto.created_by_id)
        return task_current_stage_details_dto, all_tasks_overview_details_dto
