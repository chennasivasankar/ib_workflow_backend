from dataclasses import dataclass
from typing import List, Any, Optional

from ib_tasks.interactors.stages_dtos import StageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO
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
    task_id: int
    stage_id: str


@dataclass
class TaskWithDbStageIdDTO:
    task_id: int
    stage_id: int


@dataclass
class GetTaskStageCompleteDetailsDTO:
    task_id: int
    stage_id: str
    stage_color: str
    field_dtos: List[FieldDetailsDTO]
    action_dtos: List[StageActionDetailsDTO]


@dataclass
class TaskTemplateStageDTO:
    task_id: int
    task_template_id: str
    stage_id: str


@dataclass
class TaskTemplateWithStageColorDTO:
    task_id: int
    task_template_id: str
    stage_color: str
    stage_id: str


@dataclass
class StageValueDTO:
    stage_id: str
    value: Any


@dataclass
class TaskIdWithStageValueDTO:
    stage_value: int
    task_id: int


@dataclass
class StageValueWithTaskIdsDTO:
    task_ids: List[int]
    stage_value: int


@dataclass
class TaskStageAssigneeDTO:
    task_stage_id: int
    stage_id: int
    assignee_id: Optional[str]


@dataclass
class TaskIdWithStageDetailsDTO:
    # TODO refactor stage_id_db name after removal of stage_id
    db_stage_id: int
    task_id: int
    stage_id: str
    stage_display_name: str
    stage_color: str


@dataclass
class TaskWithCompleteStageDetailsDTO:
    task_with_stage_details_dto: TaskIdWithStageDetailsDTO
    stage_assignee_dto: Optional[StageAssigneeDetailsDTO]


@dataclass
class StageDetailsDTO:
    db_stage_id: int
    stage_id: str
    color: str
    name: str
    color: str


@dataclass()
class StageDisplayValueDTO:
    stage_id: str
    display_logic: str
    value: int


@dataclass
class StageRoleDTO:
    db_stage_id: int
    role_id: str


@dataclass
class StageIdWithRoleIdsAndAssigneeIdDTO:
    db_stage_id: int
    role_ids: List[str]
    assignee_id: str


@dataclass
class StageIdWithRoleIdsDTO:
    db_stage_id: int
    role_ids: List[str]


@dataclass
class StageIdWithTemplateIdDTO:
    template_id: str
    stage_id: int


@dataclass
class TaskStageHavingAssigneeIdDTO:
    db_stage_id: int
    assignee_id: str
    stage_display_name: str
