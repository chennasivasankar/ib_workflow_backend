from dataclasses import dataclass

from ib_discussions.constants.enum import EntityType


@dataclass
class DiscussionDTO:
    user_id: str
    entity_id: str
    entity_type: EntityType
    title: str
    description: str