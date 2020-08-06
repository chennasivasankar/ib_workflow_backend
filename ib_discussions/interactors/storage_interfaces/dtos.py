from dataclasses import dataclass
from datetime import datetime


@dataclass
class DiscussionDTO:
    user_id: str
    discussion_id: str
    discussion_set_id: str
    description: str
    title: str
    created_at: datetime
    is_clarified: bool


@dataclass
class CommentIdWithRepliesCountDTO:
    comment_id: str
    replies_count: int


@dataclass
class CommentDTO:
    comment_id: str
    comment_content: str
    user_id: str
    created_at: datetime
    parent_comment_id: str = None


@dataclass
class CommentIdWithRepliesCountDTO:
    comment_id: str
    replies_count: int
