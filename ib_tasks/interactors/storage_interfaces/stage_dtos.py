from dataclasses import dataclass
from typing import List, Any

from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO, ActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO


@dataclass
class StageActionNamesDTO:
    stage_id: str
    action_names: List[str]


@dataclass
class StageLogicAttributes:
    stage_id: str
    status_id: str


@dataclass
class TaskStagesDTO:
    task_template_id: str
    stage_id: str


@dataclass
class ValidStageDTO:
    stage_id: str
    id: int


@dataclass
class StageDTO:
    stage_id: str
    task_template_id: str
    value: int
    stage_display_name: str
    stage_display_logic: str



@dataclass
class TaskStageIdsDTO:
    task_id: str
    stage_id: str


@dataclass
class GetTaskStageCompleteDetailsDTO:
    task_id: int
    stage_id: str
    field_dtos: List[FieldDetailsDTO]
    action_dtos: List[ActionDetailsDTO]


@dataclass
class TaskTemplateStageDTO:
    task_id: int
    task_template_id: str
    stage_id: str


@dataclass
class StageValueDTO:
    stage_id: str
    value: Any


@dataclass
class StageDetailsDTO:
    stage_id: str
    name: str


@dataclass()
class StageDisplayValueDTO:
    stage_id: str
    display_logic: str
    value: int
