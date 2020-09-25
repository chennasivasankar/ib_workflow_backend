from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.adapters.dtos import FieldIdAndNameDTO
from ib_adhoc_tasks.interactors.dtos.dtos import \
    TemplateFieldsAndGroupByFieldsDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_adhoc_task_template_fields_and_group_by_presenter_interface import \
    GetAdhocTaskTemplateFieldsAndGroupByPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByResponseDTO


class GetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation(
    GetAdhocTaskTemplateFieldsAndGroupByPresenterInterface, HTTPResponseMixin
):

    def get_response_for_get_template_and_group_by_fields(
            self,
            template_fields_and_group_by_fields_dto:
            TemplateFieldsAndGroupByFieldsDTO
    ):
        group_by_fields_response = [
            self._convert_to_group_by_response_dict(
                group_by_fields_dto=group_by_fields_dto
            )
            for group_by_fields_dto in
            template_fields_and_group_by_fields_dto.group_by_fields_dtos
        ]
        all_fields_response = [
            self._convert_to_group_by_key_name_dictionary(field_dto=field_dto)
            for field_dto in template_fields_and_group_by_fields_dto.field_dtos
        ]
        response_dict = {
            "all_fields": all_fields_response,
            "group_by_fields": group_by_fields_response
        }
        return self.prepare_200_success_response(
            response_dict=response_dict
        )

    @staticmethod
    def _convert_to_group_by_response_dict(
            group_by_fields_dto: GroupByResponseDTO
    ):
        return {
            "group_by_id": group_by_fields_dto.group_by_id,
            "group_by_key": group_by_fields_dto.group_by_key,
            "display_name": group_by_fields_dto.display_name,
            "order": group_by_fields_dto.order
        }

    @staticmethod
    def _convert_to_group_by_key_name_dictionary(
            field_dto: FieldIdAndNameDTO
    ):
        return {
            "group_by_key": field_dto.field_id,
            "display_name": field_dto.field_display_name
        }
