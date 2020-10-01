from dataclasses import dataclass
from ib_tasks.constants.constants import TASK_TEMPLATE_TITLE_DEFAULT_NAME


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
    project_id: str = None


@dataclass
class TaskTemplateMapDTO:
    task_id: int
    template_id: str


@dataclass
class TaskTemplateMandatoryFieldsDTO:
    template_id: str
    title_display_name: str = TASK_TEMPLATE_TITLE_DEFAULT_NAME
    title_placeholder_text: str = TASK_TEMPLATE_TITLE_DEFAULT_NAME
