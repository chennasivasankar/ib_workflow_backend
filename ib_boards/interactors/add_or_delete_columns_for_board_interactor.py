"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.exceptions.custom_exceptions import \
    ColumnIdsAssignedToDifferentBoard, InvalidUserRoles
from ib_boards.interactors.dtos import ColumnDTO, TaskTemplateStagesDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class AddOrDeleteColumnsForBoardInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_or_delete_columns_for_board_wrapper(
            self, column_dtos: List[ColumnDTO]):
        self.add_or_delete_columns_for_board(
            column_dtos=column_dtos
        )

    def add_or_delete_columns_for_board(self, column_dtos: List[ColumnDTO]):

        self.validate_columns_data(column_dtos=column_dtos)
        board_ids = [column_dto.board_id for column_dto in column_dtos]
        board_ids = list(set(board_ids))
        present_column_ids = self.storage.get_boards_column_ids(
            board_ids=board_ids
        )
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        column_ids_not_in_configuration = [
            column_id
            for column_id in present_column_ids
            if column_id not in column_ids
        ]
        column_ids_for_update = [
            column_id
            for column_id in present_column_ids
            if column_id not in column_ids_not_in_configuration
        ]
        column_dtos_dict = {}
        for column_dto in column_dtos:
            column_dtos_dict[column_dto.column_id] = column_dto
        self._delete_columns_which_are_not_in_configuration(
            column_ids=column_ids_not_in_configuration
        )
        self._create_columns_for_board(
            present_column_ids=present_column_ids,
            column_dtos_dict=column_dtos_dict
        )
        self._update_columns_for_board(
            column_ids_for_update=column_ids_for_update,
            column_dtos_dict=column_dtos_dict
        )

    def _create_columns_for_board(
            self, present_column_ids, column_dtos_dict):
        columns_dtos_for_create = [
            column_dtos_dict[column_id]
            for column_id in column_dtos_dict.keys()
            if column_id not in present_column_ids
        ]
        self.storage.create_columns_for_board(
            column_dtos=columns_dtos_for_create
        )

    def _update_columns_for_board(
            self, column_ids_for_update, column_dtos_dict):
        column_dto_for_update = []
        for column_id in column_ids_for_update:
            column_dto_for_update.append(column_dtos_dict[column_id])

        self.storage.update_columns_for_board(
            column_dtos=column_dto_for_update
        )

    def _delete_columns_which_are_not_in_configuration(self, column_ids: List[str]):
        self.storage.delete_columns_which_are_not_in_configuration(
            column_ids=column_ids
        )

    def validate_columns_data(self, column_dtos: List[ColumnDTO]):
        self._validate_column_ids(column_dtos=column_dtos)
        self._validate_column_display_name(column_dtos=column_dtos)
        self._validate_columns_display_orders(column_dtos=column_dtos)
        self._validate_task_template_ids_in_task_template_stage(
            column_dtos=column_dtos
        )
        self._validate_empty_values_in_task_template_stage(
            column_dtos=column_dtos
        )
        self._validate_task_template_stages_with_template_id(
            column_dtos=column_dtos)
        self._validate_duplicate_task_template_stages(column_dtos=column_dtos)
        self._validate_user_roles(column_dtos=column_dtos)
        self._check_for_column_ids_are_assigned_to_single_board(
            column_dtos=column_dtos
        )

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

    def _validate_columns_display_orders(self, column_dtos: List[ColumnDTO]):
        from collections import defaultdict
        column_dtos_dict = defaultdict(lambda: [])
        for column_dto in column_dtos:
            column_dtos_dict[column_dto.column_id].append(column_dto)

        for key, value in column_dtos_dict.items():
            self._validate_column_display_order(column_dtos=value)

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
        return

    @staticmethod
    def _find_duplicates(values: List):
        import collections
        duplicate_values = [
            field for field, count in collections.Counter(values).items()
            if count > 1
        ]
        return duplicate_values

    def _check_for_column_ids_are_assigned_to_single_board(
            self, column_dtos: List[ColumnDTO]):
        from collections import defaultdict
        board_column_map = defaultdict(lambda: [])

        for column_dto in column_dtos:
            board_column_map[column_dto.board_id].append(
                column_dto.column_id
            )
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        board_column_dtos = self.storage.get_board_ids_for_column_ids(
            column_ids=column_ids
        )
        for board_column_dto in board_column_dtos:
            board_id = board_column_dto.board_id
            column_id = board_column_dto.column_id
            if column_id not in board_column_map[board_id]:
                raise ColumnIdsAssignedToDifferentBoard(column_id=column_id)
