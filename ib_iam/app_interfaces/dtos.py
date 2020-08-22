from dataclasses import dataclass
from typing import Union

from ib_iam.constants.enums import Searchable


@dataclass
class SearchableDTO:
    search_type: Searchable
    id: Union[int, str]
