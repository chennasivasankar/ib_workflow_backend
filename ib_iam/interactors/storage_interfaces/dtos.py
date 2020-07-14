from dataclasses import dataclass


@dataclass
class RoleDTO:
    role_id: str
    role_name: str
    role_description: str
