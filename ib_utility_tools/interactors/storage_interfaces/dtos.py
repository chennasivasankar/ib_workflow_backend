from dataclasses import dataclass

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
    entity_id: str
    entity_type: TimerEntityType


@dataclass
class TimerDetailsDTO:
    duration_in_seconds: int
    is_running: bool