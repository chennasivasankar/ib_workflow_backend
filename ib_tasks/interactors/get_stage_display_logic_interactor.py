"""
Created on: 17/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import TaskStatusDTO


class StageDisplayLogicInteractor:
    def __init__(self):
        pass

    def get_stage_display_logic_condition(self,
                                          stage_display_logics: List[str]):
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
