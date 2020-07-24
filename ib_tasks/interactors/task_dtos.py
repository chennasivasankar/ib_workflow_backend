from dataclasses import dataclass
from typing import Union, List

from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStageIdsDTO


@dataclass
class FieldValuesDTO:
    field_id: str
    field_value: Union[str, List[str], int]


@dataclass
class GoFFieldsDTO:
    gof_id: str
    field_values_dtos: List[FieldValuesDTO]


@dataclass
class TaskDTO:
    task_template_id: str
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class TaskStatusVariableDTO:
    status_id: int
    variable: str
    value: str


@dataclass
class TaskDetailsConfigDTO:
    unique_key: int
    stage_ids: List[str]
    offset: int
    limit: int


@dataclass
class TaskIdsDTO:
    unique_key: int
    task_stage_ids: List[TaskStageIdsDTO]
    total_tasks: int

@dataclass
class GetTaskDetailsDTO:
    task_id: str
    stage_id: str

