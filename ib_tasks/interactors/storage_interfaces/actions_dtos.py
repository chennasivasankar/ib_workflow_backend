from dataclasses import dataclass
from typing import Optional, List


@dataclass()
class ActionDTO:
    action_id: int
    name: str
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


@dataclass()
class ActionDetailsDTO:
    action_id: int
    name: str
    stage_id: str
    button_text: str
    button_color: Optional[str]


@dataclass
class StageActionDetailsDTO(ActionDetailsDTO):
    action_type: str
    transition_template_id: str
