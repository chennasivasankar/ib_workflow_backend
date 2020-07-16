"""
Created on: 15/07/20
Author: Pavankumar Pamuru
"""

from typing import Union, List, Optional
from dataclasses import dataclass


@dataclass
class ActionDto:
    stage_id: str
    action_name: str
    logic: str
    role: str
    button_text: str
    button_color: Optional[str]


@dataclass
class GoFIDAndOrderDTO:
    gof_id: str
    order: int


@dataclass
class CreateTaskTemplateDTO:
    template_id: str
    template_name: str
    gof_dtos: List[GoFIDAndOrderDTO]

@dataclass
class GlobalConstantsDTO:
    constant_name: str
    value: str


@dataclass
class GlobalConstantsWithTemplateIdDTO:
    global_constants_dtos: List[GlobalConstantsDTO]
    template_id: str
