from dataclasses import dataclass
from typing import Optional

from ib_tasks.adapters.dtos import AssigneeDetailsDTO


@dataclass
class StageLogicAttributes:
    stage_id: str
    status_id: str


@dataclass
class TaskStageDTO:
    stage_id: str
    db_stage_id: int
    display_name: str
    stage_colour: str


@dataclass
class TaskStageAssigneeDetailsDTO:
    task_id: int
    stage_id: str
    assignee_details: Optional[AssigneeDetailsDTO]