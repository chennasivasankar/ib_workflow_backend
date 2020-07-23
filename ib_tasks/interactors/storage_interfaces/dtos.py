



from typing import List, Union, Optional, Any
from dataclasses import dataclass
from typing import List, Union, Optional
from ib_tasks.constants.enum import FieldTypes, PermissionTypes


@dataclass
class StageActionNamesDTO:
    stage_id: str
    action_names: List[str]


@dataclass()
class GOFMultipleEnableDTO:
    group_of_field_id: str
    multiple_status: bool


@dataclass
class StageLogicAttributes:
    stage_id: str
    status_id: str


@dataclass()
class FieldValueDTO:
    database_id: str
    gof_database_id: str
    field_id: str
    value: Any


@dataclass()
class StatusVariableDTO:
    status_id: int
    status_variable: str
    value: str


@dataclass()
class GroupOfFieldsDTO:
    database_id: str
    group_of_field_id: str


@dataclass()
class GOFMultipleStatusDTO:
    group_of_field_id: str
    multiple_status: bool


@dataclass()
class ActionDTO:
    action_id: int
    name: str
    stage_id: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class ActionRolesDTO:
    action_id: int
    roles: List[str]


@dataclass
class TaskStagesDTO:
    task_template_id: str
    stage_id: str

@dataclass
class ValidStageDTO:
    stage_id: str
    id: int


@dataclass
class StageActionNamesDTO:
    stage_id: str
    action_names: List[str]


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
class StageDTO:
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
class TaskStatusDTO:
    task_template_id: str
    status_variable_id: str