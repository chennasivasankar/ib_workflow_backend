from dataclasses import dataclass
from typing import Optional, List, Any

from ib_tasks.interactors.storage_interfaces.dtos \
    import StatusVariableDTO, GroupOfFieldsDTO, FieldValueDTO


@dataclass()
class RequestDTO:
    stage_id: str
    action_name: str
    logic: str
    role: str
    button_text: str
    button_color: Optional[str]


@dataclass()
class StageActionDTO(RequestDTO):
    pass


@dataclass()
class TaskTemplateStageActionDTO(RequestDTO):
    task_template_id: str


@dataclass()
class TaskGofAndStatusesDTO:
    task_id: str
    group_of_fields_dto: List[GroupOfFieldsDTO]
    fields_dto: List[FieldValueDTO]
    statuses_dto: List[StatusVariableDTO]