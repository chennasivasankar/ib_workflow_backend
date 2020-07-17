"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, OffsetValueExceedsTotalTasksCount, \
    UserDoNotHaveAccessToColumn
from ib_boards.interactors.dtos import ColumnTasksParametersDTO, TaskIdStageDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetColumnTasksPresenterInterface, TaskCompleteDetailsDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetColumnTasksInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_tasks_wrapper(
            self, column_tasks_parameters: ColumnTasksParametersDTO,
            presenter: GetColumnTasksPresenterInterface):
        from ib_boards.exceptions.custom_exceptions import InvalidColumnId
        try:
            task_complete_details_dto = self.get_column_tasks(
                column_tasks_parameters=column_tasks_parameters
            )
        except InvalidColumnId:
            return presenter.get_response_for_the_invalid_column_id()
        except InvalidOffsetValue:
            return presenter.get_response_for_invalid_offset()
        except InvalidLimitValue:
            return presenter.get_response_for_invalid_limit()
        except OffsetValueExceedsTotalTasksCount:
            return presenter.get_response_for_offset_exceeds_total_tasks()
        except UserDoNotHaveAccessToColumn:
            return presenter.get_response_for_user_have_no_access_for_boards()
        return presenter.get_response_column_tasks(
            task_complete_details_dto=task_complete_details_dto
        )

    def get_column_tasks(self, column_tasks_parameters: ColumnTasksParametersDTO):
        self._validate_given_data(
            column_tasks_parameters=column_tasks_parameters)
        column_id = column_tasks_parameters.column_id
        offset = column_tasks_parameters.offset
        limit = column_tasks_parameters.limit
        stage_ids = self.storage.get_column_display_stage_ids(
            column_id=column_id
        )
        task_ids_stages_dtos = self._get_task_ids_with_respective_stages(stage_ids=stage_ids)
        total_tasks = len(task_ids_stages_dtos)
        if offset >= total_tasks:
            raise OffsetValueExceedsTotalTasksCount
        task_ids_stages_dtos = task_ids_stages_dtos[offset:offset + limit]
        return self._get_tasks_complete_details(task_ids_stages_dtos, column_id)

    def _get_tasks_complete_details(
            self, task_ids_stages_dtos: List[TaskIdStageDTO], column_id: str):
        from ib_boards.interactors.get_tasks_details_interactor import \
            GetTasksDetailsInteractor
        tasks_interactor = GetTasksDetailsInteractor(
            storage=self.storage
        )
        task_dtos, action_dtos = tasks_interactor.get_task_details(
            tasks_parameters=task_ids_stages_dtos, column_id=column_id
        )
        return TaskCompleteDetailsDTO(
            total_tasks=3,
            task_dtos=task_dtos,
            action_dtos=action_dtos
        )

    def _validate_given_data(self, column_tasks_parameters):
        column_id = column_tasks_parameters.column_id
        self.storage.validate_column_id(column_id=column_id)
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = column_tasks_parameters.user_id
        print('user_id{}'.format(user_id))
        user_role = service_adapter.user_service.get_user_role(user_id=user_id)
        self.storage.validate_user_role_with_column_roles(user_role=user_role)
        offset = column_tasks_parameters.offset
        limit = column_tasks_parameters.limit
        if offset < 0:
            raise InvalidOffsetValue
        if limit < 0:
            raise InvalidLimitValue

    @staticmethod
    def _get_task_ids_with_respective_stages(stage_ids):
        from ib_boards.interactors.get_stage_display_logic_interactor \
            import StageDisplayLogicInteractor
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        stage_display_logic_interactor = StageDisplayLogicInteractor()
        task_status_dtos = stage_display_logic_interactor. \
            get_stage_display_logic_condition(
                stage_ids=stage_ids
            )
        task_ids_stages_dtos = service_adapter.task_service.\
            get_task_ids_with_respective_stages(
                task_status_dtos=task_status_dtos
            )
        return task_ids_stages_dtos
