from dataclasses import dataclass
from typing import List, Any, Optional

from ib_tasks.adapters.dtos import AssigneeDetailsDTO
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO


@dataclass
class StageAssigneeDetailsDTO:
    task_stage_id: int
    stage_id: int
    assignee_details_dto: Optional[AssigneeDetailsDTO]


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
    task_display_id: Optional[str]
    stage_id: str


@dataclass
class TaskWithDbStageIdDTO:
    task_id: int
    db_stage_id: int



@dataclass
class GetTaskStageCompleteDetailsDTO:
    task_id: int
    stage_id: str
    stage_color: str
    display_name: str
    db_stage_id: int
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
    team_id: Optional[str]


@dataclass
class TaskIdWithStageDetailsDTO:
    # TODO refactor stage_id_db name after removal of stage_id
    db_stage_id: int
    task_id: int
    task_display_id: str
    stage_id: str
    stage_display_name: str
    stage_color: str


@dataclass
class TaskWithCompleteStageDetailsDTO:
    task_with_stage_details_dto: TaskIdWithStageDetailsDTO
    stage_assignee_dto: List[TaskStageAssigneeDetailsDTO]


@dataclass
class StageDetailsDTO:
    db_stage_id: int
    stage_id: str
    color: str
    name: str


@dataclass()
class StageDisplayValueDTO:
    stage_id: str
    display_logic: str
    value: int


@dataclass()
class StageDisplayDTO:
    stage_id: str
    display_value: str


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


@dataclass
class CurrentStageDetailsDTO:
    stage_id: str
    stage_display_name: str


@dataclass
class AssigneeCurrentTasksCountDTO:
    assignee_id: str
    tasks_count: int


@dataclass
class StageIdWithValueDTO:
    db_stage_id: int
    stage_value: int


@dataclass
class StageFlowDTO:
    previous_stage_id: int
    action_name: str
    next_stage_id: int


@dataclass
class CreateStageFlowDTO:
    previous_stage_id: str
    action_name: str
    next_stage_id: str


@dataclass
class StageFlowWithActionIdDTO:
    previous_stage_id: str
    action_id: int
    next_stage_id: str


@dataclass
class StageIdActionNameDTO:
    stage_id: str
    action_name: str


@dataclass
class StageActionIdDTO(StageIdActionNameDTO):
    action_id: int


@dataclass
class StageGoFWithTemplateIdDTO:
    stage_id: int
    gof_id: str
    task_template_id: str


@dataclass
class StageIdWithGoFIdDTO:
    stage_id: int
    gof_id: str
