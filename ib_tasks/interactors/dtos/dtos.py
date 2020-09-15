from dataclasses import dataclass


@dataclass
class TaskLogDTO:
    user_id: str
    task_id: int
    action_id: int
    task_request_json: str
