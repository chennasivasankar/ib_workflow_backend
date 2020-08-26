from dataclasses import dataclass
from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.storage_interfaces.dtos \
    import UserTeamDTO, UserRoleDTO, UserCompanyDTO, \
    CompanyIdAndNameDTO, RoleIdAndNameDTO, BasicUserDetailsDTO, \
    TeamIdAndNameDTO, TeamUserIdsDTO, TeamDTO, ProjectDTO, ProjectTeamIdsDTO


@dataclass
class ListOfCompleteUsersDTO:
    users: List[UserProfileDTO]
    teams: List[UserTeamDTO]
    # roles: List[UserRoleDTO]
    companies: List[UserCompanyDTO]
    total_no_of_users: int


@dataclass
class ListOfCompleteUsersWithRolesDTO:
    users: List[UserProfileDTO]
    teams: List[UserTeamDTO]
    roles: List[UserRoleDTO]
    companies: List[UserCompanyDTO]
    total_no_of_users: int


@dataclass
class UserOptionsDetailsDTO:
    companies: List[CompanyIdAndNameDTO]
    teams: List[TeamIdAndNameDTO]
    roles: List[RoleIdAndNameDTO]


@dataclass
class TeamWithUsersDetailsDTO:
    total_teams_count: int
    team_dtos: List[TeamDTO]
    team_user_ids_dtos: List[TeamUserIdsDTO]
    user_dtos: List[BasicUserDetailsDTO]


@dataclass
class ProjectWithTeamsDTO:
    total_projects_count: int
    project_dtos: List[ProjectDTO]
    project_team_ids_dtos: List[ProjectTeamIdsDTO]
    team_dtos: List[TeamDTO]
