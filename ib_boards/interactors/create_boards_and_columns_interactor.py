"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.exceptions.custom_exceptions import \
    TaskSummaryFieldsNotBelongsToTaskTemplateId, \
    TaskListViewFieldsNotBelongsToTaskTemplateId, \
    EmptyValuesForTaskSummaryFields, EmptyValuesForTaskListViewFields, \
    InvalidTaskIdInListViewFields, InvalidTaskIdInSummaryFields, \
    InvalidTaskIdInKanbanViewFields, EmptyValuesForTaskKanbanViewFields, \
    InvalidUserRoles
from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class CreateBoardsAndColumnsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_boards_and_columns(
            self, board_dtos: List[BoardDTO], column_dtos: List[ColumnDTO]):
        self._validate_board_display_name(board_dtos=board_dtos)
        self.validate_columns_data(column_dtos)
        board_dtos, column_dtos = self._get_boards_and_columns_need_to_create(
            board_dtos=board_dtos, column_dtos=column_dtos
        )
        print(board_dtos, column_dtos)
        boards_columns_to_create = board_dtos and column_dtos
        if boards_columns_to_create:
            self.storage.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos
            )

    def _get_boards_and_columns_need_to_create(self, board_dtos, column_dtos):
        existing_board_ids = self.storage.get_existing_board_ids()
        from collections import defaultdict
        board_columns_dict = defaultdict(lambda: [])
        for column_dto in column_dtos:
            board_columns_dict[column_dto.board_id].append(
                column_dto
            )
        new_board_dtos = []
        new_column_dtos = []
        for board_dto in board_dtos:
            if board_dto.board_id not in existing_board_ids:
                new_board_dtos.append(board_dto)
                new_column_dtos += board_columns_dict[board_dto.board_id]

        return new_board_dtos, new_column_dtos

    def validate_columns_data(self, column_dtos: List[ColumnDTO]):
        self._validate_column_ids(column_dtos=column_dtos)
        self._validate_column_display_name(column_dtos=column_dtos)
        self._validate_column_display_order(column_dtos=column_dtos)
        self._validate_task_template_ids_in_task_template_stage(
            column_dtos=column_dtos
        )
        self._validate_empty_values_in_task_template_stage(
            column_dtos=column_dtos
        )
        self._validate_task_template_stages_with_template_id(
            column_dtos=column_dtos)
        self._validate_duplicate_task_template_stages(column_dtos=column_dtos)
        self._validate_task_summary_fields(column_dtos)
        self._validate_user_roles(column_dtos=column_dtos)

    def _validate_task_summary_fields(self, column_dtos: List[ColumnDTO]):
        self._validate_task_template_ids_in_list_view_fields(
            column_dtos=column_dtos
        )
        self._validate_duplicate_task_list_view_fields(column_dtos=column_dtos)
        self._validate_empty_values_in_task_template_list_view_fields(
            column_dtos=column_dtos)
        self._validate_task_template_list_view_fields_with_task_template_id(
            column_dtos=column_dtos
        )
        self._validate_task_template_ids_in_kanban_view_fields(
            column_dtos=column_dtos
        )
        self._validate_duplicate_task_kanban_view_fields(
            column_dtos=column_dtos)
        self._validate_empty_values_in_task_template_kanban_view_fields(
            column_dtos=column_dtos)
        self._validate_task_template_kanban_view_fields_with_task_template_id(
            column_dtos=column_dtos
        )

    @staticmethod
    def _validate_board_display_name(board_dtos: List[BoardDTO]):
        for board_dto in board_dtos:
            is_invalid_display_name = not board_dto.name
            if is_invalid_display_name:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidBoardDisplayName
                raise InvalidBoardDisplayName(board_id=board_dto.board_id)

    def _validate_column_ids(self, column_dtos: List[ColumnDTO]):
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        duplicate_column_ids = self._find_duplicates(values=column_ids)
        if duplicate_column_ids:
            from ib_boards.exceptions.custom_exceptions import \
                DuplicateColumnIds
            raise DuplicateColumnIds(column_ids=duplicate_column_ids)

    @staticmethod
    def _validate_column_display_name(column_dtos: List[ColumnDTO]):
        is_invalid_display_name_ids = []
        for column_dto in column_dtos:
            is_invalid_display_name = not column_dto.name
            if is_invalid_display_name:
                is_invalid_display_name_ids.append(column_dto.column_id)
        if is_invalid_display_name_ids:
            from ib_boards.exceptions.custom_exceptions import \
                InvalidColumnDisplayName
            raise InvalidColumnDisplayName(
                column_ids=is_invalid_display_name_ids
            )

    def _validate_column_display_order(self, column_dtos: List[ColumnDTO]):
        column_display_order_values = [
            column_dto.display_order for column_dto in column_dtos
        ]
        duplicate_values_in_display_order = self._find_duplicates(
            values=column_display_order_values
        )
        if duplicate_values_in_display_order:
            from ib_boards.exceptions.custom_exceptions import \
                DuplicateValuesInColumnDisplayOrder
            raise DuplicateValuesInColumnDisplayOrder(
                display_order_values=duplicate_values_in_display_order
            )

    def _validate_task_template_ids_in_task_template_stage(
            self, column_dtos: List[ColumnDTO]):
        task_template_ids = []
        for column_dto in column_dtos:
            task_template_stage_dtos = column_dto.task_template_stages
            task_template_ids += self._get_task_template_ids(
                task_template_stage_dtos=task_template_stage_dtos
            )
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        valid_task_template_ids = service_adapter.task_service. \
            get_valid_task_template_ids(
                task_template_ids=task_template_ids
            )
        invalid_task_template_ids = [
            task_template_id for task_template_id in task_template_ids
            if task_template_id not in valid_task_template_ids
        ]
        if invalid_task_template_ids:
            from ib_boards.exceptions.custom_exceptions import \
                InvalidTaskTemplateIdInStages
            raise InvalidTaskTemplateIdInStages(
                task_template_ids=invalid_task_template_ids
            )

    @staticmethod
    def _get_task_template_ids(
            task_template_stage_dtos: List[TaskTemplateStagesDTO]):
        task_template_ids = [
            task_template_stage_dto.task_template_id
            for task_template_stage_dto in task_template_stage_dtos
        ]
        return task_template_ids

    def _validate_empty_values_in_task_template_stage(
            self, column_dtos: List[ColumnDTO]):
        for column_dto in column_dtos:
            task_templates = column_dto.task_template_stages
            self._check_stages_for_task_templates_are_not_empty(
                task_templates=task_templates
            )

    @staticmethod
    def _check_stages_for_task_templates_are_not_empty(
            task_templates: List[TaskTemplateStagesDTO]):
        for task_template in task_templates:
            is_empty_value = not task_template.stages
            if is_empty_value:
                from ib_boards.exceptions.custom_exceptions import \
                    EmptyValuesForTaskTemplateStages
                raise EmptyValuesForTaskTemplateStages

    @staticmethod
    def _validate_task_template_stages_with_template_id(
            column_dtos: List[ColumnDTO]):
        task_template_stages = []
        for column_dto in column_dtos:
            task_template_stages += column_dto.task_template_stages
        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()

        service_adapter.task_service.validate_task_template_stages_with_id(
            task_template_stages=task_template_stages
        )

    def _validate_duplicate_task_template_stages(self,
                                                 column_dtos: List[ColumnDTO]):
        for column_dto in column_dtos:
            task_template_stages_dtos = column_dto.task_template_stages
            for task_template_stages_dto in task_template_stages_dtos:
                self._validate_duplicate_stages_for_task_template(
                    stages=task_template_stages_dto.stages
                )

    def _validate_duplicate_stages_for_task_template(self, stages: List[str]):
        duplicate_stages = self._find_duplicates(values=stages)
        if duplicate_stages:
            from ib_boards.exceptions.custom_exceptions import \
                DuplicateStagesInTaskTemplateStages
            raise DuplicateStagesInTaskTemplateStages(
                duplicate_stages=duplicate_stages
            )

    @staticmethod
    def _validate_user_roles(column_dtos: List[ColumnDTO]):
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_roles = []
        for column_dto in column_dtos:
            user_roles += column_dto.user_role_ids
        user_roles = sorted(list(set(user_roles)))
        valid_user_roles = service_adapter.user_service.get_valid_user_role_ids(
            user_roles=user_roles
        )
        invalid_user_roles = [
            user_role
            for user_role in user_roles
            if user_role not in valid_user_roles
        ]
        if invalid_user_roles:
            raise InvalidUserRoles(user_role_ids=invalid_user_roles)

    def _validate_task_template_ids_in_list_view_fields(
            self, column_dtos: List[ColumnDTO]):

        task_ids = []
        for column_dto in column_dtos:
            task_summary_field_dtos = column_dto.list_view_fields
            task_ids += self._get_task_template_ids_for_fields(
                task_summary_field_dtos=task_summary_field_dtos
            )

        try:
            self._get_invalid_task_template_ids_for_fields(
                task_ids=task_ids
            )
        except InvalidTaskIdInSummaryFields as error:
            raise InvalidTaskIdInListViewFields(task_ids=error.task_ids)

    def _validate_task_template_list_view_fields_with_task_template_id(
            self, column_dtos: List[ColumnDTO]):
        task_summary_fields = []
        for column_dto in column_dtos:
            task_summary_fields += column_dto.list_view_fields
        try:
            self._validate_task_summary_fields_with_template_id(
                task_summary_fields)
        except TaskSummaryFieldsNotBelongsToTaskTemplateId:
            raise TaskListViewFieldsNotBelongsToTaskTemplateId

    def _validate_empty_values_in_task_template_list_view_fields(
            self, column_dtos: List[ColumnDTO]):
        task_summary_fields_dtos = []
        for column_dto in column_dtos:
            task_summary_fields_dtos += column_dto.list_view_fields
        try:
            self._check_task_summary_fields_are_not_empty(
                task_summary_fields_dtos=task_summary_fields_dtos
            )
        except EmptyValuesForTaskSummaryFields:
            raise EmptyValuesForTaskListViewFields

    def _validate_duplicate_task_list_view_fields(
            self, column_dtos: List[ColumnDTO]):
        task_summary_field_dtos = []
        for column_dto in column_dtos:
            task_summary_field_dtos += column_dto.list_view_fields
            self._validate_duplicate_summary_fields(task_summary_field_dtos)

    def _validate_task_template_ids_in_kanban_view_fields(
            self, column_dtos: List[ColumnDTO]):
        task_ids = []
        for column_dto in column_dtos:
            task_summary_field_dtos = column_dto.kanban_view_fields
            task_ids += self._get_task_template_ids_for_fields(
                task_summary_field_dtos=task_summary_field_dtos
            )
        try:
            self._get_invalid_task_template_ids_for_fields(
                task_ids=task_ids
            )
        except InvalidTaskIdInSummaryFields as error:
            raise InvalidTaskIdInKanbanViewFields(task_ids=error.task_ids)

    def _validate_task_template_kanban_view_fields_with_task_template_id(
            self, column_dtos: List[ColumnDTO]):
        task_summary_fields = []
        for column_dto in column_dtos:
            task_summary_fields += column_dto.kanban_view_fields
        try:
            self._validate_task_summary_fields_with_template_id(
                task_summary_fields)
        except TaskSummaryFieldsNotBelongsToTaskTemplateId:
            raise TaskListViewFieldsNotBelongsToTaskTemplateId

    def _validate_empty_values_in_task_template_kanban_view_fields(
            self, column_dtos: List[ColumnDTO]):
        task_summary_fields_dtos = []
        for column_dto in column_dtos:
            task_summary_fields_dtos += column_dto.kanban_view_fields
        try:
            self._check_task_summary_fields_are_not_empty(
                task_summary_fields_dtos=task_summary_fields_dtos
            )
        except EmptyValuesForTaskSummaryFields:
            raise EmptyValuesForTaskKanbanViewFields

    def _validate_duplicate_task_kanban_view_fields(
            self, column_dtos: List[ColumnDTO]):
        task_summary_field_dtos = []
        for column_dto in column_dtos:
            task_summary_field_dtos += column_dto.list_view_fields
            self._validate_duplicate_summary_fields(task_summary_field_dtos)

    @staticmethod
    def _check_task_summary_fields_are_not_empty(
            task_summary_fields_dtos: List[TaskSummaryFieldsDTO]):
        for task_summary_fields_dto in task_summary_fields_dtos:
            is_empty_value = not task_summary_fields_dto.summary_fields
            if is_empty_value:
                raise EmptyValuesForTaskSummaryFields

    def _validate_duplicate_summary_fields(
            self, task_summary_field_dtos: List[TaskSummaryFieldsDTO]):
        for task_summary_fields_dto in task_summary_field_dtos:
            self._validate_duplicate_fields_for_task_template(
                fields=task_summary_fields_dto.summary_fields
            )

    def _validate_duplicate_fields_for_task_template(
            self, fields: List[str]):
        duplicate_fields = self._find_duplicates(
            fields)
        if duplicate_fields:
            from ib_boards.exceptions.custom_exceptions import \
                DuplicateSummaryFieldsInTask
            raise DuplicateSummaryFieldsInTask(
                duplicate_fields=duplicate_fields
            )

    @staticmethod
    def _get_invalid_task_template_ids_for_fields(
            task_ids: List[str]):
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        valid_task_ids = service_adapter.task_service.get_valid_task_template_ids(
            task_template_ids=task_ids
        )
        invalid_task_ids = [
            task_id
            for task_id in task_ids
            if task_id not in valid_task_ids
        ]
        if invalid_task_ids:
            from ib_boards.exceptions.custom_exceptions import \
                InvalidTaskIdInSummaryFields
            raise InvalidTaskIdInSummaryFields(task_ids=invalid_task_ids)

    @staticmethod
    def _get_task_template_ids_for_fields(
            task_summary_field_dtos: List[TaskSummaryFieldsDTO]):
        task_ids = [
            task_summary_field_dto.task_id
            for task_summary_field_dto in task_summary_field_dtos
        ]
        return task_ids

    @staticmethod
    def _validate_task_summary_fields_with_template_id(task_summary_fields):
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        service_adapter.task_service.validate_task_task_summary_fields_with_id(
            task_summary_fields=task_summary_fields
        )

    @staticmethod
    def _find_duplicates(values: List):
        import collections
        duplicate_values = [
            field for field, count in collections.Counter(values).items()
            if count > 1
        ]
        return duplicate_values
