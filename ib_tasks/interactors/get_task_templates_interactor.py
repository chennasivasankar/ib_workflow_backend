from typing import List

from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO
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
        except TaskTemplatesDoesNotExists as err:
            return presenter.raise_task_templates_does_not_exists_exception(
                err)

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
            task_templates_dtos=task_templates_dtos
        )
        actions_of_templates_dtos = \
            self.task_storage.get_actions_of_templates_dtos()
        gof_ids_permitted_for_user = \
            self.task_storage.get_gof_ids_with_read_permission_for_user(
                roles=user_roles)
        gofs_to_task_templates_dtos = \
            self.task_storage.get_gofs_to_task_templates_from_permitted_gofs(
                gof_ids=gof_ids_permitted_for_user
            )
        gof_ids = self._get_gof_ids_of_task_templates(
            gofs_to_task_templates_dtos=gofs_to_task_templates_dtos
        )
        gofs_details_dtos = \
            self.task_storage.get_gofs_details_dtos(gof_ids=gof_ids)
        field_dtos = \
            self.task_storage.get_fields_of_gofs_in_dtos(gof_ids=gof_ids)
        field_ids = self._get_field_ids(field_dtos=field_dtos)
        user_field_permission_dtos = self.task_storage. \
            get_user_field_permission_dtos(
            roles=user_roles, field_ids=field_ids
        )
        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_templates_dtos,
            actions_of_templates_dtos=actions_of_templates_dtos,
            gof_dtos=gofs_details_dtos,
            gofs_to_task_templates_dtos=gofs_to_task_templates_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
        )
        return complete_task_templates_dto

    @staticmethod
    def _validate_task_templates_are_exists(
            task_templates_dtos: List[TaskTemplateDTO]):
        task_templates_are_empty = not task_templates_dtos
        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskTemplatesDoesNotExists
        from ib_tasks.constants.exception_messages import \
            TASK_TEMPLATES_DOES_NOT_EXISTS
        if task_templates_are_empty:
            message = TASK_TEMPLATES_DOES_NOT_EXISTS
            raise TaskTemplatesDoesNotExists(message)

    @staticmethod
    def _get_gof_ids_of_task_templates(
            gofs_to_task_templates_dtos: List[GoFToTaskTemplateDTO]):
        gof_ids = [
            gofs_to_task_templates_dto.gof_id
            for gofs_to_task_templates_dto in gofs_to_task_templates_dtos
        ]
        return gof_ids

    @staticmethod
    def _get_field_ids(field_dtos: List[FieldDTO]):
        field_ids = [field_dto.field_id for field_dto in field_dtos]
        return field_ids
