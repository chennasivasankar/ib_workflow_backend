from dataclasses import dataclass
from typing import Optional


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: Optional[str] = None
    profile_pic_url: Optional[str] = None
    is_admin: bool = False


@dataclass
class CurrentAndNewPasswordDTO:
    current_password: str
    new_password: str
