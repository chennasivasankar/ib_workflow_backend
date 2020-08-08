import abc
from dataclasses import dataclass
from typing import List

from ib_tasks.exceptions.task_custom_exceptions import \
    TransitionTemplateDoesNotExist
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO


@dataclass
class CompleteTransitionTemplateDTO:
    transition_template_dto: TemplateDTO
    gof_dtos: List[GoFDTO]
    gofs_of_transition_template_dtos: List[GoFToTaskTemplateDTO]
    field_with_permissions_dtos: List[FieldPermissionDTO]


class GetTransitionTemplatePresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_transition_template_does_not_exists_exception(
            self, err: TransitionTemplateDoesNotExist):
        pass

    @abc.abstractmethod
    def get_transition_template_response(
            self,
            complete_transition_template_dto: CompleteTransitionTemplateDTO):
        pass
