import datetime
from typing import Dict, List, Optional, Union

from ib_tasks.constants.config import DATE_FORMAT
from ib_tasks.constants.enum import Priority
from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds
from ib_tasks.interactors.create_or_update_task.create_task_interactor import \
    CreateTaskInteractor
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldIdWithGoFIdDTO
from ib_tasks.interactors.task_dtos import FieldValuesDTO, GoFFieldsDTO, \
    CreateTaskDTO
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.storages.create_or_update_task_storage_implementation import \
    CreateOrUpdateTaskStorageImplementation
from ib_tasks.storages.elasticsearch_storage_implementation import \
    ElasticSearchStorageImplementation
from ib_tasks.storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ib_tasks.storages.gof_storage_implementation import \
    GoFStorageImplementation
from ib_tasks.storages.storage_implementation import StorageImplementation, \
    StagesStorageImplementation
from ib_tasks.storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ib_tasks.storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation
from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation
from ib_tasks.utils.get_google_sheet import get_google_sheet

TASK_DETAILS_KEYS = [
    "title*", "description", "start_date*", "due_date*", "priority*"
]


class InvalidPriorityForTask(Exception):
    def __init__(self, title: str, priority: str, valid_priorities: List[str]):
        self.title = title
        self.priority = priority
        self.valid_priorities = valid_priorities


class TitleCanNotBeEmpty(Exception):
    pass


class StartDateCanNotBeEmpty(Exception):
    def __init__(self, title: str):
        self.title = title


class InvalidStartDateFormatForTask(Exception):
    def __init__(self, title: str, start_date: str):
        self.title = title
        self.start_date = start_date


class DueDateCanNotBeEmpty(Exception):
    def __init__(self, title: str):
        self.title = title


class InvalidDueDateFormatForTask(Exception):
    def __init__(self, title: str, due_date: str):
        self.title = title
        self.due_date = due_date


class PriorityCanNotBeEmpty(Exception):
    def __init__(self, title: str):
        self.title = title


class PopulateBulkTasks:

    def __init__(
            self, project_id: str, task_template_id: str, action_id: int,
            user_id: str):
        self.user_id = user_id
        self.action_id = action_id
        self.task_template_id = task_template_id
        self.project_id = project_id
        self.task_storage = TasksStorageImplementation()
        self.field_storage = FieldsStorageImplementation()
        self.gof_storage = GoFStorageImplementation()
        self.task_template_storage = TaskTemplateStorageImplementation()
        self.create_task_storage = CreateOrUpdateTaskStorageImplementation()
        self.storage = StorageImplementation()
        self.fields_storage = FieldsStorageImplementation()
        self.stages_storage = StagesStorageImplementation()
        self.action_storage = ActionsStorageImplementation()
        self.elastic_storage = ElasticSearchStorageImplementation()
        self.task_stage_storage = TaskStageStorageImplementation()

    def populate_bulk_tasks(self):
        sheet = get_google_sheet("OTG Model Bulk Tasks Creation")
        worksheet = sheet.worksheet("Task Primary Information")
        col_headers = worksheet.row_values(1)
        self._validate_field_ids(col_headers)
        all_tasks_details = worksheet.get_all_records()
        create_task_dtos = self._prepare_create_task_dtos(all_tasks_details)
        interactor = CreateTaskInteractor(
            task_storage=self.task_storage, gof_storage=self.gof_storage,
            task_template_storage=self.task_template_storage,
            create_task_storage=self.create_task_storage, storage=self.storage,
            field_storage=self.field_storage,
            stage_storage=self.stages_storage,
            action_storage=self.action_storage,
            elastic_storage=self.elastic_storage,
            task_stage_storage=self.task_stage_storage)
        for create_task_dto in create_task_dtos:
            interactor.create_task(create_task_dto)
        return

    def _prepare_create_task_dtos(self, all_tasks_details: List[Dict]):
        create_task_dtos = []
        for task_details in all_tasks_details:
            title = task_details.pop("title*")
            description = task_details.pop("description")
            start_date = task_details.pop("start_date*")
            due_date = task_details.pop("due_date*")
            priority = task_details.pop("priority*")
            self._validate_for_mandatory_fields(
                title, start_date, due_date, priority)
            due_time = "12:00:00"
            start_date = datetime.datetime.strptime(start_date,
                                                    DATE_FORMAT).date()
            due_date = datetime.datetime.strptime(due_date, DATE_FORMAT).date()
            self._validate_priority_value(title, priority)
            priority = priority.upper()
            gof_fields_dtos = self._prepare_gof_fields_dtos(task_details)
            create_task_dtos.append(
                CreateTaskDTO(
                    project_id=self.project_id,
                    task_template_id=self.task_template_id,
                    created_by_id=self.user_id, action_id=self.action_id,
                    title=title, description=description,
                    start_date=start_date, due_date=due_date,
                    due_time=due_time, priority=priority,
                    gof_fields_dtos=gof_fields_dtos))
        return create_task_dtos

    def _prepare_gof_fields_dtos(
            self, task_details: Dict) -> List[GoFFieldsDTO]:
        field_values_dtos = [
            FieldValuesDTO(field_id=field_id,
                           field_response=field_response)
            for field_id, field_response in task_details.items()
        ]
        field_ids = [
            field_values_dto.field_id
            for field_values_dto in field_values_dtos
        ]
        field_id_with_gof_id_dtos = \
            self.field_storage.get_gof_ids_for_given_field_ids(field_ids)
        gof_ids = [
            field_id_with_gof_id_dto.gof_id
            for field_id_with_gof_id_dto in field_id_with_gof_id_dtos
        ]
        from collections import defaultdict
        gof_fields_dict = defaultdict()
        for gof_id in gof_ids:
            gof_field_dto = GoFFieldsDTO(
                gof_id=gof_id, same_gof_order=0, field_values_dtos=[])
            gof_fields_dict[gof_id] = gof_field_dto
        for field_values_dto in field_values_dtos:
            field_gof_id = self._get_field_gof_id(
                field_values_dto.field_id, field_id_with_gof_id_dtos)
            gof_fields_dict[field_gof_id].field_values_dtos.append(
                field_values_dto)
        gof_fields_dtos = [
            gof_fields_dto for gof_id, gof_fields_dto in
            gof_fields_dict.items()]
        return gof_fields_dtos

    @staticmethod
    def _get_field_gof_id(
            field_id: str, field_id_with_gof_id_dtos: List[FieldIdWithGoFIdDTO]
    ) -> Optional[str]:
        for field_id_with_gof_id_dto in field_id_with_gof_id_dtos:
            field_id_matched = field_id == field_id_with_gof_id_dto.field_id
            if field_id_matched:
                return field_id_with_gof_id_dto.gof_id
        return

    @staticmethod
    def _validate_priority_value(
            title: str, priority: str) -> Optional[InvalidPriorityForTask]:
        valid_priority_values = [priority.value for priority in Priority]
        invalid_priority_value_given = \
            priority.upper() not in valid_priority_values
        if invalid_priority_value_given:
            raise InvalidPriorityForTask(
                title, priority, valid_priority_values)
        return

    def _validate_for_mandatory_fields(
            self, title, start_date, due_date, priority):
        self._validate_for_empty_title(title)
        self._validate_start_date(title, start_date)
        self._validate_due_date(title, due_date)
        self._validate_for_emtpy_priority(title, priority)

    @staticmethod
    def _validate_for_empty_title(title):
        empty_title_given = not title
        if empty_title_given:
            raise TitleCanNotBeEmpty()
        return

    def _validate_start_date(
            self, title, start_date
    ) -> Union[None, StartDateCanNotBeEmpty, InvalidStartDateFormatForTask]:
        emtpy_start_date_given = not start_date
        if emtpy_start_date_given:
            raise StartDateCanNotBeEmpty(title)
        invalid_start_date_format = not self._check_date_format(start_date)
        if invalid_start_date_format:
            raise InvalidStartDateFormatForTask(title, start_date)
        return

    def _validate_due_date(
            self, title, due_date
    ) -> Union[None, DueDateCanNotBeEmpty, InvalidDueDateFormatForTask]:
        emtpy_due_date_given = not due_date
        if emtpy_due_date_given:
            raise DueDateCanNotBeEmpty(title)
        invalid_due_date_format = not self._check_date_format(due_date)
        if invalid_due_date_format:
            raise InvalidDueDateFormatForTask(title, due_date)
        return

    @staticmethod
    def _check_date_format(given_date) -> bool:
        try:
            datetime.datetime.strptime(given_date, DATE_FORMAT).date()
        except ValueError:
            return False
        return True

    @staticmethod
    def _validate_for_emtpy_priority(title, priority):
        empty_priority_given = not priority
        if empty_priority_given:
            raise PriorityCanNotBeEmpty(title)
        return

    def _validate_field_ids(
            self, col_headers: List[str]) -> Optional[InvalidFieldIds]:
        field_ids = [
            col_header
            for col_header in col_headers
            if col_header not in TASK_DETAILS_KEYS]
        valid_field_ids = self.task_storage.get_existing_field_ids(field_ids)
        invalid_field_ids = sorted(list(set(field_ids) - set(valid_field_ids)))
        if invalid_field_ids:
            raise InvalidFieldIds(invalid_field_ids)
        return
