from dataclasses import dataclass
from typing import List


@dataclass
class GroupByDTO:
    key: str
    value: str


@dataclass
class ApplyGroupByDTO:
    project_id: str
    template_id: str
    user_id: str
    groupby_dtos: List[GroupByDTO]
    limit: str
    offset: str


@dataclass
class TaskIdsAndCountDTO:
    task_ids: List[str]
    total_tasks_count: int
