from dataclasses import dataclass


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: str
