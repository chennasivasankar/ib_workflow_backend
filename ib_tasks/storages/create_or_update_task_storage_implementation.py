from typing import List

from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskGoFFieldDTO, \
    TaskGoFDTO, TaskGoFDetailsDTO
from ib_tasks.models import TaskGoF


class CreateOrUpdateTaskStorageImplementation(
    CreateOrUpdateTaskStorageInterface
):

    def validate_task_id(self, task_id: str):
        pass

    def create_task_with_template_id(self, template_id: str,
                                     created_by_id: str) -> int:
        from ib_tasks.models.task import Task
        task_object = Task.objects.create(
            template_id=template_id, created_by_id=created_by_id
        )
        return task_object.id

    def create_task_gofs(
            self, task_gof_dtos: List[TaskGoFDTO]
    ) -> List[TaskGoFDetailsDTO]:
        from ib_tasks.models.task_gof import TaskGoF
        task_gof_objects = [
            TaskGoF(
                task_id=task_gof_dto.task_id,
                gof_id=task_gof_dto.gof_id,
                same_gof_order=task_gof_dto.same_gof_order
            )
            for task_gof_dto in task_gof_dtos
        ]
        task_gofs = TaskGoF.objects.bulk_create(task_gof_objects)
        task_gof_details_dtos = self._prepare_task_gof_details_dtos(task_gofs)
        return task_gof_details_dtos

    @staticmethod
    def _prepare_task_gof_details_dtos(
            task_gofs: List[TaskGoF]
    ) -> List[TaskGoFDetailsDTO]:
        gof_ids = [task_gof.gof_id for task_gof in task_gofs]
        pass

    def create_task_gof_fields(
            self, task_gof_field_dtos: List[TaskGoFFieldDTO]
    ):
        pass
