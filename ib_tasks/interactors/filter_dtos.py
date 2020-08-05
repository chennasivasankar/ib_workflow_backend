

from dataclasses import dataclass
from typing import List, Any

from ib_tasks.constants.enum import Operators


@dataclass()
class ConditionDTO:
    filter_id: int
    condition_id: int
    field_id: str
    operator: Operators
    value: Any


@dataclass()
class FilterConditionDTO:
    filter_id: int
    condition_ids: List[int]


@dataclass()
class FilterDTO:
    filter_id: int
    filter_name: str
    user_id: str
    is_selected: bool
    template_id: str
    template_name: str


@dataclass()
class FilterCompleteDetailsDTO:
    filters_dto: List[FilterDTO]
    conditions_dto: List[ConditionDTO]