from dataclasses import dataclass
from typing import List, Optional

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.dtos.dtos import CompleteUserProfileDTO
from ib_iam.interactors.storage_interfaces.dtos \
    import TeamWithUserIdDTO, UserRoleDTO, UserCompanyDTO, \
    CompanyIdAndNameDTO, RoleIdAndNameDTO, BasicUserDetailsDTO, \
    TeamIdAndNameDTO, TeamUserIdsDTO, TeamDTO, ProjectTeamIdsDTO, \
    ProjectRoleDTO, ProjectWithDisplayIdDTO, CompanyDTO, \
    CompanyIdWithEmployeeIdsDTO


@dataclass
class ListOfCompleteUsersWithRolesDTO:
    users: List[UserProfileDTO]
    teams: List[TeamWithUserIdDTO]
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
class ProjectsWithTeamsAndRolesDTO:
    total_projects_count: int
    project_dtos: List[ProjectWithDisplayIdDTO]
    project_team_ids_dtos: List[ProjectTeamIdsDTO]
    team_dtos: List[TeamDTO]
    project_role_dtos: List[ProjectRoleDTO]


@dataclass
class CompanyWithEmployeeIdsAndUserDetailsDTO:
    company_dtos: List[CompanyDTO]
    company_id_with_employee_ids_dtos: List[CompanyIdWithEmployeeIdsDTO]
    user_dtos: List[BasicUserDetailsDTO]


@dataclass
class UserWithExtraDetailsDTO:
    user_profile_dto: CompleteUserProfileDTO
    company_dto: Optional[CompanyDTO]
    team_dtos: List[TeamDTO]
    team_user_ids_dto: List[TeamUserIdsDTO]
    company_id_with_employee_ids_dto: Optional[CompanyIdWithEmployeeIdsDTO]
    user_dtos: List[UserProfileDTO]
    role_dtos: List[UserRoleDTO]
