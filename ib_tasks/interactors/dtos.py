from dataclasses import dataclass
from typing import Optional


@dataclass()
class ActionDto:
    stage_id: str
    action_name: str
    logic: str
    role: str
    button_text: str
    button_color: Optional[str]
