from dataclasses import dataclass
from typing import List, Union


@dataclass
class GoFDTO:
    gof_id: str
    gof_display_name: str
    task_template_id: str
    order: int
    max_columns: int


@dataclass
class GoFRolesDTO:
    gof_id: str
    read_permission_roles: List
    write_permission_roles: List

@dataclass
class GoFFieldsDTO:
    gof_id: str
    field_ids: List[str]

@dataclass
class GoFCompleteDetailsDTO:
    gof_dto: GoFDTO
    gof_roles_dto: GoFRolesDTO
    gof_fields_dto: GoFFieldsDTO
