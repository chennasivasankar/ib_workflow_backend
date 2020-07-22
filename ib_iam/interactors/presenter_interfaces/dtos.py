from dataclasses import dataclass
from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.storage_interfaces.dtos \
    import UserTeamDTO, UserRoleDTO, UserCompanyDTO, \
    CompanyDTO, TeamDTO, RoleIdAndNameDTO


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
    teams: List[TeamDTO]
    roles: List[RoleIdAndNameDTO]
