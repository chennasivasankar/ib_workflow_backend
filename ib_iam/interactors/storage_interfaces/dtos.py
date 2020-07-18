from dataclasses import dataclass
from typing import List


@dataclass
class AddTeamParametersDTO:
    name: str
    description: str


@dataclass
class PaginationDTO:
    limit: int
    offset: int


@dataclass
class BasicTeamDTO:
    team_id: str
    name: str
    description: str


@dataclass
class TeamMembersDTO:
    team_id: str
    member_ids: List[str]


@dataclass
class MemberDTO:
    member_id: str
    name: str
    profile_pic_url: str


@dataclass
class UpdateTeamParametersDTO:
    team_id: str
    name: str
    description: str

@dataclass
class BasicCompanyDTO:
    company_id: str
    name: str
    description: str
    logo: str

@dataclass
class CompanyWithEmployeeCountDTO:
    company_id: str
    no_of_employees: int
