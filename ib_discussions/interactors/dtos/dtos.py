from dataclasses import dataclass
from typing import List

from ib_discussions.constants.enum import EntityType, FilterByEnum, SortByEnum, \
    OrderByEnum, MultimediaFormat


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
class MultimediaDTO:
    format_type: MultimediaFormat
    url: str
    thumbnail_url: str


@dataclass
class UpdateCompleteCommentDTO:
    comment_id: str
    user_id: str
    comment_content: str
    mention_user_ids: List[str]
    multimedia_dtos: List[MultimediaDTO]


@dataclass
class CreateCompleteCommentDTO:
    discussion_id: str
    user_id: str
    comment_content: str
    mention_user_ids: List[str]
    multimedia_dtos: List[MultimediaDTO]
