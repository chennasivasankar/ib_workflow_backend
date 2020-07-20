# from ib_tasks.interactors.dtos import TaskStatusVariablesDTO
# from ib_tasks.interactors.storage_interfaces.storage_interface \
#     import StorageInterface
#
#
# class GetTaskBoardsDetailsInteractor:
#
#     def __init__(self, user_id: str, board_id: str,
#                  storage: StorageInterface,
#                  task_status_variables_dto: TaskStatusVariablesDTO):
#         self.user_id = user_id
#         self.board_id = board_id
#         self.storage = storage
#         self.task_status_variables_dto = task_status_variables_dto
#
#     def get_task_boards_details(self):
#
#         from ib_tasks.adapters.service_adapter import get_service_adapter
#         adapter_instance = get_service_adapter()
#         task_details_dto = adapter_instance.boards_service \
#             .get_boards_and_column_details_to_task(
#             user_id=self.user_id, board_id=self.board_id,
#             task_status_variables_dto=self.task_status_variables_dto
#         )
#         boards_dto = task_details_dto.boards_dto
#         boards_dict = self._get_boards_dto_dict(boards_dto)
#         columns_dto = task_details_dto.columns_dto
#         columns_dict = self._get_columns_dto_dict(columns_dto)
#
#     def _get_columns_dto_dict(columns_dto):
#
#         columns_dict = {}
#         for column_dto in columns_dto:
#             columns_dict[column_dto.board_id] = column_dto
#         return columns_dict
#
#     @staticmethod
#     def _get_boards_dto_dict(boards_dto):
#
#         boards_dict = {}
#         for board_dto in boards_dto:
#             boards_dict[boards_dto.board_id] = board_dto
#         return boards_dict
