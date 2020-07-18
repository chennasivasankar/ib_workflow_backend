import abc
from typing import List

from ib_boards.interactors.dtos import TaskColumnDTO
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskActionsDTO, ColumnDetailsDTO)


class PresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_response_for_task_details(self,
                                      task_fields_dto: List[TaskFieldsDTO],
                                      task_actions_dto: List[TaskActionsDTO],
                                      task_ids: List[str]):
        pass

    @abc.abstractmethod
    def response_for_invalid_board_id(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_offset_value(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_limit_value(self):
        pass

    @abc.abstractmethod
    def response_for_user_donot_have_access_for_board(self):
        pass

    @abc.abstractmethod
    def get_response_for_column_details(self, column_details: List[ColumnDetailsDTO],
                                        task_fields_dto: List[TaskFieldsDTO],
                                        task_actions_dto: List[TaskActionsDTO],
                                        task_details: List[TaskColumnDTO]
                                        ):
        pass
