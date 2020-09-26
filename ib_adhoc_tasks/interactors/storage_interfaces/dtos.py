from dataclasses import dataclass
from typing import List, Optional

from ib_adhoc_tasks.constants.enum import ViewType


@dataclass
class GroupByResponseDTO:
    group_by_key: str
    display_name: str
    order: int


# todo need to change this after deletion of add_or_edit_wrapper
@dataclass
class AddOrEditGroupByParameterDTO:
    user_id: str
    view_type: ViewType
    group_by_key: str
    order: int = 1




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
    group_by_value: str
    total_child_groups: int


@dataclass
class GroupByDetailsDTO:
    group_by: str
    order: int
