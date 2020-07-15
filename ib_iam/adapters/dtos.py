from dataclasses import dataclass

@dataclass
class BasicUserDTO:
    user_id: str
    name: str
    profile_pic_url: str