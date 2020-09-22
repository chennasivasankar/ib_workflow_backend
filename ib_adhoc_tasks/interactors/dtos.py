from dataclasses import dataclass
from typing import List


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
