import abc
from typing import List

from ib_tasks.interactors.filter_dtos import FilterDTO, ConditionDTO, \
    FilterCompleteDetailsDTO


class FilterPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_invalid_task_template_id(self):
        pass

    @abc.abstractmethod
    def get_response_for_create_filter(
            self, filter_dto: FilterDTO, condition_dtos: List[ConditionDTO]):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_field_ids(self, error):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_have_access_to_fields(self):
        pass

    @abc.abstractmethod
    def get_response_for_update_filter(
            self, filter_dto: FilterDTO, condition_dtos: List[ConditionDTO]):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_filter_id(self):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_have_access_to_update_filter(self):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_have_access_to_delete_filter(self):
        pass

    def get_response_for_get_filters_details(
            self, filter_complete_details: FilterCompleteDetailsDTO):
        pass