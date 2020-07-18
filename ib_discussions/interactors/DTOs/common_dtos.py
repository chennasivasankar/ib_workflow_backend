from dataclasses import dataclass

from ib_discussions.constants.enum import EntityType


@dataclass
class DiscussionDTO:
    user_id: str
    entity_id: str
    entity_type: EntityType
    title: str
    description: str


@dataclass
class EntityIdAndEntityTypeDTO:
    entity_id: str
    entity_type: EntityType


@dataclass
class OffsetAndLimitDTO:
    offset: int
    limit: int
