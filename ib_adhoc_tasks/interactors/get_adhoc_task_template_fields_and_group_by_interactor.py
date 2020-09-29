from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.interactors.dtos.dtos import \
    TemplateFieldsAndGroupByFieldsDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_adhoc_task_template_fields_and_group_by_presenter_interface import \
    GetAdhocTaskTemplateFieldsAndGroupByPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetAdhocTaskTemplateFieldsAndGroupBy:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_adhoc_task_template_fields_and_group_by_wrapper(
            self, project_id: str, user_id: str, view_type: ViewType,
            presenter: GetAdhocTaskTemplateFieldsAndGroupByPresenterInterface
    ):
        template_fields_and_group_by_fields_dto = \
            self.get_adhoc_task_template_fields_and_group_by(
                project_id=project_id, user_id=user_id, view_type=view_type
            )
        return presenter.get_response_for_get_template_and_group_by_fields(
            template_fields_and_group_by_fields_dto=
            template_fields_and_group_by_fields_dto
        )

    def get_adhoc_task_template_fields_and_group_by(
            self, project_id: str, user_id: str, view_type: ViewType
    ) -> TemplateFieldsAndGroupByFieldsDTO:
        from ib_adhoc_tasks.interactors.group_by_interactor import \
            GroupByInteractor
        group_by_interactor = GroupByInteractor(storage=self.storage)
        group_by_fields_dtos = group_by_interactor.get_group_by(
            project_id=project_id, user_id=user_id, view_type=view_type
        )

        from ib_adhoc_tasks.interactors \
            .get_adhoc_task_template_fields_interactor import \
            AdhocTaskTemplateFieldsInteractor
        adhoc_template_fields_interactor = AdhocTaskTemplateFieldsInteractor()
        field_dtos = adhoc_template_fields_interactor \
            .get_adhoc_task_template_fields(
            project_id=project_id, user_id=user_id
        )

        return TemplateFieldsAndGroupByFieldsDTO(
            group_by_fields_dtos=group_by_fields_dtos, field_dtos=field_dtos
        )
