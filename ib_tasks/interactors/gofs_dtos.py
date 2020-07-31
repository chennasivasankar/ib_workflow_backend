from dataclasses import dataclass
from typing import List, Any

from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldValueDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GroupOfFieldsDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import StatusVariableDTO


@dataclass()
class TaskGofAndStatusesDTO:
    task_id: int
    group_of_fields_dto: List[GroupOfFieldsDTO]
    fields_dto: List[FieldValueDTO]
    statuses_dto: List[StatusVariableDTO]


@dataclass()
class TaskStatusVariablesDTO:
    task_id: int
    status_variables_dto: List[StatusVariableDTO]


@dataclass
class GoFWithOrderAndAddAnotherDTO:
    gof_id: str
    order: int
    enable_add_another_gof: bool


@dataclass
class GoFsWithTemplateIdDTO:
    template_id: str
    gof_dtos: List[GoFWithOrderAndAddAnotherDTO]


@dataclass()
class FieldDisplayDTO:
    field_id: int
    stage_id: str
    field_type: str
    key: str
    value: Any