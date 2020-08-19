from dataclasses import dataclass
from typing import Optional


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: Optional[str] = None
    profile_pic_url: Optional[str] = None


@dataclass
class SearchQueryWithPaginationDTO:
    limit: int
    offset: int
    search_query: str
