from dataclasses import dataclass

@dataclass
class StageInformationDTO:
    stage_id: str
    task_template_id: str
    value: int
    stage_display_name: str
    stage_display_logic: str

@dataclass
class TaskStagesDTO:
    task_template_id: str
    stage_id: str
