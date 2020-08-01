from typing import List, Optional

from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface \
    import CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import (
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO)
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO, TaskGoFDTO
from ib_tasks.models import TaskGoF, TaskGoFField, Task


class CreateOrUpdateTaskStorageImplementation(
    CreateOrUpdateTaskStorageInterface
):

    def get_task_gof_dtos(self, task_id: int) -> List[TaskGoFDTO]:
        return []

    def get_gof_ids_having_permission(self, gof_ids: List[str],
                                      user_roles: List[str]) -> List[str]:
        pass

    def get_task_gof_field_dtos(self, task_gof_ids: List[int]) -> List[
        TaskGoFFieldDTO]:
        return []

    def get_field_ids_having_permission(self, field_ids: List[str],
                                        user_roles: List[str]) -> List[str]:
        pass

    def is_valid_task_id(self, task_id: str) -> bool:
        task_existence = Task.objects.filter(id=task_id).exists()
        return task_existence

    def get_gof_ids_related_to_a_task(self, task_id: int) -> List[str]:
        gof_ids = list(
            TaskGoF.objects.filter(task_id=task_id).values_list(
                'gof_id', flat=True
            )
        )
        return gof_ids

    def get_field_ids_related_to_given_task(self, task_id: int) -> List[
        str]:
        field_ids = list(
            TaskGoFField.objects.filter(task_gof__task_id=task_id). \
                values_list('field_id', flat=True)
        )
        return field_ids

    def update_task_gofs(
            self, task_gof_dtos: List[TaskGoFWithTaskIdDTO]
    ) -> List[TaskGoFDetailsDTO]:
        task_id = task_gof_dtos[0].task_id
        task_gof_objects = TaskGoF.objects.filter(task_id=task_id)
        for task_gof_object in task_gof_objects:
            task_gof_dto = self._get_matching_task_gof_dto(
                task_gof_object, task_gof_dtos
            )
            task_gof_object.same_gof_order = task_gof_dto.same_gof_order
        TaskGoF.objects.bulk_update(task_gof_objects, ['same_gof_order'])
        task_gof_ids = [
            task_gof_object.id for task_gof_object in task_gof_objects
        ]
        task_gof_objects = list(TaskGoF.objects.filter(id__in=task_gof_ids))
        task_gof_details_dtos = self._prepare_task_gof_details_dtos(
            task_gof_objects
        )
        return task_gof_details_dtos

    @staticmethod
    def _get_matching_task_gof_dto(
            task_gof_object: TaskGoF, task_gof_dtos: List[TaskGoFWithTaskIdDTO]
    ) -> Optional[TaskGoFWithTaskIdDTO]:
        for task_gof_dto in task_gof_dtos:
            dto_matched = (
                task_gof_dto.task_id == task_gof_object.task_id,
                task_gof_dto.gof_id == task_gof_object.gof_id
            )
            if dto_matched:
                return task_gof_dto
        return

    def update_task_gof_fields(self,
                               task_gof_field_dtos: List[TaskGoFFieldDTO]):
        task_gof_ids = [
            task_gof_field_dto.task_gof_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        task_gof_field_objects = \
            TaskGoFField.objects.filter(task_gof_id__in=task_gof_ids)
        for task_gof_field_object in task_gof_field_objects:
            task_gof_field_dto = self._get_matching_task_gof_field_dto(
                task_gof_field_object, task_gof_field_dtos
            )
            if task_gof_field_dto is not None:
                task_gof_field_object.field_response = \
                    task_gof_field_dto.field_response
        TaskGoFField.objects.bulk_update(
            task_gof_field_objects, ['field_response']
        )

    @staticmethod
    def _get_matching_task_gof_field_dto(
            task_gof_field_object: TaskGoFField,
            task_gof_field_dtos: List[TaskGoFFieldDTO]
    ) -> Optional[TaskGoFFieldDTO]:
        for task_gof_field_dto in task_gof_field_dtos:
            dto_matched = (
                    task_gof_field_dto.task_gof_id == task_gof_field_object.task_gof_id and
                    task_gof_field_dto.field_id == task_gof_field_object.field_id
            )
            if dto_matched:
                return task_gof_field_dto
        return

    def validate_task_id(self, task_id: str):
        pass

    def create_task_with_template_id(self, template_id: str,
                                     created_by_id: str) -> int:
        from ib_tasks.models.task import Task
        task_object = Task.objects.create(
            template_id=template_id, created_by=created_by_id
        )
        return task_object.id

    def create_task_gofs(
            self, task_gof_dtos: List[TaskGoFWithTaskIdDTO]
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
        task_ids = [task_gof.task_id for task_gof in task_gofs]
        task_gof_objects = list(TaskGoF.objects.filter(task_id__in=task_ids))
        task_gof_details_dtos = [
            TaskGoFDetailsDTO(
                task_gof_id=task_gof_object.id,
                gof_id=task_gof_object.gof_id,
                same_gof_order=task_gof_object.same_gof_order
            )
            for task_gof_object in task_gof_objects
        ]
        return task_gof_details_dtos

    def create_task_gof_fields(
            self, task_gof_field_dtos: List[TaskGoFFieldDTO]
    ):
        task_gof_field_objects = [
            TaskGoFField(
                task_gof_id=task_gof_field_dto.task_gof_id,
                field_id=task_gof_field_dto.field_id,
                field_response=task_gof_field_dto.field_response
            )
            for task_gof_field_dto in task_gof_field_dtos
        ]
        TaskGoFField.objects.bulk_create(task_gof_field_objects)
