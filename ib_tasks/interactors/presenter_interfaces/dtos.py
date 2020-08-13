
from dataclasses import dataclass
from typing import List, Optional

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
from ib_tasks.interactors.gofs_dtos import FieldDisplayDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO, TaskWithCompleteStageDetailsDTO
from ib_tasks.interactors.user_action_on_task_interactor import TaskStageDTO


@dataclass
class TaskCompleteDetailsDTO:
    task_id: int
    task_boards_details: Optional[TaskBoardsDetailsDTO]
    actions_dto: List[ActionDTO]
    field_dtos: List[FieldDisplayDTO]
    task_stage_details: List[TaskStageDTO]


@dataclass
class AllTasksOverviewDetailsDTO:
    task_with_complete_stage_details_dtos: List[TaskWithCompleteStageDetailsDTO]
    task_fields_and_action_details_dtos: List[GetTaskStageCompleteDetailsDTO]
