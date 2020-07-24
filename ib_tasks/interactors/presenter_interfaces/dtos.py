
from dataclasses import dataclass
from typing import List

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
from ib_tasks.interactors.gofs_dtos import FieldDisplayDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO


@dataclass()
class TaskCompleteDetailsDTO:
    task_id: int
    task_boards_details: TaskBoardsDetailsDTO
    actions_dto: List[ActionDTO]
    field_dtos: List[FieldDisplayDTO]
