import uuid
from dataclasses import dataclass
from typing import Optional, List, Union

from ib_iam.constants.enums import Searchable


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    email: str
    profile_pic_url: str


@dataclass
class UserDTO:
    user_id: str
    is_admin: bool
    company_id: Optional[str] = None
    cover_page_url: Optional[str] = None


@dataclass
class CompanyIdAndNameDTO:
    company_id: str
    company_name: str


@dataclass
class TeamIdAndNameDTO:
    team_id: str
    team_name: str


@dataclass
class RoleIdAndNameDTO:
    role_id: str
    name: str


@dataclass
class UserTeamDTO:
    user_id: str
    team_id: str
    team_name: str


@dataclass
class UserCompanyDTO:
    user_id: str
    company_id: Optional[str] = None
    company_name: Optional[str] = None


@dataclass
class UserRoleDTO:
    user_id: uuid.uuid4
    role_id: str
    name: str
    description: str = None


@dataclass
class RoleDTO:
    role_id: str
    name: str
    description: Optional[str]


@dataclass
class TeamNameAndDescriptionDTO:
    name: str
    description: str


@dataclass
class TeamWithUserIdsDTO(TeamNameAndDescriptionDTO):
    user_ids: List[str]


@dataclass
class TeamWithTeamIdAndUserIdsDTO(TeamWithUserIdsDTO):
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
class TeamUserIdsDTO:
    team_id: str
    user_ids: List[str]


@dataclass
class TeamsWithTotalTeamsCountDTO:
    total_teams_count: int
    teams: List[TeamDTO]


@dataclass
class BasicUserDetailsDTO:
    user_id: str
    name: str
    profile_pic_url: str = None


@dataclass
class UserIdAndNameDTO:
    user_id: str
    name: str


@dataclass
class EmployeeDTO:
    employee_id: str
    name: str
    profile_pic_url: str


@dataclass
class CompanyNameLogoAndDescriptionDTO:
    name: str
    description: Optional[str]
    logo_url: Optional[str]


@dataclass
class CompanyDTO:
    company_id: str
    name: str
    description: str
    logo_url: Optional[str]


@dataclass
class CompanyIdWithEmployeeIdsDTO:
    company_id: str
    employee_ids: List[str]


@dataclass
class CompanyWithUserIdsDTO:
    user_ids: List[str]
    name: str
    description: str
    logo_url: Optional[str]


@dataclass
class CompanyWithCompanyIdAndUserIdsDTO:
    company_id: str
    name: str
    description: str
    logo_url: Optional[str]
    user_ids: List[str]


@dataclass
class TeamMemberLevelDetailsDTO:
    team_member_level_id: str
    team_member_level_name: str
    level_hierarchy: int


@dataclass
class MemberDTO:
    member_id: str
    immediate_superior_team_user_id: str = None


@dataclass
class ProjectDTO:
    project_id: str
    display_id: str
    name: str
    description: Optional[str] = None
    logo_url: Optional[str] = None


@dataclass
class ProjectWithoutIdDTO:
    name: str
    display_id: str
    description: Optional[str] = None
    logo_url: Optional[str] = None


@dataclass
class SearchableDetailsDTO:
    search_type: Searchable
    id: Union[int, str]
    value: str


@dataclass
class ProjectTeamIdsDTO:
    project_id: str
    team_ids: List[str]


@dataclass
class ProjectsWithTotalCountDTO:
    total_projects_count: int
    projects: List[ProjectDTO]


@dataclass
class MemberIdWithSubordinateMemberIdsDTO:
    member_id: str
    subordinate_member_ids: List[str]


@dataclass
class ProjectRoleDTO:
    project_id: str
    role_id: str
    name: str
    description: Optional[str] = None


@dataclass
class RoleNameAndDescriptionDTO:
    name: str
    description: Optional[str] = None
