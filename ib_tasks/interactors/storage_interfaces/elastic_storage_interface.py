"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
import abc
from dataclasses import dataclass
from typing import List, Tuple
from typing import Union

from ib_tasks.constants.enum import Operators
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStageIdsDTO
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO, SearchQueryDTO


@dataclass
class ApplyFilterDTO:
    project_id: str
    template_id: str
    field_id: str
    operator: Operators
    value: str
    project_id: str


from ib_tasks.documents.elastic_task import ElasticTaskDTO, Task, QueryTasksDTO
from ib_tasks.documents.elastic_task import *


class ElasticSearchStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_task(self, elastic_task_dto: ElasticTaskDTO) -> str:
        pass

    @abc.abstractmethod
    def update_task(self, task_dto: ElasticTaskDTO):
        pass

    @abc.abstractmethod
    def filter_tasks(
            self, filter_dtos: List[ApplyFilterDTO], offset: int, limit:
            int, stage_ids: List[str], project_id: str) -> Tuple[List[int], int]:
        pass

    @abc.abstractmethod
    def search_tasks(
            self, search_query_dto: SearchQueryDTO,
            apply_filter_dtos: List[ApplyFilterDTO],
            stage_ids: List[str]
    ) -> QueryTasksDTO:
        pass

    def validate_task_id_in_elasticsearch(self, task_id):
        pass

    def filter_tasks_with_stage_ids(self, filter_dtos, task_details_config):
        pass