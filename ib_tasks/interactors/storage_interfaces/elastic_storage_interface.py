"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
import abc
from dataclasses import dataclass
from typing import Tuple

from ib_tasks.constants.enum import Operators
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldTypeDTO
from ib_tasks.interactors.task_dtos import SearchQueryDTO


@dataclass
class ApplyFilterDTO:
    project_id: str
    template_id: str
    field_id: str
    operator: Operators
    value: str


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
            int, stage_ids: List[str], project_id: str, field_type_dtos: List[FieldTypeDTO]) -> Tuple[List[int], int]:
        pass

    @abc.abstractmethod
    def search_tasks(
            self, search_query_dto: SearchQueryDTO,
            apply_filter_dtos: List[ApplyFilterDTO],
            stage_ids: List[str], field_type_dtos: List[FieldTypeDTO]
    ) -> QueryTasksDTO:
        pass

    def validate_task_id_in_elasticsearch(self, task_id):
        pass

    def filter_tasks_with_stage_ids(self, filter_dtos, task_details_config, field_type_dtos: List[FieldTypeDTO]):
        pass