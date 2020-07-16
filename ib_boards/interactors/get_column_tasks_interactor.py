"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.adapters.dtos import TaskStatusDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetColumnTasksPresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetColumnTasksInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_tasks_wrapper(
            self, column_id: str, presenter: GetColumnTasksPresenterInterface):
        from ib_boards.exceptions.custom_exceptions import InvalidColumnId
        try:
            task_dtos, total_tasks = self.get_column_tasks(
                column_id=column_id
            )
        except InvalidColumnId:
            return presenter.get_response_for_the_invalid_column_id()
        return presenter.get_response_column_tasks(

        )

    def get_column_tasks(self, column_id):
        self.storage.validate_column_id(column_id=column_id)
        stage_ids = self.storage.get_column_display_stage_ids(
            column_id=column_id
        )

        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()

        stage_display_logics = service_adapter.task_service.get_stage_display_logics(
            stage_ids=stage_ids
        )
        task_status_dtos = self._get_values_from_stage_display_logic(
            stage_display_logics=stage_display_logics
        )
        task_ids, total_tasks= service_adapter.task_service.get_task_ids_and_number_total_tasks(
            task_status_dtos=task_status_dtos
        )

        return task_ids, total_tasks

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


