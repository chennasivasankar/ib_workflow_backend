from dataclasses import dataclass
from typing import Optional

from ib_adhoc_tasks.constants.enum import ViewType


@dataclass
class GroupByResponseDTO:
    group_by_id: int
    group_by_key: str
    order: int


@dataclass
class AddOrEditGroupByParameterDTO:
    project_id: str
    user_id: str
    view_type: ViewType
    group_by_key: str
    order: int = 1
    group_by_id: Optional[str] = None
