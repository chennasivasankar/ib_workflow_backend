import json
from typing import List, Tuple

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO, StarOrUnstarParametersDTO, \
    ProjectBoardDTO, ChangeFieldsStatusParameter, ChangeFieldsOrderParameter
from ib_boards.interactors.storage_interfaces.dtos import BoardColumnDTO, \
    ColumnDetailsDTO, TaskBoardsDetailsDTO, ColumnStageIdsDTO
from ib_boards.interactors.storage_interfaces.dtos import ColumnBoardDTO, \
    ColumnStageDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface, FieldDisplayStatusDTO, FieldOrderDTO
from ib_boards.models import Board, ColumnPermission, Column, UserStarredBoard
from ib_boards.models.fields_in_list_view import FieldOrder, FieldDisplayStatus


class StorageImplementation(StorageInterface):

    def get_project_id_for_board(self, board_id: str) -> str:
        board_obj = Board.objects.get(board_id=board_id)
        return board_obj.project_id

    def get_project_id_for_given_column_id(self, column_id: str) -> str:
        column = Column.objects.filter(column_id=column_id).values(
            'board__project_id')
        return column[0]['board__project_id']

    def add_project_id_for_boards(
            self, project_boards_dtos: List[ProjectBoardDTO]):
        board_ids = [item.board_id for item in project_boards_dtos]
        board_objs = Board.objects.filter(board_id__in=board_ids)
        project_board_dict = {}
        for item in project_boards_dtos:
            project_board_dict[item.board_id] = item.project_id

        for obj in board_objs:
            obj.project_id = project_board_dict[obj.board_id]

        Board.objects.bulk_update(board_objs, ["project_id"])

    def validate_board_id(self, board_id):
        is_board_id_valid = Board.objects.filter(
            board_id=board_id
        ).exists()
        return is_board_id_valid

    def get_existing_board_ids(self) -> List[str]:
        board_ids = Board.objects.values_list('board_id', flat=True)
        return list(board_ids)

    def create_boards_and_columns(
            self, board_dtos: List[BoardDTO],
            column_dtos: List[ColumnDTO]) -> None:
        board_objects = [
            Board(
                board_id=board_dto.board_id,
                name=board_dto.name
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
            self, board_ids: List[str]) -> List[str]:

        column_ids = Column.objects.filter(
            board_id__in=board_ids
        ).values_list('column_id', flat=True)
        return list(column_ids)

    def update_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        column_objects = Column.objects.filter(column_id__in=column_ids)
        user_role_ids = ColumnPermission.objects.filter(
            column_id__in=column_ids)
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
                user_role_object.user_role_id = user_role

        return user_role_objects

    def _get_updated_column_object(
            self, column_dto: ColumnDTO, column_object: Column):
        column_object.name = column_dto.name
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
            self, column_ids: List[str]) -> None:
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
                name=column_dto.name,
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

    def get_board_ids(self, user_id: str, project_id: str) -> \
            Tuple[List[str], List[str]]:
        starred_board_ids = list(
            UserStarredBoard.objects.filter(user_id=user_id,
                                            board__project_id=project_id)
            .values_list('board_id', flat=True))
        board_ids = list(Board.objects.filter(project_id=project_id)
                         .exclude(board_id__in=starred_board_ids)
                         .values_list('board_id', flat=True))
        return board_ids, starred_board_ids

    def get_user_permitted_board_ids(self, user_roles: List[str], board_ids: List[str]) -> List[str]:
        from ib_boards.constants.constants import ALL_ROLES_ID
        user_roles.append(ALL_ROLES_ID)
        column_ids = list(ColumnPermission.objects.filter(
            user_role_id__in=user_roles
        ).values_list('column_id', flat=True))
        board_ids = Column.objects.filter(
            column_id__in=column_ids, board_id__in=board_ids
        ).values_list('board_id', flat=True)
        return sorted(list(set(board_ids)))

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
        stage_ids = self._get_stage_ids_from_json_string(
            task_templates_stages[0]
        )
        return stage_ids

    def validate_user_role_with_column_roles(self, user_role: List[str],
                                             column_id: str):
        user_roles = list(ColumnPermission.objects.filter(
            column_id=column_id
        ).values_list('user_role_id', flat=True))

        is_invalid_user = not (set(user_role).issubset(set(user_roles)) or
                               set(user_roles).issubset(set(user_role)) or
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
                name=board_object.name
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
        column_objs = (Column.objects.filter(column_id__in=column_ids)
                       .order_by('display_order'))
        columns_dtos = self._convert_column_objs_to_dtos(column_objs)
        return columns_dtos

    @staticmethod
    def _convert_column_objs_to_dtos(column_objs):
        list_of_column_dtos = [
            ColumnDetailsDTO(
                column_id=obj.column_id,
                name=obj.name
            )
            for obj in column_objs
        ]
        return list_of_column_dtos

    def get_column_ids_for_board(self, board_id: str, user_roles: List[str]) \
            -> List[str]:
        column_ids = []
        column_objs = Column.objects.filter(board__board_id=board_id)
        roles = ColumnPermission.objects.filter(column__in=column_objs)
        for role in roles:
            if role.user_role_id == "ALL_ROLES":
                column_ids.append(role.column.column_id)
            elif role.user_role_id in user_roles:
                column_ids.append(role.column.column_id)
        return sorted(list(set(column_ids)))

    def get_permitted_user_roles_for_board(self, board_id: str) -> List[str]:
        return ["ALL ROLES"]

    def get_board_complete_details(self, board_id: str,
                                   stage_ids: List[str]) -> \
            TaskBoardsDetailsDTO:
        stage_related_columns = []
        column_objs = Column.objects.filter(board_id=board_id)
        for stage in stage_ids:
            for column in column_objs:
                task_selection_config = json.loads(
                    column.task_selection_config)
                for key, value in enumerate(task_selection_config.values()):
                    if stage in value:
                        stage_related_columns.append(column)

        board_obj = Board.objects.get(board_id=board_id)
        board_dto = BoardDTO(
            board_id=board_obj.board_id,
            name=board_obj.name
        )

        list_of_column_dtos, column_stages = self._convert_column_details_to_dtos(
            list(set(stage_related_columns)),
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

    @staticmethod
    def _convert_column_details_to_dtos(column_objs,
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

    def get_columns_stage_ids(self, column_ids: List[str]) -> \
            List[ColumnStageIdsDTO]:
        column_stages = (Column.objects.filter(column_id__in=column_ids)
                         .values_list('column_id', 'task_selection_config')
                         .order_by('display_order'))

        return [
            ColumnStageIdsDTO(
                column_id=key,
                stage_ids=self._get_stage_ids_from_json_string(value)
            )
            for key, value in column_stages
        ]

    def unstar_given_board(self,
                           parameters: StarOrUnstarParametersDTO):
        user_id = parameters.user_id
        board_id = parameters.board_id

        UserStarredBoard.objects.filter(
            board_id=board_id, user_id=user_id).delete()

    def star_given_board(self,
                         parameters: StarOrUnstarParametersDTO):
        user_id = parameters.user_id
        board_id = parameters.board_id

        UserStarredBoard.objects.get_or_create(
            board_id=board_id, user_id=user_id)

    def validate_field_id_with_column_id(self, column_id: str, field_id: str, user_id: str):
        is_field_status_present = not FieldDisplayStatus.objects.filter(
            user_id=user_id,
            column_id=column_id,
            field_id=field_id
        ).exists()
        if is_field_status_present:
            from ib_boards.exceptions.custom_exceptions import \
                FieldNotBelongsToColumn
            raise FieldNotBelongsToColumn

    def change_display_status_of_field(
            self, field_display_status_parameter: ChangeFieldsStatusParameter):
        field_status_object = FieldDisplayStatus.objects.get(
            user_id=field_display_status_parameter.user_id,
            column_id=field_display_status_parameter.column_id,
            field_id=field_display_status_parameter.field_id
        )
        field_status_object.display_status = field_display_status_parameter.display_status
        field_status_object.save()

    def change_display_order_of_field(self,
                                      field_order_parameter: ChangeFieldsOrderParameter):
        fields_order_object = FieldOrder.objects.get(
            column_id=field_order_parameter.column_id,
            user_id=field_order_parameter.user_id
        )
        import json
        field_ids = json.loads(fields_order_object.fields_order)['field_ids']
        field_ids.remove(field_order_parameter.field_id)
        field_ids.insert(field_order_parameter.display_order, field_order_parameter.field_id)
        new_fields_ids = json.dumps(
            {
                "field_ids": field_ids
            }
        )
        fields_order_object.fields_order = new_fields_ids
        fields_order_object.save()

    def get_valid_field_ids(
            self, column_id: str, field_ids: List[str], user_id: str) -> List[str]:
        return list(FieldDisplayStatus.objects.filter(
            user_id=user_id,
            column_id=column_id,
            field_id__in=field_ids
        ).values_list('field_id', flat=True))

    def get_field_ids_list_in_order(
            self, column_id: str, user_id: str) -> List[str]:
        try:
            field_ids = FieldOrder.objects.get(
                column_id=column_id,
                user_id=user_id
            ).fields_order
        except FieldOrder.DoesNotExist:
            return []
        import json
        field_ids = json.loads(field_ids)['field_ids']
        return field_ids

    def get_field_display_status_dtos(
            self, column_id: str, user_id: str) -> List[FieldDisplayStatusDTO]:
        field_status_objects = FieldDisplayStatus.objects.filter(
            user_id=user_id,
            column_id=column_id,
        )
        return [
            FieldDisplayStatusDTO(
                field_id=field_status_object.field_id,
                display_status=field_status_object.display_status
            )
            for field_status_object in field_status_objects
        ]

    def get_present_field_ids(self, column_id: str, user_id: str) -> List[str]:
        field_ids = FieldDisplayStatus.objects.filter(
            user_id=user_id,
            column_id=column_id,
        ).values_list('field_id', flat=True)
        return list(field_ids)

    def create_field_ids_order_and_display_status(
            self, column_id: str, user_id: str, field_ids: List[str]):
        self._create_fields_display_status(
            column_id=column_id,
            user_id=user_id,
            field_ids=field_ids
        )
        self._create_fields_order(
            column_id=column_id,
            user_id=user_id,
            field_ids=field_ids
        )

    @staticmethod
    def _create_fields_display_status(
            column_id: str, user_id: str, field_ids: List[str]):
        from ib_boards.models.fields_in_list_view import FieldDisplayStatus
        fields_display_statuses_list = [
            FieldDisplayStatus(
                column_id=column_id,
                user_id=user_id,
                field_id=field_id
            )
            for field_id in field_ids
        ]
        FieldDisplayStatus.objects.bulk_create(fields_display_statuses_list)

    def _create_fields_order(
            self, column_id: str, user_id: str, field_ids: List[str]):
        try:
            field_ids_object = FieldOrder.objects.get(
                column_id=column_id,
                user_id=user_id
            )
        except FieldOrder.DoesNotExist:
            self._create_fields_order_with_all_field_ids(
                column_id=column_id,
                user_id=user_id,
                field_ids=field_ids
            )
            return
        self._add_extra_fields(
            field_ids=field_ids,
            field_ids_object=field_ids_object
        )

    @staticmethod
    def _create_fields_order_with_all_field_ids(
            column_id: str, user_id: str, field_ids: List[str]):
        import json
        field_ids = json.dumps(
            {
                "field_ids": field_ids
            }
        )
        FieldOrder.objects.create(
            column_id=column_id,
            user_id=user_id,
            fields_order=field_ids
        )

    @staticmethod
    def _add_extra_fields(field_ids: List[str], field_ids_object: FieldOrder):
        import json
        present_field_ids = json.loads(field_ids_object.fields_order)['field_ids']
        extra_field_ids = [
            field_id
            for field_id in field_ids
            if field_id not in present_field_ids
        ]
        new_field_ids = present_field_ids + extra_field_ids
        field_ids = json.dumps(
            {
                "field_ids": present_field_ids
            }
        )
        field_ids_object.fields_order = new_field_ids
        field_ids_object.save()

