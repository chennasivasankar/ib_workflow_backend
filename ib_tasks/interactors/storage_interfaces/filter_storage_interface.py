import abc
from typing import List

from ib_tasks.interactors.filter_dtos import FilterDTO, ConditionDTO


class FilterStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_filters_dto_to_user(self, user_id: str) -> List[FilterDTO]:
        pass

    @abc.abstractmethod
    def get_conditions_to_filters(
            self, filter_ids: List[int]) -> List[ConditionDTO]:
        pass