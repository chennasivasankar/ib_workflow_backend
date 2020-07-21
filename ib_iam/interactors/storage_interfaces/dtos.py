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
class CompanyDTO:
    company_id: str
    name: str
    description: str
    logo_url: str


@dataclass
class CompanyWithTotalCompaniesCountDTO:
    company_dtos: List[CompanyDTO]
    total_companies_count: int
