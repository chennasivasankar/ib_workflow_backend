from typing import List

from ib_adhoc_tasks.adapters.dtos import FieldIdAndNameDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .adhoc_task_template_fields_presenter_interface import \
    GetAdhocTaskTemplateFieldsPresenterInterface


class AdhocTaskTemplateFieldsInteractor:

    def get_adhoc_task_template_fields_wrapper(
            self, project_id: str, user_id: str,
            presenter: GetAdhocTaskTemplateFieldsPresenterInterface
    ):
        field_dtos = self.get_adhoc_task_template_fields(
            project_id=project_id, user_id=user_id
        )
        return presenter.get_response_for_get_adhoc_task_template_fields(
            field_dtos=field_dtos
        )

    @staticmethod
    def get_adhoc_task_template_fields(
            project_id: str, user_id: str
    ) -> List[FieldIdAndNameDTO]:
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        from ib_adhoc_tasks.constants.constants import ADHOC_TEMPLATE_ID
        field_dtos = service.task_service.get_task_template_field_dtos(
            project_id=project_id, user_id=user_id,
            template_id=ADHOC_TEMPLATE_ID
        )
        from ib_adhoc_tasks.constants.enum import GroupByKey
        from ib_adhoc_tasks.adapters.dtos import FieldIdAndNameDTO
        for item in GroupByKey:
            field_dtos.append(
                FieldIdAndNameDTO(
                    field_id=item.value,
                    field_display_name=item.value.capitalize().replace('_', ' ')
                )
            )
        return field_dtos
