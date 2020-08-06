

from dataclasses import dataclass
from typing import List, Any

from ib_tasks.constants.enum import Operators, Status


@dataclass()
class ConditionDTO:
    filter_id: int
    condition_id: int
    field_id: str
    field_name: str
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
    is_selected: Status
    template_id: str
    template_name: str


@dataclass()
class FilterCompleteDetailsDTO:
    filters_dto: List[FilterDTO]
    conditions_dto: List[ConditionDTO]


@dataclass
class CreateFilterDTO:
    filter_name: str
    user_id: str
    template_id: str


@dataclass
class UpdateFilterDTO(CreateFilterDTO):
    filter_id: int


@dataclass
class CreateConditionDTO:
    field_id: int
    operator: Operators
    value: Any