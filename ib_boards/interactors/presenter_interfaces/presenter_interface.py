import abc
from typing import List

from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskActionsDTO)


class PresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_response_for_task_details(self,
                                      task_fields_dto: List[TaskFieldsDTO],
                                      task_actions_dto: List[TaskActionsDTO],
                                      task_ids: List[str]):
        pass


    @abc.abstractmethod
    def raise_exception_for_invalid_board_id(self):
        pass


    @abc.abstractmethod
    def raise_exception_for_invalid_offset_value(self):
        pass


    @abc.abstractmethod
    def raise_exception_for_invalid_limit_value(self):
        pass


    @abc.abstractmethod
    def raise_exception_for_user_donot_have_access_for_board(self):
        pass