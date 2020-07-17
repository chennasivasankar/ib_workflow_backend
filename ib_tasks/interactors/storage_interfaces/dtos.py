from typing import List, Any
from dataclasses import dataclass


@dataclass
class StageActionNamesDTO:
    stage_id: str
    action_names: List[str]


@dataclass()
class FieldValueDTO:
    database_id: str
    gof_database_id: str
    field_id: str
    value: Any


@dataclass()
class StatusVariableDTO:
    status_id: str
    status_variable: str
    value: str


@dataclass()
class GroupOfFieldsDTO:
    database_id: str
    group_of_field_id: str


@dataclass()
class TaskGofAndStatusesDTO:
    task_id: str
    group_of_fields_dto: List[GroupOfFieldsDTO]
    fields_dto: List[FieldValueDTO]
    statuses_dto: List[StatusVariableDTO]
