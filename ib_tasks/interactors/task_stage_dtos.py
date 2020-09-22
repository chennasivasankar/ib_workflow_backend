from dataclasses import dataclass
from typing import List

from ib_tasks.interactors.stage_dtos import TaskStageAssigneeTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import TaskBaseDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import GetTaskStageCompleteDetailsDTO


@dataclass
class TasksCompleteDetailsDTO:
    task_base_details_dtos: List[TaskBaseDetailsDTO]
    task_stage_details_dtos: List[GetTaskStageCompleteDetailsDTO]
    task_stage_assignee_dtos: List[TaskStageAssigneeTeamDetailsDTO]
