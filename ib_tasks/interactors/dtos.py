from typing import List, Optional
from dataclasses import dataclass


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


@dataclass
class StagesActionDTO:
    stage_id: str
    action_name: str
    logic: str
    function_path: str
    roles: List[str]
    button_text: str
    button_color: Optional[str]


@dataclass
class CreateTaskTemplateDTO:
    template_id: str
    template_name: str


@dataclass
class GlobalConstantsDTO:
    constant_name: str
    value: int


@dataclass
class GlobalConstantsWithTemplateIdDTO:
    template_id: str
    global_constants_dtos: List[GlobalConstantsDTO]
