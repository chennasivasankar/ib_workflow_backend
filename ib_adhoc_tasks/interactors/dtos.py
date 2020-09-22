from dataclasses import dataclass
from typing import Optional


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
