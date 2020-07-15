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
class StageActionDTO(RequestDTO):
    pass


@dataclass()
class TaskTemplateStageActionDTO(RequestDTO):
    task_template_id: str



