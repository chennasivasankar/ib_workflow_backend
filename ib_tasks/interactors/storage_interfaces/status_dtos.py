from dataclasses import dataclass


@dataclass()
class StatusVariableDTO:
    status_id: str
    status_variable: str
    value: str


@dataclass
class TaskTemplateStatusDTO:
    task_template_id: str
    status_variable_id: str
