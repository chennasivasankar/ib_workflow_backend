import abc
from typing import List, Tuple

from ib_tasks.constants.enum import Status
from ib_tasks.interactors.filter_dtos import CreateFilterDTO, \
    CreateConditionDTO, FilterDTO, ConditionDTO, UpdateFilterDTO


class FilterStorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_template_id(self, template_id: str):
        pass

    @abc.abstractmethod
    def get_field_ids_for_task_template(
            self, template_id: str, field_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_user_roles_with_field_ids_roles(
            self, user_roles, field_ids):
        pass

    @abc.abstractmethod
    def create_filter(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: List[CreateConditionDTO]) \
            -> Tuple[FilterDTO, List[ConditionDTO]]:
        pass

    @abc.abstractmethod
    def update_filter(
            self, filter_dto: UpdateFilterDTO,
            condition_dtos: List[CreateConditionDTO]) \
            -> Tuple[FilterDTO, List[ConditionDTO]]:
        pass

    @abc.abstractmethod
    def validate_filter_id(self, filter_id: int):
        pass

    @abc.abstractmethod
    def validate_user_with_filter_id(self, user_id: str, filter_id: int):
        pass

    @abc.abstractmethod
    def delete_filter(self, filter_id: int, user_id: str):
        pass

    @abc.abstractmethod
    def get_filters_dto_to_user(
            self, user_id: str, project_id: str) -> List[FilterDTO]:
        pass

    @abc.abstractmethod
    def get_conditions_to_filters(
            self, filter_ids: List[int]) -> List[ConditionDTO]:
        pass

    @abc.abstractmethod
    def update_filter_status(self, filter_id: int,
                             is_selected: Status) -> Status:
        pass

    @abc.abstractmethod
    def get_enabled_filters_dto_to_user(self, user_id: str, project_id: str):
        pass
