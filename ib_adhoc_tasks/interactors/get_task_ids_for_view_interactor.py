from typing import List

from ib_adhoc_tasks.interactors.dtos import GroupByDTO, \
    TaskOffsetAndLimitValuesDTO
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface\
    import \
    ElasticStorageInterface


class GetTaskIdsForViewInteractor:

    def __init__(self, elastic_storage: ElasticStorageInterface):
        self.elastic_storage = elastic_storage

    def get_task_ids_for_view(
            self, user_id: str, project_id: str, adhoc_template_id: str,
            group_by_dtos: List[GroupByDTO],
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO
    ):
        pass
