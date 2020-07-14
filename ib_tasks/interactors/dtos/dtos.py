from typing import Union, List, Optional
from dataclasses import dataclass
from ib_tasks.constants.enum import FieldTypes


@dataclass
class FieldDTO:
    field_id: int
    field_display_name: str
    field_type: FieldTypes
    field_values: Optional[Union[int, str, float, List[str]]]
    required: bool
    read_permissions_to_roles: List[str]
    write_permissions_to_roles: List[str]
    help_text: Optional[str]
    tool_tip: Optional[str]
    placeholder_text: Optional[str]
    error_message: Optional[str]


