from dataclasses import dataclass
from typing import Optional


@dataclass()
class RequestDTO:
    stage_id: str
    action_name: str
    logic: str
    role: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class StageActionDTO():
    stage_id: str
    action_name: str
    logic: str
    role: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class TaskTemplateStageActionDTO(StageActionDTO):
    task_template_id: str


@dataclass()
class TaskTemplateStageDTO:
    task_template_id: str
    stage_id: str
