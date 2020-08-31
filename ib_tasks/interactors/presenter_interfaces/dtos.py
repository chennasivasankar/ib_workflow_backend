
from dataclasses import dataclass
from typing import List, Optional

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
from ib_tasks.interactors.gofs_dtos import FieldDisplayDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO, TaskWithCompleteStageDetailsDTO
from ib_tasks.interactors.stage_dtos import TaskStageDTO, \
    TaskStageAssigneeDetailsDTO


@dataclass
class TaskCompleteDetailsDTO:
    task_id: int
    task_display_id: str
    task_boards_details: Optional[TaskBoardsDetailsDTO]
    actions_dto: Optional[List[ActionDTO]]
    field_dtos: Optional[List[FieldDisplayDTO]]
    task_stage_details: Optional[List[TaskStageDTO]]
    assignees_details: List[TaskStageAssigneeDetailsDTO]


@dataclass
class AllTasksOverviewDetailsDTO:
    task_with_complete_stage_details_dtos: List[TaskWithCompleteStageDetailsDTO]
    task_fields_and_action_details_dtos: List[GetTaskStageCompleteDetailsDTO]
