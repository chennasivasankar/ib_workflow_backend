import abc


class PresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_response_for_task_details(self, task_fields_dto, task_actions_dto, task_ids):
        pass