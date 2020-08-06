import abc
from typing import List


class TaskStageStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_stage_ids_of_task(self, task_id: int, stage_ids: List[int]):
        pass
