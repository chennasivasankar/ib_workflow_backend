"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, OffsetValueExceedsTotalTasksCount, \
    UserDoNotHaveAccessToColumn, InvalidStageIds
from ib_boards.interactors.dtos import ColumnTasksParametersDTO, \
    ColumnTaskIdsDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetColumnTasksPresenterInterface
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
            task_complete_details_dto, total_tasks= self.get_column_tasks(
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
            return presenter.get_response_for_user_have_no_access_for_column()
        except InvalidStageIds as error:
            return presenter.get_response_for_invalid_stage_ids(error=error)
        return presenter.get_response_column_tasks(
            task_complete_details_dto=task_complete_details_dto
        )

    def get_column_tasks(self,
                         column_tasks_parameters: ColumnTasksParametersDTO):
        self._validate_given_data(
            column_tasks_parameters=column_tasks_parameters)
        column_id = column_tasks_parameters.column_id
        stage_ids = self.storage.get_column_display_stage_ids(
            column_id=column_id
        )
        task_ids_stages_dto = self._get_task_ids_with_respective_stages(
            stage_ids=stage_ids,
            column_tasks_parameters=column_tasks_parameters)

        task_complete_details = self._get_tasks_complete_details(
            task_ids_stages_dto
        )
        return task_complete_details, task_ids_stages_dto.total_tasks

    @staticmethod
    def _get_tasks_complete_details(
            task_ids_stages_dtos: ColumnTaskIdsDTO):
        task_details_dtos = []
        for task_ids_stages_dto in task_ids_stages_dtos.task_stage_ids:
            from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
            task_details_dtos.append(
                GetTaskDetailsDTO(
                    task_id=task_ids_stages_dto.task_id,
                    stage_id=task_ids_stages_dto.stage_id
                )
            )
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        return service_adapter.task_service.get_task_details_dtos(
            task_details_dtos)

    def _validate_given_data(self, column_tasks_parameters):
        column_id = column_tasks_parameters.column_id
        self.storage.validate_column_id(column_id=column_id)
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = column_tasks_parameters.user_id
        user_role = service_adapter.user_service.get_user_roles(
            user_id=user_id)
        self.storage.validate_user_role_with_column_roles(user_role=user_role)
        offset = column_tasks_parameters.offset
        limit = column_tasks_parameters.limit
        if offset < 0:
            raise InvalidOffsetValue
        if limit < 0:
            raise InvalidLimitValue

    @staticmethod
    def _get_task_ids_with_respective_stages(
            stage_ids: List[str],
            column_tasks_parameters: ColumnTasksParametersDTO) -> ColumnTaskIdsDTO:
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO
        task_config_dto = [
            TaskDetailsConfigDTO(
                unique_key=column_tasks_parameters.column_id,
                stage_ids=stage_ids,
                offset=column_tasks_parameters.offset,
                limit=column_tasks_parameters.limit
            )
        ]
        task_ids_details = service_adapter.task_service.get_task_ids_for_stage_ids(
            task_config_dtos=task_config_dto
        )
        return task_ids_details[0]
