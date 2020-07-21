from dataclasses import dataclass
from typing import List
from ib_iam.interactors.storage_interfaces.dtos import (
    MemberDTO, TeamDTO, TeamMemberIdsDTO
)


@dataclass
class TeamWithMembersDetailsDTO:
    total_teams_count: int
    team_dtos: List[TeamDTO]
    team_member_ids_dtos: List[TeamMemberIdsDTO]
    member_dtos: List[MemberDTO]
