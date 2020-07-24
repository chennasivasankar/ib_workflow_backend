from dataclasses import dataclass


@dataclass
class UserDTO:
    user_id: str
    name: str
