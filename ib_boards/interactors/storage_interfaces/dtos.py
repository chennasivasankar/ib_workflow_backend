from dataclasses import dataclass
from typing import Optional


@dataclass
class ColumnDetailsDTO:
    column_id: str
    name: str


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
