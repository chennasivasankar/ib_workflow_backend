from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO


class TasksService:

    @property
    def interface(self):
        pass

    def get_task_details_dtos(self, task_ids: List[str]
                              ) -> List[TasksCompleteDetailsDTO]:
        pass
