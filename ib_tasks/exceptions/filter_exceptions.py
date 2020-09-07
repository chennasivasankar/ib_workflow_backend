"""
Created on: 05/08/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_tasks.constants.enum import Operators


class InvalidTemplateID(Exception):
    pass


class InvalidFilterId(Exception):
    pass


class InvalidProjectId(Exception):
    pass


class FieldIdsNotBelongsToTemplateId(Exception):

    def __init__(self, field_ids: List[str]):
        self.field_ids = field_ids

    def __str__(self):
        return self.field_ids


class UserNotHaveAccessToFields(Exception):
    pass


class UserNotHaveAccessToFilter(Exception):
    pass


class InvalidFilterCondition(Exception):
    def __init__(self, condition: Operators):
        self.condition = condition

    def __str__(self):
        return self.condition