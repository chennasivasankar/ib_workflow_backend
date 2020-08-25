import datetime
from dataclasses import dataclass
from typing import Union, List, Any, Optional

from ib_tasks.constants.enum import Priority, Searchable
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageActionDetailsDTO, TaskStageIdsDTO, StageDetailsDTO, \
    CurrentStageDetailsDTO


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
    project_id: str
    task_template_id: str
    created_by_id: str
    action_id: int
    title: str
    description: str
    start_date: datetime.date
    due_date: datetime.date
    due_time: str
    priority: Priority
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class StageIdWithAssigneeDTO:
    stage_id: int
    assignee_id: str
    team_id: str


@dataclass
class UpdateTaskDTO:
    task_id: int
    created_by_id: str
    title: str
    description: str
    start_date: datetime.date
    due_date: datetime.date
    due_time: str
    priority: Priority
    stage_assignee: StageIdWithAssigneeDTO
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class UpdateTaskWithTaskDisplayIdDTO:
    task_display_id: str
    created_by_id: str
    title: str
    description: str
    start_date: datetime.date
    due_date: datetime.date
    due_time: str
    priority: Priority
    stage_assignee: StageIdWithAssigneeDTO
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class SaveAndActOnTaskDTO:
    task_id: int
    created_by_id: str
    action_id: int
    title: str
    description: str
    start_date: datetime.date
    due_date: datetime.date
    due_time: str
    priority: Priority
    stage_assignee: StageIdWithAssigneeDTO
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class SaveAndActOnTaskWithTaskDisplayIdDTO:
    task_display_id: str
    created_by_id: str
    action_id: int
    title: str
    description: str
    start_date: datetime.date
    due_date: datetime.date
    due_time: str
    priority: Priority
    stage_assignee: StageIdWithAssigneeDTO
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
    project_id: str
    limit: int
    user_id: str
    search_query: Optional[str]


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
    actions_dtos: List[StageActionDetailsDTO]


@dataclass
class StatusOperandStageDTO:
    variable: Any
    operator: str
    stage: Any


@dataclass
class CreateTaskLogDTO:
    task_json: str
    task_id: int
    user_id: str
    action_id: int


@dataclass
class TaskCurrentStageDetailsDTO:
    task_display_id: str
    stage_details_dtos: List[CurrentStageDetailsDTO]
    user_has_permission: bool


@dataclass
class TaskDueParametersDTO:
    user_id: str
    stage_id: str
    due_date_time: datetime
    reason_id: int
    reason: str


@dataclass
class TaskDelayParametersDTO(TaskDueParametersDTO):
    task_id: int


@dataclass
class SearchableDTO:
    search_type: Searchable
    id: Union[int, str]




