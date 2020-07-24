from dataclasses import dataclass
from typing import List

from ib_tasks.constants.enum import PermissionTypes


@dataclass()
class GroupOfFieldsDTO:
    database_id: str
    group_of_field_id: str


@dataclass
class GoFDTO:
    gof_id: str
    gof_display_name: str
    max_columns: int


@dataclass
class GoFRolesDTO:
    gof_id: str
    read_permission_roles: List[str]
    write_permission_roles: List[str]


@dataclass
class GoFRoleDTO:
    gof_id: str
    role: str
    permission_type: PermissionTypes


@dataclass
class CompleteGoFDetailsDTO:
    gof_dto: GoFDTO
    gof_roles_dto: GoFRolesDTO


@dataclass()
class GOFMultipleEnableDTO:
    group_of_field_id: str
    multiple_status: bool


@dataclass
class GoFToTaskTemplateDTO:
    gof_id: str
    template_id: str
    order: int
    enable_multiple_gofs: bool
