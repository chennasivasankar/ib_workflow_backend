from dataclasses import dataclass
from typing import Any, Optional, Union, List

from ib_tasks.constants.enum import FieldTypes, PermissionTypes


@dataclass
class FieldValueDTO:
    database_id: int
    gof_database_id: int
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
    order: int


@dataclass()
class FieldNameDTO:
    field_id: str
    gof_id: str
    field_display_name: str


@dataclass()
class FieldDisplayNameDTO:
    field_id: str
    field_display_name: str


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
class FieldCompleteDetailsDTO:
    field_id: str
    field_type: FieldTypes
    required: bool
    field_values: Optional[str]
    allowed_formats: Optional[str]
    validation_regex: Optional[str]


@dataclass
class FieldDetailsDTO:
    field_type: str
    field_id: str
    key: str
    value: str


@dataclass
class FieldDetailsDTOWithTaskId(FieldDetailsDTO):
    field_values: str
    task_id: int


@dataclass
class TaskAndFieldsDTO:
    task_id: int
    field_dtos: List[FieldDetailsDTO]


@dataclass
class UserFieldPermissionDTO:
    field_id: str
    permission_type: PermissionTypes


@dataclass
class TaskTemplateStageFieldsDTO:
    task_template_id: str
    task_id: int
    stage_id: str
    display_name: str
    db_stage_id: int
    stage_color: str
    field_ids: List[str]


@dataclass
class StageTaskFieldsDTO:
    task_id: int
    stage_id: str
    field_ids: List[str]


@dataclass
class FieldPermissionDTO:
    field_dto: FieldDTO
    is_field_writable: bool


@dataclass
class FieldIdWithGoFIdDTO:
    field_id: str
    gof_id: str


@dataclass
class FieldWritePermissionRolesDTO:
    field_id: str
    write_permission_roles: List[str]


@dataclass
class FieldIdWithFieldDisplayNameDTO:
    field_id: str
    gof_display_name: str
    field_display_name: str


@dataclass
class FieldTypeDTO:
    field_id: str
    field_type: FieldTypes
