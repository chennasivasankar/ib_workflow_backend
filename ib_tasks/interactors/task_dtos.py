from dataclasses import dataclass
from typing import Union, List, Any

from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStageIdsDTO, \
    StageDetailsDTO


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
class CreateTaskDTO:
    task_template_id: str
    created_by_id: str
    action_id: int
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class UpdateTaskDTO:
    task_id: int
    created_by_id: str
    action_id: int
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class TaskStatusVariableDTO:
    status_id: int
    variable: str
    value: str


@dataclass
class TaskDetailsConfigDTO:
    unique_key: str
    stage_ids: List[str]
    offset: int
    limit: int


@dataclass
class TaskIdsDTO:
    unique_key: str
    task_stage_ids: List[TaskStageIdsDTO]
    total_tasks: int


@dataclass
class GetTaskDetailsDTO:
    task_id: int
    stage_id: str


@dataclass
class StageAndActionsDetailsDTO(StageDetailsDTO):
    actions_dtos: List[ActionDetailsDTO]


@dataclass
class StatusOperandStageDTO:
    variable: Any
    operator: str
    stage: Any
