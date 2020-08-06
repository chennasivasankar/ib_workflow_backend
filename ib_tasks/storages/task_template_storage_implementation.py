from typing import List

from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO
from ib_tasks.models import TaskTemplate, TaskTemplateGoFs


class TaskTemplateStorageImplementation(TaskTemplateStorageInterface):

    def create_task_template(self, template_id: str, template_name: str):
        from ib_tasks.models.task_template import TaskTemplate
        TaskTemplate.objects.create(template_id=template_id,
                                    name=template_name)

    def check_is_template_exists(self, template_id: str) -> bool:
        is_template_exists = \
            TaskTemplate.objects.filter(template_id=template_id).exists()
        return is_template_exists

    def get_constant_names_of_existing_global_constants_of_template(self,
                                                                    template_id: str):
        from ib_tasks.models.global_constant import GlobalConstant
        constant_names_of_template = GlobalConstant.objects.filter(
            task_template_id=template_id).values_list('name', flat=True)

        constant_names_of_template_list = list(constant_names_of_template)
        return constant_names_of_template_list

    def get_task_template_name(self, template_id: str):
        from ib_tasks.models.task_template import TaskTemplate
        template_name_query_set = \
            TaskTemplate.objects.filter(
                template_id=template_id
            ).values_list('name', flat=True)
        return template_name_query_set.first()

    def create_global_constants_to_template(self, template_id: str,
                                            global_constants_dtos: List[
                                                GlobalConstantsDTO]):
        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objs = [
            GlobalConstant(task_template_id=template_id,
                           name=global_constants_dto.constant_name,
                           value=global_constants_dto.value)
            for global_constants_dto in global_constants_dtos
        ]
        GlobalConstant.objects.bulk_create(global_constants_objs)

    def update_global_constants_to_template(self, template_id: str,
                                            global_constants_dtos: List[
                                                GlobalConstantsDTO]):
        global_constants_names = self._get_global_constant_names(
            global_constants_dtos=global_constants_dtos)
        global_constants_dict = self._make_global_constants_dict(
            global_constants_dtos=global_constants_dtos)

        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objs = GlobalConstant.objects.filter(
            name__in=global_constants_names, task_template_id=template_id)
        for global_constant_obj in global_constants_objs:
            global_constant_obj.value = \
                global_constants_dict[global_constant_obj.name].value

        GlobalConstant.objects.bulk_update(global_constants_objs, ['value'])

    def get_valid_template_ids_in_given_template_ids(self, template_ids: List[
        str]) -> List[str]:
        from ib_tasks.models.task_template import TaskTemplate
        valid_template_ids = list(
            TaskTemplate.objects.filter(pk__in=template_ids).values_list(
                "template_id", flat=True))
        return valid_template_ids

    def get_task_templates_dtos(self) -> List[TaskTemplateDTO]:
        task_template_objs = TaskTemplate.objects.all()
        task_template_dtos = self._convert_task_templates_objs_to_dtos(
            task_template_objs=task_template_objs)
        return task_template_dtos

    def get_gofs_to_task_templates_from_permitted_gofs(self,
                                                       gof_ids: List[str]) -> \
            List[GoFToTaskTemplateDTO]:
        task_template_gofs = \
            TaskTemplateGoFs.objects.filter(gof_id__in=gof_ids)
        gof_to_task_template_dtos = self._convert_task_template_gofs_to_dtos(
            task_template_gofs=task_template_gofs)
        return gof_to_task_template_dtos

    def get_existing_gof_ids_of_template(self, template_id: str) -> List[str]:
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs

        gof_ids_of_template_queryset = TaskTemplateGoFs.objects.filter(
            task_template_id=template_id
        ).values_list('gof_id', flat=True)

        gof_ids_of_template_list = list(gof_ids_of_template_queryset)
        return gof_ids_of_template_list

    def add_gofs_to_template(self, template_id: str,
                             gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
        gofs_to_template_objs = [
            TaskTemplateGoFs(
                task_template_id=template_id,
                gof_id=gof_dto.gof_id, order=gof_dto.order,
                enable_add_another_gof=gof_dto.enable_add_another_gof
            )
            for gof_dto in gof_dtos
        ]

        TaskTemplateGoFs.objects.bulk_create(gofs_to_template_objs)

    def update_gofs_to_template(self, template_id: str,
                                gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gof_ids = self._get_gof_ids(gof_dtos=gof_dtos)
        gofs_dict = self._make_gofs_dict(gof_dtos=gof_dtos)
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs

        gof_to_task_template_objs = TaskTemplateGoFs.objects.filter(
            gof_id__in=gof_ids, task_template_id=template_id)
        for gof_to_task_template_obj in gof_to_task_template_objs:
            gof_to_task_template_obj.order = \
                gofs_dict[gof_to_task_template_obj.gof_id].order
            gof_to_task_template_obj.enable_add_another_gof = \
                gofs_dict[
                    gof_to_task_template_obj.gof_id].enable_add_another_gof

        TaskTemplateGoFs.objects.bulk_update(
            gof_to_task_template_objs, ['order', 'enable_add_another_gof'])

    def update_task_template(self, template_id: str, template_name: str):
        from ib_tasks.models.task_template import TaskTemplate
        task_template = \
            TaskTemplate.objects.get(template_id=template_id)
        task_template.name = template_name
        task_template.save()

    @staticmethod
    def _get_global_constant_names(
            global_constants_dtos: List[GlobalConstantsDTO]):
        global_constants_names = [
            global_constants_dto.constant_name
            for global_constants_dto in global_constants_dtos
        ]
        return global_constants_names

    @staticmethod
    def _make_global_constants_dict(
            global_constants_dtos: List[GlobalConstantsDTO]):
        global_constants_dict = {}
        for global_constants_dto in global_constants_dtos:
            global_constants_dict[global_constants_dto.constant_name] = \
                global_constants_dto
        return global_constants_dict

    @staticmethod
    def _convert_task_templates_objs_to_dtos(
            task_template_objs: List[TaskTemplate]) -> List[TaskTemplateDTO]:
        task_template_dtos = [
            TaskTemplateDTO(
                template_id=task_template_obj.template_id,
                template_name=task_template_obj.name
            )
            for task_template_obj in task_template_objs
        ]
        return task_template_dtos

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
    def _get_gof_ids(gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        return gof_ids

    @staticmethod
    def _make_gofs_dict(gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gofs_dict = {}
        for gof_dto in gof_dtos:
            gofs_dict[gof_dto.gof_id] = gof_dto
        return gofs_dict