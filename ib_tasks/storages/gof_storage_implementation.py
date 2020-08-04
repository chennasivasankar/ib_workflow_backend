from typing import List, Dict, Optional

from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFToTaskTemplateDTO, GoFDTO, GoFRoleDTO
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.models import GoFRole, GoF, TaskTemplateGoFs


class GoFStorageImplementation(GoFStorageInterface):
    def get_existing_gof_ids_in_given_gof_ids(self, gof_ids: List[str]) -> \
            List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(pk__in=gof_ids).values_list('gof_id',
                                                           flat=True))
        return existing_gof_ids

    def create_gofs(self, gof_dtos: List[GoFDTO]):
        from ib_tasks.models.gof import GoF
        gof_objects = [
            GoF(gof_id=gof_dto.gof_id,
                display_name=gof_dto.gof_display_name,
                max_columns=gof_dto.max_columns) for gof_dto in gof_dtos
        ]
        GoF.objects.bulk_create(gof_objects)

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
            gof.max_columns = gof_dto.max_columns
        GoF.objects.bulk_update(
            gofs, ['display_name', 'max_columns']
        )

    def delete_gof_roles(self, gof_ids: List[str]):
        GoFRole.objects.filter(gof_id__in=gof_ids).delete()

    def get_existing_gof_ids(self, gof_ids: List[str]) -> List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(gof_id__in=gof_ids).values_list("gof_id",
                                                               flat=True))
        return existing_gof_ids

    def get_gofs_details_dtos_for_given_gof_ids(self, gof_ids: List[str]) -> \
            List[GoFDTO]:
        gof_details = GoF.objects.filter(gof_id__in=gof_ids).values(
            'gof_id', 'max_columns', 'display_name')
        gof_dtos = self._convert_gof_details_to_dtos(gof_details=gof_details)
        return gof_dtos

    def get_gofs_to_task_templates_from_permitted_gofs(self,
                                                       gof_ids: List[str]) -> \
            List[GoFToTaskTemplateDTO]:
        task_template_gofs = \
            TaskTemplateGoFs.objects.filter(gof_id__in=gof_ids)
        gof_to_task_template_dtos = self._convert_task_template_gofs_to_dtos(
            task_template_gofs=task_template_gofs)
        return gof_to_task_template_dtos

    def get_gof_ids_with_read_permission_for_user(self, roles: List[str]) -> \
            List[str]:
        from django.db.models import Q
        from ib_tasks.constants.enum import PermissionTypes
        from ib_tasks.constants.constants import ALL_ROLES_ID
        gof_ids_queryset = GoFRole.objects.filter(
            Q(permission_type=PermissionTypes.READ.value),
            (Q(role__in=roles) | Q(role=ALL_ROLES_ID))
        ).values_list('gof_id', flat=True)

        gof_ids_list = list(gof_ids_queryset)
        return gof_ids_list

    def get_valid_gof_ids_in_given_gof_ids(self, gof_ids: List[str]) -> List[
        str]:
        from ib_tasks.models.gof import GoF
        gof_ids_queryset = GoF.objects.filter(gof_id__in=gof_ids).values_list(
            'gof_id', flat=True)

        gof_ids_list = list(gof_ids_queryset)
        return gof_ids_list

    @staticmethod
    def _convert_gof_details_to_dtos(gof_details: List[Dict]) -> List[GoFDTO]:
        gof_dtos = [
            GoFDTO(gof_id=gof['gof_id'],
                   gof_display_name=gof['display_name'],
                   max_columns=gof['max_columns']) for gof in gof_details
        ]
        return gof_dtos

    @staticmethod
    def _convert_task_template_gofs_to_dtos(
            task_template_gofs) -> List[GoFToTaskTemplateDTO]:
        task_template_gof_dtos = [
            GoFToTaskTemplateDTO(
                template_id=task_template_gof.task_template_id,
                gof_id=task_template_gof.gof_id,
                order=task_template_gof.order,
                enable_add_another=task_template_gof.enable_add_another_gof

            )
            for task_template_gof in task_template_gofs
        ]
        return task_template_gof_dtos

    @staticmethod
    def _get_matching_gof_dto(gof_id: str,
                              gof_dtos: List[GoFDTO]) -> Optional[GoFDTO]:
        for gof_dto in gof_dtos:
            gof_id_matched = gof_id == gof_dto.gof_id
            if gof_id_matched:
                return gof_dto
        return
