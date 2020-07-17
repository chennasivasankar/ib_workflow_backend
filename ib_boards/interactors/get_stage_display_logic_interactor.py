"""
Created on: 17/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import TaskStatusDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    StageDisplayLogicPresenterInterface


class InvalidStageIds(Exception):
    def __init__(self, stage_ids: List[str]):
        self.stage_ids = stage_ids


class StageDisplayLogicInteractor:
    def __init__(self):
        pass

    def get_stage_display_condition_wrapper(
            self, stage_ids: List[str], presenter: StageDisplayLogicPresenterInterface):
        try:
            task_status_dtos = self.get_stage_display_condition(
                stage_ids=stage_ids
            )
        except InvalidStageIds as error:
            return presenter.get_response_for_invalid_stage_ids(error=error)
        return presenter.get_response_for_stage_display_logic(
            task_status_dtos=task_status_dtos
        )

    def get_stage_display_condition(self, stage_ids: List[str]):
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        service_adapter.task_service.validate_stage_ids(stage_ids=stage_ids)
        stage_display_logics = service_adapter.task_service.get_stage_display_logics(
            stage_ids=stage_ids
        )
        task_status_dtos = self._get_values_from_stage_display_logic(
            stage_display_logics=stage_display_logics
        )
        return task_status_dtos

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