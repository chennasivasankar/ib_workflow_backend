"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""
import json

import pytest

from ib_boards.interactors.create_boards_and_columns_interactor import \
    CreateBoardsAndColumnsInteractor
from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory, \
    ColumnDTOFactory, TaskTemplateStagesDTOFactory, TaskSummaryFieldsDTOFactory


class TestPopulateScriptInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_boards.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        from unittest import mock
        storage = mock.create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def sequence_reset(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        TaskSummaryFieldsDTOFactory.reset_sequence()
        BoardDTOFactory.reset_sequence()
        ColumnDTOFactory.reset_sequence()

    @pytest.fixture
    def board_dto_with_duplicate_ids(self):
        board_dto_1 = BoardDTOFactory()
        BoardDTOFactory.reset_sequence()
        board_dto_2 = BoardDTOFactory()
        return [
            board_dto_1,
            board_dto_2
        ]

    @pytest.fixture
    def board_dtos_with_no_display_name(self):
        return [
            BoardDTOFactory(display_name=''),
            BoardDTOFactory()
        ]

    @pytest.fixture
    def board_dtos(self):
        return BoardDTOFactory.create_batch(3)

    @pytest.fixture
    def column_dtos(self):
        return ColumnDTOFactory.create_batch(3)

    @pytest.fixture
    def column_dtos_with_duplicate_ids(self):
        column_dto_1 = ColumnDTOFactory()
        ColumnDTOFactory.reset_sequence()
        column_dto_2 = ColumnDTOFactory()
        return [
            column_dto_1,
            column_dto_2
        ]

    @pytest.fixture
    def column_dtos_with_no_display_name(self):
        return [
            ColumnDTOFactory(display_name=''),
            ColumnDTOFactory()
        ]

    @pytest.fixture
    def column_dtos_with_empty_task_template_stages(self):
        task_template_stages = TaskTemplateStagesDTOFactory.create_batch(2, stages=[])
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(task_template_stages=task_template_stages)
        ]

    @pytest.fixture
    def column_dtos_with_duplicate_task_template_stages(self):
        task_template_stages = TaskTemplateStagesDTOFactory.create_batch(
            2,
            stages=['PR_PAYMENT_REQUEST_DRAFTS', 'PR_PAYMENT_REQUEST_DRAFTS']
        )
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(task_template_stages=task_template_stages)
        ]

    @pytest.fixture
    def column_dtos_with_empty_task_summary_fields(self):
        task_summary_fields = TaskSummaryFieldsDTOFactory.create_batch(
            2, summary_fields=[]
        )
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(task_summary_fields=task_summary_fields)
        ]

    @pytest.fixture
    def column_dtos_with_duplicate_task_summary_fields(self):
        task_summary_fields = TaskSummaryFieldsDTOFactory.create_batch(
            2,
            summary_fields=['Price', 'Price']
        )
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(task_summary_fields=task_summary_fields)
        ]

    @pytest.fixture
    def column_dtos_with_invalid_task_template_id(self):
        return ColumnDTOFactory.create_batch(3)

    @pytest.fixture
    def task_summary_field_dtos(self):
        task_field_dtos_1 = TaskSummaryFieldsDTOFactory.create_batch(2)
        TaskSummaryFieldsDTOFactory.reset_sequence()
        task_field_dtos_2 = TaskSummaryFieldsDTOFactory.create_batch(2)
        TaskSummaryFieldsDTOFactory.reset_sequence()
        task_field_dtos_3 = TaskSummaryFieldsDTOFactory.create_batch(2)
        return task_field_dtos_1 + task_field_dtos_2 + task_field_dtos_3

    def test_with_invalid_board_display_name_raise_exception(
            self, storage_mock, sequence_reset,
            board_dtos_with_no_display_name, column_dtos):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import InvalidBoardDisplayName
        with pytest.raises(InvalidBoardDisplayName) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos_with_no_display_name,
                column_dtos=column_dtos
            )

    def test_with_duplicate_column_ids_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_duplicate_ids, board_dtos):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            DuplicateColumnIds
        with pytest.raises(DuplicateColumnIds) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_duplicate_ids
            )

    def test_with_invalid_column_display_name_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_no_display_name, board_dtos):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidColumnDisplayName
        with pytest.raises(InvalidColumnDisplayName) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_no_display_name
            )

    def test_with_invalid_task_template_id_in_stages_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id, mocker):
        # Arrange
        invalid_task_template_ids = ['TASK_ID_1']
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock

        adapter_mock = adapter_mock(
            mocker=mocker,
            task_template_ids=invalid_task_template_ids
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidTaskTemplateIdInStages
        with pytest.raises(InvalidTaskTemplateIdInStages) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )

    def test_with_invalid_task_template_id_in_fields_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id, mocker):
        # Arrange
        invalid_task_template_ids = ['TASK_ID_1']
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock

        adapter_mock = adapter_mock(
            mocker=mocker,
            task_template_ids=invalid_task_template_ids
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidTaskTemplateIdInStages
        with pytest.raises(InvalidTaskTemplateIdInStages) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )

    def test_with_empty_task_template_stages_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_empty_task_template_stages):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            EmptyValuesForTaskTemplateStages
        with pytest.raises(EmptyValuesForTaskTemplateStages) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_empty_task_template_stages
            )

    def test_with_duplicate_task_template_stages_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_duplicate_task_template_stages, mocker):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            DuplicateStagesInTaskTemplateStages
        with pytest.raises(DuplicateStagesInTaskTemplateStages) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_duplicate_task_template_stages
            )

    def test_with_task_template_stages_not_belongs_to_task_template_id(
            self, storage_mock, sequence_reset, board_dtos, column_dtos, mocker):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock_for_task_template_stages
        adapter_mock_for_task_template_stages(mocker)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            TaskTemplateStagesNotBelongsToTaskTemplateId
        with pytest.raises(TaskTemplateStagesNotBelongsToTaskTemplateId) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos
            )

    def test_with_task_summary_fields_not_belongs_to_task_id(
            self, storage_mock, sequence_reset, board_dtos,
            column_dtos, task_summary_field_dtos, mocker):
        # Arrange
        not_related_fields = task_summary_field_dtos
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock_for_task_template_fields
        adapter_mock = adapter_mock_for_task_template_fields(mocker)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            TaskSummaryFieldsNotBelongsToTaskTemplateId
        with pytest.raises(
                TaskSummaryFieldsNotBelongsToTaskTemplateId) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos
            )

        # Assert
        adapter_mock.assert_called_once_with(
            task_summary_fields=not_related_fields
        )

    def test_with_invalid_user_role_ids_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id, mocker):
        # Arrange
        invalid_user_roles = ['USER', 'MEMBER']
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.user_service import \
            adapter_mock

        adapter_mock(mocker=mocker, user_roles=invalid_user_roles)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidUserRoles
        with pytest.raises(InvalidUserRoles) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )
        # Assert
        assert error.value.user_role_ids == invalid_user_roles

    def test_with_valid_data_creates_data(
            self, storage_mock, sequence_reset, board_dtos, column_dtos):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        # Act
        interactor.create_boards_and_columns(
            board_dtos=board_dtos,
            column_dtos=column_dtos
        )

        # Assert
        storage_mock.create_boards_and_columns.assert_called_once_with(
            board_dtos=board_dtos,
            column_dtos=column_dtos
        )

    def test_with_duplicate_task_summary_fields_raise_exception(
            self, storage_mock, sequence_reset, board_dtos,
            column_dtos_with_duplicate_task_summary_fields):
        # Arrange
        duplicate_fields = ['Price']
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            DuplicateSummaryFieldsInTask
        with pytest.raises(DuplicateSummaryFieldsInTask) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_duplicate_task_summary_fields
            )

        # Assert
        assert error.value.duplicate_fields == duplicate_fields

    def test_with_empty_task_summary_fields_raise_exception(
            self, storage_mock, sequence_reset, board_dtos,
            column_dtos_with_empty_task_summary_fields):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            EmptyValuesForTaskSummaryFields
        with pytest.raises(EmptyValuesForTaskSummaryFields) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_empty_task_summary_fields
            )
