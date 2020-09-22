from dataclasses import dataclass
from typing import List
from typing import Optional

from ib_adhoc_tasks.constants.enum import GroupByEnum


@dataclass
class GroupByDTO:
    group_by_value: GroupByEnum
    order: int
    offset: int
    limit: int


@dataclass
class TaskOffsetAndLimitValuesDTO:
    offset: int
    limit: int


@dataclass
class GroupByValueDTO:
    group_by_display_name: str
    group_by_value: str


@dataclass
class GroupByValueDTO:
    group_by_display_name: str
    group_by_value: str


@dataclass
class TaskIdsForGroupsParameterDTO:
    project_id: str
    template_id: str
    user_id: str
    groupby_value_dtos: List[GroupByValueDTO]
    limit: str
    offset: str


@dataclass
class TaskIdsAndCountDTO:
    task_ids: List[str]
    total_tasks_count: int


@dataclass
class GroupByDTO:
    group_by_value: str
    order: int
    offset: int
    limit: int


@dataclass
class TaskOffsetAndLimitValuesDTO:
    offset: int
    limit: int


@dataclass
class OffsetLimitDTO:
    offset: int
    limit: int


@dataclass
class GroupByInfoKanbanViewDTO:
    project_id: str
    user_id: str
    task_offset_limit_dto: OffsetLimitDTO
    group1_offset_limit_dto: Optional[OffsetLimitDTO]
    group2_offset_limit_dto: Optional[OffsetLimitDTO]


@dataclass
class GroupByInfoListViewDTO:
    project_id: str
    user_id: str
    task_offset_limit_dto: OffsetLimitDTO
    group_offset_limit_dto: Optional[OffsetLimitDTO]


