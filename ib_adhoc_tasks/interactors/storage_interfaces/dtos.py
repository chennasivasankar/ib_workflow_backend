from dataclasses import dataclass


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
