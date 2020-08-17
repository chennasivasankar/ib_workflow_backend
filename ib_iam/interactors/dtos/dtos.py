from dataclasses import dataclass
from typing import List


@dataclass
class UserIdWithRoleIdsDTO:
    user_id: str
    role_ids: List[str]


@dataclass
class AddUserDetailsDTO:
    name: str
    email: str
    team_ids: List[str]
    role_ids: List[str]
    company_id: str


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
