from typing import List, Optional, Dict

from django.db.models import Q, F

from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTransitionChecklistTemplateId
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO, ProjectTemplateDTO, ProjectIdWithTaskTemplateIdDTO, \
    TaskTemplateMandatoryFieldsDTO
from ib_tasks.interactors.task_template_dtos import TaskTemplateRolesDTO
from ib_tasks.models import TaskTemplate, TaskTemplateGoFs, \
    ProjectTaskTemplate, TaskTemplatePermittedRoles


class TaskTemplateStorageImplementation(TaskTemplateStorageInterface):

    def is_common_template(self, task_template_id: str) -> bool:
        is_common_template = ProjectTaskTemplate.objects.filter(
            task_template_id=task_template_id).exists()
        return not is_common_template

    def get_template_stage_permitted_gof_ids(
            self, task_template_id: str, stage_id: int):
        gof_ids = TaskTemplateGoFs.objects.filter(
            task_template_id=task_template_id,
            gof__stagegof__stage_id=stage_id
        ).exclude(order=-1).values_list('gof_id', flat=True)
        return gof_ids

    def get_stage_permitted_gof_ids(self, stage_id: int) -> List[str]:
        from ib_tasks.models import StageGoF
        gof_ids = StageGoF.objects.filter(stage_id=stage_id).values_list(
            'gof_id', flat=True)
        return gof_ids

    def get_task_template_initial_stage_id(self, task_template_id: str):
        from ib_tasks.models import TaskTemplateInitialStage
        stage_id = TaskTemplateInitialStage.objects.get(
            task_template_id=task_template_id).stage_id
        return stage_id

    def get_project_templates(self, project_id: str) -> List[str]:
        project_templates = \
            ProjectTaskTemplate.objects.filter(project_id=project_id). \
                values_list('task_template_id', flat=True)
        return list(project_templates)

    def validate_transition_template_id(
            self, transition_checklist_template_id
    ) -> Optional[InvalidTransitionChecklistTemplateId]:
        template_exists = TaskTemplate.objects.filter(
            template_id=transition_checklist_template_id,
            is_transition_template=True)
        if not template_exists:
            raise InvalidTransitionChecklistTemplateId(
                transition_checklist_template_id)
        return

    def create_template(self, template_id: str,
                        template_name: str,
                        is_transition_template: bool):
        from ib_tasks.models.task_template import TaskTemplate
        TaskTemplate.objects.create(
            template_id=template_id, name=template_name,
            is_transition_template=is_transition_template
        )

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

    def get_valid_task_template_ids_in_given_task_template_ids(
            self, template_ids: List[str]) -> List[str]:
        from ib_tasks.models.task_template import TaskTemplate
        valid_template_ids = list(
            TaskTemplate.objects.filter(
                pk__in=template_ids, is_transition_template=False
            ).values_list("template_id", flat=True))
        return valid_template_ids

    def get_task_templates_dtos(
            self, task_template_ids: List[str]) -> List[TemplateDTO]:
        task_template_objs = TaskTemplate.objects.filter(
            template_id__in=task_template_ids, is_transition_template=False
        )
        task_template_dtos = self._convert_task_templates_objs_to_dtos(
            task_template_objs=task_template_objs)
        return task_template_dtos

    def get_task_templates_to_project_ids(
            self, project_ids: List[str]
    ) -> List[ProjectTemplateDTO]:

        query = Q(project_id__in=project_ids) & Q(task_template__is_transition_template=False)
        task_template_objs = ProjectTaskTemplate.objects.filter(
            query
        ).annotate(template_name=F('task_template__name'))
        task_template_dtos = self._convert_project_templates_objs_to_dtos(
            task_template_objs=task_template_objs)
        return task_template_dtos

    @staticmethod
    def _convert_project_templates_objs_to_dtos(
            task_template_objs: List[ProjectTaskTemplate]
    ) -> List[ProjectTemplateDTO]:
        task_template_dtos = [
            ProjectTemplateDTO(
                template_id=task_template_obj.task_template_id,
                template_name=task_template_obj.template_name,
                project_id=task_template_obj.project_id
            )
            for task_template_obj in task_template_objs
        ]
        return task_template_dtos

    def get_gofs_to_templates_from_given_gofs(
            self, gof_ids: List[str]) -> List[GoFToTaskTemplateDTO]:
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

    def update_template(self, template_id: str, template_name: str,
                        is_transition_template: bool):
        from ib_tasks.models.task_template import TaskTemplate
        template = TaskTemplate.objects.get(template_id=template_id)
        template.name = template_name
        template.is_transition_template = is_transition_template
        template.save()

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
            task_template_objs: List[TaskTemplate]) -> List[TemplateDTO]:
        task_template_dtos = [
            TemplateDTO(
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

    def get_transition_template_dto(
            self, transition_template_id: str) -> TemplateDTO:
        transition_template_queryset = TaskTemplate.objects.filter(
            template_id=transition_template_id).values('template_id', 'name')
        transition_template = transition_template_queryset.first()

        return TemplateDTO(
            template_id=transition_template['template_id'],
            template_name=transition_template['name']
        )

    def check_is_transition_template_exists(
            self, transition_template_id: str) -> bool:
        is_transition_template_exists = TaskTemplate.objects.filter(
            template_id=transition_template_id, is_transition_template=True
        ).exists()
        return is_transition_template_exists

    def get_valid_transition_template_ids(
            self, transition_template_ids: List[str]) -> List[str]:
        transition_ids = list(TaskTemplate.objects.filter(
            template_id__in=transition_template_ids).filter(
            is_transition_template=True).values_list('template_id', flat=True))
        return transition_ids

    def get_gofs_to_template_from_given_gofs(
            self, gof_ids: List[str],
            template_id: str) -> List[GoFToTaskTemplateDTO]:
        task_template_gofs = TaskTemplateGoFs.objects.filter(
            gof_id__in=gof_ids, task_template_id=template_id
        )
        gof_to_task_template_dtos = self._convert_task_template_gofs_to_dtos(
            task_template_gofs=task_template_gofs)
        return gof_to_task_template_dtos

    def get_gof_ids_of_template(self, template_id: str) -> List[str]:
        gof_ids_queryset = TaskTemplateGoFs.objects.filter(
            task_template_id=template_id).exclude(order=-1).\
            values_list('gof_id', flat=True)
        gof_ids_list = list(gof_ids_queryset)
        return gof_ids_list

    def add_project_to_task_templates(
            self, project_id: str, task_template_ids: List[str]):
        project_task_templates = []
        for task_template_id in task_template_ids:
            project_task_template = ProjectTaskTemplate(
                task_template_id=task_template_id, project_id=project_id)
            project_task_templates.append(project_task_template)

        ProjectTaskTemplate.objects.bulk_create(project_task_templates)

    def get_existing_task_template_ids_of_project_task_templates(
            self, project_id: str, task_template_ids: List[str]) -> List[str]:
        task_template_ids_queryset = \
            ProjectTaskTemplate.objects.filter(
                project_id=project_id, task_template_id__in=task_template_ids
            ).values_list('task_template_id', flat=True)
        task_template_ids_list = list(task_template_ids_queryset)
        return task_template_ids_list

    def get_project_id_with_task_template_id_dtos(
            self) -> List[ProjectIdWithTaskTemplateIdDTO]:
        project_id_with_task_template_id_dicts = \
            ProjectTaskTemplate.objects.all().values(
                'task_template_id', 'project_id')
        project_id_with_template_id_dtos = \
            self._convert_project_id_with_template_id_dicts_to_dtos(
                project_id_with_task_template_id_dicts=
                project_id_with_task_template_id_dicts)

        return project_id_with_template_id_dtos

    @staticmethod
    def _convert_project_id_with_template_id_dicts_to_dtos(
            project_id_with_task_template_id_dicts: List[Dict]
    ) -> List[ProjectIdWithTaskTemplateIdDTO]:
        project_id_with_template_id_dtos = [
            ProjectIdWithTaskTemplateIdDTO(
                project_id=project_id_with_template_id['project_id'],
                task_template_id=
                project_id_with_template_id['task_template_id']
            )
            for project_id_with_template_id in
            project_id_with_task_template_id_dicts
        ]

        return project_id_with_template_id_dtos

    def get_project_id_to_template_stages(
            self, stage_ids: List[str]) -> List[str]:
        from ib_tasks.models import Stage
        project_ids = ProjectTaskTemplate.objects.filter(
            task_template_id__in=Stage.objects.filter(
                stage_id__in=stage_ids
            ).values_list('task_template_id', flat=True)
        ).values_list('project_id', flat=True)
        return list(set(project_ids))

    def get_gof_ids_of_templates(self, template_ids: List[str]) -> List[str]:
        gof_ids_of_templates_queryset = \
            TaskTemplateGoFs.objects.filter(
                task_template_id__in=template_ids
            ).values_list('gof_id', flat=True)

        gof_ids_of_templates_list = list(gof_ids_of_templates_queryset)
        return gof_ids_of_templates_list

    def get_task_template_ids(self) -> List[str]:
        task_template_id_queryset = \
            TaskTemplate.objects.filter(
                is_transition_template=False
            ).values_list('template_id', flat=True)
        task_template_id_list = list(task_template_id_queryset)

        return task_template_id_list

    def get_task_template_ids_of_project_task_templates(self) -> List[str]:
        task_template_id_queryset = \
            ProjectTaskTemplate.objects.all().values_list(
                'task_template_id', flat=True)

        task_template_id_list = list(task_template_id_queryset)
        return task_template_id_list

    def get_common_task_template_ids(self):
        common_templates = TaskTemplate.objects.exclude(
            template_id__in=list(ProjectTaskTemplate.objects.values_list(
                'task_template_id', flat=True
            ))
        ).filter(is_transition_template=False).values('template_id', 'name')
        return [
            ProjectTemplateDTO(
                template_name=common_template['name'],
                template_id=common_template['template_id'],
            )
            for common_template in common_templates
        ]

    def get_template_mandatory_fields_dtos(
            self, template_ids: List[str]
    ) -> List[TaskTemplateMandatoryFieldsDTO]:
        from ib_tasks.models.task_template_mandatory_fields import \
            TaskTemplateMandatoryFields
        task_template_mandatory_fields_objs = \
            TaskTemplateMandatoryFields.objects.filter(
                task_template_id__in=template_ids)
        task_template_mandatory_fields_dtos = \
            self._convert_task_template_mandatory_fields_to_dtos(
                task_template_mandatory_fields_objs=
                task_template_mandatory_fields_objs)
        return task_template_mandatory_fields_dtos

    def create_template_mandatory_fields_with_default_values(
            self, template_ids: List[str]):
        from ib_tasks.models.task_template_mandatory_fields import \
            TaskTemplateMandatoryFields
        task_template_mandatory_field_objs = [
            TaskTemplateMandatoryFields(task_template_id=template_id)
            for template_id in template_ids
        ]
        TaskTemplateMandatoryFields.objects.bulk_create(
            task_template_mandatory_field_objs)

    def get_user_permitted_task_template_ids(
            self, user_roles: List[str]) -> List[str]:
        task_template_ids_queryset = \
            TaskTemplatePermittedRoles.objects.filter(
                role_id__in=user_roles).values_list(
                'task_template_id', flat=True)
        task_template_ids_list = list(task_template_ids_queryset)
        return task_template_ids_list

    def create_task_template_permitted_roles(
            self, task_template_role_dtos: List[TaskTemplateRolesDTO]):
        task_template_role_objs = self._make_task_template_permitted_role_objs(
            task_template_role_dtos=task_template_role_dtos
        )
        TaskTemplatePermittedRoles.objects.bulk_create(task_template_role_objs)

    def get_existing_role_dtos_of_task_templates(
            self, task_template_ids: List[str]) -> List[TaskTemplateRolesDTO]:
        task_template_role_values = TaskTemplatePermittedRoles.objects.filter(
            task_template_id__in=task_template_ids
        ).values('task_template_id', 'role_id')

        task_template_role_dtos = self._convert_task_template_role_dtos(
            task_template_role_values=task_template_role_values)
        return task_template_role_dtos

    @staticmethod
    def _convert_task_template_role_dtos(
            task_template_role_values: List[Dict]
    ) -> List[TaskTemplateRolesDTO]:
        import collections
        role_ids_group_by_task_template_ids = collections.defaultdict(List)
        for task_template_role_value in task_template_role_values:
            role_ids_group_by_task_template_ids[
                task_template_role_value['task_template_id']
            ].append(task_template_role_value['role_id'])

        task_template_role_dtos = []
        for task_template_id, role_ids in role_ids_group_by_task_template_ids:
            task_template_role_dtos.append(
                TaskTemplateRolesDTO(
                    task_template_id=task_template_id,
                    role_ids=role_ids
                )
            )
        return task_template_role_dtos

    @staticmethod
    def _make_task_template_permitted_role_objs(
            task_template_role_dtos: List[TaskTemplateRolesDTO]):
        task_template_role_objs = []
        for task_template_roles_dto in task_template_role_dtos:
            for role_id in task_template_roles_dto.role_ids:
                task_template_role_objs.append(
                    TaskTemplatePermittedRoles(
                        task_template_id=
                        task_template_roles_dto.task_template_id,
                        role_id=role_id
                    )
                )
        return task_template_role_objs

    @staticmethod
    def _convert_task_template_mandatory_fields_to_dtos(
            task_template_mandatory_fields_objs
    ) -> List[TaskTemplateMandatoryFieldsDTO]:
        task_template_mandatory_fields_dtos = [
            TaskTemplateMandatoryFieldsDTO(
                template_id=
                task_template_mandatory_fields_obj.task_template_id,
                title_display_name=
                task_template_mandatory_fields_obj.title_display_name,
                title_placeholder_text=
                task_template_mandatory_fields_obj.title_placeholder_text
            )
            for task_template_mandatory_fields_obj in
            task_template_mandatory_fields_objs
        ]
        return task_template_mandatory_fields_dtos
