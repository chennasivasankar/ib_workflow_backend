from dataclasses import dataclass

@dataclass
class TaskStageDTO:
    task_id: str
    stage_id: str


@dataclass
class TaskFieldsDTO:
    task_id: str
    field_type: str
    key: str
    value: str