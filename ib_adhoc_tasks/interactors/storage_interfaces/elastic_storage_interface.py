import abc
from typing import List

from ib_adhoc_tasks.interactors.dtos import TaskIdsAndCountDTO, \
    TaskIdsForGroupsParameterDTO


class ElasticStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_task_ids_and_count_dto_based_on_given_groupby_and_pagination_detail(
            self,
            task_ids_for_groups_parameter_dto: TaskIdsForGroupsParameterDTO,
            stage_ids: List[str]
    ) -> TaskIdsAndCountDTO:
        pass
