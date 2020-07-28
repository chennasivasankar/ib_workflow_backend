import abc
from typing import List


class GetAllTasksOverviewForUserPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_limit_should_be_greater_than_zero_exception(
            self):
        pass

    @abc.abstractmethod
    def raise_offset_should_be_greater_than_or_equal_to_minus_one_exception(
            self):
        pass

    @abc.abstractmethod
    def raise_stage_ids_empty_exception(
            self):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_ids(
            self, invalid_stage_ids: List[str]):
        pass
