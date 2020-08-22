import abc
from dataclasses import dataclass
from typing import List

from ib_tasks.adapters.auth_service import InvalidProjectIdsException
from ib_tasks.constants.enum import Status
from ib_tasks.interactors.filter_dtos import FilterDTO, ConditionDTO, \
    FilterCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldNameDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO


@dataclass()
class TaskTemplateFieldsDto:
    task_template_dtos: List[TemplateDTO]
    gofs_of_task_templates_dtos: List[GoFToTaskTemplateDTO]
    fields_dto: List[FieldNameDTO]


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

    @abc.abstractmethod
    def get_response_for_invalid_user_to_update_filter_status(self):
        pass

    @abc.abstractmethod
    def get_response_for_update_filter_status(
            self, filter_id: int, is_selected: Status):
        pass

    @abc.abstractmethod
    def get_response_for_get_task_templates_fields(
            self, task_template_fields: TaskTemplateFieldsDto):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_project_id(
            self, err: InvalidProjectIdsException):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_in_project(self):
        pass