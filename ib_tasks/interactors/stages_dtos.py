from dataclasses import dataclass
from typing import Optional, List


@dataclass
class StageLogicAttributes:
    stage_id: str
    status_id: str


@dataclass
class StageDTO:
    stage_id: str
    task_template_id: str
    value: int
    id: Optional[int]
    stage_display_name: str
    stage_display_logic: str


@dataclass()
class StageActionDTO:
    stage_id: str
    action_name: str
    logic: str
    roles: List[str]
    function_path: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class TaskTemplateStageActionDTO(StageActionDTO):
    task_template_id: str


@dataclass
class StagesActionDTO:
    stage_id: str
    action_name: str
    logic: str
    roles: List[str]
    function_path: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class TaskTemplateStageDTO:
    task_template_id: str
    stage_id: str