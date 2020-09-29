from dataclasses import dataclass
from typing import Optional, List

from ib_tasks.adapters.dtos import AssigneeDetailsDTO, TeamDetailsDTO


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
class TaskStageAssigneeTeamDetailsDTO:
    task_id: int
    stage_id: str
    assignee_details: Optional[AssigneeDetailsDTO]
    team_details: Optional[TeamDetailsDTO]


@dataclass
class StageIdWithGoFIdsDTO:
    stage_id: str
    gof_ids: List[str]


@dataclass
class DBStageIdWithStageIdDTO:
    db_stage_id: int
    stage_id: str


@dataclass
class DBStageIdWithGoFIdsDTO:
    db_stage_id: int
    gof_ids: List[str]
