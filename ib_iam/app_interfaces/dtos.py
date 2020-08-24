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
