import abc
from ib_tasks.interactors.storage_interfaces.dtos import \
    CompleteTaskTemplatesDTO


class GetTaskTemplatesPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_task_templates_response(
            self, complete_task_templates_dto: CompleteTaskTemplatesDTO):
        pass
