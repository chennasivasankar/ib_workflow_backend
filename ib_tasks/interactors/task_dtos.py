from dataclasses import dataclass
from typing import Union, List, Optional


@dataclass
class FieldValuesDTO:
    field_id: str
    field_response: Union[str, List[str], int]


@dataclass
class GoFFieldsDTO:
    gof_id: str
    same_gof_order: int
    field_values_dtos: List[FieldValuesDTO]


@dataclass
class TaskDTO:
    task_id: Optional[int]
    task_template_id: Optional[str]
    created_by_id: str
    action_id: str
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class TaskStatusVariableDTO:
    status_id: int
    variable: str
    value: str
