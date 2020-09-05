from dataclasses import dataclass
from typing import List, Optional

from ib_boards.constants.enum import ViewType, DisplayStatus


@dataclass
class ColumnParametersDTO:
    board_id: str
    user_id: str
    view_type: ViewType
    search_query: Optional[str]


@dataclass
class ColumnTasksDTO:
    column_id: str
    stage_id: str
    task_id: int
    task_display_id: str


@dataclass
class PaginationParametersDTO:
    offset: int
    limit: int


@dataclass
class TaskStageIdDTO:
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
    name: str


@dataclass
class ColumnDTO:
    column_id: str
    name: str
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
    user_id: str
    project_id: str
    offset: int
    limit: int


@dataclass
class ColumnTasksParametersDTO:
    user_id: str
    column_id: str
    offset: int
    limit: int
    view_type: ViewType
    search_query: Optional[str]


@dataclass
class FieldDTO:
    task_id: int
    field_type: str
    field_id: int
    key: str
    value: str
    stage_id: str


@dataclass
class ActionDTO:
    action_id: str
    name: str
    action_type: str
    button_text: str
    button_color: str
    task_id: int
    stage_id: str
    transition_template_id: str


@dataclass
class StageActionDetailsDTO(ActionDTO):
    action_type: str
    transition_template_id: str


@dataclass
class TaskStatusDTO:
    status: str
    stage: str


@dataclass
class TaskIdStageDTO:
    task_id: int
    task_display_id: str
    stage_id: str


@dataclass
class TasksParameterDTO(TaskIdStageDTO):
    column_id: str


@dataclass
class ColumnTaskIdsDTO:
    unique_key: str
    task_stage_ids: List[TaskIdStageDTO]
    total_tasks: int


@dataclass
class FieldDetailsDTO:
    field_type: str
    field_id: int
    stage_id: str
    key: str
    value: str


@dataclass()
class ActionDetailsDTO:
    action_id: int
    name: str
    stage_id: str
    button_text: str
    button_color: Optional[str]


@dataclass
class TaskCompleteDetailsDTO:
    task_id: int
    stage_id: str
    stage_color: str
    field_dtos: List[FieldDetailsDTO]
    action_dtos: List[ActionDetailsDTO]


@dataclass
class ColumnTotalTasksDTO:
    column_id: str
    total_tasks: int


@dataclass
class StarredAndOtherBoardsDTO:
    starred_boards_dtos: List[BoardDTO]
    other_boards_dtos: List[BoardDTO]


@dataclass
class StarOrUnstarParametersDTO:
    board_id: str
    user_id: str
    action: str


@dataclass
class TaskStageDTO:
    task_id: int
    stage_id: str
    db_stage_id: int
    display_name: str
    stage_color: str


@dataclass
class AssigneesDTO:
    assignee_id: str
    name: str
    profile_pic_url: str


@dataclass
class StageAssigneesDTO:
    task_id: int
    stage_id: str
    assignees_details: AssigneesDTO


@dataclass
class ProjectBoardDTO:
    project_id: str
    board_id: str


@dataclass
class ChangeFieldsStatusParameter:
    user_id: str
    column_id: str
    field_id: str
    display_status: DisplayStatus


@dataclass
class ChangeFieldsOrderParameter:
    user_id: str
    column_id: str
    field_id: str
    display_order: int


@dataclass
class FieldNameDTO:
    field_id: str
    display_name: str