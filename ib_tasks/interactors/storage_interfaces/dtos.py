from dataclasses import dataclass
from typing import List
from ib_tasks.constants.enum import PermissionTypes


@dataclass
class StageInformationDTO:
    stage_id: str
    task_template_id: str
    value: int
    stage_display_name: str
    stage_display_logic: str


@dataclass
class TaskStagesDTO:
    task_template_id: str
    stage_id: str


@dataclass
class StageActionsDTO:
    stage_id: str
    action_names: List[str]


@dataclass
class GoFDTO:
    gof_id: str
    gof_display_name: str
    task_template_id: str
    order: int
    max_columns: int
    enable_multiple_gofs: bool


@dataclass
class GoFRolesDTO:
    gof_id: str
    read_permission_roles: List
    write_permission_roles: List


@dataclass
class GoFRoleDTO:
    gof_id: str
    role: str
    permission_type: PermissionTypes


@dataclass
class CompleteGoFDetailsDTO:
    gof_dto: GoFDTO
    gof_roles_dto: GoFRolesDTO

