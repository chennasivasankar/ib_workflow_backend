from dataclasses import dataclass

from ib_utility_tools.constants.enum import EntityType


@dataclass
class EntityDetailsDTO:
    entity_id: str
    entity_type: EntityType


@dataclass
class ChecklistItemWithEntityDetailsDTO(EntityDetailsDTO):
    text: str
    is_checked: bool


@dataclass
class ChecklistItemWithItemIdDTO:
    checklist_item_id: str
    text: str
    is_checked: bool
