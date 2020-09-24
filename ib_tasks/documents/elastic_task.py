"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass
from typing import List, Any, Optional

from django.conf import settings
from elasticsearch_dsl import Document, Nested, InnerDoc, Text, Integer

from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import TaskStageAssigneeTeamIdDTO

TASK_INDEX_NAME = 'task-{}'.format(settings.STAGE)


@dataclass
class ElasticFieldDTO:
    field_id: str
    value: Any


@dataclass
class ElasticTaskDTO:
    project_id: Optional[str]
    template_id: Optional[str]
    task_id: int
    title: str
    fields: List[ElasticFieldDTO]
    stages: List[TaskStageAssigneeTeamIdDTO]


class Field(InnerDoc):
    field_id = Text()
    value = Text()


class Stage(InnerDoc):
    stage_id = Text()


class Task(Document):
    project_id = Text()
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

    def add_stages(self, stages: List[str]):
        self.stages = [
            Stage(stage_id=stage_id)
            for stage_id in stages
        ]


@dataclass()
class ElasticTaskIdDto:
    task_id: int
    elastic_task_id: str


@dataclass()
class QueryTasksDTO:
    total_tasks_count: int
    task_ids: List[int]

