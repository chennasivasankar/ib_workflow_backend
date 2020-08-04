
from dataclasses import dataclass
from typing import List

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
from ib_tasks.interactors.gofs_dtos import FieldDisplayDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageDetailsDTO, GetTaskStageCompleteDetailsDTO


@dataclass
class TaskCompleteDetailsDTO:
    task_id: int
    task_boards_details: TaskBoardsDetailsDTO
    actions_dto: List[ActionDTO]
    field_dtos: List[FieldDisplayDTO]



@dataclass
class AllTasksOverviewDetailsDTO:
    task_id_with_stage_details_dtos: List[TaskIdWithStageDetailsDTO]
    task_fields_and_action_details_dtos: List[GetTaskStageCompleteDetailsDTO]
