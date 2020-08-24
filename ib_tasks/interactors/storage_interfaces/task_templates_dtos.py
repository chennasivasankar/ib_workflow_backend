from dataclasses import dataclass


@dataclass
class TemplateDTO:
    template_id: str
    template_name: str


@dataclass
class ProjectIdWithTaskTemplateIdDTO:
    project_id: str
    task_template_id: str


@dataclass
class ProjectTemplateDTO(TemplateDTO):
    project_id: str
