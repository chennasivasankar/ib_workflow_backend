from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface \
    import CreateOrUpdateTaskStorageInterface
from typing import Union, List
from ib_tasks.exceptions.task_custom_exceptions \
    import InvalidTaskIdException

from ib_tasks.interactors.storage_interfaces.get_task_dtos import (
    TaskGoFDTO,
    TaskGoFFieldDTO
)


class CreateOrUpdateTaskStorageImplementation(CreateOrUpdateTaskStorageInterface):

    def validate_task_id(
            self, task_id: int
    ) -> Union[str, InvalidTaskIdException]:
        pass

    def get_task_gof_dtos(self, task_id: int) -> List[TaskGoFDTO]:
        pass

    def get_gof_ids_having_permission(
            self, gof_ids: List[str], user_roles: List[str]
    ) -> List[str]:
        pass

    def get_task_gof_field_dtos(
            self, task_gof_ids: List[int]
    ) -> List[TaskGoFFieldDTO]:
        pass

    def get_field_ids_having_permission(
            self, field_ids: List[str], user_roles: List[str]
    ) -> List[str]:
        pass
