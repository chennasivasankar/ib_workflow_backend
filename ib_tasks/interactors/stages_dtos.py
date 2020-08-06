from dataclasses import dataclass
from typing import Optional, List


@dataclass
class StageLogicAttributes:
    stage_id: str
    status_id: str


@dataclass
class StageDTO:
    stage_id: str
    task_template_id: str
    value: int
    id: Optional[int]
    card_info_kanban: str
    card_info_list: str
    stage_display_name: str
    stage_display_logic: str


@dataclass
class StageActionDTO:
    stage_id: str
    action_name: str
    logic: str
    roles: List[str]
    function_path: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class TaskTemplateStageActionDTO(StageActionDTO):
    task_template_id: str


@dataclass
class StagesActionDTO:
    stage_id: str
    action_name: str
    logic: str
    roles: List[str]
    function_path: str
    button_text: str
    button_color: Optional[str]


@dataclass
class TemplateStageDTO:
    task_template_id: str
    stage_id: str


@dataclass
class UserStagesWithPaginationDTO:
    stage_ids: List[str]
    user_id: str
    limit: int
    offset: int


@dataclass
class StageAssigneeDTO:
    stage_id: str
    assignee_id: str


@dataclass
class TaskIdWithStageAssigneesDTO:
    task_id: int
    stage_assignees: List[StageAssigneeDTO]


@dataclass
class TaskIdWithStageAssigneeDTO:
    task_id: int
    stage_id: str
    assignee_id: str
