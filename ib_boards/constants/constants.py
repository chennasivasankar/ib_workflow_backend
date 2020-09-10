"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
from ib_boards.constants.enum import DisplayStatus

BOARDS_AND_COLUMN_SUB_SHEET = "Boards and Columns"

PROJECT_BOARDS_SUB_SHEET = "Project Boards"

DISPLAY_STATUSES = [(item.value, item.value) for item in DisplayStatus]