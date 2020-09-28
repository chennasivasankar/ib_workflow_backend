from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.adapters.dtos import FieldIdAndNameDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .adhoc_task_template_fields_presenter_interface import \
    GetAdhocTaskTemplateFieldsPresenterInterface


class GetAdhocTaskTemplateFieldsPresenterImplementation(
    GetAdhocTaskTemplateFieldsPresenterInterface, HTTPResponseMixin
):
    def get_response_for_get_adhoc_task_template_fields(
            self, field_dtos: List[FieldIdAndNameDTO]
    ):
        from ib_adhoc_tasks.constants.enum import GroupByKey
        response = [
            self._convert_to_group_by_key_name_dictionary(field_dto=field_dto)
            for field_dto in field_dtos
            if field_dto.field_id not in [
                GroupByKey.DUE_DATE.value, GroupByKey.START_DATE.value
            ]
        ]
        return self.prepare_200_success_response(response_dict=response)

    @staticmethod
    def _convert_to_group_by_key_name_dictionary(
            field_dto: FieldIdAndNameDTO
    ):
        return {
            "group_by_key": field_dto.field_id,
            "display_name": field_dto.field_display_name
        }
