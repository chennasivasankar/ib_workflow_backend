import abc
from typing import List

from ib_tasks.adapters.dtos import UserDTO
from ib_tasks.interactors.field_dtos import SearchableFieldDetailDTO


class SearchableFieldValuesPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_limit_should_be_greater_than_zero_exception(
            self):
        pass

    @abc.abstractmethod
    def raise_offset_should_be_greater_than_or_equal_to_minus_one_exception(
            self):
        pass

    @abc.abstractmethod
    def get_searchable_field_values_response(self,
                                             searchable_value_detail_dtos:
                                             List[SearchableFieldDetailDTO]):
        pass
