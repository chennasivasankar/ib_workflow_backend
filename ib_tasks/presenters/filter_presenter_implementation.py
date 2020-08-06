from typing import List
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.constants.enum import Status
from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO, \
    ConditionDTO, FilterDTO
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import FilterPresenterInterface


class FilterPresenterImplementation(
        FilterPresenterInterface, HTTPResponseMixin):

    def get_response_for_invalid_filter_id(self):
        from ib_tasks.constants.exception_messages import INVALID_FILTER_ID
        response_dict = {
            "response": INVALID_FILTER_ID[0],
            "http_status_code": 404,
            "res_status": INVALID_FILTER_ID[1]
        }

        response_object = self.prepare_404_not_found_response(response_dict)
        return response_object

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
                "template_id": filter_dto.template_id,
                "template_name": filter_dto.template_name,
                "status": filter_dto.is_selected,
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

    def get_response_for_invalid_task_template_id(self):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_TEMPLATE_ID
        response_dict = {
            "response": INVALID_TASK_TEMPLATE_ID[0],
            "http_status_code": 403,
            "res_status": INVALID_TASK_TEMPLATE_ID[1]
        }

        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object

    def get_response_for_create_filter(
            self, filter_dto: FilterDTO, condition_dtos: List[ConditionDTO]):
        response_object = self._get_filter_details_dict(
            condition_dtos=condition_dtos, filter_dto=filter_dto
        )
        response_object = self.prepare_201_created_response(response_object)
        return response_object

    def get_response_for_invalid_field_ids(self, error):
        from ib_tasks.constants.exception_messages import \
            FIELDS_NOT_BELONGS_TO_TASK_TEMPLATE
        response_dict = {
            "response": FIELDS_NOT_BELONGS_TO_TASK_TEMPLATE[0].format(error.field_ids),
            "http_status_code": 403,
            "res_status": FIELDS_NOT_BELONGS_TO_TASK_TEMPLATE[1]
        }
        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object

    def get_response_for_user_not_have_access_to_fields(self):
        from ib_tasks.constants.exception_messages import \
            USER_NOT_ACCESS_TO_FIELDS
        response_dict = {
            "response": USER_NOT_ACCESS_TO_FIELDS[0],
            "http_status_code": 403,
            "res_status": USER_NOT_ACCESS_TO_FIELDS[1]
        }

        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object

    def get_response_for_update_filter(
            self, filter_dto: FilterDTO, condition_dtos: List[ConditionDTO]):
        response_object = self._get_filter_details_dict(
            condition_dtos=condition_dtos, filter_dto=filter_dto
        )
        response_object = self.prepare_201_created_response(response_object)
        return response_object

    def _get_filter_details_dict(
            self, filter_dto: FilterDTO, condition_dtos: List[ConditionDTO]):
        response_object = {
            "filter_id": filter_dto.filter_id,
            "name": filter_dto.filter_name,
            "template_id": filter_dto.template_id,
            "template_name": filter_dto.template_name,
            "status": filter_dto.is_selected,
            "conditions": self._get_conditions_to_filter(
                conditions_dto=condition_dtos
            )
        }
        return response_object

    def get_response_for_user_not_have_access_to_update_filter(self):
        from ib_tasks.constants.exception_messages import \
            USER_DO_NOT_ACCESS_TO_UPDATE_FILTER
        response_dict = {
            "response": USER_DO_NOT_ACCESS_TO_UPDATE_FILTER[0],
            "http_status_code": 403,
            "res_status": USER_DO_NOT_ACCESS_TO_UPDATE_FILTER[1]
        }

        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object

    def get_response_for_user_not_have_access_to_delete_filter(self):
        from ib_tasks.constants.exception_messages import \
            USER_DO_NOT_ACCESS_TO_DELETE_FILTER
        response_dict = {
            "response": USER_DO_NOT_ACCESS_TO_DELETE_FILTER[0],
            "http_status_code": 403,
            "res_status": USER_DO_NOT_ACCESS_TO_DELETE_FILTER[1]
        }

        response_object = self.prepare_403_forbidden_response(response_dict)
        return response_object
