

import abc


class UserActionOnTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_task(self, task_id: str):
        pass
