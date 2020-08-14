from dataclasses import dataclass
from typing import Optional


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: Optional[str] = None
    profile_pic_url: Optional[str] = None
    cover_page_url: Optional[str] = ""
    is_admin: bool = False


@dataclass
class SearchQueryWithPaginationDTO:
    limit: int
    offset: int
    search_query: str
