from dataclasses import dataclass
from typing import List
from ib_iam.interactors.storage_interfaces.dtos import (
    MemberDTO, BasicTeamDTO, TeamMembersDTO
)


@dataclass
class TeamWithMembersDetailsDTO:
    team_dtos: List[BasicTeamDTO]
    team_member_ids_dtos: List[TeamMembersDTO]
    member_dtos: List[MemberDTO]
