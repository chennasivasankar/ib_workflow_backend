from dataclasses import dataclass
from typing import Optional

from ib_iam.constants.enums import Searchable


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: Optional[str] = None
    profile_pic_url: Optional[str] = None
    is_admin: bool = False


@dataclass
class SearchQueryWithPaginationDTO:
    limit: int
    offset: int
    search_query: str
