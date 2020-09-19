import abc
from typing import List

from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    FilterForStageDTO, FilterForFieldDTO


class ElasticStorageInterface(abc.ABC):

    def get_task_ids_filtered_on_stage_id(
            self, filter_for_stage_dto: FilterForStageDTO
    ) -> List[str]:
        pass

    def get_task_ids_filtered_on_given_field(
            self,
            filter_for_field_dto: FilterForFieldDTO
    ):
        pass
