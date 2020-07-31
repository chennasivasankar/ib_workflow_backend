from typing import List

from django.http import response
from ib_tasks.interactors.field_dtos import SearchableFieldDetailDTO
from ib_tasks.interactors.presenter_interfaces. \
    searchable_field_values_presenter_interface import \
    SearchableFieldValuesPresenterInterface
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin


class SearchableFieldValuesPresenterImplementation(
    SearchableFieldValuesPresenterInterface, HTTPResponseMixin):

    def raise_limit_should_be_greater_than_zero_exception(
            self) -> response.HttpResponse:
        from ib_tasks.constants.exception_messages import \
            LIMIT_SHOULD_BE_GREATER_THAN_ZERO
        response_dict = {
            "response": LIMIT_SHOULD_BE_GREATER_THAN_ZERO[0],
            "http_status_code": 400,
            "res_status": LIMIT_SHOULD_BE_GREATER_THAN_ZERO[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_offset_should_be_greater_than_or_equal_to_minus_one_exception(
            self) -> response.HttpResponse:
        from ib_tasks.constants.exception_messages import \
            OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_MINUS_ONE
        response_dict = {
            "response": OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_MINUS_ONE[0],
            "http_status_code": 400,
            "res_status": OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_MINUS_ONE[
                1]
        }

        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

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

        return self.prepare_200_success_response(
            response_dict=searchable_value_details
        )
