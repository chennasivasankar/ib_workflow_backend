from dataclasses import dataclass


@dataclass
class TaskGoFFiledDetailsDTO:
    task_gof_id: int
    field_id: str
    field_response: str

