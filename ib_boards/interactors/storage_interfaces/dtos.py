from dataclasses import dataclass


@dataclass
class BoardDTO:
    board_id: str
    display_name: str


@dataclass
class BoardColumnDTO:
    board_id: str
    column_id: str