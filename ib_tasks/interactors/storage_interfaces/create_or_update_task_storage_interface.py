import abc

from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFDetailsDTO
from typing import Union, List
from ib_tasks.exceptions.task_custom_exceptions \
    import InvalidTaskIdException
from ib_tasks.interactors.storage_interfaces.get_task_dtos import (
    TaskGoFDTO
)
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO


class CreateOrUpdateTaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_task_id(
            self, task_id: int
    ) -> Union[str, InvalidTaskIdException]:
        pass

    @abc.abstractmethod
    def get_task_gof_dtos(self, task_id: int) -> List[TaskGoFDTO]:
        pass

    @abc.abstractmethod
    def get_gof_ids_having_permission(
            self, gof_ids: List[str], user_roles: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def get_task_gof_field_dtos(
            self, task_gof_ids: List[int]
    ) -> List[TaskGoFFieldDTO]:
        pass

    @abc.abstractmethod
    def get_field_ids_having_permission(
            self, field_ids: List[str], user_roles: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def is_valid_task_id(self, task_id: int) -> bool:
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

    @abc.abstractmethod
    def get_gof_ids_related_to_a_task(self, task_id: int) -> List[str]:
        pass

    @abc.abstractmethod
    def get_field_ids_related_to_given_task(
            self, task_id: int
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def update_task_gofs(
            self, task_gof_dtos: List[TaskGoFDTO]
    ) -> List[TaskGoFDetailsDTO]:
        pass

    @abc.abstractmethod
    def update_task_gof_fields(
            self, task_gof_field_dtos: List[TaskGoFFieldDTO]
    ):
        pass

