from dataclasses import dataclass
from typing import List

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.interactors.storage_interfaces.dtos import \
    CompleteDiscussionDTO


@dataclass
class DiscussionsDetailsDTO:
    complete_discussion_dtos: List[CompleteDiscussionDTO]
    user_profile_dtos: List[UserProfileDTO]
    total_count: int
