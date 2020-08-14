from dataclasses import dataclass
from typing import List, Union

from ib_tasks.constants.enum import Searchable


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


@dataclass
class UserDTO:
    user_id: str
    name: str


@dataclass
class AssigneeDetailsDTO:
    assignee_id: str
    name: str
    profile_pic_url: str


@dataclass
class UserDetailsDTO:
    user_id: str
    user_name: str
    profile_pic_url: str


@dataclass
class SearchableDetailsDTO:
    search_type: Searchable
    id: Union[int, str]
    value: str
