import abc
from typing import List


class UpdateTaskStageAssigneesPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_duplicate_stage_ids_not_valid(self,
                                            duplicate_stage_ids: List[str]):
        pass

    @abc.abstractmethod
    def raise_invalid_task_id_exception(self, task_id: int):
        pass

    @abc.abstractmethod
    def raise_invalid_stage_ids_exception(self,
                                          invalid_stage_ids: List[str]):
        pass

    @abc.abstractmethod
    def raise_stage_ids_with_invalid_permission_for_assignee_exception(
            self, invalid_stage_ids: List[str]):
        pass
