# from typing import List
#
# from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
#     TaskStorageInterface
# from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
#
#
# class GetTaskFieldsAndActionsInteractor:
#     def __init__(self, storage: TaskStorageInterface):
#         self.storage = storage
#
#     def get_task_fields_and_action(self, task_dtos: List[GetTaskDetailsDTO]):
#
#         task_details_dtos = self.storage.get_task_details(task_dtos)
#         return task_details_dtos
