from django.db.models import Q
from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface \
    import CreateOrUpdateTaskStorageInterface
from typing import Union, List
from ib_tasks.exceptions.task_custom_exceptions \
    import InvalidTaskIdException

from ib_tasks.interactors.storage_interfaces.get_task_dtos import (
    TaskGoFDTO,
    TaskGoFFieldDTO
)
from ib_tasks.models.task import Task
from ib_tasks.models.task_gof import TaskGoF
from ib_tasks.models.task_gof_field import TaskGoFField
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.models.field_role import FieldRole


class CreateOrUpdateTaskStorageImplementation(
    CreateOrUpdateTaskStorageInterface
):

    def validate_task_id(
            self, task_id: int
    ) -> Union[str, InvalidTaskIdException]:
        try:
            task_obj = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise InvalidTaskIdException(task_id)
        template_id = task_obj.template_id
        return template_id

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
