from typing import List

from ib_tasks.interactors.task_dtos import StatusOperandStageDTO


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
            self, stage_display_logics: List[str]) -> List[StatusOperandStageDTO]:
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
            stage_display_logic: str) -> StatusOperandStageDTO:
        import astroid
        node = astroid.extract_node(stage_display_logic)
        children = list(node.get_children())

        operator = node.ops[0][0]
        if operator == "==":
            variable = children[0].name
            stage = children[1].name
        else:
            variable = list(children[0].get_children())[1].value.name
            stage = list(children[1].get_children())[1].value.name

        return StatusOperandStageDTO(
            variable=variable,
            operator=operator,
            stage=stage
        )