import abc
from typing import List

from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO


class TaskTemplateStorageInterface(abc.ABC):
    @abc.abstractmethod
    def create_task_template(self, template_id: str, template_name: str):
        pass

    @abc.abstractmethod
    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):
        pass

    @abc.abstractmethod
    def get_task_template_name(self, template_id: str):
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
    def get_valid_template_ids_in_given_template_ids(
            self, template_ids: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def get_task_templates_dtos(self) -> List[TaskTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_gofs_to_task_templates_from_permitted_gofs(
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
    def update_task_template(
            self, template_id: str, template_name: str):
        pass

