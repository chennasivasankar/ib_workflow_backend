import abc
from typing import List

from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


class GetAllTasksOverviewForUserPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_limit_should_be_greater_than_zero_exception(
            self):
        pass

    @abc.abstractmethod
    def raise_offset_should_be_greater_than_zero_exception(
            self):
        pass


    @abc.abstractmethod
    def raise_stage_ids_empty_exception(
            self):
        pass

    @abc.abstractmethod
    def all_tasks_overview_details_response(
            self, all_tasks_overview_details_dto: AllTasksOverviewDetailsDTO):
        pass
