from typing import List
from dataclasses import dataclass


@dataclass
class StageActionsDto:
    stage_id: str
    action_names: List[str]