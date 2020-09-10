from dataclasses import dataclass
from typing import List

from ib_tasks.interactors.task_dtos import GoFFieldsDTO


@dataclass
class CreateTemplateDTO:
    template_id: str
    template_name: str
    is_transition_template: bool


@dataclass
class CreateTransitionChecklistTemplateDTO:
    task_id: int
    created_by_id: str
    transition_checklist_template_id: str
    action_id: int
    stage_id: int
    transition_checklist_gofs: List[GoFFieldsDTO]


@dataclass
class CreateTransitionChecklistTemplateWithTaskDisplayIdDTO:
    task_display_id: str
    created_by_id: str
    transition_checklist_template_id: str
    action_id: int
    stage_id: int
    transition_checklist_gofs: List[GoFFieldsDTO]
