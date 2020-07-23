from dataclasses import dataclass


@dataclass
class CreateTaskTemplateDTO:
    template_id: str
    template_name: str
