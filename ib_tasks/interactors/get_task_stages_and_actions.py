from collections import defaultdict
from typing import List

from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO


class GetTaskStagesAndActions:
    def __init__(self, storage: FieldsStorageInterface):
        self.storage = storage

    def get_task_stages_and_actions(self, task_id: int, user_id: int) -> \
            List[StageAndActionsDetailsDTO]:
        # TODO: validate user tasks
        stage_ids = self.storage.get_task_stages(task_id)
        stage_details_dtos = self.storage.get_stage_complete_details(stage_ids)

        stage_actions_dtos = self.storage.get_actions_details(stage_ids)

        stage_actions_dtos = self._convert_to_task_complete_details_dto(
            stage_details_dtos, stage_actions_dtos, stage_ids)
        return stage_actions_dtos

    @staticmethod
    def _convert_to_task_complete_details_dto(stage_details_dtos,
                                              stage_actions_dtos,
                                              stage_ids):
        stages_dtos = {}
        for stage in stage_details_dtos:
            stages_dtos[stage.stage_id] = stage

        list_of_actions = defaultdict(list)
        for item in stage_actions_dtos:
            list_of_actions[item.stage_id].append(item)

        list_of_stage_actions = []
        for stage in stage_ids:
            list_of_stage_actions.append(
                StageAndActionsDetailsDTO(
                    stage_details_dto=stages_dtos[stage],
                    actions_dtos=list_of_actions[stage]
                ))
        return list_of_stage_actions
