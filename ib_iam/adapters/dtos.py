from dataclasses import dataclass
from typing import Optional


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: str
    profile_pic_url: Optional[str] = None
    is_admin: bool = False
