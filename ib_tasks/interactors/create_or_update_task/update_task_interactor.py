from typing import Optional, List, Union

from ib_tasks.constants.config import TIME_FORMAT
from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.datetime_custom_exceptions import \
    DueTimeHasExpiredForToday, InvalidDueTimeFormat, \
    StartDateIsAheadOfDueDate, \
    DueDateIsBehindStartDate, DueDateHasExpired
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
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsWithInvalidPermissionForAssignee, InvalidStageId
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException, \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF, InvalidTaskDisplayId
from ib_tasks.interactors.create_or_update_task. \
    template_gofs_fields_base_validations import \
    TemplateGoFsFieldsBaseValidationsInteractor
from ib_tasks.interactors.field_dtos import FieldIdWithTaskGoFIdDTO
from ib_tasks.interactors.gofs_dtos import GoFIdWithSameGoFOrderDTO
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.presenter_interfaces.update_task_presenter import \
    UpdateTaskPresenterInterface
from ib_tasks.interactors.stages_dtos import StageAssigneeDTO, \
    TaskIdWithStageAssigneesDTO
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
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import UpdateTaskDTO, CreateTaskDTO, \
    UpdateTaskWithTaskDisplayIdDTO
from ib_tasks.interactors.update_task_stage_assignees_interactor import \
    UpdateTaskStageAssigneesInteractor


class UpdateTaskInteractor(GetTaskIdForTaskDisplayIdMixin):

    def __init__(
            self, task_storage: TaskStorageInterface,
            gof_storage: GoFStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface,
            stage_storage: StageStorageInterface,
            elastic_storage: ElasticSearchStorageInterface
    ):
        self.gof_storage = gof_storage
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.storage = storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.elastic_storage = elastic_storage

    def update_task_wrapper(
            self, presenter: UpdateTaskPresenterInterface,
            task_dto: UpdateTaskWithTaskDisplayIdDTO
    ):
        try:
            return self._prepare_update_task_response(
                task_dto, presenter)
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id(err)
        except InvalidTaskException as err:
            return presenter.raise_invalid_task_id(err)
        except InvalidStageId as err:
            return presenter.raise_invalid_stage_id(err)
        except InvalidDueTimeFormat as err:
            return presenter.raise_invalid_due_time_format(err)
        except DueDateHasExpired as err:
            return presenter.raise_due_date_has_expired(err)
        except StartDateIsAheadOfDueDate as err:
            return presenter.raise_start_date_is_ahead_of_due_date(err)
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
        except StageIdsWithInvalidPermissionForAssignee as err:
            return presenter. \
                raise_stage_ids_with_invalid_permission_for_assignee_exception(
                err)

    def _prepare_update_task_response(
            self, task_dto: UpdateTaskWithTaskDisplayIdDTO,
            presenter: UpdateTaskPresenterInterface
    ):
        self.update_task_with_task_display_id(task_dto)
        return presenter.get_update_task_response()

    def update_task_with_task_display_id(
            self, task_dto: UpdateTaskWithTaskDisplayIdDTO):
        task_id = self.get_task_id_for_task_display_id(
            task_dto.task_display_id)
        task_dto_with_db_task_id = UpdateTaskDTO(
            task_id=task_id, created_by_id=task_dto.created_by_id,
            title=task_dto.title, description=task_dto.description,
            start_date=task_dto.start_date, due_date=task_dto.due_date,
            due_time=task_dto.due_time, priority=task_dto.priority,
            stage_assignee=task_dto.stage_assignee,
            gof_fields_dtos=task_dto.gof_fields_dtos
        )
        self.update_task(task_dto_with_db_task_id)

    def update_task(self, task_dto: UpdateTaskDTO, action_type=None):
        task_id = task_dto.task_id
        self._validate_task_id(task_id)
        self._validate_stage_id(task_dto.stage_assignee.stage_id)
        task_template_id = \
            self.create_task_storage.get_template_id_for_given_task(task_id)
        self._validate_task_details(task_dto, action_type)
        base_validations_interactor = \
            TemplateGoFsFieldsBaseValidationsInteractor(
                self.task_storage, self.gof_storage,
                self.create_task_storage, self.storage,
                self.field_storage
            )
        base_validations_interactor \
            .perform_base_validations_for_template_gofs_and_fields(
            task_dto.gof_fields_dtos, task_dto.created_by_id,
            task_template_id, action_type=action_type)
        self.create_task_storage.update_task_with_given_task_details(
            task_dto=task_dto)
        existing_gofs = \
            self.create_task_storage \
                .get_gof_ids_with_same_gof_order_related_to_a_task(task_id)
        existing_fields = \
            self.create_task_storage \
                .get_field_ids_with_task_gof_id_related_to_given_task(
                task_id)
        task_gof_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=task_id,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_gof_dtos_for_updation, task_gof_dtos_for_creation = [], []
        for task_gof_dto in task_gof_dtos:
            gof_already_exists = \
                self._is_gof_already_exists(
                    task_gof_dto.gof_id, task_gof_dto.same_gof_order,
                    existing_gofs
                )
            if gof_already_exists:
                task_gof_dtos_for_updation.append(task_gof_dto)
            else:
                task_gof_dtos_for_creation.append(task_gof_dto)
        if task_gof_dtos_for_updation:
            self._update_task_gofs(
                task_gof_dtos_for_updation, task_dto, existing_fields)
        if task_gof_dtos_for_creation:
            self._create_task_gofs(task_gof_dtos_for_creation, task_dto)
        update_stage_assignee_interactor = UpdateTaskStageAssigneesInteractor(
            stage_storage=self.stage_storage, task_storage=self.task_storage)
        stage_assignees = [
            StageAssigneeDTO(
                db_stage_id=task_dto.stage_assignee.stage_id,
                assignee_id=task_dto.stage_assignee.assignee_id,
                team_id=task_dto.stage_assignee.team_id
            )
        ]
        task_stage_assignee_dto = TaskIdWithStageAssigneesDTO(
            task_id=task_dto.task_id, stage_assignees=stage_assignees)
        update_stage_assignee_interactor.update_task_stage_assignees(
            task_stage_assignee_dto)

    def _validate_task_id(
            self, task_id: int) -> Optional[InvalidTaskException]:
        invalid_task_id = \
            not self.create_task_storage.is_valid_task_id(task_id)
        if invalid_task_id:
            raise InvalidTaskException(task_id)
        return

    def _prepare_task_gof_fields_dtos(
            self, task_dto: UpdateTaskDTO,
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_field_dtos = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            task_gof_id = self._get_task_gof_id_for_field_in_task_gof_details(
                gof_fields_dto.gof_id, gof_fields_dto.same_gof_order,
                task_gof_details_dtos)
            if task_gof_id is not None:
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
    ) -> (List[TaskGoFFieldDTO], List[TaskGoFFieldDTO]):
        task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation = \
            [], []
        for task_gof_field_dto in task_gof_field_dtos:
            field_id_already_exists = self._is_field_already_exists(
                task_gof_field_dto.field_id, task_gof_field_dto.task_gof_id,
                existing_fields
            )
            if field_id_already_exists:
                task_gof_field_dtos_for_updation.append(task_gof_field_dto)
            else:
                task_gof_field_dtos_for_creation.append(task_gof_field_dto)
        return (
            task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation
        )

    def _update_task_gofs(
            self, task_gof_dtos_for_updation: List[TaskGoFWithTaskIdDTO],
            task_dto: UpdateTaskDTO,
            existing_fields: List[FieldIdWithTaskGoFIdDTO]
    ):
        task_gof_details_dtos = \
            self.create_task_storage.update_task_gofs(
                task_gof_dtos_for_updation)
        task_gof_field_dtos = self._prepare_task_gof_fields_dtos(
            task_dto, task_gof_details_dtos)
        task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation = \
            self._filter_task_gof_field_dtos(
                task_gof_field_dtos, existing_fields)
        if task_gof_field_dtos_for_updation:
            self.create_task_storage.update_task_gof_fields(
                task_gof_field_dtos_for_updation)

        if task_gof_field_dtos_for_creation:
            self.create_task_storage.create_task_gof_fields(
                task_gof_field_dtos_for_creation)

    def _create_task_gofs(
            self, task_gof_dtos_for_creation: List[TaskGoFWithTaskIdDTO],
            task_dto: UpdateTaskDTO
    ):
        task_gof_details_dtos = \
            self.create_task_storage.create_task_gofs(
                task_gof_dtos_for_creation
            )
        task_gof_field_dtos = \
            self._prepare_task_gof_fields_dtos(
                task_dto, task_gof_details_dtos
            )
        self.create_task_storage.create_task_gof_fields(
            task_gof_field_dtos
        )

    @staticmethod
    def _is_field_already_exists(
            field_id: str, task_gof_id: int,
            existing_fields: List[FieldIdWithTaskGoFIdDTO]
    ) -> bool:
        for existing_field in existing_fields:
            field_already_exists = (
                    field_id == existing_field.field_id and
                    task_gof_id == existing_field.task_gof_id)
            if field_already_exists:
                return True
        return False

    @staticmethod
    def _is_gof_already_exists(
            gof_id: str, same_gof_order: int,
            existing_gofs_with_same_gof_order: List[GoFIdWithSameGoFOrderDTO]
    ) -> bool:
        for existing_gof in existing_gofs_with_same_gof_order:
            gof_already_exists = (
                    gof_id == existing_gof.gof_id and
                    same_gof_order == existing_gof.same_gof_order)
            if gof_already_exists:
                return True
        return False

    def _validate_task_details(
            self, task_dto: Union[CreateTaskDTO, UpdateTaskDTO],
            action_type: Optional[ActionTypes]
    ):
        start_date = task_dto.start_date
        due_date = task_dto.due_date
        due_time = task_dto.due_time
        dates_validation_is_not_required = False
        action_type_is_no_validations = action_type == \
                                        ActionTypes.NO_VALIDATIONS.value
        if action_type_is_no_validations:
            empty_values_given = (
                    not start_date or not due_date or not due_time)
            if empty_values_given:
                dates_validation_is_not_required = True
        if dates_validation_is_not_required:
            return
        self._validate_start_date_and_due_date_dependencies(
            start_date, due_date)
        import datetime
        self._validate_due_time_format(due_time)
        due_date_is_expired = (due_date < datetime.datetime.today().date())
        if due_date_is_expired:
            raise DueDateHasExpired(due_date)
        due_time_obj = datetime.datetime.strptime(due_time, TIME_FORMAT).time()
        now_time = datetime.datetime.now().time()
        due_time_is_expired_if_due_date_is_today = (
                due_date == datetime.datetime.today().date() and
                due_time_obj < now_time)
        if due_time_is_expired_if_due_date_is_today:
            raise DueTimeHasExpiredForToday(due_time)

    @staticmethod
    def _validate_due_time_format(due_time: str):
        import datetime
        try:
            datetime.datetime.strptime(due_time, TIME_FORMAT)
        except ValueError:
            raise InvalidDueTimeFormat(due_time)

    @staticmethod
    def _validate_start_date_and_due_date_dependencies(start_date,
                                                       due_date):
        start_date_is_ahead_of_due_date = start_date > due_date
        if start_date_is_ahead_of_due_date:
            raise StartDateIsAheadOfDueDate(start_date, due_date)
        due_date_is_behind_start_date = due_date < start_date
        if due_date_is_behind_start_date:
            raise DueDateIsBehindStartDate(due_date, start_date)

    def _validate_stage_id(self, stage_id: int) -> Optional[InvalidStageId]:
        stage_id_is_valid = self.stage_storage.check_is_stage_exists(stage_id)
        if not stage_id_is_valid:
            raise InvalidStageId(stage_id)
        return
