"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
import abc
from dataclasses import dataclass
from typing import List
from typing import Union

from ib_tasks.constants.enum import Operators


@dataclass
class ApplyFilterDTO:
    template_id: str
    field_id: str
    operator: Operators
    value: str


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
    def filter_tasks(self, filter_dtos: List[ApplyFilterDTO], offset: int, limit: int) -> List[int]:
        pass

    @abc.abstractmethod
    def search_tasks(
            self, offset: int, limit: int, search_query: str,
            apply_filter_dtos: List[ApplyFilterDTO]
    ) -> QueryTasksDTO:
        pass

    @abc.abstractmethod
    def create_elastic_user(self, user_dto: ElasticUserDTO):
        pass

    @abc.abstractmethod
    def query_users(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticUserDTO]:
        pass

    @abc.abstractmethod
    def create_elastic_country(self, country_dto: ElasticCountryDTO):
        pass

    @abc.abstractmethod
    def query_countries(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCountryDTO]:
        pass

    @abc.abstractmethod
    def create_elastic_state(self, state_dto: ElasticStateDTO):
        pass

    @abc.abstractmethod
    def query_states(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticStateDTO]:
        pass

    @abc.abstractmethod
    def create_elastic_city(self, city_dto: ElasticCityDTO):
        pass

    @abc.abstractmethod
    def query_cities(
            self, offset: int, limit: int, search_query: str
    ) -> List[ElasticCityDTO]:
        pass