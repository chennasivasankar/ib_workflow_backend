import abc
from typing import List

from ib_tasks.constants.enum import Status
from ib_tasks.interactors.filter_dtos import FilterDTO, ConditionDTO


class FilterStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_filters_dto_to_user(self, user_id: str) -> List[FilterDTO]:
        pass

    @abc.abstractmethod
    def get_conditions_to_filters(
            self, filter_ids: List[int]) -> List[ConditionDTO]:
        pass

    @abc.abstractmethod
    def validate_filter_id(self, filter_id: int):
        pass

    @abc.abstractmethod
    def validate_user_with_filter_id(self, user_id: str, filter_id: int):
        pass

    @abc.abstractmethod
    def enable_filter_status(self, filter_id: int) -> Status:
        pass

    @abc.abstractmethod
    def disable_filter_status(self, filter_id: int) -> Status:
        pass