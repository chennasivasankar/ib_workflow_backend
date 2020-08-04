import abc


class UpdateTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_update_task_response(self):
        pass
