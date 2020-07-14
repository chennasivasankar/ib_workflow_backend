import abc
from typing import List
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO


class TaskStorageInterface(abc.ABC):
    @abc.abstractmethod
    def create_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    @abc.abstractmethod
    def update_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    @abc.abstractmethod
    def get_task_template_name_if_exists(self, template_id: str) -> str:
        pass

    @abc.abstractmethod
    def get_existing_group_of_fields_of_template(self,
                                                 template_id: str
                                                 ) -> List[str]:
        pass