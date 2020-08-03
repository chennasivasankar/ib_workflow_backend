from collections import defaultdict
from typing import List

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO


class GetTaskStagesAndActions:
    def __init__(self, storage: FieldsStorageInterface):
        self.storage = storage

    def get_task_stages_and_actions(self, task_id: int, user_id: str) -> \
            List[StageAndActionsDetailsDTO]:
        # TODO: validate user tasks

        is_valid = self.storage.validate_task_id(task_id)
        is_invalid = not is_valid
        if is_invalid:
            raise InvalidTaskIdException(task_id)

        stage_ids = self.storage.get_task_stages(task_id)
        stage_details_dtos = self.storage.get_stage_complete_details(stage_ids)

        stage_actions_dtos = self.storage.get_actions_details(stage_ids)

        stage_actions_dtos = self._convert_to_task_complete_details_dto(
            stage_details_dtos, stage_actions_dtos, stage_ids)
        return stage_actions_dtos

    def _convert_to_task_complete_details_dto(self, stage_details_dtos,
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
            stage_dto = stages_dtos[stage]
            list_of_stage_actions.append(self._get_stage_actions_dto(
                list_of_actions[stage], stage_dto))

        return list_of_stage_actions

    @staticmethod
    def _get_stage_actions_dto(actions_dtos, stage_dto):
        return StageAndActionsDetailsDTO(
                stage_id=stage_dto.stage_id,
                name=stage_dto.name,
                actions_dtos=actions_dtos
            )
