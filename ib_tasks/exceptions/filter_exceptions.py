"""
Created on: 05/08/20
Author: Pavankumar Pamuru

"""
from typing import List


class InvalidTemplateID(Exception):
    pass


class FieldIdsNotBelongsToTemplateId:

    def __init__(self, field_ids: List[str]):
        self.field_ids = field_ids

    def __str__(self):
        return self.field_ids
