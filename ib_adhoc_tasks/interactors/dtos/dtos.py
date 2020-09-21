from dataclasses import dataclass


@dataclass
class GroupByDTO:
    group_by_key: str
    order: int
    offset: int
    limit: int


@dataclass
class TaskOffsetAndLimitValuesDTO:
    offset: int
    limit: int
