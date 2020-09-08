from dataclasses import dataclass
from typing import Optional, List

from ib_boards.constants.enum import DisplayStatus


@dataclass
class TaskDetailsDTO:
    task_id: str
    stage_id: str
    column_id: str


@dataclass
class ColumnDetailsDTO:
    column_id: str
    name: str


@dataclass
class ColumnCompleteDetails(ColumnDetailsDTO):
    total_tasks: int


@dataclass
class TaskFieldsDTO:
    task_id: str
    field_type: str
    key: str
    value: str


@dataclass
class TaskActionsDTO:
    task_id: str
    action_id: str
    name: str
    button_text: str
    button_color: Optional[str]


@dataclass
class BoardDTO:
    board_id: str
    name: str


@dataclass
class BoardColumnDTO:
    board_id: str
    column_id: str


@dataclass()
class ColumnBoardDTO:
    column_id: str
    board_id: str
    name: str


@dataclass()
class ColumnFieldDTO:
    column_id: str
    field_ids: List[str]


@dataclass()
class ColumnStageDTO:
    column_id: str
    stage_id: str


@dataclass()
class TaskBoardsDetailsDTO:
    board_dto: BoardDTO
    column_stage_dtos: List[ColumnStageDTO]
    columns_dtos: List[ColumnBoardDTO]


@dataclass
class ColumnStageIdsDTO:
    column_id: str
    stage_ids: List[str]


@dataclass
class AllFieldsDTO:
    field_id: str
    display_name: str
    display_order: int
    display_status: DisplayStatus
