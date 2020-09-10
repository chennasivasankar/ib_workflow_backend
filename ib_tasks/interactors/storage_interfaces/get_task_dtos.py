from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from ib_tasks.adapters.dtos import ProjectDetailsDTO
from ib_tasks.constants.enum import Priority, Searchable


@dataclass
class TaskGoFDTO:
    task_gof_id: int
    gof_id: str
    same_gof_order: int


@dataclass
class TaskGoFFieldDTO:
    task_gof_id: int
    field_id: str
    field_response: str


@dataclass
class TaskBaseDetailsDTO:
    template_id: str
    project_id: str
    task_display_id: str
    title: str
    description: Optional[str]
    start_date: datetime
    due_date: datetime
    priority: Priority


@dataclass
class TaskDetailsDTO:
    project_details_dto: ProjectDetailsDTO
    task_base_details_dto: TaskBaseDetailsDTO
    task_gof_dtos: List[TaskGoFDTO]
    task_gof_field_dtos: List[TaskGoFFieldDTO]


@dataclass
class TemplateFieldsDTO:
    task_template_id: str
    field_ids: List[str]


@dataclass
class FieldSearchableDTO:
    field_id: str
    field_value: Searchable
    field_response: Union[int, str]
