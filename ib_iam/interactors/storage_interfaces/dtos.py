from dataclasses import dataclass
from typing import List


@dataclass
class TeamNameAndDescriptionDTO:
    name: str
    description: str


@dataclass
class TeamDetailsWithUserIdsDTO(TeamNameAndDescriptionDTO):
    user_ids: List[str]


@dataclass
class TeamWithUserIdsDTO(TeamDetailsWithUserIdsDTO):
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
class TeamMemberIdsDTO:
    team_id: str
    member_ids: List[str]


@dataclass
class TeamsWithTotalTeamsCountDTO:
    total_teams_count: int
    teams: List[TeamDTO]


@dataclass
class MemberDTO:
    member_id: str
    name: str
    profile_pic_url: str


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
class CompanyDetailsWithUserIdsDTO(CompanyNameLogoAndDescriptionDTO):
    user_ids: List[str]


@dataclass
class CompanyWithUserIdsDTO(CompanyDetailsWithUserIdsDTO):
    company_id: str
