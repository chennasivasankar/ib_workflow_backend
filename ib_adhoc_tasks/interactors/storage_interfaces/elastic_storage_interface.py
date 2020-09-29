import abc
from typing import List

from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO, \
    TaskOffsetAndLimitValuesDTO, TaskIdsForGroupsParameterDTO, \
    TaskIdsAndCountDTO, GetChildGroupsInGroupInputDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO, \
    GroupByResponseDTO


class ElasticStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_group_details_of_project(
            self, project_id: str, adhoc_template_id: str, stage_ids: List[str],
            group_by_dtos: List[GroupByDTO],
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO
    ) -> List[GroupDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_task_ids_and_count_dto_based_on_given_groupby_and_pagination_detail(
            self,
            task_ids_for_groups_parameter_dto: TaskIdsForGroupsParameterDTO,
            stage_ids: List[str]
    ) -> TaskIdsAndCountDTO:
        pass

    @abc.abstractmethod
    def get_child_group_details_of_group(
            self, group_by_response_dtos: List[GroupByResponseDTO],
            get_child_groups_in_group_input_dto: GetChildGroupsInGroupInputDTO,
            stage_ids: List[str]
    ):
        pass
