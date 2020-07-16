from dataclasses import dataclass


@dataclass
class TaskStatusDTO:
    status: str
    stage: str