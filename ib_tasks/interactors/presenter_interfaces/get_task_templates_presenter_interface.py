import abc
from dataclasses import dataclass
from typing import List
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionsOfTemplateDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithPermissionsDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO
from ib_tasks.exceptions.task_custom_exceptions import \
    TaskTemplatesDoesNotExists


@dataclass
class CompleteTaskTemplatesDTO:
    task_template_dtos: List[TaskTemplateDTO]
    actions_of_templates_dtos: List[ActionsOfTemplateDTO]
    gof_dtos: List[GoFDTO]
    gofs_to_task_templates_dtos: List[GoFToTaskTemplateDTO]
    field_with_permissions_dtos: List[FieldWithPermissionsDTO]


class GetTaskTemplatesPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_task_templates_does_not_exists_exception(
            self, err: TaskTemplatesDoesNotExists):
        pass

    @abc.abstractmethod
    def get_task_templates_response(
            self, complete_task_templates_dto: CompleteTaskTemplatesDTO):
        pass
