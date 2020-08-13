from dataclasses import dataclass


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