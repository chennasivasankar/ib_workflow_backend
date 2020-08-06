from typing import List
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.constants.enum import Status
from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO, ConditionDTO
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import FilterPresenterInterface


class FilterPresenterImplementation(
        FilterPresenterInterface, HTTPResponseMixin):

    def get_response_for_invalid_filter_id(self):
        pass

    def get_response_for_update_filter_status(
            self, filter_id: int, is_selected: Status):

        response_dict = {
            "filter_id": filter_id,
            "action": "ENABLED"
        }
        response_object = self.prepare_200_success_response(response_dict)
        return response_object

    def get_response_for_invalid_user_to_update_filter_status(self):
        from ib_tasks.constants.exception_messages import \
            USER_DO_NOT_ACCESS_TO_UPDATE_FILTER_STATUS

        response_dict = {
            "response": USER_DO_NOT_ACCESS_TO_UPDATE_FILTER_STATUS[0],
            "http_status_code": 403,
            "res_status": USER_DO_NOT_ACCESS_TO_UPDATE_FILTER_STATUS[1]
        }

        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object

    def get_response_for_get_filters_details(
            self, filter_complete_details: FilterCompleteDetailsDTO):

        filters_dto = filter_complete_details.filters_dto
        conditions_dto = filter_complete_details.conditions_dto
        filter_conditions_dict = self._get_filter_conditions_dict(conditions_dto)
        response_object = [
            {
                "filter_id": filter_dto.filter_id,
                "name": filter_dto.filter_name,
                "status": filter_dto.is_selected,
                "template_id": filter_dto.template_id,
                "template_name": filter_dto.template_name,
                "conditions": self._get_conditions_to_filter(
                    conditions_dto=filter_conditions_dict[filter_dto.filter_id]
                )
            }
            for filter_dto in filters_dto
        ]
        response_object = self.prepare_200_success_response(response_object)
        return response_object

    @staticmethod
    def _get_conditions_to_filter(conditions_dto: List[ConditionDTO]):
        return [
            {
                "condition_id": condition_dto.condition_id,
                "field_id": condition_dto.field_id,
                "operator": condition_dto.operator,
                "value": condition_dto.value,
                "field_name": condition_dto.field_name
            }
            for condition_dto in conditions_dto
        ]

    @staticmethod
    def _get_filter_conditions_dict(conditions_dto: List[ConditionDTO]):

        from collections import defaultdict
        filter_conditions_dict = defaultdict(list)

        for condition_dto in conditions_dto:
            filter_id = condition_dto.filter_id
            filter_conditions_dict[filter_id].append(condition_dto)
        return filter_conditions_dict
