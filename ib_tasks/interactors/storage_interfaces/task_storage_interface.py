import abc
from typing import List
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO


class TaskStorageInterface(abc.ABC):
    @abc.abstractmethod
    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    @abc.abstractmethod
    def create_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    @abc.abstractmethod
    def update_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    @abc.abstractmethod
    def get_task_template_name(self, template_id: str) -> str:
        pass

    @abc.abstractmethod
    def get_existing_gof_of_template(self, template_id: str) -> List[str]:
        pass
