from dataclasses import dataclass
from typing import Union, List

from ib_iam.constants.enums import Searchable
from ib_iam.interactors.storage_interfaces.dtos import TeamIdAndNameDTO


@dataclass
class SearchableDTO:
    search_type: Searchable
    id: Union[int, str]


@dataclass
class UserTeamsDTO:
    user_id: str
    user_teams: List[TeamIdAndNameDTO]


@dataclass
class ProjectTeamUserDTO:
    project_id: str
    team_id: str
    user_id: str


@dataclass
class UserIdWithTeamIDAndNameDTO:
    team_id: str
    user_id: str
    name: str
