import abc


class CreateOrUpdateTaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_task_id(self, task_id: str):
        pass