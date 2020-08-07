from django.db.models import Q

from ib_tasks.interactors.field_dtos import FieldIdWithTaskGoFIdDTO
from ib_tasks.interactors.gofs_dtos import GoFIdWithSameGoFOrder
from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface \
    import CreateOrUpdateTaskStorageInterface
from typing import Union, List, Optional
from ib_tasks.exceptions.task_custom_exceptions \
    import InvalidTaskIdException
from ib_tasks.interactors.storage_interfaces.task_dtos import (
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO)
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO, TaskGoFDTO, TaskBaseDetailsDTO
from ib_tasks.models.task import Task
from ib_tasks.models.task_gof import TaskGoF
from ib_tasks.models.task_gof_field import TaskGoFField
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.models.field_role import FieldRole


class CreateOrUpdateTaskStorageImplementation(
    CreateOrUpdateTaskStorageInterface
):

    def create_initial_task_stage(self, task_id: int, template_id: str):
        from ib_tasks.models import TaskStage
        from ib_tasks.models import TaskTemplateInitialStage
        TaskStage.objects.get_or_create(
            task_id=task_id,
            stage=TaskTemplateInitialStage.objects.get(
                task_template_id=template_id
            ).stage
        )

    def get_all_gof_ids_related_to_a_task_template(self,
                                                   task_template_id: str) -> \
    List[str]:
        from ib_tasks.models import TaskTemplateGoFs
        gof_ids = list(
            TaskTemplateGoFs.objects.filter(task_template_id=task_template_id)\
            .values_list('gof_id', flat=True)
        )
        return gof_ids

    def get_template_id_for_given_task(self, task_id: int) -> str:
        from ib_tasks.models import Task
        template_id = Task.objects.get(pk=task_id).template_id
        return template_id

    def set_status_variables_for_template_and_task(self, task_template_id,
                                                   task_id):
        from ib_tasks.models import \
            TaskTemplateStatusVariable

        status_variables = TaskTemplateStatusVariable.objects.filter(
            task_template_id=task_template_id
        ).values_list('variable', flat=True)

        from ib_tasks.models.task_status_variable import TaskStatusVariable
        task_status_variables = [
            TaskStatusVariable(
                task_id=task_id,
                variable=status_variable,
                value=''
            )
            for status_variable in status_variables
        ]
        TaskStatusVariable.objects.bulk_create(task_status_variables)

    def get_task_gof_dtos(self, task_id: int) -> List[TaskGoFDTO]:
        task_gof_objs = TaskGoF.objects.filter(task_id=task_id)
        task_gof_dtos = []
        for task_gof_obj in task_gof_objs:
            task_gof_dto = TaskGoFDTO(
                task_gof_id=task_gof_obj.id,
                gof_id=task_gof_obj.gof_id,
                same_gof_order=task_gof_obj.same_gof_order
            )
            task_gof_dtos.append(task_gof_dto)
        return task_gof_dtos

    def get_gof_ids_having_permission(
            self, gof_ids: List[str], user_roles: List[str]
    ) -> List[str]:

        from ib_tasks.constants.constants import ALL_ROLES_ID
        gof_ids = list(
            GoFRole.objects.filter(
                Q(role__in=user_roles) | Q(role=ALL_ROLES_ID),
                gof_id__in=gof_ids
            ).values_list('gof_id', flat=True)
        )
        return gof_ids

    def get_task_gof_field_dtos(
            self, task_gof_ids: List[int]
    ) -> List[TaskGoFFieldDTO]:

        task_gof_field_objs = TaskGoFField.objects.filter(
            task_gof_id__in=task_gof_ids
        )
        task_gof_field_dtos = []
        for task_gof_field_obj in task_gof_field_objs:
            task_gof_field_dto = TaskGoFFieldDTO(
                task_gof_id=task_gof_field_obj.task_gof_id,
                field_id=task_gof_field_obj.field_id,
                field_response=task_gof_field_obj.field_response
            )
            task_gof_field_dtos.append(task_gof_field_dto)
        return task_gof_field_dtos

    def get_field_ids_having_permission(
            self, field_ids: List[str], user_roles: List[str]
    ) -> List[str]:

        from ib_tasks.constants.constants import ALL_ROLES_ID
        field_ids = list(
            FieldRole.objects.filter(
                Q(role__in=user_roles) | Q(role=ALL_ROLES_ID),
                field_id__in=field_ids
            ).values_list('field_id', flat=True)
        )
        return field_ids

    def is_valid_task_id(self, task_id: str) -> bool:
        task_existence = Task.objects.filter(id=task_id).exists()
        return task_existence

    def get_gof_ids_with_same_gof_order_related_to_a_task(
            self, task_id: int) -> List[GoFIdWithSameGoFOrder]:
        gof_dicts = list(
            TaskGoF.objects.filter(task_id=task_id).values(
                'gof_id', 'same_gof_order'))
        gof_id_with_same_gof_order_dtos = [
            GoFIdWithSameGoFOrder(
                gof_id=gof_dict['gof_id'],
                same_gof_order=gof_dict['same_gof_order']
            )
            for gof_dict in gof_dicts
        ]
        return gof_id_with_same_gof_order_dtos

    def get_field_ids_with_task_gof_id_related_to_given_task(
            self, task_id: int) -> List[FieldIdWithTaskGoFIdDTO]:
        field_dicts = list(
            TaskGoFField.objects.filter(task_gof__task_id=task_id).values(
                'field_id', 'task_gof_id')
        )
        field_ids_with_task_gof_ids_dtos = [
            FieldIdWithTaskGoFIdDTO(
                field_id=field_dict['field_id'],
                task_gof_id=field_dict['task_gof_id']
            )
            for field_dict in field_dicts
        ]
        return field_ids_with_task_gof_ids_dtos

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

    def validate_task_id(
            self, task_id: int
    ) -> Union[TaskBaseDetailsDTO, InvalidTaskIdException]:

        try:
            task_obj = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise InvalidTaskIdException(task_id)
        task_base_details_dto = self._get_task_base_details_dto(task_obj)
        return task_base_details_dto

    @staticmethod
    def _get_task_base_details_dto(task_obj: Task):
        task_base_details_dto = TaskBaseDetailsDTO(
            template_id=task_obj.template_id,
            title=task_obj.title,
            description=task_obj.description,
            start_date=task_obj.start_date,
            due_date=task_obj.due_date,
            priority=task_obj.priority
        )
        return task_base_details_dto

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
        refined_task_gof_objects = []
        for task_gof_object in task_gof_objects:
            for task_gof in task_gofs:
                task_gof_matched = (
                    task_gof.gof_id == task_gof_object.gof_id and
                    task_gof.same_gof_order == task_gof_object.same_gof_order
                )
                if task_gof_matched:
                    refined_task_gof_objects.append(task_gof_object)
        task_gof_details_dtos = [
            TaskGoFDetailsDTO(
                task_gof_id=task_gof_object.id,
                gof_id=task_gof_object.gof_id,
                same_gof_order=task_gof_object.same_gof_order
            )
            for task_gof_object in refined_task_gof_objects
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
