from dataclasses import dataclass
from typing import List

from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO, AllTasksOverviewDetailsDTO
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO


@dataclass
class TaskOverallCompleteDetailsDTO:
    task_complete_details_dto: TaskCompleteDetailsDTO
    task_current_stage_details_dto: TaskCurrentStageDetailsDTO
    all_tasks_overview_details_dto: AllTasksOverviewDetailsDTO


@dataclass
class TasksDetailsInputDTO:
    task_ids: List[int]
    project_id: str
    user_id: str
    view_type: ViewType
