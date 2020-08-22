from dataclasses import dataclass
from typing import Union

from ib_iam.constants.enums import Searchable


@dataclass
class SearchableDTO:
    search_type: Searchable
    id: Union[int, str]


@dataclass
class ProjectTeamUserDTO:
    project_id: str
    team_id: str
    user_id: str
