"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from django.conf import settings
from dataclasses import dataclass
from typing import List, Any, Optional

from elasticsearch_dsl import Document, Nested, InnerDoc, Text, Integer

TASK_INDEX_NAME = 'task-{}'.format(settings.STAGE)


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


@dataclass()
class ElasticTaskIdDto:
    task_id: int
    elastic_task_id: str


@dataclass()
class QueryTasksDTO:
    total_tasks_count: int
    task_ids: List[int]


class Field(InnerDoc):
    field_id = Text()
    value = Text()


class Task(Document):
    template_id = Text()
    task_id = Integer()
    title = Text()
    fields = Nested(Field)

    class Index:
        name = TASK_INDEX_NAME

    def add_fields(self, field_dtos: List[ElasticFieldDTO]):
        self.fields = [
            Field(field_id=field_dto.field_id, value=field_dto.value)
            for field_dto in field_dtos
        ]
