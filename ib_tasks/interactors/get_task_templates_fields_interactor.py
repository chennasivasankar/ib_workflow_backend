from typing import List

from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException, UserIsNotInProjectsException
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import FilterPresenterInterface, ProjectTemplateFieldsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface


class GetTaskTemplatesFieldsInteractor:
    def __init__(
            self, task_template_storage: TaskTemplateStorageInterface,
            gof_storage: GoFStorageInterface,
            field_storage: FieldsStorageInterface,
    ):
        self.field_storage = field_storage
        self.task_template_storage = task_template_storage
        self.gof_storage = gof_storage

    def get_task_templates_fields_wrapper(
            self, user_id: str, project_id: str,
            presenter: FilterPresenterInterface):
        try:
            task_template_fields_dto = self._get_task_template_fields(
                user_id=user_id, project_id=project_id
            )
        except InvalidProjectIdsException as err:
            return presenter.get_response_for_invalid_project_id(err=err)
        except UserIsNotInProjectsException:
            return presenter.get_response_for_user_not_in_project()
        return presenter.get_response_for_get_task_templates_fields(
            task_template_fields=task_template_fields_dto
        )

    def _get_task_template_fields(
            self, user_id: str, project_id: str
    ) -> ProjectTemplateFieldsDTO:

        from ib_tasks.interactors.get_templates_fields_to_project_ids \
            import GetProjectsTemplatesFieldsInteractor
        interactor = GetProjectsTemplatesFieldsInteractor(
            field_storage=self.field_storage,
            task_template_storage=self.task_template_storage,
            gof_storage=self.gof_storage
        )
        return interactor.get_task_templates(
            user_id=user_id, project_ids=[project_id]
        )
