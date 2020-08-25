import abc

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
