"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import ColumnDTO, BoardColumnDTO
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

        self._validate_the_data(column_dtos=column_dtos)
        board_ids = [column_dto.board_id for column_dto in column_dtos]
        board_ids = list(set(board_ids))
        present_column_ids = self.storage.get_board_column_ids(
            board_ids=board_ids
        )
        from collections import defaultdict
        board_column_map = defaultdict(lambda: [])
        for column_dto in column_dtos:
            board_column_map[column_dto.board_id].append(
                column_dto.column_id
            )
        column_dtos_dict = {}
        for column_dto in column_dtos:
            column_dtos_dict[column_dto.column_id] = column_dto
        self._update_columns_for_board(
            present_column_ids=present_column_ids,
            column_dtos_dict=column_dtos_dict
        )
        self._create_columns_for_board(
            present_column_ids=present_column_ids,
            column_dtos_dict=column_dtos_dict
        )
        self._delete_columns_which_are_not_in_configuration(
            board_column_map=board_column_map
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
            self, present_column_ids, column_dtos_dict):
        column_dto_for_update = [
            column_dtos_dict[column_id]
            for column_id in present_column_ids
        ]
        self.storage.update_columns_for_board(
            column_dtos=column_dto_for_update
        )

    def _delete_columns_which_are_not_in_configuration(self, board_column_map):

        column_for_delete_dtos = [
            BoardColumnDTO(
                board_id=key,
                column_ids=value
            )
            for key, value in board_column_map.items()
        ]
        self.storage.delete_columns_which_are_not_in_configuration(
            column_for_delete_dtos=column_for_delete_dtos
        )

    def _validate_the_data(self, column_dtos: List[ColumnDTO]):
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        self._validate_column_ids(column_ids=column_ids)
        self._validate_column_display_name(column_dtos=column_dtos)
        self._validate_task_template_stages_json(column_dtos=column_dtos)
        self._validate_task_template_ids_in_task_template_stage(
            column_dtos=column_dtos
        )
        self._validate_task_template_summary_fields_json(
            column_dtos=column_dtos
        )
        self._validate_task_template_ids_in_task_template_fields(
            column_dtos=column_dtos
        )
        self._validate_empty_values_in_task_template_stage(
            column_dtos=column_dtos
        )
        self._validate_duplicate_task_template_stages(column_dtos=column_dtos)
        self._validate_task_template_stages_with_id(column_dtos=column_dtos)
        self._validate_task_summary_fields_with_id(column_dtos=column_dtos)
        self._validate_user_roles(column_dtos=column_dtos)

        self._check_for_column_ids_are_assigned_to_single_board(
            column_dtos=column_dtos
        )

    @staticmethod
    def _validate_column_ids(column_ids: List[str]):
        import collections
        duplicate_column_ids = [
            column_id for column_id, count in
            collections.Counter(column_ids).items()
            if count > 1
        ]
        if duplicate_column_ids:
            from ib_boards.exceptions.custom_exceptions import \
                DuplicateColumnIds
            raise DuplicateColumnIds(column_ids=duplicate_column_ids)

    @staticmethod
    def _validate_column_display_name(column_dtos: List[ColumnDTO]):
        for column_dto in column_dtos:
            is_invalid_display_name = not column_dto.display_name
            if is_invalid_display_name:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidColumnDisplayName
                raise InvalidColumnDisplayName(column_id=column_dto.column_id)

    @staticmethod
    def _validate_task_template_stages_json(column_dtos: List[ColumnDTO]):
        import json
        for column_dto in column_dtos:
            try:
                json.loads(column_dto.task_template_stages)
            except json.JSONDecodeError:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidJsonForTaskTemplateStages
                raise InvalidJsonForTaskTemplateStages

    @staticmethod
    def _validate_task_template_ids_in_task_template_stage(
            column_dtos: List[ColumnDTO]):
        import json
        task_template_ids = []
        for column_dto in column_dtos:
            task_template_stages = json.loads(column_dto.task_template_stages)
            task_template_ids += task_template_stages.keys()

        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()

        service_adapter.task_service.validate_task_template_ids(
            task_template_ids=task_template_ids
        )

    @staticmethod
    def _validate_task_template_ids_in_task_template_fields(
            column_dtos: List[ColumnDTO]):
        import json
        task_template_ids = []
        for column_dto in column_dtos:
            task_summary_fields = json.loads(column_dto.task_summary_fields)
            task_template_ids += task_summary_fields.keys()

        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()

        service_adapter.task_service.validate_task_template_ids(
            task_template_ids=task_template_ids
        )

    @staticmethod
    def _validate_task_template_summary_fields_json(
            column_dtos: List[ColumnDTO]):
        import json
        for column_dto in column_dtos:
            try:
                json.loads(column_dto.task_summary_fields)
            except json.JSONDecodeError:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidJsonForTaskTemplateSummaryFields
                raise InvalidJsonForTaskTemplateSummaryFields

    @staticmethod
    def _validate_empty_values_in_task_template_stage(
            column_dtos: List[ColumnDTO]):
        import json
        task_template_ids = []
        for column_dto in column_dtos:
            task_template_stages = json.loads(column_dto.task_template_stages)
            for value in task_template_stages.values():
                is_empty_value = not value
                if is_empty_value:
                    from ib_boards.exceptions.custom_exceptions import \
                        EmptyValuesForTaskTemplateStages
                    raise EmptyValuesForTaskTemplateStages

        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()

        service_adapter.task_service.validate_task_template_ids(
            task_template_ids=task_template_ids
        )

    @staticmethod
    def _validate_task_template_stages_with_id(column_dtos: List[ColumnDTO]):
        task_template_stages = []
        for column_dto in column_dtos:
            import json
            task_template_stages.append(
                json.loads(column_dto.task_template_stages)
            )
        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()

        service_adapter.task_service.validate_task_template_stages_with_id(
            task_template_stages=task_template_stages
        )

    @staticmethod
    def _validate_task_summary_fields_with_id(column_dtos: List[ColumnDTO]):
        task_summary_fields = []
        for column_dto in column_dtos:
            import json
            task_summary_fields.append(
                json.loads(column_dto.task_summary_fields)
            )
        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()

        service_adapter.task_service.validate_task_task_summary_fields_with_id(
            task_summary_fields=task_summary_fields
        )

    def _validate_duplicate_task_template_stages(self,
                                                 column_dtos: List[ColumnDTO]):
        import json
        for column_dto in column_dtos:
            task_template_stages = json.loads(column_dto.task_template_stages)
            for key, value in task_template_stages.items():
                self._validate_duplicate_values(stages=value)

    @staticmethod
    def _validate_duplicate_values(stages: List[str]):
        import collections
        duplicate_stages = [
            stage for stage, count in
            collections.Counter(stages).items()
            if count > 1
        ]
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
        service_adapter.user_service.validate_user_role_ids(
            user_role_ids=user_roles
        )

    def _check_for_column_ids_are_assigned_to_single_board(
            self, column_dtos: List[ColumnDTO]):
        from collections import defaultdict

        from ib_boards.exceptions.custom_exceptions import \
            ColumnIdsAssignedToDifferentBoard
        board_column_map = defaultdict(lambda: [])

        for column_dto in column_dtos:
            board_column_map[column_dto.board_id].append(
                column_dto.column_id
            )
        for key, value in board_column_map.items():
            board_ids = self.storage.get_board_ids_for_column_ids(
                column_ids=value
            )
            is_having_multiple_boards = (
                    len(board_ids) == 1 and key not in board_ids
                    or len(board_ids) > 1
            )
            if is_having_multiple_boards:
                raise ColumnIdsAssignedToDifferentBoard(column_ids=value)
