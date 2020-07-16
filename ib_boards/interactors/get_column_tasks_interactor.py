"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.adapters.dtos import TaskStatusDTO
from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, OffsetValueExceedsTotalTasksCount
from ib_boards.interactors.dtos import GetColumnTasksDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetColumnTasksPresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetColumnTasksInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_tasks_wrapper(
            self, get_column_tasks_dto: GetColumnTasksDTO,
            presenter: GetColumnTasksPresenterInterface):
        from ib_boards.exceptions.custom_exceptions import InvalidColumnId
        try:
            task_dtos, total_tasks = self.get_column_tasks(
                get_column_tasks_dto=get_column_tasks_dto
            )
        except InvalidColumnId:
            return presenter.get_response_for_the_invalid_column_id()
        except InvalidOffsetValue:
            return presenter.get_response_for_invalid_offset()
        except InvalidLimitValue:
            return presenter.get_response_for_invalid_limit()
        except OffsetValueExceedsTotalTasksCount:
            return presenter.get_response_for_offset_exceeds_total_tasks()
        return presenter.get_response_column_tasks(
            task_dtos=task_dtos, total_tasks=total_tasks
        )

    def get_column_tasks(self, get_column_tasks_dto: GetColumnTasksDTO):
        self._validate_given_data(get_column_tasks_dto=get_column_tasks_dto)
        column_id = get_column_tasks_dto.column_id
        offset = get_column_tasks_dto.offset
        limit = get_column_tasks_dto.limit
        stage_ids = self.storage.get_column_display_stage_ids(
            column_id=column_id
        )
        task_ids = self._get_task_ids(stage_ids=stage_ids)
        total_tasks = len(task_ids)
        if offset >= total_tasks:
            raise OffsetValueExceedsTotalTasksCount
        task_ids = task_ids[offset:offset+limit]
        from ib_boards.interactors.get_tasks_details_interactor import \
            GetTasksDetailsInteractor
        tasks_interactor = GetTasksDetailsInteractor(
            storage=self.storage
        )
        task_dtos = tasks_interactor.get_task_details(task_ids=task_ids)
        return task_dtos, total_tasks

    def _get_values_from_stage_display_logic(
            self, stage_display_logics: List[str]) -> List[TaskStatusDTO]:
        task_status_dtos = []
        for stage_display_logic in stage_display_logics:
            task_status_dto = self._get_task_status_dto_from_stage_display_logic(
                stage_display_logic=stage_display_logic
            )
            task_status_dtos.append(
                task_status_dto
            )
        return task_status_dtos

    @staticmethod
    def _get_task_status_dto_from_stage_display_logic(
            stage_display_logic: str) -> TaskStatusDTO:

        import astroid
        node = astroid.extract_node(stage_display_logic)
        children = node.get_children()
        children_values = []
        for item in children:
            children_values.append(
                item.name
            )
        return TaskStatusDTO(
            status=children_values[0],
            stage=children_values[1]
        )

    def _validate_given_data(self, get_column_tasks_dto):
        column_id = get_column_tasks_dto.column_id
        self.storage.validate_column_id(column_id=column_id)
        offset = get_column_tasks_dto.offset
        limit = get_column_tasks_dto.limit
        if offset < 0:
            raise InvalidOffsetValue
        if limit < 0:
            raise InvalidLimitValue

    def _get_task_ids(self, stage_ids):
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()

        stage_display_logics = service_adapter.task_service.get_stage_display_logics(
            stage_ids=stage_ids
        )
        task_status_dtos = self._get_values_from_stage_display_logic(
            stage_display_logics=stage_display_logics
        )
        task_ids = service_adapter.task_service. \
            get_task_ids_and_number_total_tasks(
            task_status_dtos=task_status_dtos
        )
        return task_ids
