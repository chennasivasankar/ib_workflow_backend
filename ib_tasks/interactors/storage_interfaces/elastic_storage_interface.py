"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
import abc
from dataclasses import dataclass
from typing import List
from typing import Union

from ib_tasks.constants.enum import Operators
from ib_tasks.documents.elastic_task import *


@dataclass
class ApplyFilterDTO:
    template_id: str
    field_id: str
    operator: Operators
    value: str


class ElasticSearchStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_task(self, elastic_task_dto: ElasticTaskDTO) -> str:
        pass

    @abc.abstractmethod
    def update_task(self, task_dto: ElasticTaskDTO):
        pass

    @abc.abstractmethod
    def filter_tasks(self, filter_dtos: List[ApplyFilterDTO],
                     offset: int, limit: int) -> List[int]:
        pass

    @abc.abstractmethod
    def search_tasks(
            self, offset: int, limit: int, search_query: str,
            apply_filter_dtos: List[ApplyFilterDTO]
    ) -> QueryTasksDTO:
        pass