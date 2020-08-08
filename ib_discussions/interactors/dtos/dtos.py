from dataclasses import dataclass

from ib_discussions.constants.enum import EntityType, FilterByEnum, SortByEnum, \
    OrderByEnum, MultiMediaFormatEnum


@dataclass
class DiscussionWithEntityDetailsDTO:
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


@dataclass
class FilterByDTO:
    filter_by: FilterByEnum
    value: [str, bool]


@dataclass
class SortByDTO:
    sort_by: SortByEnum
    order: OrderByEnum


@dataclass
class DiscussionIdWithTitleAndDescriptionDTO:
    discussion_id: str
    title: str
    description: str


@dataclass
class MultiMediaDTO:
    format_type: MultiMediaFormatEnum
    url: str
