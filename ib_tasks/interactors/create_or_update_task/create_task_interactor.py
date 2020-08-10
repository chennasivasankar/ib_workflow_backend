from typing import List, Optional, Union

from ib_tasks.constants.config import TIME_FORMAT
from ib_tasks.documents.elastic_task import ElasticTaskDTO, ElasticFieldDTO
from ib_tasks.exceptions.action_custom_exceptions import \
    InvalidActionException, InvalidKeyError, InvalidCustomLogicException
from ib_tasks.exceptions.datetime_custom_exceptions import \
    DueTimeHasExpiredForToday, InvalidDueTimeFormat, \
    StartDateIsAheadOfDueDate, \
    DueDateIsBehindStartDate
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
    UserActionPermissionDenied, UserBoardPermissionDenied
from ib_tasks.exceptions.stage_custom_exceptions import DuplicateStageIds, \
    InvalidDbStageIdsListException, StageIdsWithInvalidPermissionForAssignee
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskTemplateIds, \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF
from ib_tasks.interactors.create_or_update_task \
    .template_gofs_fields_base_validations import \
    TemplateGoFsFieldsBaseValidationsInteractor
from ib_tasks.interactors \
    .get_next_stages_random_assignees_of_a_task_interactor import \
    InvalidModulePathFound, InvalidMethodFound
from ib_tasks.interactors \
    .get_random_assignees_of_next_stages_and_update_in_db_interactor import \
    GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor
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
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, TaskGoFFieldDTO, TaskGoFDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import CreateTaskDTO, GoFFieldsDTO, \
    UpdateTaskDTO, FieldValuesDTO
from ib_tasks.interactors.user_action_on_task_interactor import \
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
            elastic_storage: ElasticSearchStorageInterface
    ):
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
            task_dto: CreateTaskDTO
    ):
        try:
            return self._prepare_create_task_response(
                task_dto, presenter
            )
        except InvalidTaskTemplateIds as err:
            return presenter.raise_invalid_task_template_ids(err)
        except InvalidActionException as err:
            return presenter.raise_invalid_action_id(err)
        except DuplicateSameGoFOrderForAGoF as err:
            return presenter.raise_duplicate_same_gof_orders_for_a_gof(err)
        except InvalidDueTimeFormat as err:
            return presenter.raise_invalid_due_time_format(err)
        except StartDateIsAheadOfDueDate as err:
            return presenter.raise_start_date_is_ahead_of_due_date(err)
        except DueDateIsBehindStartDate as err:
            return presenter.raise_due_date_is_behind_start_date(err)
        except DueTimeHasExpiredForToday as err:
            return presenter.raise_due_time_has_expired_for_today(err)
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
                error_obj=err
            )
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

    def _prepare_create_task_response(
            self, task_dto: CreateTaskDTO,
            presenter: CreateTaskPresenterInterface
    ):
        self.create_task(task_dto)
        return presenter.get_create_task_response()

    def create_task(self, task_dto: CreateTaskDTO):
        self._validate_task_template_id(task_dto.task_template_id)
        is_valid_action_id = self.storage.validate_action(
            action_id=task_dto.action_id)
        if not is_valid_action_id:
            raise InvalidActionException(task_dto.action_id)
        self._validate_task_details(task_dto)
        self._validate_same_gof_order(task_dto.gof_fields_dtos)
        action_type = self.action_storage.get_action_type_for_given_action_id(
            action_id=task_dto.action_id
        )
        base_validations_interactor = \
            TemplateGoFsFieldsBaseValidationsInteractor(
                self.task_storage, self.gof_storage,
                self.create_task_storage, self.storage,
                self.field_storage
            )
        base_validations_interactor. \
            perform_base_validations_for_template_gofs_and_fields(
            task_dto.gof_fields_dtos, task_dto.created_by_id,
            task_dto.task_template_id, action_type
        )
        created_task_id = \
            self.create_task_storage.create_task_with_given_task_details(
                task_dto)
        elastic_dto = self._get_elastic_task_dto(task_dto, created_task_id)
        elastic_task_id = \
            self.elastic_storage.create_task(elastic_task_dto=elastic_dto)
        self.task_storage.create_elastic_task(
            task_id=created_task_id, elastic_task_id=elastic_task_id
        )
        task_gof_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=created_task_id,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_gof_details_dtos = self.create_task_storage.create_task_gofs(
            task_gof_dtos=task_gof_dtos
        )
        task_gof_field_dtos = self._prepare_task_gof_fields_dtos(
            task_dto, task_gof_details_dtos
        )
        self.create_task_storage.create_task_gof_fields(task_gof_field_dtos)
        act_on_task_interactor = UserActionOnTaskInteractor(
            user_id=task_dto.created_by_id, board_id=None,
            task_id=created_task_id,
            action_id=task_dto.action_id,
            storage=self.storage,
            gof_storage=self.create_task_storage,
            field_storage=self.field_storage,
            stage_storage=self.stage_storage,
            task_storage=self.task_storage,
            action_storage=self.action_storage,
        )
        self.create_task_storage.set_status_variables_for_template_and_task(
            task_dto.task_template_id, created_task_id
        )
        self.create_task_storage.create_initial_task_stage(
            task_id=created_task_id, template_id=task_dto.task_template_id
        )
        act_on_task_interactor.user_action_on_task()
        set_stage_assignees_interactor = \
            GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor(
                storage=self.storage, stage_storage=self.stage_storage,
                task_storage=self.task_storage,
                action_storage=self.action_storage
            )
        set_stage_assignees_interactor \
            .get_random_assignees_of_next_stages_and_update_in_db(
            task_id=created_task_id, action_id=task_dto.action_id
        )

    def _get_elastic_task_dto(self, task_dto: CreateTaskDTO, task_id: int):

        fields_dto = self._get_fields_dto(task_dto)
        elastic_task_dto = ElasticTaskDTO(
            template_id=task_dto.task_template_id,
            task_id=task_id,
            title=task_dto.title,
            fields=fields_dto
        )
        return elastic_task_dto

    def _get_fields_dto(
            self, task_dto: CreateTaskDTO) -> List[ElasticFieldDTO]:

        fields_dto = []
        gof_fields_dtos = task_dto.gof_fields_dtos
        for gof_fields_dto in gof_fields_dtos:
            for field_value_dto in gof_fields_dto.field_values_dtos:
                fields_dto.append(self._get_elastic_field_dto(field_value_dto))

        return fields_dto

    @staticmethod
    def _get_elastic_field_dto(field_dto: FieldValuesDTO) -> ElasticFieldDTO:
        return ElasticFieldDTO(
            field_id=field_dto.field_id,
            value=field_dto.field_response
        )

    def _validate_task_template_id(
            self, task_template_id: str
    ) -> Optional[InvalidTaskTemplateIds]:
        task_template_existence = \
            self.task_template_storage.check_is_template_exists(
                template_id=task_template_id)
        if not task_template_existence:
            raise InvalidTaskTemplateIds(
                invalid_task_template_ids=[task_template_id])
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

    def _validate_same_gof_order(
            self, gof_fields_dtos: List[GoFFieldsDTO]
    ) -> Optional[DuplicateSameGoFOrderForAGoF]:
        from collections import defaultdict
        gof_with_order_dict = defaultdict(list)
        for gof_fields_dto in gof_fields_dtos:
            gof_with_order_dict[
                gof_fields_dto.gof_id].append(gof_fields_dto.same_gof_order)
        for gof_id, same_gof_orders in gof_with_order_dict.items():
            duplicate_same_gof_orders = self._get_duplicates_in_given_list(
                same_gof_orders)
            if duplicate_same_gof_orders:
                raise DuplicateSameGoFOrderForAGoF(gof_id,
                                                   duplicate_same_gof_orders)
        return

    @staticmethod
    def _get_duplicates_in_given_list(values: List) -> List:
        duplicate_values = list(
            set(
                [
                    value
                    for value in values if values.count(value) > 1
                ]
            )
        )
        duplicate_values.sort()
        return duplicate_values

    def _validate_task_details(self,
                               task_dto: Union[CreateTaskDTO, UpdateTaskDTO]):
        start_date = task_dto.start_date
        due_date = task_dto.due_date
        due_time = task_dto.due_time
        self._validate_start_date_and_due_date_dependencies(
            start_date, due_date
        )
        import datetime
        self._validate_due_time_format(due_time)
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
