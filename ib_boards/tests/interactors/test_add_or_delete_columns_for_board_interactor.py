"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_boards.interactors.add_or_delete_columns_for_board_interactor import \
    AddOrDeleteColumnsForBoardInteractor
from ib_boards.tests.factories.interactor_dtos import ColumnDTOFactory, \
    TaskTemplateStagesDTOFactory, TaskSummaryFieldsDTOFactory


class TestAddOrDeleteColumnsForBoardInteractor:

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
        ColumnDTOFactory.reset_sequence()

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
        task_template_stages = TaskTemplateStagesDTOFactory.create_batch(2,
                                                                         stages=[])
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
    def column_dtos_with_invalid_task_template_id(self):
        return ColumnDTOFactory.create_batch(1)

    @pytest.fixture
    def column_dtos_with_invalid_user_roles(self):
        column_dto_1 = ColumnDTOFactory(user_role_ids=['USER', 'MEMBER'])
        column_dto_2 = ColumnDTOFactory()
        return [
            column_dto_1,
            column_dto_2
        ]

    @pytest.fixture
    def valid_column_dtos(self):
        return ColumnDTOFactory.create_batch(10)

    @pytest.fixture
    def task_summary_field_dtos(self):
        task_field_dtos_1 = TaskSummaryFieldsDTOFactory.create_batch(2)
        TaskSummaryFieldsDTOFactory.reset_sequence()
        task_field_dtos_2 = TaskSummaryFieldsDTOFactory.create_batch(2)
        TaskSummaryFieldsDTOFactory.reset_sequence()
        task_field_dtos_3 = TaskSummaryFieldsDTOFactory.create_batch(2)
        return task_field_dtos_1 + task_field_dtos_2 + task_field_dtos_3

    @pytest.fixture
    def task_template_stages_dtos(self):
        task_field_dtos_1 = TaskTemplateStagesDTOFactory.create_batch(2)
        TaskTemplateStagesDTOFactory.reset_sequence()
        task_field_dtos_2 = TaskTemplateStagesDTOFactory.create_batch(2)
        TaskTemplateStagesDTOFactory.reset_sequence()
        task_field_dtos_3 = TaskTemplateStagesDTOFactory.create_batch(2)
        return task_field_dtos_1 + task_field_dtos_2 + task_field_dtos_3

    @pytest.fixture
    def mock_valid_task_and_template_ids(self, mocker):
        task_template_ids = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        task_ids = [
            'TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3',
            'TASK_ID_4', 'TASK_ID_5',
            'TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3',
            'TASK_ID_4', 'TASK_ID_5',
        ]
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_valid_task_template_ids_mock
        get_valid_task_template_ids_mock(
            mocker=mocker,
            task_template_ids=task_template_ids
        )

    def test_with_duplicate_column_ids_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_duplicate_ids):
        # Arrange
        duplicate_column_ids = ['COLUMN_ID_1']
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            DuplicateColumnIds
        with pytest.raises(DuplicateColumnIds) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos_with_duplicate_ids
            )

        # Assert
        assert error.value.column_ids == duplicate_column_ids

    def test_with_invalid_column_display_name_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_no_display_name):
        # Arrange
        invalid_display_name_column_id = ['COLUMN_ID_1']
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidColumnDisplayName
        with pytest.raises(InvalidColumnDisplayName) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos_with_no_display_name
            )

        # Assert
        assert error.value.column_ids == invalid_display_name_column_id

    def test_with_invalid_task_template_id_in_stages_raise_exception(
            self, storage_mock, sequence_reset,
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
        interactor = AddOrDeleteColumnsForBoardInteractor(
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
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos_with_invalid_task_template_id
            )

        # Assert
        adapter_mock.assert_called_once_with(
            task_template_ids=task_template_ids
        )
        assert error.value.task_template_ids == invalid_task_template_ids

    def test_with_invalid_task_id_in_fields_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_invalid_task_template_id, mocker):
        # Arrange
        task_template_ids = [
            'TASK_TEMPLATE_ID_1', 'TASK_TEMPLATE_ID_2', 'TASK_TEMPLATE_ID_3',
            'TASK_TEMPLATE_ID_4', 'TASK_TEMPLATE_ID_5',
        ]
        invalid_task_ids = ['TASK_ID_4', 'TASK_ID_5']
        task_ids = [
            'TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3',
            'TASK_ID_4', 'TASK_ID_5',
        ]
        valid_task_ids = [
            'TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3'
        ]
        interactor = AddOrDeleteColumnsForBoardInteractor(
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
            InvalidTaskIdInSummaryFields
        with pytest.raises(InvalidTaskIdInSummaryFields) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos_with_invalid_task_template_id
            )

        # Assert
        assert error.value.task_ids == invalid_task_ids

    def test_with_empty_task_template_stages_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_empty_task_template_stages,
            mock_valid_task_and_template_ids):
        # Arrange
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            EmptyValuesForTaskTemplateStages
        with pytest.raises(EmptyValuesForTaskTemplateStages) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos_with_empty_task_template_stages
            )

    def test_with_duplicate_task_template_stages_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_duplicate_task_template_stages,
            mock_valid_task_and_template_ids):
        # Arrange
        duplicate_stages = ['PR_PAYMENT_REQUEST_DRAFTS']
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            DuplicateStagesInTaskTemplateStages
        with pytest.raises(DuplicateStagesInTaskTemplateStages) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos_with_duplicate_task_template_stages
            )

        # Assert
        assert error.value.duplicate_stages == duplicate_stages

    def test_with_task_template_stages_not_belongs_to_task_template_id(
            self, storage_mock, sequence_reset,
            column_dtos, task_template_stages_dtos, mocker,
            mock_valid_task_and_template_ids):
        # Arrange
        not_related_stages = task_template_stages_dtos
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock_for_task_template_stages
        adapter_mock = adapter_mock_for_task_template_stages(mocker)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            TaskTemplateStagesNotBelongsToTaskTemplateId
        with pytest.raises(
                TaskTemplateStagesNotBelongsToTaskTemplateId) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos
            )

    def test_with_task_summary_fields_not_belongs_to_task_template_id(
            self, storage_mock, sequence_reset,
            column_dtos, task_summary_field_dtos, mocker,
            mock_valid_task_and_template_ids):
        # Arrange
        not_related_fields = task_summary_field_dtos
        interactor = AddOrDeleteColumnsForBoardInteractor(
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
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos
            )

    def test_with_invalid_user_role_ids_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_invalid_user_roles, mocker,
            mock_valid_task_and_template_ids):
        # Arrange
        invalid_user_roles = ['ALL_ROLES', 'MEMBER', 'USER']
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.user_service import \
            adapter_mock

        adapter_mock = adapter_mock(mocker=mocker,
                                    user_roles=invalid_user_roles)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidUserRoles
        with pytest.raises(InvalidUserRoles) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos_with_invalid_user_roles
            )
        # Assert
        adapter_mock.assert_called_once_with(
            user_role_ids=invalid_user_roles
        )
        assert error.value.user_role_ids == invalid_user_roles

    def test_with_column_ids_are_assigned_to_multiple_boards(
            self, storage_mock, sequence_reset,
            column_dtos, mock_valid_task_and_template_ids):
        # Arrange
        column_ids = ['COLUMN_ID_1', 'COLUMN_ID_2', 'COLUMN_ID_3']
        storage_mock.get_board_ids_for_column_ids.return_value = ['BOARD_ID_1']
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            ColumnIdsAssignedToDifferentBoard
        with pytest.raises(ColumnIdsAssignedToDifferentBoard) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos
            )

        # Assert
        storage_mock.get_board_ids_for_column_ids.assert_called_once_with(
            column_ids=column_ids
        )
        assert error.value.column_ids == column_ids

    def test_with_update_and_create_and_delete_columns(
            self, storage_mock, sequence_reset, valid_column_dtos,
            mock_valid_task_and_template_ids):
        # Arrange
        board_ids = ['BOARD_ID_0']
        present_column_ids = ['COLUMN_ID_1', 'COLUMN_ID_2', 'COLUMN_ID_3']
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )
        storage_mock.get_boards_column_ids.return_value = present_column_ids
        storage_mock.get_board_ids_for_column_ids.return_value = []

        # Act
        interactor.add_or_delete_columns_for_board_wrapper(
            column_dtos=valid_column_dtos
        )

        # Assert
        storage_mock.get_boards_column_ids.assert_called_once_with(
            board_ids=board_ids
        )
        storage_mock.create_columns_for_board.assert_called_once_with(
            column_dtos=valid_column_dtos[3:]
        )
        storage_mock.update_columns_for_board(
            column_dtos=valid_column_dtos[:3]
        )
        storage_mock.delete_columns_which_are_not_in_configuration. \
            assert_called_once()

    def test_with_duplicate_task_summary_fields_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_duplicate_list_view_fields,
            mock_valid_task_and_template_ids):
        # Arrange
        duplicate_fields = ['Price']
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            DuplicateSummaryFieldsInTask
        with pytest.raises(DuplicateSummaryFieldsInTask) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos_with_duplicate_list_view_fields
            )

        # Assert
        assert error.value.duplicate_fields == duplicate_fields

    def test_with_empty_task_summary_fields_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_empty_task_list_view_fields,
            mock_valid_task_and_template_ids):
        # Arrange
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            EmptyValuesForTaskSummaryFields
        with pytest.raises(EmptyValuesForTaskSummaryFields) as error:
            assert interactor.add_or_delete_columns_for_board_wrapper(
                column_dtos=column_dtos_with_empty_task_list_view_fields
            )
