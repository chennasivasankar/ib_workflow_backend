import abc
from typing import List

from ib_tasks.adapters.dtos import UserDetailsDTO
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskDisplayId


class GetTaskRpsPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def response_for_invalid_task_id(self, err: InvalidTaskDisplayId):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_assignee_for_task(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_stage_id(self):
        pass

    @abc.abstractmethod
    def response_for_get_rps_details(self, rps_dtos: List[UserDetailsDTO]):
        pass

    @abc.abstractmethod
    def response_for_due_date_does_not_exist_to_task(self):
        pass
