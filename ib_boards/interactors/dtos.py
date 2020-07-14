"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""
import json
from dataclasses import dataclass
from typing import List


@dataclass
class BoardDTO:
    board_id: str
    display_name: str


@dataclass
class ColumnDTO:
    column_id: str
    display_name: str
    task_template_stages: json
    user_role_ids: List[str]
    column_summary: str
    task_summary_fields: json
    board_id: str


@dataclass
class BoardColumnDTO:
    board_id: str
    column_ids: List[str]