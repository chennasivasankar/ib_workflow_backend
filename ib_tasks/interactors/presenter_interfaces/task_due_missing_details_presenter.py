import abc


class TaskDueDetailsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_invalid_task_id(self):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_assignee_for_task(self):
        pass

    @abc.abstractmethod
    def get_response_for_get_task_due_details(self, task_dtos):
        pass

