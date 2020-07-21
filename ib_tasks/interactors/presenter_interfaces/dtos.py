
from dataclasses import dataclass
from typing import List

from ib_tasks.interactors.dtos import FieldDisplayDTO
from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
from ib_tasks.interactors.storage_interfaces.dtos import ActionDTO


@dataclass()
class TaskCompleteDetailsDTO:
    board_id: str
    task_boards_details: TaskBoardsDetailsDTO
    actions_dto: List[ActionDTO]
    field_dtos: List[FieldDisplayDTO]
