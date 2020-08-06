from typing import List, Dict
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.constants.enum import Status
from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO, \
    ConditionDTO, FilterDTO
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import FilterPresenterInterface, TaskTemplateFieldsDto
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldNameDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import TaskTemplateDTO


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
            "action": is_selected
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
        response_object = self.prepare_200_success_response(response_object)
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
        response_object = self.prepare_200_success_response(response_object)
        return response_object

    def _get_filter_details_dict(
            self, filter_dto: FilterDTO, condition_dtos: List[ConditionDTO]):
        response_object = {
            "filter_id": filter_dto.filter_id,
            "name": filter_dto.filter_name,
            "template_id": filter_dto.template_id,
            "template_name": filter_dto.template_name,
            "is_selected": filter_dto.is_selected,
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

    def get_response_for_get_task_templates_fields(
            self, task_template_fields: TaskTemplateFieldsDto):
        task_template_dtos = task_template_fields.task_template_dtos
        fields_dto = task_template_fields.fields_dto
        task_template_gofs = task_template_fields.gofs_of_task_templates_dtos
        gof_fields_dict = self._get_gof_fields_dict(fields_dto)
        task_template_gofs_dict = \
            self._get_task_template_gof_dict(task_template_gofs)
        task_template_fields_dict = self._get_template_fields_dict(
            task_template_gofs_dict, gof_fields_dict
        )
        response_dict = {
            "task_template_fields_details": [
                {
                    "task_template_id": template_dto.template_id,
                    "name": template_dto.template_name,
                    "fields": self._convert_template_fields(
                        task_template_fields_dict[template_dto.template_id]
                    )
                }
                for template_dto in task_template_dtos
            ],
            "operators": [
                "GTE", "LTE", "GT", "LE", "NE", "EQ", "CONTAINS"
            ]
        }
        response_object = self.prepare_200_success_response(response_dict)
        return response_object

    @staticmethod
    def _convert_template_fields(fields_dto: List[FieldNameDTO]):
        return [
            {
                "field_id": field_dto.field_id,
                "name": field_dto.field_display_name
            }
            for field_dto in fields_dto
        ]

    @staticmethod
    def _get_template_fields_dict(
            task_template_gofs_dict: Dict[str, List[str]],
            gof_fields_dict: Dict[str, List[FieldNameDTO]]
    ):
        from collections import defaultdict
        template_fields_dict = defaultdict(list)
        for key, values in task_template_gofs_dict.items():
            for item in values:
                for field_dto in gof_fields_dict[item]:
                    if field_dto not in template_fields_dict[key]:
                        template_fields_dict[key].append(field_dto)
        return template_fields_dict

    @staticmethod
    def _get_task_template_gof_dict(
            task_template_gofs: List[GoFToTaskTemplateDTO]):
        from collections import defaultdict
        template_gof_dict = defaultdict(list)
        for task_template_gof in task_template_gofs:
            template_id = task_template_gof.template_id
            gof_id = task_template_gof.gof_id
            template_gof_dict[template_id].append(gof_id)
        return template_gof_dict

    @staticmethod
    def _get_gof_fields_dict(fields_dto: List[FieldNameDTO]):
        from collections import defaultdict
        gof_field_dict = defaultdict(list)

        for field_dto in fields_dto:
            gof_id = field_dto.gof_id
            gof_field_dict[gof_id].append(field_dto)
        return gof_field_dict