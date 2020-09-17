from dataclasses import dataclass
from typing import Optional


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: Optional[str] = None
    profile_pic_url: Optional[str] = None
    is_admin: Optional[bool] = False
    is_email_verified: Optional[bool] = None


@dataclass
class SearchQueryWithPaginationDTO:
    limit: int
    offset: int
    search_query: str


@dataclass
class EmailAndPasswordDTO:
    email: str
    password: str


@dataclass
class UserTokensDTO:
    access_token: str
    refresh_token: str
    expires_in_seconds: int
    user_id: str
