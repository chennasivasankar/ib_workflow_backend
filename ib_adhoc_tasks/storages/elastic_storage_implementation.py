from typing import List

from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO, \
    TaskOffsetAndLimitValuesDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticStorageInterface


class ElasticStorageImplementation(ElasticStorageInterface):

    def get_group_details_of_project(
            self, project_id: str, adhoc_template_id: str,
            group_by_dtos: List[GroupByDTO],
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO
    ) -> List[GroupDetailsDTO]:
        pass
