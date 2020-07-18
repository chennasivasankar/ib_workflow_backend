from typing import List, Optional

from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, FieldDTO, \
    GlobalConstantsDTO
from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFDTO, GoFRoleDTO, GoFRoleWithIdDTO
)
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.models import GoFRole, GoF


class TasksStorageImplementation(TaskStorageInterface):

    def create_task_template(self, template_id: str, template_name: str):
        pass

    def update_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    def get_task_template_name_if_exists(self, template_id: str) -> str:
        pass

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

    def update_gof_roles(self, gof_role_with_id_dtos: List[GoFRoleWithIdDTO]):
        from ib_tasks.models.gof_role import GoFRole
        role_ids = [
            gof_role_dto.id
            for gof_role_dto in gof_role_with_id_dtos
        ]
        gof_roles = GoFRole.objects.filter(pk__in=role_ids)
        for gof_role in gof_roles:
            gof_role_dto = self._get_matching_gof_role_dto(
                gof_role, gof_role_with_id_dtos
            )
            gof_role.permission_type = gof_role_dto.permission_type
        GoFRole.objects.bulk_update(gof_roles, ['permission_type'])

    @staticmethod
    def _get_matching_gof_role_dto(
            gof_role: GoFRole, gof_role_with_id_dtos: List[GoFRoleWithIdDTO]
    ) -> GoFRoleWithIdDTO:
        for gof_role_dto in gof_role_with_id_dtos:
            gof_role_is_matched = gof_role.id == gof_role_dto.id
            if gof_role_is_matched:
                return gof_role_dto

    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):
        pass

    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass

    def get_roles_for_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[GoFRoleWithIdDTO]:
        from ib_tasks.models.gof_role import GoFRole
        gof_roles = list(GoFRole.objects.filter(gof_id__in=gof_ids))
        gof_role_with_id_dtos = self._prepare_gof_role_with_id_dtos(gof_roles)
        return gof_role_with_id_dtos

    @staticmethod
    def _prepare_gof_role_with_id_dtos(
            gof_roles: List[GoFRole]
    ) -> List[GoFRoleWithIdDTO]:
        gof_role_with_id_dtos = [
            GoFRoleWithIdDTO(
                id=gof_role.id,
                gof_id=gof_role.gof_id,
                role=gof_role.role,
                permission_type=gof_role.permission_type
            )
            for gof_role in gof_roles
        ]
        return gof_role_with_id_dtos

    def get_gof_dtos_for_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[GoFDTO]:
        gofs = GoF.objects.filter(pk__in=gof_ids)
        gof_dtos = self._prepare_gof_dtos(gofs)
        return gof_dtos

    @staticmethod
    def _prepare_gof_dtos(gofs: List[GoF]):
        gof_dtos = [
            GoFDTO(
                gof_id=gof.gof_id,
                gof_display_name=gof.display_name,
                task_template_id=gof.task_template_id,
                order=gof.order,
                max_columns=gof.max_columns,
                enable_multiple_gofs=gof.enable_multiple_gofs
            )
            for gof in gofs
        ]
        return gof_dtos
