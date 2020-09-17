from dataclasses import dataclass

from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO, AllTasksOverviewDetailsDTO
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO


@dataclass
class TaskOverallCompleteDetailsDTO:
    task_complete_details_dto: TaskCompleteDetailsDTO
    task_current_stage_details_dto: TaskCurrentStageDetailsDTO
    all_tasks_overview_details_dto: AllTasksOverviewDetailsDTO
