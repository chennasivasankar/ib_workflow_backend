from dataclasses import dataclass
from datetime import datetime
from typing import List

from ib_tasks.adapters.dtos import UserDetailsDTO, AssigneeDetailsDTO


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
    task_id: int
    due_date_time: datetime
    due_missed_count: int
    reason: str
    user_id: str


@dataclass
class TaskDueDetailsDTO:
    task_id: int
    due_date_time: datetime
    due_missed_count: int
    reason: str
    user: AssigneeDetailsDTO


@dataclass
class TaskDisplayIdDTO:
    task_id: int
    display_id: str
