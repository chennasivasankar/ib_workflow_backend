from dataclasses import dataclass
from typing import List

@dataclass
class ColumnParametersDTO:
    board_id: str
    user_id: str


@dataclass
class TaskColumnDTO:
    column_id: str
    task_id: str

@dataclass
class PaginationParametersDTO:
    offset: int
    limit: int

@dataclass
class TaskStageDTO:
    task_id: str
    stage_id: str

@dataclass
class TaskDetailsDTO:
    task_id: str
    stage_id: str
    column_id: str

@dataclass
class FieldsDTO:
    task_template_id: str
    field_id: str




@dataclass
class TaskTemplateStagesDTO:
    task_template_id: str
    stages: List[str]


@dataclass
class TaskSummaryFieldsDTO:
    task_id: int
    summary_fields: List[str]


@dataclass
class BoardDTO:
    board_id: str
    display_name: str


@dataclass
class ColumnDTO:
    column_id: str
    display_name: str
    display_order: int
    task_template_stages: List[TaskTemplateStagesDTO]
    user_role_ids: List[str]
    column_summary: str
    column_actions: str
    list_view_fields: List[TaskSummaryFieldsDTO]
    kanban_view_fields: List[TaskSummaryFieldsDTO]
    board_id: str


@dataclass
class BoardColumnsDTO:
    board_id: str
    column_ids: List[str]


@dataclass
class GetBoardsDTO:
    user_id: int
    offset: int
    limit: int


@dataclass
class ColumnTasksParametersDTO:
    user_id = 1
    column_id: str
    offset: int
    limit: int


@dataclass
class TaskDTO:
    task_id: str
    field_type: str
    key: str
    value: str


@dataclass
class ActionDTO:
    action_id: str
    name: str
    button_text: str
    button_color: str
    task_id: str


@dataclass
class TaskStatusDTO:
    status: str
    stage: str


@dataclass
class TaskIdStageDTO:
    task_id: str
    stage_id: str


@dataclass
class TasksParameterDTO(TaskIdStageDTO):
    column_id: str

