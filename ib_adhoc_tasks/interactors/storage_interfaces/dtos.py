from dataclasses import dataclass
from typing import List


@dataclass
class FieldIdAndValueDTO:
    field_id: str
    value: str


@dataclass
class FilterForStageDTO:
    project_id: str
    template_id: str
    stage_id: str


@dataclass
class FilterForFieldDTO:
    project_id: str
    template_id: str
    stage_ids: List[str]
    field_dto: FieldIdAndValueDTO


@dataclass
class FilterForAssigneeDTO:
    project_id: str
    template_id: str
    stage_ids: List[str]
    assignee_id: str
