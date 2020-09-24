from dataclasses import dataclass
from typing import List, Optional

from ib_adhoc_tasks.constants.enum import GroupByEnum, ViewType


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
    limit: int
    offset: int


@dataclass
class TaskIdsAndCountDTO:
    task_ids: List[int]
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


@dataclass
class GetTaskDetailsInGroupInputDTO:
    project_id: str
    view_type: ViewType
    limit: int
    offset: int
    group_by_values: List[str]
    user_id: str


@dataclass
class GetSubtasksParameterDTO:
    user_id: str
    task_id: int
    view_type: ViewType
