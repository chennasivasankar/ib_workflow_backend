from dataclasses import dataclass


@dataclass
class CreateTemplateDTO:
    template_id: str
    template_name: str
    is_transition_template: bool
