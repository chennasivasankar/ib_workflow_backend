from typing import List, Optional

from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import TaskStatusDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, FieldRoleDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, GoFRoleDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO, StageDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.models import TaskTemplateStatusVariable
from ib_tasks.models import GoFRole, GoF
from ib_tasks.models.field import Field
from ib_tasks.models.field_role import FieldRole


class TasksStorageImplementation(TaskStorageInterface):


    def get_task_template_name_if_exists(self, template_id: str) -> str:
        pass

    def create_task_template(self, template_id: str, template_name: str):
        from ib_tasks.models.task_template import TaskTemplate
        TaskTemplate.objects.create(
            template_id=template_id, name=template_name
        )

    def update_task_template(
            self, template_id: str, template_name: str):
        from ib_tasks.models.task_template import TaskTemplate
        task_template = \
            TaskTemplate.objects.get(template_id=template_id)
        task_template.name = template_name
        task_template.save()

    def get_task_template_name(self, template_id: str) -> str:
        from ib_tasks.models.task_template import TaskTemplate
        template_name_query_set = \
            TaskTemplate.objects.filter(
                template_id=template_id
            ).values_list('name', flat=True)
        return template_name_query_set.first()

    def get_task_template_ids(self) -> List[str]:
        pass

    def create_fields(self, field_dtos: List[FieldDTO]):
        from ib_tasks.models.field import Field
        fields = self._get_fields(field_dtos)
        Field.objects.bulk_create(fields)

    def get_valid_template_ids_in_given_template_ids(
            self, template_ids: List[str]
    ) -> List[str]:
        from ib_tasks.models.task_template import TaskTemplate
        valid_template_ids = list(
            TaskTemplate.objects.filter(pk__in=template_ids).
                values_list("template_id", flat=True)
        )
        # TODO need to set return value
        return ['FIN_PR', 'FIN_PR', 'FIN_PR', 'FIN_PR']

    def get_existing_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(pk__in=gof_ids).values_list('gof_id', flat=True)
        )
        return existing_gof_ids

    def create_gofs(self, gof_dtos: List[GoFDTO]):
        from ib_tasks.models.gof import GoF
        gof_objects = [
            GoF(
                gof_id=gof_dto.gof_id,
                display_name=gof_dto.gof_display_name,
                max_columns=gof_dto.max_columns
            )
            for gof_dto in gof_dtos
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

    @staticmethod
    def _get_matching_gof_dto(
            gof_id: str, gof_dtos: List[GoFDTO]
    ) -> Optional[GoFDTO]:
        for gof_dto in gof_dtos:
            gof_id_matched = gof_id == gof_dto.gof_id
            if gof_id_matched:
                return gof_dto
        return

    def delete_gof_roles(self, gof_ids: List[str]):
        GoFRole.objects.filter(gof_id__in=gof_ids).delete()

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
        list_of_fields = [
            'display_name', 'gof_id',
            'required', 'field_type',
            'field_values', 'allowed_formats',
            'help_text', 'tooltip',
            'placeholder_text', 'error_messages',
            'validation_regex'
        ]
        fields = self._get_fields(field_dtos)
        Field.objects.bulk_update(fields, list_of_fields)

    def create_fields_roles(self, field_role_dtos: List[FieldRoleDTO]):
        fields_roles = self._get_fields_roles(field_role_dtos)
        FieldRole.objects.bulk_create(fields_roles)

    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        from ib_tasks.models.field import Field
        existing_field_ids = list(
            Field.objects.filter(
                field_id__in=field_ids
            ).values_list("field_id", flat=True)
        )
        return existing_field_ids

    def get_existing_gof_ids(self, gof_ids: List[str]) -> List[str]:
        from ib_tasks.models.gof import GoF
        existing_gof_ids = list(
            GoF.objects.filter(gof_id__in=gof_ids).values_list("gof_id", flat=True)
        )
        return existing_gof_ids

    @staticmethod
    def _get_fields(field_dtos: List[FieldDTO]):
        fields = [
            Field(
                field_id=field_dto.field_id,
                display_name=field_dto.field_display_name,
                required=field_dto.required,
                field_type=field_dto.field_type,
                field_values=field_dto.field_values,
                allowed_formats=field_dto.allowed_formats,
                help_text=field_dto.help_text,
                tooltip=field_dto.tooltip,
                placeholder_text=field_dto.placeholder_text,
                error_messages=field_dto.error_message,
                validation_regex=field_dto.validation_regex,
                gof_id=field_dto.gof_id
            )
            for field_dto in field_dtos
        ]
        return fields

    @staticmethod
    def _get_fields_roles(field_role_dtos):
        fields_roles = [
            FieldRole(
                field_id=field_role_dto.field_id,
                role=field_role_dto.role,
                permission_type=field_role_dto.permission_type
            )
            for field_role_dto in field_role_dtos
        ]
        return fields_roles

    def get_existing_template_ids(self):
        pass

    def get_existing_gof_ids_of_template(
            self, template_id: str) -> List[str]:
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs

        gof_ids_of_template_queryset = TaskTemplateGoFs.objects.filter(
            task_template_id=template_id
        ).values_list('gof_id', flat=True)

        gof_ids_of_template_list = list(gof_ids_of_template_queryset)
        return gof_ids_of_template_list

    def add_gofs_to_template(
            self, template_id: str,
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

    def update_gofs_to_template(
            self, template_id: str,
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):

        gof_ids = self._get_gof_ids(gof_dtos=gof_dtos)
        gofs_dict = self._make_gofs_dict(gof_dtos=gof_dtos)
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs

        gof_to_task_template_objs = TaskTemplateGoFs.objects.filter(
            gof_id__in=gof_ids, task_template_id=template_id
        )
        for gof_to_task_template_obj in gof_to_task_template_objs:
            gof_to_task_template_obj.order = \
                gofs_dict[gof_to_task_template_obj.gof_id].order
            gof_to_task_template_obj.enable_add_another_gof = \
                gofs_dict[gof_to_task_template_obj.gof_id].enable_add_another_gof

        TaskTemplateGoFs.objects.bulk_update(
            gof_to_task_template_objs, ['order', 'enable_add_another_gof']
        )

    def get_valid_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]) -> List[str]:
        from ib_tasks.models.gof import GoF
        gof_ids_queryset = GoF.objects.filter(
            gof_id__in=gof_ids
        ).values_list('gof_id', flat=True)

        gof_ids_list = list(gof_ids_queryset)
        return gof_ids_list

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
                max_columns=gof.max_columns
            )
            for gof in gofs
        ]
        return gof_dtos

    def create_status_for_tasks(self, create_status_for_tasks: List[TaskStatusDTO]):
        list_of_status_tasks = [TaskTemplateStatusVariable(
            variable=status.status_variable_id,
            task_template_id=status.task_template_id
        ) for status in create_status_for_tasks]

        TaskTemplateStatusVariable.objects.bulk_create(list_of_status_tasks)

    def update_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):

        global_constants_names = self._get_global_constant_names(
            global_constants_dtos=global_constants_dtos
        )
        global_constants_dict = self._make_global_constants_dict(
            global_constants_dtos=global_constants_dtos
        )

        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objs = GlobalConstant.objects.filter(
            name__in=global_constants_names, task_template_id=template_id
        )
        for global_constant_obj in global_constants_objs:
            global_constant_obj.value = \
                global_constants_dict[global_constant_obj.name].value

        GlobalConstant.objects.bulk_update(global_constants_objs, ['value'])

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
    def _get_gof_ids(gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        return gof_ids

    @staticmethod
    def _make_gofs_dict(gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gofs_dict = {}
        for gof_dto in gof_dtos:
            gofs_dict[gof_dto.gof_id] = gof_dto
        return gofs_dict

    def delete_field_roles(self, field_ids: List[str]):
        FieldRole.objects.filter(field_id__in=field_ids).delete()

    def create_stages_with_given_information(self,
                                             stage_information: StageDTO):
        pass

    def validate_stage_ids(self, stage_ids) -> Optional[List[str]]:
        pass

    def update_stages_with_given_information(self,
                                             update_stages_information: StageDTO):
        pass

    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto: TaskStagesDTO) -> \
            Optional[List[TaskStagesDTO]]:
        pass
