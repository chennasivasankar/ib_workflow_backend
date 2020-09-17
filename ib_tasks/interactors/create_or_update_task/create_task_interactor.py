from typing import List, Optional

from ib_tasks.constants.enum import ActionTypes, ViewType, Priority
from ib_tasks.exceptions.action_custom_exceptions import \
    (InvalidActionException, InvalidKeyError, InvalidCustomLogicException,
     InvalidPresentStageAction
     )
from ib_tasks.exceptions.custom_exceptions import InvalidProjectId, \
    InvalidMethodFound
from ib_tasks.exceptions.datetime_custom_exceptions import \
    (StartDateIsAheadOfDueDate,
     DueDateTimeHasExpired, DueDateTimeWithoutStartDateTimeIsNotValid,
     StartDateTimeIsRequired, DueDateTimeIsRequired
     )
from ib_tasks.exceptions.field_values_custom_exceptions import \
    (EmptyValueForRequiredField, InvalidPhoneNumberValue,
     InvalidEmailFieldValue, InvalidURLValue, NotAStrongPassword,
     InvalidNumberValue, InvalidFloatValue, InvalidValueForDropdownField,
     IncorrectNameInGoFSelectorField, IncorrectRadioGroupChoice,
     IncorrectCheckBoxOptionsSelected, IncorrectMultiSelectOptionsSelected,
     IncorrectMultiSelectLabelsSelected, InvalidDateFormat, InvalidTimeFormat,
     InvalidUrlForImage, InvalidImageFormat, InvalidUrlForFile,
     InvalidFileFormat
     )
from ib_tasks.exceptions.fields_custom_exceptions import (InvalidFieldIds,
                                                          DuplicateFieldIdsToGoF,
                                                          UserDidNotFillRequiredFields
                                                          )
from ib_tasks.exceptions.gofs_custom_exceptions import (InvalidGoFIds,
                                                        DuplicateSameGoFOrderForAGoF,
                                                        UserDidNotFillRequiredGoFs
                                                        )
from ib_tasks.exceptions.permission_custom_exceptions import \
    (UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission,
     UserActionPermissionDenied
     )
from ib_tasks.exceptions.stage_custom_exceptions import (DuplicateStageIds,
                                                         InvalidDbStageIdsListException,
                                                         StageIdsWithInvalidPermissionForAssignee,
                                                         StageIdsListEmptyException,
                                                         InvalidStageIdsListException
                                                         )
from ib_tasks.exceptions.task_custom_exceptions import \
    (InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF, InvalidTaskTemplateDBId,
     InvalidTaskTemplateOfProject, PriorityIsRequired, InvalidTaskJson
     )
from ib_tasks.interactors.create_or_update_task \
    .template_gofs_fields_base_validations import \
    TemplateGoFsFieldsBaseValidationsInteractor
from ib_tasks.interactors \
    .get_next_stages_random_assignees_of_a_task_interactor import \
    InvalidModulePathFound
from ib_tasks.interactors.presenter_interfaces.create_task_presenter import \
    CreateTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface \
    import ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    (TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO
     )
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import (CreateTaskDTO, CreateTaskLogDTO,
                                            GoFFieldsDTO
                                            )
from ib_tasks.interactors.user_action_on_task.user_action_on_task_interactor import \
    UserActionOnTaskInteractor


class CreateTaskInteractor:

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
            return presenter.raise_invalid_name_in_gof_selector_field_value(
                err)
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
            return presenter.raise_stage_ids_with_invalid_permission_for_assignee(
                err)
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
        task_current_stage_details_dto, all_tasks_overview_dto, \
        created_task_id = self.create_task(task_dto)
        from ib_tasks.interactors.task_log_interactor import TaskLogInteractor
        task_log_interactor = TaskLogInteractor(
            storage=self.storage, task_storage=self.task_storage,
            action_storage=self.action_storage
        )
        create_task_log_dto = CreateTaskLogDTO(
            task_json=task_request_json, task_id=created_task_id,
            user_id=task_dto.created_by_id, action_id=task_dto.action_id)
        task_log_interactor.create_task_log(create_task_log_dto)
        return presenter.get_create_task_response(
            task_current_stage_details_dto, all_tasks_overview_dto)

    def create_task(self, task_dto: CreateTaskDTO):
        self._validate_project_id(task_dto.project_id)
        self._validate_task_template_id(task_dto.task_template_id)
        self._validate_task_template_project_id(
            task_dto.project_id, task_dto.task_template_id)
        is_valid_action_id = self.action_storage.validate_action(
            action_id=task_dto.action_id)
        if not is_valid_action_id:
            raise InvalidActionException(task_dto.action_id)
        action_type = self.action_storage.get_action_type_for_given_action_id(
            action_id=task_dto.action_id)
        self._validate_task_details(task_dto, action_type)
        base_validations_interactor = \
            TemplateGoFsFieldsBaseValidationsInteractor(
                self.task_storage, self.gof_storage,
                self.create_task_storage, self.storage,
                self.field_storage, self.task_template_storage)
        base_validations_interactor. \
            perform_base_validations_for_template_gofs_and_fields(
            gof_fields_dtos=task_dto.gof_fields_dtos,
            user_id=task_dto.created_by_id,
            task_template_id=task_dto.task_template_id,
            project_id=task_dto.project_id, action_type=action_type)
        action_type_is_not_no_validations = \
            action_type != ActionTypes.NO_VALIDATIONS.value
        if action_type_is_not_no_validations:
            self._validate_all_user_template_permitted_fields_are_filled_or_not(
                user_id=task_dto.created_by_id, project_id=task_dto.project_id,
                task_template_id=task_dto.task_template_id,
                gof_fields_dtos=task_dto.gof_fields_dtos
            )
        created_task_id = \
            self.create_task_storage.create_task_with_given_task_details(
                task_dto)
        task_gof_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=created_task_id,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_gof_details_dtos = self.create_task_storage.create_task_gofs(
            task_gof_dtos=task_gof_dtos)
        task_gof_field_dtos = self._prepare_task_gof_fields_dtos(
            task_dto, task_gof_details_dtos)
        self.create_task_storage.create_task_gof_fields(task_gof_field_dtos)
        self.create_task_storage.set_status_variables_for_template_and_task(
            task_dto.task_template_id, created_task_id)
        self.create_task_storage.create_initial_task_stage(
            task_id=created_task_id, template_id=task_dto.task_template_id)
        act_on_task_interactor = UserActionOnTaskInteractor(
            user_id=task_dto.created_by_id, board_id=None,
            action_id=task_dto.action_id,
            storage=self.storage,
            gof_storage=self.gof_storage,
            field_storage=self.field_storage,
            stage_storage=self.stage_storage,
            task_storage=self.task_storage,
            action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage,
            elasticsearch_storage=self.elastic_storage,
            create_task_storage=self.create_task_storage,
            task_template_storage=self.task_template_storage
        )
        act_on_task_interactor.user_action_on_task_and_set_random_assignees(task_id=created_task_id)
        from ib_tasks.interactors.get_task_current_stages_interactor import \
            GetTaskCurrentStagesInteractor
        get_task_current_stages_interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=self.task_stage_storage)
        task_current_stage_details_dto = \
            get_task_current_stages_interactor.get_task_current_stages_details(
                task_id=created_task_id, user_id=task_dto.created_by_id)
        from ib_tasks.interactors \
            .get_all_task_overview_with_filters_and_searches_for_user import \
            GetTasksOverviewForUserInteractor
        task_overview_interactor = GetTasksOverviewForUserInteractor(
            stage_storage=self.stage_storage, task_storage=self.task_storage,
            field_storage=self.field_storage,
            action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage
        )
        all_tasks_overview_details_dto = \
            task_overview_interactor.get_filtered_tasks_overview_for_user(
                user_id=task_dto.created_by_id, task_ids=[created_task_id],
                view_type=ViewType.KANBAN.value,
                project_id=task_dto.project_id)
        return (
            task_current_stage_details_dto, all_tasks_overview_details_dto,
            created_task_id)

    def _validate_task_template_id(
            self, task_template_id: str
    ) -> Optional[InvalidTaskTemplateDBId]:
        task_template_existence = \
            self.task_template_storage.check_is_template_exists(
                template_id=task_template_id)
        if not task_template_existence:
            raise InvalidTaskTemplateDBId(task_template_id)
        return

    def _prepare_task_gof_fields_dtos(
            self, task_dto: CreateTaskDTO,
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_field_dtos = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            task_gof_id = self._get_gof_id_for_field_in_task_gof_details(
                gof_fields_dto.gof_id, gof_fields_dto.same_gof_order,
                task_gof_details_dtos
            )
            task_gof_field_dtos += [
                TaskGoFFieldDTO(
                    field_id=field_values_dto.field_id,
                    field_response=field_values_dto.field_response,
                    task_gof_id=task_gof_id
                )
                for field_values_dto in gof_fields_dto.field_values_dtos
            ]
        return task_gof_field_dtos

    @staticmethod
    def _get_gof_id_for_field_in_task_gof_details(
            gof_id: str, same_gof_order: int,
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> Optional[int]:
        for task_gof_details_dto in task_gof_details_dtos:
            gof_matched = (
                    task_gof_details_dto.gof_id == gof_id and
                    task_gof_details_dto.same_gof_order == same_gof_order
            )
            if gof_matched:
                return task_gof_details_dto.task_gof_id
        return

    def _validate_task_details(
            self, task_dto: CreateTaskDTO,
            action_type: Optional[ActionTypes]
    ):
        start_datetime = task_dto.start_datetime
        due_datetime = task_dto.due_datetime
        self._validate_due_datetime_without_start_datetime(
            start_datetime, due_datetime)
        action_type_is_no_validations = \
            action_type == ActionTypes.NO_VALIDATIONS.value
        self._validate_priority_in_no_validations_case(
            task_dto.priority, action_type_is_no_validations)
        if action_type_is_no_validations and due_datetime is None:
            return
        start_datetime_is_emtpy = not start_datetime
        due_datetime_is_empty = not due_datetime
        if start_datetime_is_emtpy:
            raise StartDateTimeIsRequired()
        if due_datetime_is_empty:
            raise DueDateTimeIsRequired()
        self._validate_start_date_and_due_date_dependencies(
            start_datetime, due_datetime)
        import datetime
        due_datetime_is_expired = due_datetime <= datetime.datetime.now()
        if due_datetime_is_expired:
            raise DueDateTimeHasExpired(due_datetime)

    @staticmethod
    def _validate_start_date_and_due_date_dependencies(start_date,
                                                       due_date):
        start_date_is_ahead_of_due_date = start_date > due_date
        if start_date_is_ahead_of_due_date:
            raise StartDateIsAheadOfDueDate(start_date, due_date)

    def _validate_task_template_project_id(
            self, project_id: str, task_template_id: str
    ) -> Optional[InvalidTaskTemplateOfProject]:
        project_task_templates = \
            self.task_template_storage.get_project_templates(project_id)
        invalid_template_of_project = \
            task_template_id not in project_task_templates
        if invalid_template_of_project:
            raise InvalidTaskTemplateOfProject(project_id, task_template_id)
        return

    @staticmethod
    def _validate_due_datetime_without_start_datetime(
            start_datetime, due_datetime
    ) -> Optional[DueDateTimeWithoutStartDateTimeIsNotValid]:
        due_datetime_given_without_start_date = not start_datetime and \
                                                due_datetime
        if due_datetime_given_without_start_date:
            raise DueDateTimeWithoutStartDateTimeIsNotValid(due_datetime)
        return

    @staticmethod
    def _validate_priority_in_no_validations_case(
            priority: Priority, action_type_is_no_validations: bool
    ) -> Optional[PriorityIsRequired]:
        priority_is_not_given = not priority
        if priority_is_not_given and not action_type_is_no_validations:
            raise PriorityIsRequired()
        return

    @staticmethod
    def _validate_project_id(project_id: str) -> Optional[InvalidProjectId]:
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        valid_project_ids = \
            service_adapter.project_service.get_valid_project_ids([project_id])
        project_id_is_not_valid = project_id not in valid_project_ids
        if project_id_is_not_valid:
            raise InvalidProjectId(project_id)
        return

    def _validate_all_user_template_permitted_fields_are_filled_or_not(
            self, user_id: str, project_id: str, task_template_id: str,
            gof_fields_dtos: List[GoFFieldsDTO]
    ):
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service \
            .get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id)
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
        filled_gof_ids = [
            gof_field_dto.gof_id for gof_field_dto in gof_fields_dtos]
        filled_field_ids = []
        for gof_fields_dto in gof_fields_dtos:
            filled_field_ids += [
                field_value_dto.field_id
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
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
