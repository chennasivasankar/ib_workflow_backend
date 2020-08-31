from dataclasses import dataclass
from typing import List, Optional

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.storage_interfaces.dtos import MemberDTO, \
    TeamMemberLevelDetailsDTO, MemberIdWithSubordinateMemberIdsDTO, \
    RoleNameAndDescriptionDTO, RoleDTO


@dataclass
class UserIdWithRoleIdsDTO:
    user_id: str
    role_ids: List[str]


@dataclass
class AddUserDetailsDTO:
    name: str
    email: str
    team_ids: List[str]
    # role_ids: List[str]
    company_id: str


@dataclass
class CompleteUserProfileDTO:
    user_id: str
    name: str
    email: str
    is_admin: Optional[bool] = None
    profile_pic_url: Optional[str] = None
    cover_page_url: Optional[str] = ""


@dataclass
class TeamMemberLevelDTO:
    team_member_level_name: str
    level_hierarchy: int


@dataclass
class TeamMemberLevelIdWithMemberIdsDTO:
    team_member_level_id: str
    member_ids: List[str]


@dataclass
class ImmediateSuperiorUserIdWithUserIdsDTO:
    immediate_superior_user_id: str
    member_ids: List[str]


@dataclass
class CompleteTeamMemberLevelsDetailsDTO:
    member_dtos: List[MemberDTO]
    user_profile_dtos: List[UserProfileDTO]
    team_member_level_details_dtos: List[TeamMemberLevelDetailsDTO]
    team_member_level_id_with_member_ids_dtos: List[
        TeamMemberLevelIdWithMemberIdsDTO]
    member_id_with_subordinate_member_ids_dtos: List[
        MemberIdWithSubordinateMemberIdsDTO]


@dataclass
class ProjectWithTeamIdsAndRolesDTO:
    name: str
    display_id: str
    team_ids: List[str]
    roles: List[RoleNameAndDescriptionDTO]
    description: Optional[str] = None
    logo_url: Optional[str] = None


@dataclass
class CompleteProjectDetailsDTO:
    project_id: str
    name: str
    team_ids: List[str]
    roles: List[RoleDTO]
    description: Optional[str] = None
    logo_url: Optional[str] = None
