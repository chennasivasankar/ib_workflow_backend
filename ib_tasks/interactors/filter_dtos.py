

from dataclasses import dataclass
from typing import List, Any

from ib_tasks.constants.enum import Operators


@dataclass()
class ConditionDTO:
    filter_id: int
    condition_id: int
    field_id: str
    field_name: str
    operator: Operators
    value: Any


@dataclass()
class FilterDTO:
    filter_id: int
    filter_name: str
    user_id: str
    is_selected: bool
    template_id: str
    template_name: str


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


@dataclass
class UpdateConditionDTO(CreateConditionDTO):
    condition_id: int
