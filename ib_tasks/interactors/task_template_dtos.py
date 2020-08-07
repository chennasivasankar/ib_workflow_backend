from dataclasses import dataclass
from typing import Union, List


@dataclass
class CreateTemplateDTO:
    template_id: str
    template_name: str
    is_transition_template: bool


@dataclass
class FieldValuesDTO:
    field_id: str
    field_response: Union[str, List[str], int]


@dataclass
class GoFFieldsDTO:
    gof_id: str
    same_gof_order: int
    field_values_dtos: List[FieldValuesDTO]


@dataclass
class CreateTransitionChecklistTemplateDTO:
    task_id: int
    created_by_id: str
    transition_checklist_template_id: str
    action_id: int
    stage_id: int
    transition_checklist_gofs: List[GoFFieldsDTO]

