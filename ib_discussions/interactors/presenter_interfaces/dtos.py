import datetime
from dataclasses import dataclass
from typing import List

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.interactors.storage_interfaces.dtos import \
    DiscussionDTO


@dataclass
class DiscussionsWithUsersAndDiscussionCountDTO:
    discussion_dtos: List[DiscussionDTO]
    user_profile_dtos: List[UserProfileDTO]
    total_count: int


@dataclass
class CommentIdWithEditableStatusDTO:
    comment_id: str
    is_editable: bool


@dataclass
class CommentWithRepliesCountAndEditableDTO:
    comment_id: str
    comment_content: str
    user_id: str
    created_at: datetime
    replies_count: int
    is_editable: bool


@dataclass
class DiscussionIdWithEditableStatusDTO:
    discussion_id: str
    is_editable: bool