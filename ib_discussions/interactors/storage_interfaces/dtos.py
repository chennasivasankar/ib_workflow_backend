from dataclasses import dataclass
from datetime import datetime


@dataclass
class CompleteDiscussionDTO:
    user_id: str
    discussion_id: str
    discussion_set_id: str
    description: str
    title: str
    created_at: datetime
    is_clarified: bool
