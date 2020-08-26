from dataclasses import dataclass
from typing import Optional, List

from ib_tasks.constants.enum import ValidationType, ActionTypes


@dataclass()
class ActionDTO:
    action_id: int
    name: str
    action_type: Optional[ActionTypes]
    transition_template_id: str
    stage_id: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class ActionRolesDTO:
    action_id: int
    roles: List[str]


@dataclass
class ActionWithStageIdDTO:
    stage_id: int
    action_id: int
    button_text: str
    button_color: str
    action_type: Optional[ValidationType]
    transition_template_id: Optional[str]


@dataclass()
class ActionDetailsDTO:
    action_id: int
    name: str
    stage_id: str
    button_text: str
    button_color: Optional[str]


@dataclass
class StageActionDetailsDTO(ActionDetailsDTO):
    action_type: Optional[ActionTypes]
    transition_template_id: Optional[str]


