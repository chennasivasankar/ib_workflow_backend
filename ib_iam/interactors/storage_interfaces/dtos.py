import uuid
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class UserDTO:
    user_id: str
    is_admin: bool
    company_id: Optional[str] = None


@dataclass
class CompanyIdAndNameDTO:
    company_id: str
    company_name: str


@dataclass
class TeamIdAndNameDTO:
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


@dataclass
class TeamNameAndDescriptionDTO:
    name: str
    description: str


@dataclass
class TeamWithUserIdsDTO(TeamNameAndDescriptionDTO):
    user_ids: List[str]


@dataclass
class TeamWithTeamIdAndUserIdsDTO(TeamWithUserIdsDTO):
    team_id: str


@dataclass
class PaginationDTO:
    limit: int
    offset: int


@dataclass
class TeamDTO:
    team_id: str
    name: str
    description: str


@dataclass
class TeamUserIdsDTO:
    team_id: str
    user_ids: List[str]


@dataclass
class TeamsWithTotalTeamsCountDTO:
    total_teams_count: int
    teams: List[TeamDTO]


@dataclass
class BasicUserDetailsDTO:
    user_id: str
    name: str
    profile_pic_url: str


@dataclass
class UserIdAndNameDTO:
    user_id: str
    name: str


@dataclass
class EmployeeDTO:
    employee_id: str
    name: str
    profile_pic_url: str


@dataclass
class CompanyNameLogoAndDescriptionDTO:
    name: str
    description: str
    logo_url: str


@dataclass
class CompanyDTO(CompanyNameLogoAndDescriptionDTO):
    company_id: str


@dataclass
class CompanyIdWithEmployeeIdsDTO:
    company_id: str
    employee_ids: List[str]


@dataclass
class CompanyWithUserIdsDTO(CompanyNameLogoAndDescriptionDTO):
    user_ids: List[str]


@dataclass
class CompanyWithCompanyIdAndUserIdsDTO(CompanyWithUserIdsDTO):
    company_id: str
