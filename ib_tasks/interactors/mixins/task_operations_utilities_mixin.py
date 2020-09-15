import datetime as datetime
from typing import List, Optional

from ib_tasks.constants.enum import ViewType, Priority, ActionTypes
from ib_tasks.exceptions.datetime_custom_exceptions import \
    StartDateTimeIsRequired, DueDateTimeIsRequired, DueDateTimeHasExpired, \
    DueDateTimeWithoutStartDateTimeIsNotValid, StartDateIsAheadOfDueDate
from ib_tasks.exceptions.task_custom_exceptions import PriorityIsRequired
from ib_tasks.interactors.dtos.dtos import TaskLogDTO
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO
from ib_tasks.interactors.task_dtos import GoFFieldsDTO, CreateTaskLogDTO


class TaskOperationsUtilitiesMixin:

    def create_task_log(self, task_log_dto: TaskLogDTO):
        from ib_tasks.interactors.task_log_interactor import TaskLogInteractor
        task_log_interactor = TaskLogInteractor(
            storage=self.storage, task_storage=self.task_storage)
        create_task_log_dto = CreateTaskLogDTO(
            task_json=task_log_dto.task_request_json,
            task_id=task_log_dto.task_id, user_id=task_log_dto.user_id,
            action_id=task_log_dto.action_id)
        task_log_interactor.create_task_log(create_task_log_dto)

    @staticmethod
    def prepare_task_gof_dtos(
            task_id: int, gof_field_dtos: List[GoFFieldsDTO]
    ) -> List[TaskGoFWithTaskIdDTO]:
        task_gof_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=task_id, gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order)
            for gof_fields_dto in gof_field_dtos
        ]
        return task_gof_dtos

    def prepare_task_gof_fields_dtos(
            self, gof_fields_dtos: List[GoFFieldsDTO],
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_field_dtos = []
        for gof_fields_dto in gof_fields_dtos:
            task_gof_id = self._get_task_gof_id_for_field_in_task_gof_details(
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

    def _get_task_overview_details_dto(
            self, task_id: int, user_id: str, project_id: str
    ) -> AllTasksOverviewDetailsDTO:
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
                user_id=user_id, task_ids=[task_id],
                view_type=ViewType.KANBAN.value, project_id=project_id)
        return all_tasks_overview_details_dto

    def validate_task_dates_and_priority(
            self, start_datetime: datetime.datetime,
            due_datetime: datetime.datetime, priority: Priority,
            action_type: Optional[ActionTypes]) -> Optional[Exception]:
        self._validate_due_datetime_without_start_datetime(
            start_datetime, due_datetime)
        action_type_is_no_validations = \
            action_type == ActionTypes.NO_VALIDATIONS.value
        self._validate_priority_in_no_validations_case(
            priority, action_type_is_no_validations)
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
    def _validate_start_date_and_due_date_dependencies(
            start_date: datetime.datetime, due_date: datetime.datetime
    ) -> Optional[StartDateIsAheadOfDueDate]:
        start_date_is_ahead_of_due_date = start_date > due_date
        if start_date_is_ahead_of_due_date:
            raise StartDateIsAheadOfDueDate(start_date, due_date)
        return
