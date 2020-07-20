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
