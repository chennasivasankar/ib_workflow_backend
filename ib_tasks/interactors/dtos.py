"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""

from typing import List, Optional
from dataclasses import dataclass

@dataclass
class ActionDTO:
    stage_id: str
    action_name: str
    logic: str
    role: str
    button_text: str
    button_color: Optional[str]


@dataclass
class CreateTaskTemplateDTO:
    template_id: str
    template_name: str


@dataclass
class GlobalConstantsDTO:
    constant_name: str
    value: int


@dataclass
class GlobalConstantsWithTemplateIdDTO:
    template_id: str
    global_constants_dtos: List[GlobalConstantsDTO]


@dataclass
class GoFWithOrderAndAddAnotherDTO:
    gof_id: str
    order: int
    is_add_another_enable: bool


@dataclass
class GoFsWithTemplateIdDTO:
    template_id: str
    gof_dtos: List[GoFWithOrderAndAddAnotherDTO]
