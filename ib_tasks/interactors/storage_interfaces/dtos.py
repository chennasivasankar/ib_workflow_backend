from dataclasses import dataclass
from typing import List, Union


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
class StageActionsDto:
    stage_id: str
    action_names: List[str]


@dataclass
class GOFDTO:
    gof_id: str
    gof_display_name: str
    read_permission_roles: Union[List, str]
    write_permission_roles: Union[List, str]
    field_ids: List[str]