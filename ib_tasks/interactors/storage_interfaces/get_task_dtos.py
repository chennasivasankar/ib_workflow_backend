from dataclasses import dataclass
from typing import List


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
class TaskDetailsDTO:
    template_id: str
    task_gof_dtos: List[TaskGoFDTO]
    task_gof_field_dtos: List[TaskGoFFieldDTO]


@dataclass
class TemplateFieldsDTO:
    task_template_id: str
    field_ids: List[str]
