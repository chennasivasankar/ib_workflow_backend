from typing import List

from ib_tasks.interactors.storage_interfaces \
    .create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO
from ib_tasks.interactors.task_dtos import BasicTaskDetailsDTO, \
    UpdateTaskBasicDetailsDTO


class TaskCrudOperationsInteractor:

    def __init__(
            self, create_task_storage: CreateOrUpdateTaskStorageInterface):
        self.storage = create_task_storage

    def create_task(self, task_details_dto: BasicTaskDetailsDTO) -> int:
        created_task_id = self.storage.create_task(task_details_dto)
        return created_task_id

    def create_task_gofs(
            self, task_gof_dtos: List[TaskGoFWithTaskIdDTO]
    ) -> List[TaskGoFDetailsDTO]:
        task_gof_details_dtos = self.storage.create_task_gofs(
            task_gof_dtos=task_gof_dtos)
        return task_gof_details_dtos

    def create_task_gof_fields(self, gof_field_dtos: List[TaskGoFFieldDTO]):
        self.storage.create_task_gof_fields(gof_field_dtos)

    def update_task(self, task_basic_details: UpdateTaskBasicDetailsDTO):
        self.storage.update_task(task_basic_details)

    def update_task_gofs(self, task_gof_dtos: List[TaskGoFWithTaskIdDTO]):
        task_gof_details_dtos = self.storage.update_task_gofs(task_gof_dtos)
        return task_gof_details_dtos

    def update_task_gof_fields(self, gof_field_dtos: List[TaskGoFFieldDTO]):
        self.storage.update_task_gof_fields(gof_field_dtos)
