import abc
from typing import List, Optional

from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTransitionChecklistTemplateId
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO


class TaskTemplateStorageInterface(abc.ABC):
    @abc.abstractmethod
    def create_template(self, template_id: str,
                        template_name: str,
                        is_transition_template: bool):
        pass

    @abc.abstractmethod
    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):
        pass

    @abc.abstractmethod
    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass

    @abc.abstractmethod
    def update_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass

    @abc.abstractmethod
    def get_valid_task_template_ids_in_given_task_template_ids(
            self, template_ids: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def get_task_templates_dtos(self) -> List[TemplateDTO]:
        pass

    @abc.abstractmethod
    def get_gofs_to_templates_from_permitted_gofs(
            self, gof_ids: List[str]) -> List[GoFToTaskTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_existing_gof_ids_of_template(
            self, template_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def add_gofs_to_template(
            self, template_id: str,
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        pass

    @abc.abstractmethod
    def update_gofs_to_template(
            self, template_id: str,
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        pass

    @abc.abstractmethod
    def update_template(
            self, template_id: str, template_name: str,
            is_transition_template: bool):
        pass

    @abc.abstractmethod
    def get_valid_transition_template_ids(
            self, transition_template_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_transition_template_dto(
            self, transition_template_id: str) -> TemplateDTO:
        pass

    @abc.abstractmethod
    def check_is_transition_template_exists(
            self, transition_template_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_gofs_to_template_from_permitted_gofs(
            self, gof_ids: List[str],
            template_id: str) -> List[GoFToTaskTemplateDTO]:
        pass

    @abc.abstractmethod
    def validate_transition_template_id(
            self, transition_checklist_template_id
    ) -> Optional[InvalidTransitionChecklistTemplateId]:
        pass

    @abc.abstractmethod
    def get_gof_ids_of_template(self, template_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def add_project_to_task_templates(
            self, project_id: str, task_template_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_existing_task_template_ids_of_project_task_templates(
            self, project_id: str, task_template_ids: List[str]) -> List[str]:
        pass
