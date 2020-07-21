from dataclasses import dataclass

@dataclass
class ColumnParametersDTO:
    board_id: str
    user_id: str


@dataclass
class TaskColumnDTO:
    column_id: str
    task_id: str

@dataclass
class PaginationParametersDTO:
    offset: int
    limit: int

@dataclass
class TaskDTO:
    task_id: str
    stage_id: str

@dataclass
class TaskDetailsDTO:
    task_id: str
    stage_id: str
    column_id: str

@dataclass
class FieldsDTO:
    task_template_id: str
    field_id: str
