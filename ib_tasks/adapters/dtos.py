from dataclasses import dataclass
from typing import List


@dataclass()
class ColumnDTO:
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
class BoardDTO:
    board_id: str
    name: str


@dataclass()
class TaskBoardsDetailsDTO:
    board_dto: BoardDTO
    column_stage_dtos: List[ColumnStageDTO]
    columns_dtos: List[ColumnDTO]
