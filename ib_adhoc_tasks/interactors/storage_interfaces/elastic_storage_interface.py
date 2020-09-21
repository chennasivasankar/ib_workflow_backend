import abc
from dataclasses import dataclass
from typing import List

from ib_adhoc_tasks.interactors.dtos import GroupByDTO, TaskIdsAndCountDTO


@dataclass
class ApplyGroupByDTO:
    project_id: str
    template_id: str
    user_id: str
    groupby_dtos: List[GroupByDTO]
    limit: str
    offset: str


class ElasticStorageInterface(abc.ABC):

    # def get_task_ids_filtered_on_stage_id(
    #         self, filter_for_stage_dto: FilterForStageDTO
    # ) -> List[str]:
    #     pass
    #
    # def get_task_ids_filtered_on_given_field(
    #         self,
    #         filter_for_field_dto: FilterForFieldDTO
    # ) -> List[str]:
    #     pass
    #
    # def get_task_ids_filtered_on_assignee_id(
    #         self, filter_for_assignee_dto: FilterForAssigneeDTO
    # ) -> List[str]:
    #     pass

    @abc.abstractmethod
    def get_task_ids_and_count_dto_based_on_given_groupby_and_pagination_detail(
            self, apply_group_dto: ApplyGroupByDTO, stage_ids: List[str]
    ) -> TaskIdsAndCountDTO:
        pass
