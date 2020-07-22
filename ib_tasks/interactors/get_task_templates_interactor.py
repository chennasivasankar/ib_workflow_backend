from typing import List
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.presenter_interfaces.presenter_interface import \
    GetTaskTemplatesPresenterInterface
from ib_tasks.interactors.storage_interfaces.dtos import TaskTemplateDTO


class GetTaskTemplatesInteractor:
    def __init__(self, task_storage: TaskStorageInterface):
        self.task_storage = task_storage

    def get_task_templates_wrapper(
            self, user_id: int,
            presenter: GetTaskTemplatesPresenterInterface):
        complete_task_template_dto = self.get_task_templates(user_id=user_id)
        complete_task_templates_response_object = \
            presenter.get_task_templates_response(
                complete_task_templates_dto=complete_task_template_dto
            )
        return complete_task_templates_response_object

    def get_task_templates(self, user_id: int):
        task_template_dtos = self.task_storage.get_task_template_dtos()
        self._validate_task_templates_are_exists(
            task_template_dtos=task_template_dtos
        )
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        service_adapter = get_roles_service_adapter()
        roles_of_user = \
            service_adapter.roles_service.get_user_role_ids(user_id=user_id)
        actions_of_templates_dtos = self.task_storage.\
            get_user_actions_of_template_dtos(roles=roles_of_user)
        gofs_of_task_templates_dtos = \
            self.task_storage.get_gofs_of_task_templates_dtos()
        gofs_to_task_templates_dtos = \
            self.task_storage.get_gofs_to_task_templates_dtos()
        field_dtos = self.task_storage.get_field_dtos()
        user_field_permission_dtos = self.task_storage.\
            get_user_field_permission_dtos(roles=roles_of_user)
        from ib_tasks.interactors.storage_interfaces.dtos import \
            CompleteTaskTemplatesDTO
        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_templates_dtos,
            gof_dtos=gofs_of_task_templates_dtos,
            gofs_to_task_templates_dtos=gofs_to_task_templates_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
        )
        return complete_task_templates_dto

    @staticmethod
    def _validate_task_templates_are_exists(
            task_template_dtos: List[TaskTemplateDTO]):
        task_templates_are_empty = not task_template_dtos
        from ib_tasks.exceptions.custom_exceptions import \
            TaskTemplatesDoesNotExists
        from ib_tasks.constants.exception_messages import \
            TASK_TEMPLATES_DOES_NOT_EXISTS_IN_DATABASE
        if task_templates_are_empty:
            message = TASK_TEMPLATES_DOES_NOT_EXISTS_IN_DATABASE
            raise TaskTemplatesDoesNotExists(message)
