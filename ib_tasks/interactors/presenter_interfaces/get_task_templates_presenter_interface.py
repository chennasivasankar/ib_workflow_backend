import abc
from dataclasses import dataclass
from typing import List

from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionsOfTemplateDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    UserFieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO


@dataclass
class CompleteTaskTemplatesDTO:
    task_template_dtos: List[TaskTemplateDTO]
    actions_of_templates_dtos: List[ActionsOfTemplateDTO]
    gof_dtos: List[GoFDTO]
    gofs_to_task_templates_dtos: List[GoFToTaskTemplateDTO]
    field_dtos: List[FieldDTO]
    user_field_permission_dtos: List[UserFieldPermissionDTO]


class GetTaskTemplatesPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_task_templates_response(
            self, complete_task_templates_dto: CompleteTaskTemplatesDTO):
        pass
