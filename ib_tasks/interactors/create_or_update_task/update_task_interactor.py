import datetime
from typing import Optional, List, Tuple

from ib_tasks.constants.enum import ViewType, ActionTypes
from ib_tasks.exceptions.datetime_custom_exceptions import \
    StartDateIsAheadOfDueDate, \
    DueDateTimeHasExpired, \
    DueDateTimeWithoutStartDateTimeIsNotValid, StartDateTimeIsRequired, \
    DueDateTimeIsRequired
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
    DuplicateSameGoFOrderForAGoF, InvalidStagePermittedGoFs
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsWithInvalidPermissionForAssignee, InvalidStageId, \
    StageIdsListEmptyException, InvalidStageIdsListException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException, \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF, InvalidTaskDisplayId, \
    TaskDelayReasonIsNotUpdated, PriorityIsRequired
from ib_tasks.interactors.create_or_update_task. \
    gofs_details_validations_interactor import \
    GoFsDetailsValidationsInteractor
from ib_tasks.interactors.create_or_update_task \
    .task_crud_operations_interactor import TaskCrudOperationsInteractor
from ib_tasks.interactors.field_dtos import FieldIdWithTaskGoFIdDTO
from ib_tasks.interactors.gofs_dtos import GoFIdWithSameGoFOrderDTO
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.mixins.task_operations_utilities_mixin import \
    TaskOperationsUtilitiesMixin
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.presenter_interfaces.update_task_presenter import \
    UpdateTaskPresenterInterface
from ib_tasks.interactors.stages_dtos import StageAssigneeDTO, \
    TaskIdWithStageAssigneesDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
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
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import UpdateTaskDTO, \
    UpdateTaskWithTaskDisplayIdDTO, GoFFieldsDTO, StageIdWithAssigneeDTO, \
    UpdateTaskBasicDetailsDTO, CreateTaskLogDTO
from ib_tasks.interactors.update_task_stage_assignees_interactor import \
    UpdateTaskStageAssigneesInteractor


class UpdateTaskInteractor(
    GetTaskIdForTaskDisplayIdMixin, TaskOperationsUtilitiesMixin
):

    def __init__(
            self, task_storage: TaskStorageInterface,
            gof_storage: GoFStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface,
            stage_storage: StageStorageInterface,
            elastic_storage: ElasticSearchStorageInterface,
            action_storage: ActionStorageInterface,
            task_stage_storage: TaskStageStorageInterface,
            task_template_storage: TaskTemplateStorageInterface
    ):
        self.task_stage_storage = task_stage_storage
        self.action_storage = action_storage
        self.gof_storage = gof_storage
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.storage = storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.elastic_storage = elastic_storage
        self.task_template_storage = task_template_storage

    def update_task_wrapper(
            self, presenter: UpdateTaskPresenterInterface,
            task_dto: UpdateTaskWithTaskDisplayIdDTO,
            request_json: str):
        try:
            return self._prepare_update_task_response(
                task_dto, presenter, request_json)
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id(err)
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
        except UserDidNotFillRequiredFields as err:
            return presenter.raise_user_did_not_fill_required_fields(err)
        except StageIdsWithInvalidPermissionForAssignee as err:
            return presenter.raise_invalid_stage_assignees(err)
        except StageIdsListEmptyException as err:
            return presenter.raise_stage_ids_list_empty_exception(err)
        except InvalidStageIdsListException as err:
            return presenter.raise_invalid_stage_ids_list_exception(err)

    def _prepare_update_task_response(
            self, task_dto: UpdateTaskWithTaskDisplayIdDTO,
            presenter: UpdateTaskPresenterInterface, request_json: str):
        all_tasks_overview_details_dto = self.update_task_with_task_display_id(
            task_dto)
        return presenter.get_update_task_response(
            all_tasks_overview_details_dto)

    def update_task_with_task_display_id(
            self, task_dto: UpdateTaskWithTaskDisplayIdDTO):
        task_display_id = task_dto.task_display_id
        task_id = self.get_task_id_for_task_display_id(task_display_id)
        task_basic_details = UpdateTaskBasicDetailsDTO(
            task_id=task_id, created_by_id=task_dto.created_by_id,
            title=task_dto.title, description=task_dto.description,
            start_datetime=task_dto.start_datetime,
            due_datetime=task_dto.due_datetime, priority=task_dto.priority,
            action_type=task_dto.action_type)
        task_dto_with_db_task_id = UpdateTaskDTO(
            task_basic_details=task_basic_details,
            stage_assignee=task_dto.stage_assignee,
            gof_fields_dtos=task_dto.gof_fields_dtos)
        all_tasks_overview_details_dto = self.update_task(
            task_dto_with_db_task_id)
        task_log_dto = CreateTaskLogDTO(
            task_id=task_id, user_id=task_dto.created_by_id,
            action_id=task_dto.action_id, task_json=task_request_json)
        self._create_task_log(task_log_dto)
        return all_tasks_overview_details_dto

    def update_task(
            self, task_dto: UpdateTaskDTO) -> AllTasksOverviewDetailsDTO:
        task_id = task_dto.task_basic_details.task_id
        project_id = self._validate_task_details_and_get_project_id(task_dto)
        self._update_task_details(task_dto)
        self._update_stage_assignee_only_if_assignee_restriction_is_false(
            task_id, task_dto.stage_assignee, project_id)
        self._update_stage_assignee(task_id, task_dto.stage_assignee)
        all_tasks_overview_details_dto = self._get_task_overview_details(
            task_id, task_dto.task_basic_details.created_by_id)
        return all_tasks_overview_details_dto

    def _validate_task_details_and_get_project_id(
            self, task_dto: UpdateTaskDTO) -> str:
        task_id = task_dto.task_basic_details.task_id
        self._validate_task_id(task_id)
        task_template_id = \
            self.create_task_storage.get_template_id_for_given_task(task_id)
        from ib_tasks.constants.constants import ADHOC_TEMPLATE_ID
        is_not_adhoc_template = not task_template_id == ADHOC_TEMPLATE_ID
        action_type_is_not_no_validations = \
            task_dto.task_basic_details.action_type != \
            ActionTypes.NO_VALIDATIONS.value
        if action_type_is_not_no_validations and is_not_adhoc_template:
            self.validate_task_dates_and_priority(
                task_dto.task_basic_details.start_datetime,
                task_dto.task_basic_details.due_datetime,
                task_dto.task_basic_details.priority,
                task_dto.task_basic_details.action_type)
            self._validate_task_delay_reason_is_added_if_due_date_is_changed(
                updated_due_date=task_dto.task_basic_details.due_datetime,
                task_id=task_dto.task_basic_details.task_id,
                stage_id=task_dto.stage_assignee.stage_id)
        self._validate_stage_id(task_dto.stage_assignee.stage_id)
        project_id = self.task_storage.get_project_id_for_the_task_id(task_id)
        base_validations_interactor = GoFsDetailsValidationsInteractor(
            self.task_storage, self.gof_storage,
            self.create_task_storage, self.storage,
            self.field_storage, self.task_template_storage)
        base_validations_interactor.perform_gofs_details_validations(
            gof_fields_dtos=task_dto.gof_fields_dtos,
            user_id=task_dto.task_basic_details.created_by_id,
            task_template_id=task_template_id, project_id=project_id,
            action_type=task_dto.task_basic_details.action_type,
            stage_id=task_dto.stage_assignee.stage_id)
        if action_type_is_not_no_validations and is_not_adhoc_template:
            self._validate_all_user_permitted_fields_are_filled_or_not(
                user_id=task_dto.task_basic_details.created_by_id,
                project_id=project_id,
                gof_fields_dtos=task_dto.gof_fields_dtos,
                stage_id=task_dto.stage_assignee.stage_id,
                task_template_id=task_template_id)
        return project_id

    def _update_task_details(self, task_dto: UpdateTaskDTO):
        task_crud_interactor = TaskCrudOperationsInteractor(
            self.create_task_storage)
        task_crud_interactor.update_task(task_dto.task_basic_details)
        self._update_existing_fields_and_create_new_fields_of_task(
            task_dto, task_crud_interactor)

    def _update_existing_fields_and_create_new_fields_of_task(
            self, task_dto: UpdateTaskDTO,
            task_crud_interactor: TaskCrudOperationsInteractor
    ):
        task_id = task_dto.task_basic_details.task_id
        gof_fields_dtos = task_dto.gof_fields_dtos
        existing_gofs = self.create_task_storage.get_gofs_details_of_task(
            task_id)
        existing_fields = self.create_task_storage.get_field_id_with_task_gof_id_dtos(
            task_id)
        task_gof_dtos = self.prepare_task_gof_dtos(task_id, gof_fields_dtos)
        gofs_for_updation, gofs_for_creation = \
            self._get_updation_and_creation_gofs(task_gof_dtos, existing_gofs)
        if gofs_for_creation:
            self._create_task_gofs_and_fields(
                gofs_for_creation, task_dto, task_crud_interactor)
        if gofs_for_updation:
            self._update_task_gofs_and_fields(
                gofs_for_updation, gof_fields_dtos,
                existing_fields, task_crud_interactor)

    def _update_stage_assignee_only_if_assignee_restriction_is_false(
            self, task_id: int, stage_assignee: StageIdWithAssigneeDTO,
            project_id: str):
        from ib_tasks.adapters.service_adapter import get_service_adapter
        project_service = get_service_adapter().project_service
        projects_config = project_service.get_projects_config()
        project_config = projects_config.get(project_id)
        given_project_has_config = project_config is not None

        if given_project_has_config:
            assignee_restriction_is_true = project_config.get(
                "restrict_assignee_to_user")
            if assignee_restriction_is_true:
                return
        self._update_stage_assignee(task_id, stage_assignee)

    def _update_stage_assignee(
            self, task_id: int, stage_assignee: StageIdWithAssigneeDTO):
        update_stage_assignee_interactor = UpdateTaskStageAssigneesInteractor(
            stage_storage=self.stage_storage, task_storage=self.task_storage)
        stage_assignees = [
            StageAssigneeDTO(
                db_stage_id=stage_assignee.stage_id,
                assignee_id=stage_assignee.assignee_id,
                team_id=stage_assignee.team_id)]
        task_stage_assignee_dto = TaskIdWithStageAssigneesDTO(
            task_id=task_id, stage_assignees=stage_assignees)
        update_stage_assignee_interactor.update_task_stage_assignees(
            task_stage_assignee_dto)

    def _get_task_overview_details(self, task_id: int, user_id: str):
        from ib_tasks.interactors \
            .get_all_task_overview_with_filters_and_searches_for_user import \
            GetTasksOverviewForUserInteractor
        task_overview_interactor = GetTasksOverviewForUserInteractor(
            stage_storage=self.stage_storage, task_storage=self.task_storage,
            field_storage=self.field_storage,
            action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage,
            template_storage=self.task_template_storage
        )
        project_id = self.task_storage.get_project_id_for_the_task_id(task_id)
        self._update_task_in_elasticsearch(task_id=task_id)
        all_tasks_overview_details_dto = \
            task_overview_interactor.get_filtered_tasks_overview_for_user(
                user_id=user_id, task_ids=[task_id],
                view_type=ViewType.KANBAN.value,
                project_id=project_id)
        return all_tasks_overview_details_dto

    def _get_updation_and_creation_gofs(
            self, task_gof_dtos: List[TaskGoFWithTaskIdDTO],
            existing_gofs: List[GoFIdWithSameGoFOrderDTO]
    ):
        gofs_for_updation, gofs_for_creation = [], []
        for task_gof_dto in task_gof_dtos:
            gof_already_exists, task_gof_id = \
                self._get_task_gof_id_if_exists_for_gof(
                    task_gof_dto.gof_id, task_gof_dto.same_gof_order,
                    existing_gofs)
            task_gof_dto.task_gof_id = task_gof_id
            if gof_already_exists:
                gofs_for_updation.append(task_gof_dto)
            else:
                gofs_for_creation.append(task_gof_dto)
        return gofs_for_updation, gofs_for_creation

    def _validate_all_user_permitted_fields_are_filled_or_not(
            self, user_id: str, project_id: str,
            gof_fields_dtos: List[GoFFieldsDTO], stage_id: int,
            task_template_id: str
    ):
        user_roles = self._get_user_roles_of_project(user_id, project_id)
        permitted_gof_ids = self._get_user_writable_gof_ids_based_on_stage(
            stage_id, user_roles, task_template_id)
        self._validate_permitted_fields_filled_or_not(
            user_roles, permitted_gof_ids, gof_fields_dtos)

    @staticmethod
    def _get_user_roles_of_project(
            user_id: str, project_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service \
            .get_user_role_ids_based_on_project(user_id, project_id)
        return user_roles

    def _get_user_writable_gof_ids_based_on_stage(
            self, stage_id: int, user_roles: List[str],
            task_template_id: str
    ) -> List[str]:
        stage_permitted_gof_ids = \
            self.task_template_storage.get_template_stage_permitted_gof_ids(
                task_template_id, stage_id)
        gof_id_with_display_name_dtos = \
            self.gof_storage.get_user_write_permitted_gof_ids_in_given_gof_ids(
                user_roles, stage_permitted_gof_ids)
        user_permitted_gof_ids = [
            dto.gof_id for dto in gof_id_with_display_name_dtos]
        return user_permitted_gof_ids

    def _validate_permitted_fields_filled_or_not(
            self, user_roles: List[str], permitted_gof_ids: List[str],
            gof_fields_dtos: List[GoFFieldsDTO]):
        field_id_with_display_name_dtos = \
            self.field_storage.get_user_writable_fields_for_given_gof_ids(
                user_roles, permitted_gof_ids)
        filled_field_ids = []
        for gof_fields_dto in gof_fields_dtos:
            filled_field_ids += [
                field_value_dto.field_id
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
        self._validate_all_user_permitted_field_ids_are_filled_or_not(
            field_id_with_display_name_dtos, filled_field_ids)

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

    def _validate_task_id(
            self, task_id: int) -> Optional[InvalidTaskException]:
        invalid_task_id = \
            not self.create_task_storage.is_valid_task_id(task_id)
        if invalid_task_id:
            raise InvalidTaskException(task_id)
        return

    @staticmethod
    def _get_task_gof_id_for_field_in_task_gof_details(
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

    def _filter_task_gof_field_dtos(
            self, task_gof_field_dtos: List[TaskGoFFieldDTO],
            existing_fields: List[FieldIdWithTaskGoFIdDTO]
    ) -> Tuple[List[TaskGoFFieldDTO], List[TaskGoFFieldDTO]]:
        fields_for_updation, fields_for_creation = [], []
        for task_gof_field_dto in task_gof_field_dtos:
            field_id_already_exists = self._is_field_already_exists(
                task_gof_field_dto.field_id, task_gof_field_dto.task_gof_id,
                existing_fields)
            if field_id_already_exists:
                fields_for_updation.append(task_gof_field_dto)
            else:
                fields_for_creation.append(task_gof_field_dto)
        return fields_for_updation, fields_for_creation

    def _update_task_gofs_and_fields(
            self, task_gof_dtos_for_updation: List[TaskGoFWithTaskIdDTO],
            gof_fields_dtos: List[GoFFieldsDTO],
            existing_fields: List[FieldIdWithTaskGoFIdDTO],
            task_crud_interactor: TaskCrudOperationsInteractor
    ):
        task_gof_details_dtos = task_crud_interactor.update_task_gofs(
            task_gof_dtos_for_updation)
        task_gof_field_dtos = self.prepare_task_gof_fields_dtos(
            gof_fields_dtos, task_gof_details_dtos)
        task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation = \
            self._filter_task_gof_field_dtos(
                task_gof_field_dtos, existing_fields)
        if task_gof_field_dtos_for_updation:
            task_crud_interactor.update_task_gof_fields(
                task_gof_field_dtos_for_updation)
        if task_gof_field_dtos_for_creation:
            task_crud_interactor.create_task_gof_fields(
                task_gof_field_dtos_for_creation)

    def _create_task_gofs_and_fields(
            self, task_gof_dtos_for_creation: List[TaskGoFWithTaskIdDTO],
            task_dto: UpdateTaskDTO,
            task_crud_interactor: TaskCrudOperationsInteractor
    ):
        task_gof_details_dtos = task_crud_interactor.create_task_gofs(
            task_gof_dtos=task_gof_dtos_for_creation)
        task_gof_field_dtos = self.prepare_task_gof_fields_dtos(
            task_dto.gof_fields_dtos, task_gof_details_dtos)
        task_crud_interactor.create_task_gof_fields(task_gof_field_dtos)

    @staticmethod
    def _is_field_already_exists(
            field_id: str, task_gof_id: int,
            existing_fields: List[FieldIdWithTaskGoFIdDTO]) -> bool:
        for existing_field in existing_fields:
            field_already_exists = (
                    field_id == existing_field.field_id and
                    task_gof_id == existing_field.task_gof_id)
            if field_already_exists:
                return True
        return False

    @staticmethod
    def _get_task_gof_id_if_exists_for_gof(
            gof_id: str, same_gof_order: int,
            existing_gofs_with_same_gof_order: List[GoFIdWithSameGoFOrderDTO]
    ) -> Tuple[bool, Optional[int]]:
        for existing_gof in existing_gofs_with_same_gof_order:
            gof_already_exists = (
                    gof_id == existing_gof.gof_id and
                    same_gof_order == existing_gof.same_gof_order)
            if gof_already_exists:
                return True, existing_gof.task_gof_id
        return False, None

    def _validate_task_delay_reason_is_added_if_due_date_is_changed(
            self, updated_due_date: datetime.datetime, task_id: int,
            stage_id: int
    ) -> Optional[TaskDelayReasonIsNotUpdated]:
        existing_due_date = \
            self.create_task_storage.get_existing_task_due_date(task_id)
        now = datetime.datetime.now()

        if existing_due_date is None:
            existing_due_date = datetime.datetime.now()
        existing_due_date_is_not_expired = \
            existing_due_date > now
        if existing_due_date_is_not_expired:
            return
        due_date_has_changed = (
                existing_due_date != updated_due_date and existing_due_date
                is not None)
        if due_date_has_changed:
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
        task_display_id = \
            self.create_task_storage.get_task_display_id_for_task_id(task_id)
        stage_display_name = \
            self.stage_storage.get_stage_display_name_for_stage_id(stage_id)
        if task_delay_reason_is_not_updated:
            raise TaskDelayReasonIsNotUpdated(
                updated_due_date, task_display_id, stage_display_name)
        return

    def _validate_stage_id(self, stage_id: int) -> Optional[InvalidStageId]:
        stage_id_is_valid = self.stage_storage.check_is_stage_exists(stage_id)
        if not stage_id_is_valid:
            raise InvalidStageId(stage_id)
        return

    def _update_task_in_elasticsearch(self, task_id: int):
        from ib_tasks.interactors \
            .create_or_update_tasks_into_elasticsearch_interactor import \
            CreateOrUpdateDataIntoElasticsearchInteractor
        interactor = CreateOrUpdateDataIntoElasticsearchInteractor(
            elasticsearch_storage=self.elastic_storage,
            storage=self.create_task_storage, task_storage=self.task_storage,
            stage_storage=self.stage_storage, gof_storage=self.gof_storage,
            field_storage=self.field_storage)
        interactor.create_or_update_task_in_elasticsearch_storage(task_id)
