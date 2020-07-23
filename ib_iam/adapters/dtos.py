from dataclasses import dataclass


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: str
    profile_pic_url: str
    is_admin: bool = False

