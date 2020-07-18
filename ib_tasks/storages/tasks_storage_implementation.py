from typing import List, Optional

from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, \
    GlobalConstantsDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFDTO, GoFRoleDTO, FieldDTO, FieldRoleDTO
)
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class TasksStorageImplementation(TaskStorageInterface):

    def create_task_template(self, template_id: str, template_name: str):
        from ib_tasks.models.task_template import TaskTemplate
        TaskTemplate.objects.create(
            template_id=template_id, name=template_name
        )

    def update_task_template(
            self, template_id: str, template_name: str):
        from ib_tasks.models.task_template import TaskTemplate
        task_template = \
            TaskTemplate.objects.filter(template_id=template_id).first()
        task_template.name = template_name
        task_template.save()

    def get_task_template_name(self, template_id: str) -> str:
        from ib_tasks.models.task_template import TaskTemplate
        task_template = \
            TaskTemplate.objects.filter(template_id=template_id).first()
        return task_template.name

    def get_task_template_ids(self) -> List[str]:
        pass

    def create_fields(self, field_dtos: List[FieldDTO]):
        pass

    def get_existing_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(pk__in=gof_ids).values_list('gof_id', flat=True)
        )
        return existing_gof_ids

    def get_valid_template_ids_in_given_template_ids(
            self, template_ids: List[str]
    ) -> List[str]:
        from ib_tasks.models.task_template import TaskTemplate
        valid_template_ids = list(
            TaskTemplate.objects.filter(pk__in=template_ids). \
                values_list("template_id", flat=True)
        )
        return valid_template_ids

    def create_gofs(self, gof_dtos: List[GoFDTO]):
        from ib_tasks.models.gof import GoF
        gofs = [
            GoF(
                gof_id=gof_dto.gof_id,
                display_name=gof_dto.gof_display_name,
                task_template_id=gof_dto.task_template_id,
                order=gof_dto.order,
                max_columns=gof_dto.max_columns,
                enable_multiple_gofs=gof_dto.enable_multiple_gofs
            )
            for gof_dto in gof_dtos
        ]
        GoF.objects.bulk_create(gofs)

    def create_gof_roles(self, gof_role_dtos: List[GoFRoleDTO]):
        from ib_tasks.models.gof_role import GoFRole
        gof_roles = [
            GoFRole(
                gof_id=gof_role_dto.gof_id,
                role=gof_role_dto.role,
                permission_type=gof_role_dto.permission_type
            )
            for gof_role_dto in gof_role_dtos
        ]
        GoFRole.objects.bulk_create(gof_roles)

    def update_gofs(self, gof_dtos: List[GoFDTO]):
        from ib_tasks.models.gof import GoF
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        gofs = GoF.objects.filter(pk__in=gof_ids)
        for gof in gofs:
            gof_dto = self._get_matching_gof_dto(gof.gof_id, gof_dtos)
            gof.display_name = gof_dto.gof_display_name
            gof.task_template_id = gof_dto.task_template_id
            gof.order = gof_dto.order
            gof.max_columns = gof_dto.max_columns
            gof.enable_multiple_gofs = gof_dto.enable_multiple_gofs
        GoF.objects.bulk_update(
            gofs, ['display_name', 'task_template_id', 'order', 'max_columns']
        )

    @staticmethod
    def _get_matching_gof_dto(
            gof_id: str, gof_dtos: List[GoFDTO]
    ) -> Optional[GoFDTO]:
        for gof_dto in gof_dtos:
            gof_id_matched = gof_id == gof_dto.gof_id
            if gof_id_matched:
                return gof_dto
        return

    def update_gof_roles(self, gof_role_dtos: List[GoFRoleDTO]):
        pass

    def check_is_template_exists(self, template_id: str) -> bool:
        from ib_tasks.models.task_template import TaskTemplate
        is_template_exists = \
            TaskTemplate.objects.filter(template_id=template_id).exists()
        return is_template_exists

    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):

        from ib_tasks.models.global_constant import GlobalConstant
        constant_names_of_template = GlobalConstant.objects.filter(
            task_template_id=template_id).values_list('name', flat=True)

        constant_names_of_template_list = list(constant_names_of_template)
        return constant_names_of_template_list

    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objs = [
            GlobalConstant(
                task_template_id=template_id,
                name=global_constants_dto.constant_name,
                value=global_constants_dto.value
            )
            for global_constants_dto in global_constants_dtos
        ]
        GlobalConstant.objects.bulk_create(global_constants_objs)

    def update_fields(self, field_dtos: List[FieldDTO]):
        pass

    def update_fields_roles(self, field_roles_dto: List[FieldRoleDTO]):
        pass

    def create_fields_roles(self, field_roles_dto: List[FieldRoleDTO]):
        pass

    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        pass

    def get_existing_gof_ids(self, gof_ids: List[str]) -> List[str]:
        pass
