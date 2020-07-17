from dataclasses import dataclass


@dataclass
class RoleDTO:
    role_id: str
    name: str
    description: str
