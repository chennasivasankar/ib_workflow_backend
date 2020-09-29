from dataclasses import dataclass
from datetime import datetime
from typing import List

from ib_tasks.adapters.dtos import AssigneeDetailsDTO


@dataclass
class TaskGoFWithTaskIdDTO:
    task_id: int
    gof_id: str
    same_gof_order: int


@dataclass
class TaskGoFDetailsDTO:
    task_gof_id: int
    gof_id: str
    same_gof_order: int


@dataclass
class TaskGoFFieldDTO:
    field_id: str
    field_response: str
    task_gof_id: int


@dataclass
class TaskDueMissingDTO:
    task_id: str
    due_date_time: datetime
    due_missed_count: int
    reason: str
    user_id: str


@dataclass
class TaskDueDetailsDTO:
    task_id: str
    due_date_time: datetime
    due_missed_count: int
    reason: str
    user: AssigneeDetailsDTO


@dataclass
class TaskDisplayIdDTO:
    task_id: int
    display_id: str


@dataclass
class TaskProjectDTO:
    task_id: int
    project_id: str


@dataclass
class TaskProjectRolesDTO(TaskProjectDTO):
    roles: List[str]


@dataclass
class TaskStageAssigneeDTO:
    task_id: int
    stage_id: int
    assignee_dto: AssigneeDetailsDTO


@dataclass
class SubTasksCountDTO:
    task_id: int
    sub_tasks_count: int


@dataclass
class SubTasksIdsDTO:
    task_id: int
    sub_task_ids: List[int]

