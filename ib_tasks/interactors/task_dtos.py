from dataclasses import dataclass
from typing import Union, List


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