from typing import List
from dataclasses import dataclass


@dataclass
class StageActionNamesDTO:
    stage_id: str
    action_names: List[str]
