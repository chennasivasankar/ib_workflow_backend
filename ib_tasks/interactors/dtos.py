
from dataclasses import dataclass
from typing import Optional, List, Any, Union

from ib_tasks.interactors.storage_interfaces.dtos \
    import StatusVariableDTO, GroupOfFieldsDTO, FieldValueDTO

@dataclass
class StageLogicAttributes:
    stage_id: str
    status_id: str

@dataclass
class StageActionDTO:
    stage_id: str
    action_name: str
    logic: str
    roles: List[str]
    function_path: str
    button_text: str
    button_color: Optional[str]

@dataclass
class StageLogicAttributes:
    stage_id: str
    status_id: str

@dataclass
class StageDTO:
    stage_id: str
    task_template_id: str
    value: int
    id: Optional[int]
    stage_display_name: str
    stage_display_logic: str


@dataclass
class StagesActionDTO:
    stage_id: str
    action_name: str
    logic: str
    roles: List[str]
    function_path: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class TaskTemplateStageActionDTO(StageActionDTO):
    task_template_id: str

@dataclass
class StageLogicAttributes:
    stage_id: str
    status_id: str


@dataclass
class ActionDTO:
    stage_id: str
    action_name: str
    logic: str
    role: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class TaskTemplateStageDTO:
    task_template_id: str
    stage_id: str

@dataclass()
class TaskGofAndStatusesDTO:
    task_id: str
    group_of_fields_dto: List[GroupOfFieldsDTO]
    fields_dto: List[FieldValueDTO]
    statuses_dto: List[StatusVariableDTO]

@dataclass()
class TaskStatusVariablesDTO:
    task_id: str
    status_variables_dto: List[StatusVariableDTO]

@dataclass
class CreateTaskTemplateDTO:
    template_id: str
    template_name: str


@dataclass
class GlobalConstantsDTO:
    constant_name: str
    value: int


@dataclass
class GlobalConstantsWithTemplateIdDTO:
    template_id: str
    global_constants_dtos: List[GlobalConstantsDTO]


@dataclass
class GoFWithOrderAndAddAnotherDTO:
    gof_id: str
    order: int
    enable_add_another_gof: bool


@dataclass
class GoFsWithTemplateIdDTO:
    template_id: str
    gof_dtos: List[GoFWithOrderAndAddAnotherDTO]


@dataclass
class FieldValuesDTO:
    field_id: str
    field_value: Union[str, List[str], int]


@dataclass
class GoFFieldsDTO:
    gof_id: str
    field_values_dtos: List[FieldValuesDTO]


@dataclass
class TaskDTO:
    task_template_id: str
    gof_fields_dtos: List[GoFFieldsDTO]
