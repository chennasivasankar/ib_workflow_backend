from dataclasses import dataclass
from typing import List, Optional, Any

from ib_tasks.interactors.storage_interfaces.dtos \
    import StatusVariableDTO, GroupOfFieldsDTO, FieldValueDTO


@dataclass()
class StageActionDTO:
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
class FieldDisplayDTO:
    field_id: str
    field_type: str
    key: str
    value: Any
