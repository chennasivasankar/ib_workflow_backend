import dataclasses
from typing import List


@dataclasses.dataclass
class GoFDTO:
    gof_id: str
    order: int


@dataclasses.dataclass
class CreateTaskTemplateDTO:
    template_id: str
    template_name: str
    gof_dtos: List[GoFDTO]
