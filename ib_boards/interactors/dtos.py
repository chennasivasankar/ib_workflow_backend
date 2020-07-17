"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""
import json
from dataclasses import dataclass
from typing import List


@dataclass
class TaskTemplateStagesDTO:
    task_template_id: str
    stages: List[str]


@dataclass
class TaskSummaryFieldsDTO:
    task_id: int
    summary_fields: List[str]


@dataclass
class CreateBoardDTO:
    board_id: str
    display_name: str


@dataclass
class ColumnDTO:
    column_id: str
    display_name: str
    task_template_stages: List[TaskTemplateStagesDTO]
    user_role_ids: List[str]
    column_summary: str
    task_summary_fields: List[TaskSummaryFieldsDTO]
    board_id: str


@dataclass
class BoardColumnDTO:
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

