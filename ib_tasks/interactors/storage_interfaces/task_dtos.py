from dataclasses import dataclass


@dataclass
class TaskGoFWithTaskIdDTO:
    task_id: int
    gof_id: str
    same_gof_order: int


@dataclass
class TaskGoFDetailsDTO:
    task_gof_id: int
    gof_id: str
    same_gof_order: int


@dataclass
class TaskGoFFieldDTO:
    field_id: str
    field_response: str
    task_gof_id: int
