"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""
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
class BoardColumnDTO:
    board_id: str
    column_ids: List[str]