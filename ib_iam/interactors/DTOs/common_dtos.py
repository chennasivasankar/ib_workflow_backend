from dataclasses import dataclass
from typing import List


@dataclass
class UserIdWithRoleIdsDTO:
    user_id: str
    role_ids: List[str]


@dataclass
class UserDetailsWithTeamRoleAndCompanyIdsDTO:
    name: str
    email: str
    team_ids: List[str]
    role_ids: List[str]
    company_id: str