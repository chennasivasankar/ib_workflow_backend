from dataclasses import dataclass
from typing import Any, Optional, Union, List

from ib_tasks.constants.enum import FieldTypes, PermissionTypes


@dataclass
class FieldValueDTO:
    database_id: str
    gof_database_id: str
    field_id: str
    value: Any


@dataclass
class FieldDTO:
    gof_id: str
    field_id: str
    field_display_name: str
    field_type: FieldTypes
    field_values: Optional[Union[str, List[str]]]
    required: bool
    help_text: Optional[str]
    tooltip: Optional[str]
    placeholder_text: Optional[str]
    error_message: Optional[str]
    allowed_formats: Optional[List[str]]
    validation_regex: Optional[str]


@dataclass
class FieldRolesDTO:
    field_id: str
    write_permission_roles: List[str]
    read_permission_roles: List[str]


@dataclass
class FieldRoleDTO:
    field_id: str
    role: str
    permission_type: PermissionTypes


@dataclass
class FieldDetailsDTO:
    field_id: str
    field_type: FieldTypes
    required: bool
    field_values: Optional[str]
    allowed_formats: Optional[str]
    validation_regex: Optional[str]


@dataclass
class UserFieldPermissionDTO:
    field_id: str
    permission_type: PermissionTypes
