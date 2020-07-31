from dataclasses import dataclass
from typing import Union, List

from ib_tasks.interactors.storage_interfaces.actions_dtos \
    import ActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos \
    import StageDetailsDTO


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
class GetTaskDetailsDTO:
    task_id: str
    stage_id: str


@dataclass
class TaskStageCompleteDetailsDTO:
    stage_details_dto: StageDetailsDTO
    actions_dtos: List[ActionDetailsDTO]



