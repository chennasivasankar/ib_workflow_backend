from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional

from ib_adhoc_tasks.constants.enum import ActionTypes, ViewType
from ib_tasks.constants.enum import Priority


@dataclass
class FieldDetailsDTO:
    field_type: str
    field_id: str
    key: str
    value: str


@dataclass
class StageActionDetailsDTO:
    action_id: int
    name: str
    stage_id: str
    button_text: str
    button_color: Optional[str]
    action_type: Optional[ActionTypes]
    transition_template_id: Optional[str]


@dataclass
class GetTaskStageCompleteDetailsDTO:
    task_id: int
    stage_id: str
    stage_color: str
    display_name: str
    db_stage_id: int
    field_dtos: List[FieldDetailsDTO]
    action_dtos: List[StageActionDetailsDTO]


@dataclass
class AssigneeDetailsDTO:
    assignee_id: str
    name: str
    profile_pic_url: Optional[str]


@dataclass
class TeamDetailsDTO:
    team_id: str
    name: str


@dataclass
class TaskStageAssigneeDetailsDTO:
    task_id: int
    stage_id: str
    assignee_details: Optional[AssigneeDetailsDTO]
    team_details: Optional[TeamDetailsDTO]


@dataclass
class TaskBaseDetailsDTO:
    template_id: str
    project_id: str
    task_id: int
    task_display_id: str
    title: str
    description: Optional[str]
    start_date: datetime
    due_date: datetime
    priority: Priority


@dataclass
class TasksCompleteDetailsDTO:
    task_base_details_dtos: List[TaskBaseDetailsDTO]
    task_stage_details_dtos: List[GetTaskStageCompleteDetailsDTO]
    task_stage_assignee_dtos: List[TaskStageAssigneeDetailsDTO]


@dataclass
class TasksDetailsInputDTO:
    task_ids: List[int]
    project_id: str
    user_id: str
    view_type: ViewType
