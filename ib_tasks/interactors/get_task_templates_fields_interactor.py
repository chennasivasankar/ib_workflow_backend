from typing import List

from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import FilterPresenterInterface, TaskTemplateFieldsDto
from ib_tasks.interactors.storage_interfaces.fields_dtos \
    import FieldPermissionDTO, FieldNameDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface


class GetTaskTemplatesFieldsInteractor:
    def __init__(
            self, task_storage: TaskStorageInterface,
            task_template_storage: TaskTemplateStorageInterface,
            gof_storage: GoFStorageInterface,
            field_storage: FieldsStorageInterface,
    ):
        self.field_storage = field_storage
        self.task_storage = task_storage
        self.task_template_storage = task_template_storage
        self.gof_storage = gof_storage

    def get_task_templates_fields_wrapper(
            self, user_id: str, presenter: FilterPresenterInterface):
        task_template_fields_dto = \
            self._get_task_template_fields(user_id=user_id)

        return presenter.get_response_for_get_task_templates_fields(
            task_template_fields=task_template_fields_dto
        )

    def _get_task_template_fields(self, user_id: str):
        from ib_tasks.interactors.get_task_templates_interactor \
            import GetTaskTemplatesInteractor
        interactor = GetTaskTemplatesInteractor(
            field_storage=self.field_storage,
            task_storage=self.task_storage,
            task_template_storage=self.task_template_storage,
            gof_storage=self.gof_storage
        )
        task_templates_dto = interactor.get_task_templates(user_id=user_id)
        task_templates_gofs = task_templates_dto.gofs_of_task_templates_dtos
        fields_with_permission_dtos = \
            task_templates_dto.field_with_permissions_dtos
        fields_dto = self._get_fields_dto(fields_with_permission_dtos)
        return TaskTemplateFieldsDto(
            task_template_dtos=task_templates_dto.task_template_dtos,
            gofs_of_task_templates_dtos=task_templates_gofs,
            fields_dto=fields_dto
        )

    @staticmethod
    def _get_fields_dto(fields_extra_dto: List[FieldPermissionDTO]):
        fields_dto = [
            field_dto.field_dto
            for field_dto in fields_extra_dto
        ]
        return [
            FieldNameDTO(
                field_id=field_dto.field_id,
                gof_id=field_dto.gof_id,
                field_display_name=field_dto.field_display_name
            )
            for field_dto in fields_dto
        ]
