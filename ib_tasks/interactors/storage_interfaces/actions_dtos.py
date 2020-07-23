from dataclasses import dataclass
from typing import Optional, List


@dataclass()
class ActionDTO:
    action_id: str
    name: str
    stage_id: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class ActionRolesDTO:
    action_id: str
    roles: List[str]


@dataclass
class ActionsOfTemplateDTO:
    template_id: str
    action_id: str
    action_name: str
    button_text: str
    button_color: str
