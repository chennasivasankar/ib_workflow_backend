from typing import List

from ib_tasks.interactors.storage_interfaces.stage_dtos import StageDisplayDTO
from ib_tasks.interactors.task_dtos import StatusOperandStageDTO, StageDisplayLogicDTO


class StageDisplayLogicInteractor:
    def __init__(self):
        pass

    def get_stage_display_logic_condition(
            self, stage_display_dtos: List[StageDisplayDTO]
    ) -> List[StageDisplayLogicDTO]:
        task_status_dtos = self._get_values_from_stage_display_logic(
            stage_display_dtos=stage_display_dtos
        )

        return task_status_dtos

    def _get_values_from_stage_display_logic(
            self, stage_display_dtos: List[StageDisplayDTO]
    ) -> List[StageDisplayLogicDTO]:
        task_status_dtos = []
        for stage_display_dto in stage_display_dtos:
            if not stage_display_dto.display_value:
                continue
            task_status_dto = self._get_task_status_dto_from_stage_display_logic(
                stage_display_dto=stage_display_dto
            )
            task_status_dtos.append(
                task_status_dto
            )
        return task_status_dtos

    @staticmethod
    def _get_task_status_dto_from_stage_display_logic(
            stage_display_dto: StageDisplayDTO) -> StageDisplayLogicDTO:

        import astroid
        display_value = stage_display_dto.display_value
        node = astroid.extract_node(display_value)
        children = list(node.get_children())

        operator = node.ops[0][0]
        if operator == "==":
            variable = children[0].name
            stage = children[1].name
        else:
            variable = list(children[0].get_children())[1].value.name
            stage = list(children[1].get_children())[1].value.name

        display_logic_dto = StatusOperandStageDTO(
            variable=variable,
            operator=operator,
            stage=stage
        )

        return StageDisplayLogicDTO(
            current_stage=stage_display_dto.stage_id,
            display_logic_dto=display_logic_dto
        )
