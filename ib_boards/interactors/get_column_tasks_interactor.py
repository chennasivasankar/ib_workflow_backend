"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""

from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, OffsetValueExceedsTotalTasksCount, \
    UserDoNotHaveAccessToColumn, InvalidStageIds
from ib_boards.interactors.dtos import ColumnTasksParametersDTO
from ib_boards.interactors.get_tasks_details_for_the_column_ids import \
    ColumnsTasksParametersDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetColumnTasksPresenterInterface, TaskDisplayIdDTO, CompleteTasksDetailsDTO
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
            complete_tasks_details_dto = self.get_column_tasks(
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
            complete_tasks_details_dto=complete_tasks_details_dto
        )

    def get_column_tasks(self,
                         column_tasks_parameters: ColumnTasksParametersDTO):
        column_id = column_tasks_parameters.column_id
        project_id = self.storage.get_project_id_for_given_column_id(column_id)
        self._validate_given_data(
            column_tasks_parameters=column_tasks_parameters,
            project_id=project_id)
        user_id = column_tasks_parameters.user_id
        view_type = column_tasks_parameters.view_type

        column_tasks = ColumnsTasksParametersDTO(
            column_ids=[column_id],
            limit=column_tasks_parameters.limit,
            offset=column_tasks_parameters.offset,
            user_id=user_id,
            project_id=project_id,
            view_type=view_type,
            search_query=column_tasks_parameters.search_query
        )
        return self._get_column_tasks_complete_details(column_tasks)

    def _get_column_tasks_complete_details(self, column_tasks: ColumnsTasksParametersDTO):
        from ib_boards.interactors.get_tasks_details_for_the_column_ids import \
            GetColumnsTasksDetailsInteractor
        interactor = GetColumnsTasksDetailsInteractor(
            storage=self.storage
        )
        task_field_dtos, task_action_dtos, task_stage_dtos, task_ids_stages_dtos, assignees_dtos = \
            interactor.get_column_tasks_with_column_ids(
                column_tasks_parameters=column_tasks
            )
        total_tasks = task_ids_stages_dtos[0].total_tasks
        task_id_dtos = [
            TaskDisplayIdDTO(
                task_id=task_stage_dto.task_id,
                display_id=task_stage_dto.task_display_id
            )
            for task_stage_dto in task_ids_stages_dtos[0].task_stage_ids
        ]
        complete_tasks_details_dto = CompleteTasksDetailsDTO(
            task_fields_dtos=task_field_dtos,
            task_actions_dtos=task_action_dtos,
            total_tasks=total_tasks,
            task_id_dtos=task_id_dtos,
            task_stage_dtos=task_stage_dtos,
            assignees_dtos=assignees_dtos,
        )

        return complete_tasks_details_dto

    def _validate_given_data(self, column_tasks_parameters, project_id):
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
        user_role = service_adapter.user_service.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id)
        self.storage.validate_user_role_with_column_roles(
            user_role=user_role,
            column_id=column_id
        )
