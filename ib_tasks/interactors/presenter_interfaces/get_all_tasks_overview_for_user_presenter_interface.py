import abc

from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO


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


class GetFilteredTasksOverviewForUserPresenterInterface(GetAllTasksOverviewForUserPresenterInterface):

    @abc.abstractmethod
    def get_response_for_filtered_tasks_overview_details_response(
            self,
            filtered_tasks_overview_details_dto: AllTasksOverviewDetailsDTO,
            total_tasks: int):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_project_id(
            self, err: InvalidProjectIdsException):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_in_project(self):
        pass
