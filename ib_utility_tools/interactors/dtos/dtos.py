from dataclasses import dataclass

from ib_utility_tools.constants.enum import EntityType


@dataclass
class ChecklistItemWithEntityDetailsDTO:
    user_id: str
    entity_id: str
    entity_type: EntityType
    text: str
