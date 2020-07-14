import dataclasses
from typing import List


@dataclasses.dataclass
class GroupOfFieldsDTO:
    group_of_fields_id: str
    order: int


@dataclasses.dataclass
class CreateTaskTemplateDTO:
    template_id: str
    template_name: str
    group_of_fields_dtos: List[GroupOfFieldsDTO]

