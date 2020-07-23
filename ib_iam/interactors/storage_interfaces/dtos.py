import uuid
from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDTO:
    user_id: str
    is_admin: bool
    company_id: Optional[str]


@dataclass
class CompanyDTO:
    company_id: str
    company_name: str


@dataclass
class TeamDTO:
    team_id: str
    team_name: str


@dataclass
class RoleIdAndNameDTO:
    role_id: str
    name: str


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
    name: str
    description: str


@dataclass
class RoleDTO:
    role_id: str
    name: str
    description: str
