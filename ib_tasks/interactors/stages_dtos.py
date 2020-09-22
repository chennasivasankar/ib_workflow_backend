from dataclasses import dataclass
from datetime import time, datetime, timedelta
from typing import Optional, List

from ib_tasks.adapters.dtos import AssigneeDetailsDTO, \
    UserIdWIthTeamDetailsDTOs, UserDetailsDTO, UserIdWIthTeamDetailsDTO, \
    TeamInfoDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageFlowDTO


@dataclass
class StageLogicAttributes:
    stage_id: str
    status_id: str


@dataclass
class StageDTO:
    stage_id: str
    task_template_id: str
    value: int
    card_info_kanban: str
    card_info_list: str
    stage_color: Optional[str]
    roles: str
    stage_display_name: str
    stage_display_logic: str


@dataclass
class StageActionDTO:
    stage_id: str
    action_name: str
    logic: str
    roles: List[str]
    function_path: str
    button_text: str
    button_color: Optional[str]
    action_type: Optional[str]
    transition_template_id: Optional[str]


@dataclass()
class TaskTemplateStageActionDTO(StageActionDTO):
    task_template_id: str


@dataclass
class StagesActionDTO:
    stage_id: str
    action_name: str
    logic: str
    roles: List[str]
    function_path: str
    button_text: str
    button_color: Optional[str]


@dataclass
class TemplateStageDTO:
    task_template_id: str
    stage_id: str


@dataclass
class UserStagesWithPaginationDTO:
    stage_ids: List[str]
    user_id: str
    limit: int
    offset: int


@dataclass
class StageAssigneeDTO:
    db_stage_id: int
    assignee_id: str
    team_id: str


@dataclass
class TaskIdWithStageAssigneesDTO:
    task_id: int
    stage_assignees: List[StageAssigneeDTO]


@dataclass
class TaskDisplayIdWithStageAssigneesDTO:
    task_display_id: str
    stage_assignees: List[StageAssigneeDTO]


@dataclass
class TaskIdWithStageAssigneeDTO(StageAssigneeDTO):
    task_id: int


@dataclass
class StageIdWithNameDTO:
    db_stage_id: int
    stage_display_name: str


@dataclass
class StageWithUserDetailsDTO:
    stage_details_dto: StageIdWithNameDTO
    assignee_details_dto: Optional[AssigneeDetailsDTO]


@dataclass
class StageWithUserDetailsAndTeamDetailsDTO:
    stages_with_user_details_dtos: List[StageWithUserDetailsDTO]
    user_with_team_details_dtos: List[UserIdWIthTeamDetailsDTO]


@dataclass
class StageRolesDTO:
    stage_id: str
    role_ids: List[str]


@dataclass()
class TaskStageHistoryDTO:
    log_id: int
    task_id: int
    stage_id: int
    stage_duration: Optional[time]
    started_at: datetime
    assignee_id: str
    left_at: Optional[datetime]


@dataclass()
class StageMinimalDTO:
    stage_id: int
    name: str
    color: str


@dataclass()
class EntityTypeDTO:
    entity_id: int
    entity_type: str


@dataclass()
class LogDurationDTO:
    entity_id: int
    duration: timedelta


@dataclass()
class TaskStageCompleteDetailsDTO:
    stage_dtos: List[StageMinimalDTO]
    task_stage_dtos: List[TaskStageHistoryDTO]
    log_duration_dtos: List[LogDurationDTO]
    assignee_details: List[AssigneeDetailsDTO]


@dataclass()
class StageActionLogicDTO:
    action_id: int
    stage_id: str
    action_logic: str
    action_name: str
    py_function_import_path: str


@dataclass
class UserDetailsWithTeamDetailsDTO:
    user_details_dtos: List[UserDetailsDTO]
    user_id_with_team_details_dtos: List[UserIdWIthTeamDetailsDTOs]


@dataclass
class AssigneeWithTeamDetailsDTO(AssigneeDetailsDTO):
    team_info_dto: TeamInfoDTO


@dataclass()
class StageAssigneeWithTeamDetailsDTO:
    task_stage_id: int
    stage_id: int
    assignee_details_dto: Optional[AssigneeWithTeamDetailsDTO]
