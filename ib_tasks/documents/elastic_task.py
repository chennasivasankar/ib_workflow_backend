"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from django.conf import settings
from dataclasses import dataclass
from typing import List, Any, Optional

from elasticsearch_dsl import Document, Nested, InnerDoc, Text, Integer

TASK_INDEX_NAME = 'task-{}'.format(settings.STAGE)
USER_INDEX_NAME = 'user-{}'.format(settings.STAGE)
COUNTRY_INDEX_NAME = 'country-{}'.format(settings.STAGE)
STATE_INDEX_NAME = 'state-{}'.format(settings.STAGE)
CITY_INDEX_NAME = 'city-{}'.format(settings.STAGE)


@dataclass
class ElasticFieldDTO:
    field_id: str
    value: Any


@dataclass
class ElasticTaskDTO:
    template_id: Optional[str]
    task_id: int
    title: str
    fields: List[ElasticFieldDTO]


class Field(InnerDoc):
    field_id = Text()
    value = Text()


class Stage(InnerDoc):
    stage_id: Text()


class Task(Document):
    template_id = Text()
    task_id = Integer()
    title = Text()
    fields = Nested(Field)
    stages = Nested(Stage)

    class Index:
        name = TASK_INDEX_NAME

    def add_fields(self, field_dtos: List[ElasticFieldDTO]):
        self.fields = [
            Field(field_id=field_dto.field_id, value=field_dto.value)
            for field_dto in field_dtos
        ]


@dataclass()
class ElasticTaskIdDto:
    task_id: int
    elastic_task_id: str


@dataclass()
class QueryTasksDTO:
    total_tasks_count: int
    task_ids: List[int]


@dataclass()
class ElasticUserDTO:
    user_id: str
    username: Optional[str]
    elastic_user_id: Optional[str]


class User(Document):
    user_id = Text()
    username = Text()

    class Index:
        name = USER_INDEX_NAME


@dataclass()
class ElasticCountryDTO:
    country_id: int
    country_name: Optional[str]
    elastic_country_id: Optional[str]


class Country(Document):
    country_id = Integer()
    country_name = Text()

    class Index:
        name = COUNTRY_INDEX_NAME


@dataclass()
class ElasticStateDTO:
    state_id: int
    state_name: Optional[str]
    elastic_state_name: Optional[str]


class State(Document):
    state_id = Integer()
    state_name = Text()

    class Index:
        name = STATE_INDEX_NAME


@dataclass()
class ElasticCityDTO:
    city_id: int
    city_name: Optional[str]
    elastic_city_name: Optional[str]


class City(Document):
    city_id = Integer()
    city_name = Text()

    class Index:
        name = CITY_INDEX_NAME
