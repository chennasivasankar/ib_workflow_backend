from dataclasses import dataclass
from typing import List


@dataclass
class GroupDetailsDTO:
    group_id: str
    parent_group_id: str
    group_name: str
    task_ids: List[str]
