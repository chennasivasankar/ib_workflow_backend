from typing import List, Dict

from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import ProjectTemplateFieldsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    TaskTemplateGofsDTO
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface

from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    ProjectTemplateDTO


class GetProjectsTemplatesFieldsInteractor(ValidationMixin):
    def __init__(
            self, task_template_storage: TaskTemplateStorageInterface,
            gof_storage: GoFStorageInterface,
            field_storage: FieldsStorageInterface,
    ):
        self.field_storage = field_storage
        self.task_template_storage = task_template_storage
        self.gof_storage = gof_storage

    def get_task_templates(
            self, user_id: str, project_ids: List[str]
    ) -> ProjectTemplateFieldsDTO:

        self.validate_given_project_ids(project_ids=project_ids)
        self.validate_if_user_is_in_projects(
            user_id=user_id, project_ids=project_ids
        )
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        service_adapter = get_roles_service_adapter()
        user_roles = \
            service_adapter.roles_service.get_user_role_ids(user_id=user_id)

        complete_task_templates_dto = self._get_complete_task_templates_dto(
            user_roles=user_roles, project_ids=project_ids
        )
        return complete_task_templates_dto

    @staticmethod
    def _get_template_ids(template_dtos: List[ProjectTemplateDTO]) -> List[str]:

        return [
            template_dto.template_id
            for template_dto in template_dtos
        ]

    @staticmethod
    def _get_gof_ids(template_gof_dtos: List[TaskTemplateGofsDTO]):

        gof_ids = []
        for template_gof_dto in template_gof_dtos:
            for gof_id in template_gof_dto.gof_ids:
                gof_ids.append(gof_id)
        return sorted(list(set(gof_ids)))

    def _get_complete_task_templates_dto(
            self, user_roles: List[str], project_ids: List[str]
    ) -> ProjectTemplateFieldsDTO:
        template_dtos = self.task_template_storage.get_task_templates_to_project_ids(
            project_ids=project_ids
        )
        template_ids = self._get_template_ids(template_dtos)
        template_gof_dtos = self.gof_storage.get_user_permitted_template_gof_dtos(
                user_roles=user_roles, template_ids=template_ids)

        gof_ids = self._get_gof_ids(template_gof_dtos)

        field_dtos = self.field_storage.get_user_permitted_gof_field_dtos(
            user_roles=user_roles, gof_ids=gof_ids
        )
        return ProjectTemplateFieldsDTO(
            task_template_dtos=template_dtos,
            task_template_gofs_dtos=template_gof_dtos,
            fields_dto=field_dtos
        )
