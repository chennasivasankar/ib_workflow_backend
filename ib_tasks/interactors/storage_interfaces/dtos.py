from dataclasses import dataclass
from typing import Optional


@dataclass
class StageDTO:
    stage_id: str
    task_template_id: str
    value: int
    id: Optional[int]
    stage_display_name: str
    stage_display_logic: str

@dataclass
class TaskStagesDTO:
    task_template_id: str
    stage_id: str

@dataclass
class TaskStatusDTO:
    task_template_id: str
    status_variable_id: str

@dataclass
class ValidStageDTO:
    stage_id: str
    id: int
