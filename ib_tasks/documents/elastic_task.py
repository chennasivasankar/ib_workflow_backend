"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass
from typing import List

from elasticsearch_dsl import connections

connections.create_connection(hosts=['localhost'], timeout=20)

from elasticsearch_dsl import Document, Nested, InnerDoc, Text, Integer


@dataclass
class ElasticFieldDTO:
    field_id: str
    value: str


@dataclass
class ElasticTaskDTO:
    template_id: str
    task_id: int
    title: str
    fields: List[ElasticFieldDTO]


@dataclass
class QueryTasksDTO:
    pass


class Field(InnerDoc):
    field_id = Text()
    value = Text()


class Task(Document):
    template_id = Text()
    task_id = Integer()
    title = Text()
    fields = Nested(Field)

    class Index:
        name = 'task'

    def add_fields(self, field_dtos: List[ElasticFieldDTO]):
        self.fields = [
            Field(field_id=field_dto.field_id, value=field_dto.value)
            for field_dto in field_dtos
        ]
