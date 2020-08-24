from dataclasses import dataclass


@dataclass
class TemplateDTO:
    template_id: str
    template_name: str


@dataclass
class ProjectTemplateDTO(TemplateDTO):
    project_id: str
