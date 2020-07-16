import uuid
from dataclasses import dataclass


@dataclass
class UserProfileDTO:
    user_id: str
    is_admin: bool
    company_id: str


@dataclass
class UserTeamDTO:
    user_id: str
    team_id: str
    team_name: str


@dataclass
class UserCompanyDTO:
    user_id: str
    company_id: str
    company_name: str


@dataclass
class UserRoleDTO:
    user_id: uuid.uuid4
    role_id: str
    role_name: str
    role_description: str
