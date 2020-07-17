"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""

from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, OffsetValueExceedsTotalTasksCount
from ib_boards.interactors.dtos import GetColumnTasksDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetColumnTasksPresenterInterface, TaskCompleteDetailsDTO
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
            task_complete_details_dto = self.get_column_tasks(
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
            task_complete_details_dto=task_complete_details_dto
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
        task_ids = task_ids[offset:offset + limit]
        from ib_boards.interactors.get_tasks_details_interactor import \
            GetTasksDetailsInteractor
        tasks_interactor = GetTasksDetailsInteractor(
            storage=self.storage
        )
        task_dtos, action_dtos = tasks_interactor.get_task_details(
            task_ids=task_ids
        )
        return TaskCompleteDetailsDTO(
            total_tasks=3,
            task_dtos=task_dtos,
            action_dtos=action_dtos
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

    @staticmethod
    def _get_task_ids(stage_ids):
        from ib_boards.interactors.get_stage_display_logic_interactor \
            import StageDisplayLogicInteractor
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        stage_display_logic_interactor = StageDisplayLogicInteractor()
        task_status_dtos = stage_display_logic_interactor. \
            get_stage_display_condition(
                stage_ids=stage_ids
            )
        task_ids = service_adapter.task_service.get_task_ids(
            task_status_dtos=task_status_dtos
        )
        return task_ids
