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


class TestCreateBoardsAndColumnsInteractor:

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
    def column_dtos_with_empty_task_list_view_fields(self):
        list_view_fields = TaskSummaryFieldsDTOFactory.create_batch(
            2, summary_fields=[]
        )
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(list_view_fields=list_view_fields)
        ]

    @pytest.fixture
    def column_dtos_with_duplicate_list_view_fields(self):
        list_view_fields = TaskSummaryFieldsDTOFactory.create_batch(
            2,
            summary_fields=['Price', 'Price']
        )
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(list_view_fields=list_view_fields)
        ]

    @pytest.fixture
    def column_dtos_with_empty_task_kanban_view_fields(self):
        kanban_view_fields = TaskSummaryFieldsDTOFactory.create_batch(
            2, summary_fields=[]
        )
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(kanban_view_fields=kanban_view_fields)
        ]

    @pytest.fixture
    def column_dtos_with_duplicate_kanban_view_fields(self):
        kanban_view_fields = TaskSummaryFieldsDTOFactory.create_batch(
            2,
            summary_fields=['Price', 'Price']
        )
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(list_view_fields=kanban_view_fields)
        ]

    @pytest.fixture
    def column_dtos_with_invalid_task_template_id(self):
        return ColumnDTOFactory.create_batch(1)

    @pytest.fixture
    def column_dtos_with_invalid_display_name(self):
        return ColumnDTOFactory.create_batch(3, display_order=1)

    @pytest.fixture
    def task_summary_field_dtos(self):
        task_field_dtos_1 = TaskSummaryFieldsDTOFactory.create_batch(2)
        TaskSummaryFieldsDTOFactory.reset_sequence()
        task_field_dtos_2 = TaskSummaryFieldsDTOFactory.create_batch(2)
        TaskSummaryFieldsDTOFactory.reset_sequence()
        task_field_dtos_3 = TaskSummaryFieldsDTOFactory.create_batch(2)
        return task_field_dtos_1 + task_field_dtos_2 + task_field_dtos_3

    @pytest.fixture
    def mock_valid_task_and_template_ids(self, mocker):
        task_template_ids = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_valid_task_template_ids_mock
        get_valid_task_template_ids_mock(
            mocker=mocker,
            task_template_ids=task_template_ids
        )

    @pytest.fixture
    def mock_valid_template_ids(self, mocker):
        task_template_ids_for_stages = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        task_template_ids_list_view = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        task_template_ids_kanban_view = [
            'TASK_TEMPLATE_ID_6', 'TASK_TEMPLATE_ID_7', 'TASK_TEMPLATE_ID_8',
            'TASK_TEMPLATE_ID_9', 'TASK_TEMPLATE_ID_10',
            'TASK_TEMPLATE_ID_6', 'TASK_TEMPLATE_ID_7', 'TASK_TEMPLATE_ID_8',
            'TASK_TEMPLATE_ID_9', 'TASK_TEMPLATE_ID_10',
            'TASK_TEMPLATE_ID_6', 'TASK_TEMPLATE_ID_7', 'TASK_TEMPLATE_ID_8',
            'TASK_TEMPLATE_ID_9', 'TASK_TEMPLATE_ID_10'

        ]
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_valid_task_ids_for_kanban_view_mock
        get_valid_task_ids_for_kanban_view_mock(
            mocker=mocker,
            task_template_ids_for_stages=task_template_ids_for_stages,
            task_template_ids_list_view=task_template_ids_list_view,
            task_ids=task_template_ids_kanban_view
        )

    @pytest.fixture
    def mock_valid_template_ids_for_empty_fields(self, mocker):
        task_template_ids_for_stages = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        task_template_ids_list_view = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        task_template_ids_kanban_view = [
            'TASK_TEMPLATE_ID_6', 'TASK_TEMPLATE_ID_7', 'TASK_TEMPLATE_ID_8',
            'TASK_TEMPLATE_ID_9', 'TASK_TEMPLATE_ID_10', 'TASK_TEMPLATE_ID_1',
            'TASK_TEMPLATE_ID_2'

        ]
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_valid_task_ids_for_kanban_view_mock
        get_valid_task_ids_for_kanban_view_mock(
            mocker=mocker,
            task_template_ids_for_stages=task_template_ids_for_stages,
            task_template_ids_list_view=task_template_ids_list_view,
            task_ids=task_template_ids_kanban_view
        )

    @pytest.fixture
    def task_template_stages_dtos(self):
        task_field_dtos_1 = TaskTemplateStagesDTOFactory.create_batch(2)
        TaskTemplateStagesDTOFactory.reset_sequence()
        task_field_dtos_2 = TaskTemplateStagesDTOFactory.create_batch(2)
        TaskTemplateStagesDTOFactory.reset_sequence()
        task_field_dtos_3 = TaskTemplateStagesDTOFactory.create_batch(2)
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
        duplicate_column_ids = ['COLUMN_ID_1']
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
        # Assert
        assert error.value.column_ids == duplicate_column_ids

    def test_with_invalid_column_display_name_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_no_display_name, board_dtos):
        # Arrange
        invalid_display_name_column_id = ['COLUMN_ID_1']
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
        assert error.value.column_ids == invalid_display_name_column_id

    def test_with_invalid_task_template_id_in_stages_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id, mocker):
        # Arrange
        invalid_task_template_ids = ['TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5']
        task_template_ids = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        valid_task_template_ids = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3'
        ]
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_valid_task_template_ids_mock

        adapter_mock = get_valid_task_template_ids_mock(
            mocker=mocker,
            task_template_ids=valid_task_template_ids
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidTaskTemplateIdInStages
        with pytest.raises(InvalidTaskTemplateIdInStages) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )

        # Assert
        adapter_mock.assert_called_once_with(
            task_template_ids=task_template_ids
        )
        assert error.value.task_template_ids == invalid_task_template_ids

    def test_with_invalid_task_id_in_list_view_fields_fields_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id, mocker):
        # Arrange
        task_template_ids = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        invalid_task_ids = ['TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5']
        valid_task_ids = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3'
        ]
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_valid_task_ids_mock
        get_valid_task_ids_mock(
            mocker=mocker,
            task_template_ids=task_template_ids,
            task_ids=valid_task_ids
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidTaskIdInListViewFields
        with pytest.raises(InvalidTaskIdInListViewFields) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )

        # Assert
        assert error.value.task_ids == invalid_task_ids

    def test_with_empty_task_template_stages_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_empty_task_template_stages,
            mock_valid_task_and_template_ids):
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
            column_dtos_with_duplicate_task_template_stages,
            mock_valid_task_and_template_ids):
        # Arrange
        duplicate_stages = ['PR_PAYMENT_REQUEST_DRAFTS']
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

        # Assert
        assert error.value.duplicate_stages == duplicate_stages

    def test_with_task_template_stages_not_belongs_to_task_template_id(
            self, storage_mock, sequence_reset, board_dtos, column_dtos, mocker,
            mock_valid_task_and_template_ids, task_template_stages_dtos):
        # Arrange
        not_related_stages = task_template_stages_dtos
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock_for_task_template_stages
        adapter_mock = adapter_mock_for_task_template_stages(mocker)

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
            column_dtos, task_summary_field_dtos, mocker,
            mock_valid_task_and_template_ids):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock_for_task_template_fields
        adapter_mock = adapter_mock_for_task_template_fields(mocker)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            TaskListViewFieldsNotBelongsToTaskTemplateId
        with pytest.raises(
                TaskListViewFieldsNotBelongsToTaskTemplateId) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos
            )

    def test_with_invalid_user_role_ids_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id,
            mocker, mock_valid_template_ids):
        # Arrange
        valid_user_roles = ['ALL_ROLES', 'MEMBER']
        user_roles = ['ALL_ROLES']
        invalid_user_roles = ['USER']
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock

        adapter_mock = adapter_mock(mocker=mocker,
                                    user_roles=invalid_user_roles)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidUserRoles
        with pytest.raises(InvalidUserRoles) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )
        # Assert
        adapter_mock.assert_called_once_with(
            user_roles=user_roles
        )
        assert error.value.user_role_ids == user_roles

    def test_with_valid_data_creates_data(
            self, storage_mock, sequence_reset, board_dtos, column_dtos,
            mock_valid_template_ids, mocker):
        # Arrange
        user_roles = ['ALL_ROLES', 'MEMBER', 'USER']
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock
        adapter_mock = adapter_mock(mocker=mocker,
                                    user_roles=user_roles)
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )
        board_dtos.append(
            BoardDTOFactory(board_id='BOARD_ID_0')
        )
        storage_mock.get_existing_board_ids.return_value = []
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

    def test_with_duplicate_task_list_view_fields_raise_exception(
            self, storage_mock, sequence_reset, board_dtos,
            column_dtos_with_duplicate_list_view_fields,
            mock_valid_task_and_template_ids):
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
                column_dtos=column_dtos_with_duplicate_list_view_fields
            )

        # Assert
        assert error.value.duplicate_fields == duplicate_fields

    def test_with_empty_task_list_view_fields_raise_exception(
            self, storage_mock, sequence_reset, board_dtos,
            column_dtos_with_empty_task_list_view_fields,
            mock_valid_task_and_template_ids):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            EmptyValuesForTaskListViewFields
        with pytest.raises(EmptyValuesForTaskListViewFields) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_empty_task_list_view_fields
            )

    def test_with_duplicate_column_display_order_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_invalid_display_name, board_dtos,
            mock_valid_task_and_template_ids):
        # Arrange
        duplicate_display_order_values = [1]
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            DuplicateValuesInColumnDisplayOrder
        with pytest.raises(DuplicateValuesInColumnDisplayOrder) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_display_name
            )
        # Assert
        assert error.value.display_order_values == duplicate_display_order_values

    def test_with_invalid_task_id_in_kanban_view_fields_fields_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id, mocker):
        # Arrange
        task_template_ids_for_stages = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        task_template_ids_list_view = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        invalid_task_ids = ['TASK_TEMPLATE_ID_9', 'TASK_TEMPLATE_ID_10']
        valid_task_ids = [
            'TASK_TEMPLATE_ID_6', 'TASK_TEMPLATE_ID_7', 'TASK_TEMPLATE_ID_8'
        ]
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_valid_task_ids_for_kanban_view_mock
        get_valid_task_ids_for_kanban_view_mock(
            mocker=mocker,
            task_template_ids_for_stages=task_template_ids_for_stages,
            task_template_ids_list_view=task_template_ids_list_view,
            task_ids=valid_task_ids
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidTaskIdInKanbanViewFields
        with pytest.raises(InvalidTaskIdInKanbanViewFields) as error:
            assert interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )

        # Assert
        assert error.value.task_ids == invalid_task_ids

    def test_with_duplicate_task_kanban_view_fields_raise_exception(
            self, storage_mock, sequence_reset, board_dtos,
            column_dtos_with_duplicate_kanban_view_fields,
            mock_valid_template_ids):
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
                column_dtos=column_dtos_with_duplicate_kanban_view_fields
            )

        # Assert
        assert error.value.duplicate_fields == duplicate_fields

    def test_with_empty_task_kanban_view_fields_raise_exception(
            self, storage_mock, sequence_reset, board_dtos,
            column_dtos_with_empty_task_kanban_view_fields,
            mock_valid_template_ids_for_empty_fields):
        # Arrange
        interactor = CreateBoardsAndColumnsInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            EmptyValuesForTaskKanbanViewFields
        with pytest.raises(EmptyValuesForTaskKanbanViewFields) as error:
            interactor.create_boards_and_columns(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_empty_task_kanban_view_fields
            )
