"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass
from typing import Union, List, Optional
from ib_tasks.constants.enum import FieldTypes


@dataclass
class FieldDTO:
    field_id: int
    field_display_name: str
    field_type: FieldTypes
    field_values: Optional[Union[str, List[str]]]
    required: bool
    read_permissions_to_roles: List[str]
    write_permissions_to_roles: List[str]
    help_text: Optional[str]
    tool_tip: Optional[str]
    placeholder_text: Optional[str]
    error_message: Optional[str]


@dataclass()
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
