from dataclasses import dataclass


@dataclass
class RoleDto:
    role_id: str
    role_name: str
    role_description: str