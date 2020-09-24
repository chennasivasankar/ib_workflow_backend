import datetime
from dataclasses import dataclass
from typing import Union, List, Any, Optional

from ib_tasks.constants.enum import Priority, Searchable, ViewType, ActionTypes
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
class BasicTaskDetailsDTO:
    project_id: str
    task_template_id: str
    created_by_id: str
    action_id: int
    title: str
    description: Optional[str]
    start_datetime: Optional[datetime.datetime]
    due_datetime: Optional[datetime.datetime]
    priority: Optional[Priority]


@dataclass
class CreateTaskDTO:
    basic_task_details_dto: BasicTaskDetailsDTO
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class CreateSubTaskDTO(CreateTaskDTO):
    parent_task_id: str


@dataclass
class StageIdWithAssigneeDTO:
    stage_id: int
    assignee_id: str
    team_id: str


@dataclass
class UpdateTaskBasicDetailsDTO:
    task_id: int
    action_type: Optional[ActionTypes]
    created_by_id: str
    title: str
    description: str
    start_datetime: datetime.datetime
    due_datetime: datetime.datetime
    priority: Priority


@dataclass
class UpdateTaskDTO:
    task_basic_details: UpdateTaskBasicDetailsDTO
    stage_assignee: StageIdWithAssigneeDTO
    gof_fields_dtos: List[GoFFieldsDTO]


@dataclass
class UpdateTaskWithTaskDisplayIdDTO:
    task_display_id: str
    action_type: Optional[ActionTypes]
    created_by_id: str
    title: str
    description: str
    start_datetime: datetime.datetime
    due_datetime: datetime.datetime
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
    start_datetime: datetime.datetime
    due_datetime: datetime.datetime
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
    start_datetime: datetime.datetime
    due_datetime: datetime.datetime
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
class StageDisplayLogicDTO:
    current_stage: str
    display_logic_dto: StatusOperandStageDTO


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
    stage_id: int
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


@dataclass
class SearchQueryDTO:
    offset: int
    limit: int
    query_value: Any
    project_id: str
    user_id: str = None
    view_type: ViewType = None


@dataclass
class GetTaskRPsParametersDTO:
    task_id: str
    user_id: str
    stage_id: int

@dataclass
class TaskWithCompletedSubTasksCountDTO:
    task_id: int
    completed_sub_tasks_count: int
