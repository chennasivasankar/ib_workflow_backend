from dataclasses import dataclass
from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.storage_interfaces.dtos \
    import UserTeamDTO, UserRoleDTO, UserCompanyDTO, \
    CompanyDTO, TeamIdAndNameDTO, RoleIdAndNameDTO


@dataclass
class CompleteUsersDetailsDTO:
    users: List[UserProfileDTO]
    teams: List[UserTeamDTO]
    roles: List[UserRoleDTO]
    companies: List[UserCompanyDTO]
    total_no_of_users: int


@dataclass
class UserOptionsDetails:
    companies: List[CompanyDTO]
    teams: List[TeamIdAndNameDTO]
    roles: List[RoleIdAndNameDTO]


from ib_iam.interactors.storage_interfaces.dtos import (
    BasicUserDetailsDTO, TeamIdAndNameDTO, TeamUserIdsDTO
)


@dataclass
class TeamWithMembersDetailsDTO:
    total_teams_count: int
    team_dtos: List[TeamIdAndNameDTO]
    team_user_ids_dtos: List[TeamUserIdsDTO]
    member_dtos: List[BasicUserDetailsDTO]
