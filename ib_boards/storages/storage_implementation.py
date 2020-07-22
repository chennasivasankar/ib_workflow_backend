"""
Created on: 18/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Tuple

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, \
    BoardColumnsDTO, TaskTemplateStagesDTO, TaskSummaryFieldsDTO
from ib_boards.interactors.storage_interfaces.dtos import BoardColumnDTO, \
    ColumnDetailsDTO
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
            self, board_dtos: List[BoardDTO],
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

    def get_boards_column_ids(
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
            for key, value in board_columns_map.items()
        ]
        return board_columns_dtos

    def update_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        column_objects = Column.objects.filter(column_id__in=column_ids)
        user_role_ids = ColumnPermission.objects.filter(column_id__in=column_ids)
        updated_column_objects = self._get_updated_column_objects(
            column_dtos=column_dtos,
            column_objects=column_objects
        )
        updated_user_role_objects = self._get_updated_user_role_objects(
            column_dtos=column_dtos,
            user_role_ids=user_role_ids
        )
        Column.objects.bulk_update(
            updated_column_objects,
            [
                'name',
                'display_order', 'task_selection_config',
                'kanban_brief_view_config',
                'list_brief_view_config'
            ]
        )
        ColumnPermission.objects.bulk_update(
            updated_user_role_objects,
            ['user_role_id']
        )

    def _get_updated_column_objects(
            self, column_dtos: List[ColumnDTO],
            column_objects: List[Column]) -> List[Column]:
        column_dtos_dict = {}
        for column_dto in column_dtos:
            column_dtos_dict[column_dto.column_id] = column_dto

        updated_column_objects = []
        for column_object in column_objects:
            updated_column_object = self._get_updated_column_object(
                column_dtos_dict[column_object.column_id], column_object
            )
            updated_column_objects.append(updated_column_object)
        return updated_column_objects

    def _get_updated_user_role_objects(self, column_dtos, user_role_ids):
        from collections import defaultdict
        user_role_ids_dict = defaultdict(lambda: [])
        for user_role_id in user_role_ids:
            user_role_ids_dict[user_role_id.column_id].append(user_role_id)

        updated_user_role_objects = []
        for column_dto in column_dtos:
            updated_user_role_objects += self._get_user_role_objects_from_column_dtos(
                column_dto=column_dto,
                user_role_objects=user_role_ids_dict[column_dto.column_id]
            )
        return updated_user_role_objects

    @staticmethod
    def _get_user_role_objects_from_column_dtos(column_dto,
                                                user_role_objects):
        for user_role in column_dto.user_role_ids:
            for user_role_object in user_role_objects:
                user_role_object.user_role_id=user_role

        return user_role_objects

    def _get_updated_column_object(
            self, column_dto: ColumnDTO, column_object: Column):
        column_object.name = column_dto.display_name
        column_object.display_order = column_dto.display_order
        column_object.task_selection_config = \
            self._get_json_string_for_task_selection_config(
                column_dto.task_template_stages
            )
        column_object.kanban_brief_view_config = \
            self._get_json_string_for_view_config(
                column_dto.kanban_view_fields
            )
        column_object.list_brief_view_config = \
            self._get_json_string_for_view_config(
                column_dto.list_view_fields
            )
        return column_object

    def create_columns_for_board(self, column_dtos) -> None:
        column_objects, user_role_ids = \
            self._get_column_objects_and_column_permission_objects_from_dtos(
                column_dtos=column_dtos
            )
        Column.objects.bulk_create(column_objects)
        ColumnPermission.objects.bulk_create(user_role_ids)

    def delete_columns_which_are_not_in_configuration(
            self, column_for_delete_dtos: List[BoardColumnsDTO]) -> None:
        column_ids = []
        for column_for_delete_dto in column_for_delete_dtos:
            column_ids += column_for_delete_dto.column_ids
        column_objects = Column.objects.filter(
            column_id__in=column_ids
        )
        column_objects.delete()

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
                    column_dto.kanban_view_fields
                ),
                list_brief_view_config=self._get_json_string_for_view_config(
                    column_dto.list_view_fields
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

    def get_board_details(self, board_ids: List[str]) -> List[BoardDTO]:
        pass

    def get_valid_board_ids(self, board_ids: List[str]) -> List[str]:
        pass

    def validate_column_id(self, column_id: str) -> None:
        pass

    def get_column_display_stage_ids(self, column_id: str) -> List[str]:
        pass

    def validate_user_role_with_column_roles(self, user_role: str):
        pass

    def get_columns_details(self, column_ids: List[str]) -> \
            List[ColumnDetailsDTO]:
        pass

    def get_column_ids_for_board(self, board_id: str, user_roles: List[str]) \
            -> List[str]:
        pass

    def get_permitted_user_roles_for_board(self, board_id: str) -> List[str]:
        pass
