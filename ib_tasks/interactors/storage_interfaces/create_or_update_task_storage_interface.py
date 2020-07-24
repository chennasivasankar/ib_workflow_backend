import abc
from typing import List

from ib_tasks.interactors.storage_interfaces.task_dtos import TaskGoFDTO, \
    TaskGoFDetailsDTO, TaskGoFFieldDTO


class CreateOrUpdateTaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_task_id(self, task_id: str):
        pass

    @abc.abstractmethod
    def create_task_with_template_id(
            self, template_id: str, created_by_id: str
    ) -> int:
        pass

    @abc.abstractmethod
    def create_task_gofs(
            self, task_gof_dtos: List[TaskGoFDTO]
    ) -> List[TaskGoFDetailsDTO]:
        pass

    @abc.abstractmethod
    def create_task_gof_fields(
        self, task_gof_field_dtos: List[TaskGoFFieldDTO]
    ):
        pass
