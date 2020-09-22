from dataclasses import dataclass
from typing import List


@dataclass
class GroupDetailsDTO:
    task_ids: List[int]
    total_tasks: int
    group_by_value: str = None
    group_by_display_name: str = None
    child_group_by_value: str = None
    child_group_by_display_name: str = None


@dataclass
class GroupCountDTO:
    group_by_value: str
    total_groups: int


@dataclass
class ChildGroupCountDTO:
    child_group_by_value: str
    total_child_groups: int


@dataclass
class GroupByDetailsDTO:
    group_by: str
    order: int
