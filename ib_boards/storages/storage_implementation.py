
from typing import List, Tuple

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, \
    BoardColumnsDTO, TaskTemplateStagesDTO, TaskSummaryFieldsDTO
from ib_boards.interactors.storage_interfaces.dtos import BoardColumnDTO, \
    ColumnDetailsDTO, ColumnBoardDTO, ColumnStageDTO
from ib_boards.interactors.storage_interfaces.dtos import BoardColumnDTO, ColumnDetailsDTO, TaskBoardsDetailsDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_boards.models import Board, ColumnPermission, Column


class StorageImplementation(StorageInterface):

    def validate_board_id(self, board_id):
        boards = Board.objects.all().values('board_id')
        is_board_id_valid = Board.objects.filter(
            board_id=board_id
        ).exists()
        return is_board_id_valid

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
        print(Column.objects.all())
        board_column_ids = Column.objects.filter(
            board_id__in=board_ids
        ).values('board_id', 'column_id')
        print(board_column_ids)
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
        print(board_columns_dtos)
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
                'display_name',
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
        board_ids = Board.objects.values_list('board_id', flat=True)
        return list(board_ids)

    def get_board_details(self, board_ids: List[str]) -> List[BoardDTO]:
        board_objects = Board.objects.filter(
            board_id__in=board_ids
        )
        board_dtos = self._convert_board_objects_to_board_dtos(
            board_objects=board_objects
        )
        return board_dtos

    def get_valid_board_ids(self, board_ids: List[str]) -> List[str]:
        board_ids = Board.objects.filter(
            board_id__in=board_ids
        ).values_list('board_id', flat=True)
        return list(board_ids)

    def validate_column_id(self, column_id: str) -> None:
        is_invalid_column_id = not Column.objects.filter(
            column_id=column_id
        ).exists()
        if is_invalid_column_id:
            from ib_boards.exceptions.custom_exceptions import InvalidColumnId
            raise InvalidColumnId

    def get_column_display_stage_ids(self, column_id: str) -> List[str]:
        task_templates_stages = Column.objects.filter(
            column_id=column_id
        ).values_list('task_selection_config', flat=True)
        print(task_templates_stages)
        stage_ids = self._get_stage_ids_from_json_string(
            task_templates_stages[0]
        )
        return stage_ids

    # TODO: need to pass column  Id
    def validate_user_role_with_column_roles(self, user_role: str):
        user_roles = ColumnPermission.objects.filter(
            column_id='COLUMN_ID_1'
        ).values_list('user_role_id', flat=True)

        is_invalid_user = not (user_role in user_roles or
                               'ALL_ROLES' in user_roles)
        if is_invalid_user:
            from ib_boards.exceptions.custom_exceptions import \
                UserDoNotHaveAccessToColumn
            raise UserDoNotHaveAccessToColumn


    @staticmethod
    def _convert_board_objects_to_board_dtos(board_objects):
        board_dtos = [
            BoardDTO(
                board_id=board_object.board_id,
                display_name=board_object.display_name
            )
            for board_object in board_objects
        ]
        return board_dtos

    @staticmethod
    def _get_stage_ids_from_json_string(
            task_template_stages: str) -> List[str]:
        import json
        task_template_stages = json.loads(task_template_stages)
        stage_ids = []
        for key, value in task_template_stages.items():
            stage_ids += value

        return stage_ids

    def get_columns_details(self, column_ids: List[str]) -> \
            List[ColumnDetailsDTO]:
        pass

    def get_columns_details(self, column_ids: List[str]) -> \
            List[ColumnDetailsDTO]:
        column_objs = Column.objects.filter(column_id__in=column_ids)
        columns_dtos = self._convert_column_objs_to_dtos(column_objs)
        return columns_dtos

    @staticmethod
    def _convert_column_objs_to_dtos(column_objs):
        list_of_column_dtos = [
            ColumnDetailsDTO(
                column_id=obj.column_id,
                name=obj.display_name
            )
            for obj in column_objs
        ]
        return list_of_column_dtos

    def get_column_ids_for_board(self, board_id: str, user_roles: List[str]) \
            -> List[str]:
        column_objs = Column.objects.filter(board__board_id=board_id)
        roles = ColumnPermission.objects.filter(column__in=column_objs)
        column_ids = []
        for role in roles:
            if role.user_role_id == "ALL_ROLES":
                column_ids.append(role.column.column_id)
            elif role.user_role_id in user_roles:
                column_ids.append(role.column.column_id)
        return sorted(list(set(column_ids)))


    def get_permitted_user_roles_for_board(self, board_id: str) -> List[str]:
        return "ALL ROLES"

    def get_board_complete_details(self, board_id: str, stage_ids: List[str]) -> \
            TaskBoardsDetailsDTO:

        column_objs = Column.objects.filter(board_id=board_id)
        board_obj = Board.objects.get(board_id=board_id)
        board_dto = BoardDTO(
            board_id=board_obj.board_id,
            display_name=board_obj.name
        )

        list_of_column_dtos, column_stages = self._convert_column_details_to_dtos(column_objs,
                                                                   stage_ids)
        board_details_dto = TaskBoardsDetailsDTO(
            board_dto=board_dto,
            columns_dtos=list_of_column_dtos,
            column_stage_dtos=column_stages
        )
        return board_details_dto

    def get_column_details(self, board_id: str, user_roles: List[str]) \
            -> List[BoardColumnDTO]:
        pass


    def _convert_column_details_to_dtos(self, column_objs,
                                        stage_ids):
        list_of_column_dtos = []
        for column_obj in column_objs:
            list_of_column_dtos.append(
                ColumnBoardDTO(
                    column_id=column_obj.column_id,
                    board_id=column_obj.board_id,
                    name=column_obj.name
                )
            )
        column_stages = []
        for column_obj in column_objs:
            tasks = column_obj.task_selection_config
            import json
            tasks_stages = json.loads(tasks)
            for key, value in enumerate(tasks_stages):
                stages = tasks_stages[value]
                for stage in stages:
                    if stage in stage_ids:
                        column_stages.append(
                            ColumnStageDTO(
                                column_id=column_obj.column_id,
                                stage_id=stage
                            )
                        )
        return list_of_column_dtos, column_stages
