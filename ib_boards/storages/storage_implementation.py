"""
Created on: 18/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Tuple

from ib_boards.interactors.dtos import CreateBoardDTO, ColumnDTO, \
    BoardColumnsDTO, TaskTemplateStagesDTO, TaskSummaryFieldsDTO
from ib_boards.interactors.storage_interfaces.dtos import BoardColumnDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_boards.models import Board, ColumnPermission, Column


class StorageImplementation(StorageInterface):

    def validate_board_id(self, board_id):
        is_board_id_invalid = not Board.objects.filter(
            board_id=board_id
        ).exists()
        if is_board_id_invalid:
            from ib_boards.exceptions.custom_exceptions import InvalidBoardId
            raise InvalidBoardId

    def create_boards_and_columns(
            self, board_dtos: List[CreateBoardDTO],
            column_dtos: List[ColumnDTO]) -> None:
        board_objects = [
            Board(
                board_id=board_dto.board_id,
                name=board_dto.display_name
            )
            for board_dto in board_dtos
        ]
        Board.objects.bulk_create(board_objects)
        column_objects, user_role_ids = \
            self._get_column_objects_and_column_permission_objects_from_dtos(
                column_dtos=column_dtos
            )
        Column.objects.bulk_create(column_objects)
        ColumnPermission.objects.bulk_create(user_role_ids)

    def get_board_ids_for_column_ids(self, column_ids: List[str]) \
            -> List[BoardColumnDTO]:
        board_column_ids = Column.objects.filter(
            column_id__in=column_ids
        ).values('board_id', 'column_id')

        board_column_id_dtos = [
            BoardColumnDTO(
                board_id=board_column_id['board_id'],
                column_id=board_column_id['column_id']
            )
            for board_column_id in board_column_ids
        ]
        return board_column_id_dtos

    def get_board_column_ids(
            self, board_ids: List[str]) -> List[BoardColumnsDTO]:
        board_column_ids = Column.objects.filter(
            board_id__in=board_ids
        ).values('board_id', 'column_id')

        from collections import defaultdict
        board_columns_map = defaultdict(lambda: [])
        for board_column_id in board_column_ids:
            board_columns_map[board_column_id['board_id']].append(
                board_column_id['column_id']
            )

        board_columns_dtos = [
            BoardColumnsDTO(
                board_id=key,
                column_ids=value
            )
            for key, value in board_columns_map
        ]
        return board_columns_dtos

    def update_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    def create_columns_for_board(self, column_dtos) -> None:
        column_objects, user_role_ids = \
            self._get_column_objects_and_column_permission_objects_from_dtos(
                column_dtos=column_dtos
            )
        Column.objects.bulk_create(column_objects)
        ColumnPermission.objects.bulk_create(user_role_ids)

    def delete_columns_which_are_not_in_configuration(
            self, column_for_delete_dtos: List[BoardColumnsDTO]) -> None:
        pass

    def _get_column_objects_and_column_permission_objects_from_dtos(
            self, column_dtos: List[ColumnDTO]) -> Tuple[
            List[Column], List[ColumnPermission]]:
        column_objects = [
            Column(
                column_id=column_dto.column_id,
                board_id=column_dto.board_id,
                name=column_dto.display_name,
                display_order=column_dto.display_order,
                task_selection_config=self._get_json_string_for_task_selection_config(
                    column_dto.task_template_stages
                ),
                kanban_brief_view_config=self._get_json_string_for_view_config(
                    column_dto.list_view_fields
                ),
                list_brief_view_config=self._get_json_string_for_view_config(
                    column_dto.kanban_view_fields
                ),
            )
            for column_dto in column_dtos
        ]
        user_role_ids = []
        for column_dto in column_dtos:
            for user_role in column_dto.user_role_ids:
                user_role_ids.append(ColumnPermission(
                    column_id=column_dto.column_id,
                    user_role_id=user_role
                ))

        return column_objects, user_role_ids

    @staticmethod
    def _get_json_string_for_task_selection_config(
            task_template_stages: List[TaskTemplateStagesDTO]):
        task_template_stages_dict = {}
        for task_template_stage in task_template_stages:
            task_template_stages_dict.update(
                {
                    task_template_stage.task_template_id: task_template_stage.stages
                }
            )
        import json
        return json.dumps(task_template_stages_dict)

    @staticmethod
    def _get_json_string_for_view_config(
            task_summary_fields: List[TaskSummaryFieldsDTO]):
        task_summary_fields_dict = {}
        for task_summary_field in task_summary_fields:
            task_summary_fields_dict.update(
                {
                    task_summary_field.task_id: task_summary_field.summary_fields
                }
            )
        import json
        return json.dumps(task_summary_fields_dict)

    def validate_user_role_with_boards_roles(self, user_role: str):
        pass

    def get_board_ids(
            self, user_role: str, ) -> List[str]:
        pass

    def get_board_details(self, board_ids: List[str]) -> List[CreateBoardDTO]:
        pass

    def get_valid_board_ids(self, board_ids: List[str]) -> List[str]:
        pass

    def validate_column_id(self, column_id: str) -> None:
        pass

    def get_column_display_stage_ids(self, column_id: str) -> List[str]:
        pass

    def validate_user_role_with_column_roles(self, user_role: str):
        pass


"""
 @abc.abstractmethod
    def create_boards_and_columns(
            self, board_dtos: List[BoardDTO],
            column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def get_board_ids_for_column_ids(self, column_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_boards_column_ids(self, board_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def update_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def create_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def delete_columns_which_are_not_in_configuration(
            self, column_for_delete_dtos: List[BoardColumnDTO]) -> None:
        pass

"""
