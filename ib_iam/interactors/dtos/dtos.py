from dataclasses import dataclass
from typing import List

from ib_iam.constants.enums import SearchType


@dataclass
class UserIdWithRoleIdsDTO:
    user_id: str
    role_ids: List[str]


@dataclass
class UserWithTeamIdsANDRoleIdsAndCompanyIdsDTO:
    name: str
    email: str
    team_ids: List[str]
    role_ids: List[str]
    company_id: str


@dataclass
class SearchQueryAndTypeDTO:
    search_type: SearchType
    search_query: str = ""
