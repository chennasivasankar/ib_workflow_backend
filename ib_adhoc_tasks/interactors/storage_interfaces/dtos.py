from dataclasses import dataclass
from typing import List


@dataclass
class GroupDetailsDTO:
    task_ids: List[str]
    total_tasks: int
    group_by_value: str = None
    group_by_display_name: str = None
    child_group_by_value: str = None
    child_group_by_display_name: str = None
