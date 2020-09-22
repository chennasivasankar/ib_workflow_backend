from typing import List

from ib_tasks.exceptions.stage_custom_exceptions import \
    InvalidStageIdsException
from ib_tasks.interactors.stage_dtos import StageIdAndNameDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


class GetStageDetails:
    def __init__(self, storage: StageStorageInterface):
        self.stage_storage = storage

    def get_stage_details(self, stage_ids: List[str]) -> \
            List[StageIdAndNameDTO]:
        self._validate_stage_ids(stage_ids)
        stage_complete_details_dtos = self.stage_storage \
            .get_stage_detail_dtos_given_stage_ids(stage_ids=stage_ids)

        stage_details_dtos = self._get_stage_details_dtos(
            stage_complete_details_dtos)
        return stage_details_dtos

    def _validate_stage_ids(self, stage_ids: List[str]):
        db_stage_ids = \
            self.stage_storage.get_valid_stage_ids_in_given_stage_ids(
                stage_ids=stage_ids)
        invalid_stage_ids = self._get_invalid_stage_ids(
            stage_ids=stage_ids, db_stage_ids=db_stage_ids)
        is_invalid_stage_ids_present = invalid_stage_ids
        if is_invalid_stage_ids_present:
            raise InvalidStageIdsException(stage_ids_dict=invalid_stage_ids)

    @staticmethod
    def _get_invalid_stage_ids(stage_ids: List[str], db_stage_ids: List[str]):
        invalid_stage_ids = [
            stage_id
            for stage_id in stage_ids if stage_id not in db_stage_ids
        ]
        return invalid_stage_ids

    def _get_stage_details_dtos(self, stage_complete_details_dtos: List[
        StageDetailsDTO]) -> List[StageIdAndNameDTO]:
        stage_details_dtos = [StageIdAndNameDTO(stage_id=stage_dto.stage_id,
                                                name=stage_dto.name)
                              for stage_dto in stage_complete_details_dtos]
        return stage_details_dtos
