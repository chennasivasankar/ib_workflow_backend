from dataclasses import dataclass


@dataclass
class GroupByDTO:
    group_by_key: str
    order: int
