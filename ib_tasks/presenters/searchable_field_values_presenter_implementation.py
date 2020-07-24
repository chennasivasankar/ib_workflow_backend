from typing import List

from django.http import response
from ib_tasks.interactors.field_dtos import SearchableFieldDetailDTO
from ib_tasks.interactors.presenter_interfaces. \
    searchable_field_values_presenter_interface import \
    SearchableFieldValuesPresenterInterface


class SearchableFieldValuesPresenterImplementation(
    SearchableFieldValuesPresenterInterface):

    def raise_limit_should_be_greater_than_zero_exception(
            self) -> response.HttpResponse:
        import json
        from ib_tasks.constants.exception_messages import \
            LIMIT_SHOULD_BE_GREATER_THAN_ZERO
        data = json.dumps({
            "response": LIMIT_SHOULD_BE_GREATER_THAN_ZERO[0],
            "http_status_code": 400,
            "res_status": LIMIT_SHOULD_BE_GREATER_THAN_ZERO[1]
        })

        response_object = response.HttpResponse(data, 400)
        return response_object

    def raise_offset_should_be_greater_than_or_equal_to_minus_one_exception(
            self) -> response.HttpResponse:
        import json
        from ib_tasks.constants.exception_messages import \
            OFFSET_SHOULD_BE_GREATER_THAN_OR_EQAL_TO_MINUS_ONE
        data = json.dumps({
            "response": OFFSET_SHOULD_BE_GREATER_THAN_OR_EQAL_TO_MINUS_ONE[0],
            "http_status_code": 400,
            "res_status": OFFSET_SHOULD_BE_GREATER_THAN_OR_EQAL_TO_MINUS_ONE[1]
        })

        response_object = response.HttpResponse(data, 400)
        return response_object

    def get_searchable_field_values_response(self,
                                             searchable_value_detail_dtos:
                                             List[
                                                 SearchableFieldDetailDTO]) \
            -> response.HttpResponse:
        searchable_value_details = []
        for searchable_detail_dto in searchable_value_detail_dtos:
            searchable_values_detail_dict = {'id': searchable_detail_dto.id,
                                             'name': searchable_detail_dto.name}
            searchable_value_details.append(searchable_values_detail_dict)

        import json
        data = json.dumps(searchable_value_details)
        response_object = response.HttpResponse(
            data, status=200
        )
        return response_object
