from typing import List

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO, ColumnStageDTO, ColumnDTO
from ib_tasks.exceptions.permission_custom_exceptions \
    import UserBoardPermissionDenied


class BoardsService:

    @property
    def interface(self):
        from ib_boards.app_interfaces.service_interface \
            import BoardServiceInterface
        return BoardServiceInterface()

    def get_display_boards_and_column_details(self, user_id: str,
                                              board_id: str,
                                              stage_ids: List[str]):
        try:
            board_details = self.interface.get_board_details(
                user_id=user_id, board_id=board_id, stage_ids=stage_ids
            )
        except:
            raise UserBoardPermissionDenied(board_id=board_id)
        task_board_details = self._get_board_details(board_details)
        return task_board_details

    def _get_board_details(self, board_details):

        return TaskBoardsDetailsDTO(
            board_dto=board_details.board_dto,
            column_stage_dtos=self._get_column_stage_dtos(board_details.column_stage_dtos),
            columns_dtos=self._get_column_dtos(board_details.columns_dtos)
        )

    @staticmethod
    def _get_column_dtos(column_dtos):

        return [
            ColumnDTO(
                column_id=column_dto.column_id,
                board_id=column_dto.board_id,
                name=column_dto.name
            )
            for column_dto in column_dtos
        ]

    @staticmethod
    def _get_column_stage_dtos(column_stage_dtos):

        return [
            ColumnStageDTO(
                column_id=column_stage_dto.column_id,
                stage_id=column_stage_dto.stage_id
            )
            for column_stage_dto in column_stage_dtos
        ]

    def validate_board_id(self, board_id: str):
        # TODO validate board id
        return True
