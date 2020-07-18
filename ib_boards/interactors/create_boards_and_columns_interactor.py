"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class CreateBoardsAndColumnsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_boards_and_columns(
            self, board_dtos: List[BoardDTO], column_dtos: List[ColumnDTO]):
        board_ids = [board_dto.board_id for board_dto in board_dtos]
        self._validate_board_display_name(board_dtos=board_dtos)
        self.validate_columns_data(column_dtos)
        self.storage.create_boards_and_columns(
            board_dtos=board_dtos,
            column_dtos=column_dtos
        )

    def validate_columns_data(self, column_dtos):
        self._validate_column_ids(column_dtos=column_dtos)
        self._validate_column_display_name(column_dtos=column_dtos)
        self._validate_task_template_ids_in_task_template_stage(
            column_dtos=column_dtos
        )
        self._validate_task_template_ids_in_task_template_fields(
            column_dtos=column_dtos
        )
        self._validate_empty_values_in_task_template_stage(
            column_dtos=column_dtos
        )
        self._validate_duplicate_task_template_stages(column_dtos=column_dtos)
        self._validate_duplicate_task_summary_fields(column_dtos=column_dtos)
        self._validate_empty_values_in_task_summary_fields(
            column_dtos=column_dtos)
        self._validate_task_template_stages_with_id(column_dtos=column_dtos)
        self._validate_task_summary_fields_with_id(column_dtos=column_dtos)
        self._validate_user_roles(column_dtos=column_dtos)

    @staticmethod
    def _validate_board_display_name(board_dtos: List[BoardDTO]):
        for board_dto in board_dtos:
            is_invalid_display_name = not board_dto.display_name
            if is_invalid_display_name:
                from ib_boards.exceptions.custom_exceptions import \
                    InvalidBoardDisplayName
                raise InvalidBoardDisplayName(board_id=board_dto.board_id)

    @staticmethod
    def _validate_column_ids(column_dtos: List[ColumnDTO]):
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        import collections
        duplicate_column_ids = [
            column_id for column_id, count in collections.Counter(
                column_ids
            ).items()
            if count > 1
        ]
        if duplicate_column_ids:
            from ib_boards.exceptions.custom_exceptions import \
                DuplicateColumnIds
            raise DuplicateColumnIds(column_ids=duplicate_column_ids)

    @staticmethod
    def _validate_column_display_name(column_dtos: List[ColumnDTO]):
        is_invalid_display_name_ids = []
        for column_dto in column_dtos:
            is_invalid_display_name = not column_dto.display_name
            if is_invalid_display_name:
                is_invalid_display_name_ids.append(column_dto.column_id)
        if is_invalid_display_name_ids:
            from ib_boards.exceptions.custom_exceptions import \
                InvalidColumnDisplayName
            raise InvalidColumnDisplayName(column_ids=is_invalid_display_name_ids)

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
        valid_task_template_ids = service_adapter.task_service.\
            get_valid_task_template_ids(
                task_template_ids=task_template_ids
            )

        invalid_task_template_ids = [
            task_template_id for task_template_id in task_template_ids
            if task_template_id not in valid_task_template_ids
        ]
        print(invalid_task_template_ids, task_template_ids)
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

    def _validate_task_template_ids_in_task_template_fields(
            self, column_dtos: List[ColumnDTO]):

        task_ids = []
        for column_dto in column_dtos:
            task_summary_field_dtos = column_dto.task_summary_fields
            task_ids += self._get_task_ids(
                task_summary_field_dtos=task_summary_field_dtos
            )

        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()

        valid_task_ids = service_adapter.task_service.get_valid_task_ids(
            task_ids=task_ids
        )
        invalid_task_ids = [
            task_id
            for task_id in task_ids
            if task_id not in valid_task_ids
        ]
        if invalid_task_ids:
            from ib_boards.exceptions.custom_exceptions import \
                InvalidTaskIdInSummaryFields
            raise InvalidTaskIdInSummaryFields(task_ids=task_ids)

    @staticmethod
    def _get_task_ids(
            task_summary_field_dtos: List[TaskSummaryFieldsDTO]):
        task_ids = [
            task_summary_field_dto.task_id
            for task_summary_field_dto in task_summary_field_dtos
        ]
        return task_ids

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
    def _validate_task_template_stages_with_id(column_dtos: List[ColumnDTO]):
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

    @staticmethod
    def _validate_duplicate_stages_for_task_template(stages: List[str]):
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

    @staticmethod
    def _validate_task_summary_fields_with_id(column_dtos: List[ColumnDTO]):
        task_summary_fields = []
        for column_dto in column_dtos:
            task_summary_fields += column_dto.task_summary_fields
        from ib_boards.adapters.service_adapter import get_service_adapter

        service_adapter = get_service_adapter()

        service_adapter.task_service.validate_task_task_summary_fields_with_id(
            task_summary_fields=task_summary_fields
        )

    def _validate_empty_values_in_task_summary_fields(
            self, column_dtos: List[ColumnDTO]):
        for column_dto in column_dtos:
            task_summary_fields_dtos = column_dto.task_summary_fields
            self._check_task_summary_fields_are_not_empty(
                task_summary_fields_dtos=task_summary_fields_dtos
            )

    @staticmethod
    def _check_task_summary_fields_are_not_empty(
            task_summary_fields_dtos: List[TaskSummaryFieldsDTO]):
        for task_summary_fields_dto in task_summary_fields_dtos:
            is_empty_value = not task_summary_fields_dto.summary_fields
            if is_empty_value:
                from ib_boards.exceptions.custom_exceptions import \
                    EmptyValuesForTaskSummaryFields
                raise EmptyValuesForTaskSummaryFields

    def _validate_duplicate_task_summary_fields(self,
                                                column_dtos: List[ColumnDTO]):
        for column_dto in column_dtos:
            task_summary_field_dtos = column_dto.task_summary_fields
            for task_summary_fields_dto in task_summary_field_dtos:
                self._validate_duplicate_summary_fields_for_task(
                    fields=task_summary_fields_dto.summary_fields
                )

    @staticmethod
    def _validate_duplicate_summary_fields_for_task(fields: List[str]):
        import collections
        duplicate_fields = [
            field for field, count in
            collections.Counter(fields).items()
            if count > 1
        ]
        if duplicate_fields:
            from ib_boards.exceptions.custom_exceptions import \
                DuplicateSummaryFieldsInTask
            raise DuplicateSummaryFieldsInTask(
                duplicate_fields=duplicate_fields
            )
