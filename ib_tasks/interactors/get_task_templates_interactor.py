from typing import List, Dict

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageIdWithTemplateIdDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    UserFieldPermissionDTO, FieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO
from ib_tasks.interactors.presenter_interfaces. \
    get_task_templates_presenter_interface import \
    GetTaskTemplatesPresenterInterface, CompleteTaskTemplatesDTO


class GetTaskTemplatesInteractor:
    def __init__(self, task_storage: TaskStorageInterface):
        self.task_storage = task_storage

    def get_task_templates_wrapper(
            self, user_id: str,
            presenter: GetTaskTemplatesPresenterInterface):

        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskTemplatesDoesNotExists
        try:
            complete_task_templates_dto = \
                self.get_task_templates(user_id=user_id)
        except TaskTemplatesDoesNotExists:
            return presenter.raise_task_templates_does_not_exists_exception()

        complete_task_templates_response_object = \
            presenter.get_task_templates_response(
                complete_task_templates_dto=complete_task_templates_dto
            )
        return complete_task_templates_response_object

    def get_task_templates(self, user_id: str):

        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        service_adapter = get_roles_service_adapter()
        user_roles = \
            service_adapter.roles_service.get_user_role_ids(user_id=user_id)

        complete_task_templates_dto = \
            self._get_complete_task_templates_dto(user_roles=user_roles)
        return complete_task_templates_dto

    def _get_complete_task_templates_dto(
            self, user_roles: List[str]) -> CompleteTaskTemplatesDTO:
        task_templates_dtos = self.task_storage.get_task_templates_dtos()
        self._validate_task_templates_are_exists(
            task_templates_dtos=task_templates_dtos)
        stage_id_with_template_id_dtos = \
            self.task_storage.get_initial_stage_id_with_template_id_dtos()
        stage_ids = self._get_stage_ids(
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos)
        action_with_stage_id_dtos = \
            self.task_storage.get_actions_for_given_stage_ids_in_dtos(
                stage_ids=stage_ids)
        gof_ids_permitted_for_user = \
            self.task_storage.get_gof_ids_with_read_permission_for_user(
                roles=user_roles)
        gofs_of_task_templates_dtos = \
            self.task_storage.get_gofs_to_task_templates_from_permitted_gofs(
                gof_ids=gof_ids_permitted_for_user)
        gofs_details_dtos = \
            self.task_storage.get_gofs_details_dtos(
                gof_ids=gof_ids_permitted_for_user)
        field_with_permissions_dtos = \
            self._get_field_with_permissions_of_gofs_in_dtos(
                gof_ids=gof_ids_permitted_for_user, user_roles=user_roles)

        return CompleteTaskTemplatesDTO(
            task_template_dtos=task_templates_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gofs_details_dtos,
            gofs_of_task_templates_dtos=gofs_of_task_templates_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos)

    def _get_field_with_permissions_of_gofs_in_dtos(
            self, gof_ids: List[str],
            user_roles: List[str]) -> List[FieldPermissionDTO]:
        field_dtos = \
            self.task_storage.get_fields_of_gofs_in_dtos(gof_ids=gof_ids)
        field_ids = self._get_field_ids(field_dtos=field_dtos)
        user_field_permission_dtos = self.task_storage. \
            get_user_field_permission_dtos(
            roles=user_roles, field_ids=field_ids
        )
        user_field_permission_dtos_dict = \
            self._make_user_field_permission_dtos_dict(
                user_field_permission_dtos=user_field_permission_dtos
            )

        field_with_write_permission_dtos = []
        for field_dto in field_dtos:
            if field_dto.field_id in user_field_permission_dtos_dict.keys():
                permission_type = \
                    user_field_permission_dtos_dict[
                        field_dto.field_id].permission_type
                field_with_write_permission_dto = \
                    self._get_field_with_permissions_dto(
                        field_dto=field_dto,
                        permission_type=permission_type
                    )
                field_with_write_permission_dtos. \
                    append(field_with_write_permission_dto)
        return field_with_write_permission_dtos

    @staticmethod
    def _get_field_with_permissions_dto(
            field_dto: FieldDTO,
            permission_type: PermissionTypes) -> FieldPermissionDTO:
        has_write_permission = permission_type == PermissionTypes.WRITE.value
        is_field_writable = False
        if has_write_permission:
            is_field_writable = True

        field_with_write_permission_dto = FieldPermissionDTO(
            field_dto=field_dto,
            is_field_writable=is_field_writable
        )
        return field_with_write_permission_dto

    @staticmethod
    def _make_user_field_permission_dtos_dict(
            user_field_permission_dtos: List[UserFieldPermissionDTO]) -> Dict:
        import collections
        user_permission_dtos_dict = collections.defaultdict()

        for user_field_permission_dto in user_field_permission_dtos:
            user_permission_dtos_dict[user_field_permission_dto.field_id] = \
                user_field_permission_dto

        return user_permission_dtos_dict

    @staticmethod
    def _validate_task_templates_are_exists(
            task_templates_dtos: List[TaskTemplateDTO]):
        task_templates_are_empty = not task_templates_dtos
        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskTemplatesDoesNotExists

        if task_templates_are_empty:
            raise TaskTemplatesDoesNotExists()

    @staticmethod
    def _get_gof_ids_of_task_templates(
            gofs_of_task_templates_dtos: List[GoFToTaskTemplateDTO]
    ) -> List[str]:
        gof_ids = [
            gofs_to_task_templates_dto.gof_id
            for gofs_to_task_templates_dto in gofs_of_task_templates_dtos
        ]
        return gof_ids

    @staticmethod
    def _get_field_ids(field_dtos: List[FieldDTO]) -> List[str]:
        field_ids = [field_dto.field_id for field_dto in field_dtos]
        return field_ids

    @staticmethod
    def _get_stage_ids(
            stage_id_with_template_id_dtos: List[StageIdWithTemplateIdDTO]
    ) -> List[int]:
        stage_ids = [
            stage_id_with_template_id_dto.stage_id
            for stage_id_with_template_id_dto in stage_id_with_template_id_dtos
        ]
        return stage_ids
