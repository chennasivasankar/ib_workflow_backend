"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Tuple

from ib_boards.constants.enum import VIEWTYPE
from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, OffsetValueExceedsTotalTasksCount, \
    UserDoNotHaveAccessToColumn, InvalidStageIds
from ib_boards.interactors.dtos import ColumnTasksParametersDTO, \
    ColumnTaskIdsDTO, FieldDTO, ActionDTO
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
            task_fields_dtos, tasks_action_dtos, total_tasks, task_ids = self.get_column_tasks(
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
        return presenter.get_response_for_column_tasks(
            task_actions_dtos=tasks_action_dtos,
            task_fields_dtos=task_fields_dtos,
            total_tasks=total_tasks,
            task_ids=task_ids
        )

    def get_column_tasks(self,
                         column_tasks_parameters: ColumnTasksParametersDTO):
        self._validate_given_data(
            column_tasks_parameters=column_tasks_parameters)
        column_id = column_tasks_parameters.column_id
        user_id = column_tasks_parameters.user_id
        view_type = column_tasks_parameters.view_type
        stage_ids = self.storage.get_column_display_stage_ids(
            column_id=column_id
        )
        task_ids_stages_dto = self._get_task_ids_with_respective_stages(
            stage_ids=stage_ids,
            column_tasks_parameters=column_tasks_parameters)

        task_fields_dtos, tasks_action_dtos = self._get_tasks_complete_details(
            task_ids_stages_dtos=task_ids_stages_dto, user_id=user_id,
            view_type=view_type
        )
        task_ids = [
            task_ids_stage_dto.task_id
            for task_ids_stage_dto in task_ids_stages_dto.task_stage_ids
        ]
        return task_fields_dtos, tasks_action_dtos, task_ids_stages_dto.total_tasks, task_ids

    @staticmethod
    def _get_tasks_complete_details(
            task_ids_stages_dtos: ColumnTaskIdsDTO,
            user_id: str, view_type: VIEWTYPE) -> \
            Tuple[List[FieldDTO], List[ActionDTO]]:
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
        return service_adapter.task_service.get_task_complete_details(
            task_details_dtos, user_id=user_id, view_type=view_type)

    def _validate_given_data(self, column_tasks_parameters):
        column_id = column_tasks_parameters.column_id
        self.storage.validate_column_id(column_id=column_id)
        offset = column_tasks_parameters.offset
        limit = column_tasks_parameters.limit
        if offset < 0:
            raise InvalidOffsetValue
        if limit < 0:
            raise InvalidLimitValue
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = column_tasks_parameters.user_id
        user_role = service_adapter.user_service.get_user_roles(
            user_id=user_id)
        self.storage.validate_user_role_with_column_roles(
            user_role=user_role,
            column_id=column_id
        )

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
