from dataclasses import dataclass

@dataclass
class ColumnParametersDTO:
    board_id: str
    offset: int
    limit: int
    user_id: str


@dataclass
class TaskColumnDTO:
    column_id: str
    task_id: str
