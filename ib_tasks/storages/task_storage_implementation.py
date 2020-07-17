from typing import List
from ib_tasks.interactors.storage_interfaces.dtos import (
    GoFDTO, GoFRolesDTO, GoFFieldsDTO
)
from ib_tasks.interactors.dtos import FieldDTO, GoFIdAndOrderDTO, \
    GlobalConstantsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class TaskStorageImplementation(TaskStorageInterface):

    def create_task_template(self, template_id: str, template_name: str):
        from ib_tasks.models.task_template import TaskTemplate
        TaskTemplate.objects.create(
            template_id=template_id, name=template_name
        )

    def add_gofs_to_task_template(
            self, template_id: str,
            gof_id_and_order_dtos: List[GoFIdAndOrderDTO]):
        given_gof_ids = self._get_gof_ids(gof_id_and_order_dtos)
        from ib_tasks.models.gof import GoF
        gof_objs = GoF.objects.filter(gof_id__in=given_gof_ids)

        gof_id_and_order_dict = self._get_gof_id_and_order_dto_in_dict(
            gof_id_and_order_dtos=gof_id_and_order_dtos
        )
        for gof_obj in gof_objs:
            gof_obj.task_template_id = template_id
            gof_obj.order = gof_id_and_order_dict[gof_obj.gof_id]

        GoF.objects.bulk_update(gof_objs, ['task_template', 'order'])

    def get_task_template_ids(self) -> List[str]:
        pass

    def create_fields(self, field_dtos: List[FieldDTO]):
        pass

    def get_existing_gof_ids_of_template(self, template_id: str) -> List[str]:
        from ib_tasks.models.gof import GoF

        gof_ids_of_template = GoF.objects.filter(
            task_template_id=template_id
        ).values_list('gof_id', flat=True)
        return list(gof_ids_of_template)

    def create_gofs(self, gof_dtos: List[GoFDTO]):
        pass

    def create_gof_roles(self, gof_roles_dtos: List[GoFRolesDTO]):
        pass

    def create_gof_fields(self, gof_fields_dtos: List[GoFFieldsDTO]):
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

    @staticmethod
    def _get_gof_ids(gof_id_and_order_dtos: List[GoFIdAndOrderDTO]):
        gof_ids = [
            gof_id_and_order_dto.gof_id
            for gof_id_and_order_dto in gof_id_and_order_dtos
        ]
        return gof_ids

    @staticmethod
    def _get_gof_id_and_order_dto_in_dict(
            gof_id_and_order_dtos: List[GoFIdAndOrderDTO]):
        gof_id_and_order_dict = {}
        for gof_id_and_order_dto in gof_id_and_order_dtos:
            gof_id_and_order_dict[gof_id_and_order_dto.gof_id] = \
                gof_id_and_order_dto.order
        return gof_id_and_order_dict
