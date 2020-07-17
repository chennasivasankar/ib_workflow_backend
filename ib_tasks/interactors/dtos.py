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
class GoFIdAndOrderDTO:
    gof_id: str
    order: int


@dataclass
class CreateTaskTemplateDTO:
    template_id: str
    template_name: str
    gof_dtos: List[GoFIdAndOrderDTO]


@dataclass
class GlobalConstantsDTO:
    constant_name: str
    value: int


@dataclass
class GlobalConstantsWithTemplateIdDTO:
    template_id: str
    global_constants_dtos: List[GlobalConstantsDTO]
