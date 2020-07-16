"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetTasksDetailsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_tasks_details_wrapper(self, task_ids: List[str]):
        pass

    def get_task_details(self, task_ids: List[str]):
        pass
