from dataclasses import dataclass
from typing import Optional


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: Optional[str] = None
    profile_pic_url: Optional[str] = None
    is_admin: Optional[bool] = False
    is_email_verify: Optional[bool] = None


@dataclass
class SearchQueryWithPaginationDTO:
    limit: int
    offset: int
    search_query: str
