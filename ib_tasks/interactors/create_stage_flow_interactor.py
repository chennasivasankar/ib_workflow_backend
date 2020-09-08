from collections import defaultdict
from typing import List, Dict

from ib_tasks.exceptions.action_custom_exceptions import InvalidStageActionException
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageIdsException
from ib_tasks.interactors.storage_interfaces.action_storage_interface import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import CreateStageFlowDTO, StageIdActionNameDTO, \
    StageActionIdDTO, StageFlowWithActionIdDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface


class CreateStageFlowInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 action_storage: ActionStorageInterface):
        self.stage_storage = stage_storage
        self.action_storage = action_storage

    def create_stage_flows(self, stage_flow_dtos: List[CreateStageFlowDTO]):

        stage_ids = self._get_stage_ids(stage_flow_dtos)
        self._validate_stage_ids(stage_ids)
        stage_id_action_dtos = self._get_stage_id_action_name_dtos(stage_flow_dtos)
        stage_action_id_dtos = self.action_storage \
            .get_stage_action_name_dtos(stage_id_action_dtos)
        stage_action_name_dict = self._get_stage_action_name_dict(stage_action_id_dtos)
        self._validate_stage_actions(stage_flow_dtos, stage_action_name_dict)
        self._create_stage_flows(stage_flow_dtos, stage_action_name_dict)

    def _create_stage_flows(
            self, stage_flow_dtos: List[CreateStageFlowDTO],
            stage_action_name_dict: Dict[str, StageActionIdDTO]
    ):
        create_stage_flow_dtos = []
        for stage_flow_dto in stage_flow_dtos:
            key = stage_flow_dto.previous_stage_id + stage_flow_dto.action_name
            create_stage_flow_dtos.append(
                StageFlowWithActionIdDTO(
                    previous_stage_id=stage_flow_dto.previous_stage_id,
                    action_id=stage_action_name_dict[key].action_id,
                    next_stage_id=stage_flow_dto.next_stage_id
                )
            )
        if create_stage_flow_dtos:
            self.stage_storage.create_stage_flows(
                stage_flow_dtos=create_stage_flow_dtos
            )

    @staticmethod
    def _validate_stage_actions(
            stage_flow_dtos: List[CreateStageFlowDTO],
            stage_action_name_dict: Dict[str, StageActionIdDTO]
    ):
        invalid_stage_action = defaultdict(list)
        for stage_flow_dto in stage_flow_dtos:
            key = stage_flow_dto.previous_stage_id + stage_flow_dto.action_name
            if key not in stage_action_name_dict:
                stage_id = stage_flow_dto.previous_stage_id
                action_name = stage_flow_dto.action_name
                invalid_stage_action[stage_id].append(action_name)

        if invalid_stage_action:
            import json
            stage_actions = json.dumps(invalid_stage_action)
            raise InvalidStageActionException(
                stage_actions=stage_actions
            )

    @staticmethod
    def _get_stage_action_name_dict(stage_action_dtos: List[StageActionIdDTO]):

        from collections import defaultdict
        stage_action_name_dict = defaultdict()
        for stage_action_dto in stage_action_dtos:
            key = stage_action_dto.stage_id + stage_action_dto.action_name
            stage_action_name_dict[key] = stage_action_dto

        return stage_action_name_dict

    @staticmethod
    def _get_stage_id_action_name_dtos(
            stage_flow_dtos: List[CreateStageFlowDTO]):

        return [
            StageIdActionNameDTO(
                stage_id=stage_flow_dto.previous_stage_id,
                action_name=stage_flow_dto.action_name
            )
            for stage_flow_dto in stage_flow_dtos
        ]

    def _validate_stage_ids(self, stage_ids: List[str]):
        valid_stage_ids = self.stage_storage \
            .get_valid_stage_ids_in_given_stage_ids(stage_ids=stage_ids)
        invalid_stage_ids = [
            stage_id
            for stage_id in stage_ids
            if stage_id not in valid_stage_ids
        ]
        if invalid_stage_ids:
            import json
            stage_ids_dict = json.dumps(
                {"invalid_stage_ids": invalid_stage_ids}
            )
            raise InvalidStageIdsException(stage_ids_dict=stage_ids_dict)

    @staticmethod
    def _get_stage_ids(stage_flow_dtos: List[CreateStageFlowDTO]):

        stage_ids = []
        for stage_flow_dto in stage_flow_dtos:
            stage_ids.append(stage_flow_dto.previous_stage_id)
            stage_ids.append(stage_flow_dto.next_stage_id)
        return stage_ids