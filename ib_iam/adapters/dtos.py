from dataclasses import dataclass

@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    profile_pic_url: str