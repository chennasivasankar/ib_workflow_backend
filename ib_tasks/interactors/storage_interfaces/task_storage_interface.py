import abc
from typing import List
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, GoFDTO


class TaskStorageInterface(abc.ABC):
    @abc.abstractmethod
    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    @abc.abstractmethod
    def create_task_template(self, template_id: str, template_name: str):
        pass

    @abc.abstractmethod
    def add_gofs_to_task_template(
            self, template_id: str,
            gof_dtos_to_add_to_template: List[GoFDTO]):
        pass

    @abc.abstractmethod
    def get_existing_gof_ids_of_template(self, template_id: str) -> List[str]:
        pass
