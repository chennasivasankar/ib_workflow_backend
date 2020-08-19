from dataclasses import dataclass
from datetime import datetime

from ib_utility_tools.constants.enum import EntityType, TimerEntityType


@dataclass
class EntityDTO:
    entity_id: str
    entity_type: EntityType


@dataclass
class ChecklistItemDTO:
    text: str
    is_checked: str


@dataclass
class ChecklistItemWithIdDTO(ChecklistItemDTO):
    checklist_item_id: str


@dataclass
class ChecklistItemWithChecklistIdDTO(ChecklistItemDTO):
    checklist_id: str


@dataclass
class ChecklistItemWithEntityDTO(EntityDTO):
    text: str
    is_checked: str


@dataclass
class TimerEntityDTO:
    entity_id: str = None
    entity_type: TimerEntityType = None


@dataclass
class TimerDetailsDTO(TimerEntityDTO):
    duration_in_seconds: int = 0
    is_running: bool = False
    start_datetime: datetime = None
