from dataclasses import dataclass
from typing import List


@dataclass
class GroupDetailsDTO:
    group_by_key: str
    group_by_value: str
    parent_group_by_key: str
    parent_group_by_value: str
    task_ids: List[str]
    total_tasks: int
