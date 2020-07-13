from dataclasses import dataclass
from typing import List, Union


@dataclass
class GOFDTO:
    gof_id: str
    gof_display_name: str
    read_permission_roles: Union[List, str]
    write_permission_roles: Union[List, str]
    field_ids: List[str]
