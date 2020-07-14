"""
Created on: 13/07/20
Author: Pavankumar Pamuru

"""
import json

import pytest

from ib_boards.interactors.populate_script_interactor import \
    PopulateScriptInteractor
from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory, \
    ColumnDTOFactory


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
    def column_dtos_with_invalid_task_template_stages(self):
        invalid_json = """
            {
                "FIN_PR": ["PR_PAYMENT_REQUEST_DRAFTS"],
            },
            {
                "FIN_PR": ["PR_PAYMENT_REQUEST_DRAFTS"],
            }
        """
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(task_template_stages=invalid_json)

        ]

    @pytest.fixture
    def column_dtos_with_empty_task_template_stages(self):
        task_template_stages = """
                    {
                        "FIN_PR": []
                    }
                """
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(task_template_stages=task_template_stages)
        ]

    @pytest.fixture
    def column_dtos_with_invalid_task_template_summary_fields(self):
        invalid_json = """
                {
                    "CardInfo_Requester": "Field Description"
                },
                {
                    "CardInfo_Requester": "Field Description"
                }
            """
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(task_summary_fields=invalid_json)

        ]

    @pytest.fixture
    def column_dtos_with_duplicate_task_template_stages(self):
        task_template_stages = """
                            {
                                "FIN_PR": [
                                    "PR_PAYMENT_REQUEST_DRAFTS", 
                                    "PR_PAYMENT_REQUEST_DRAFTS"
                                ]
                            }
                        """
        return [
            ColumnDTOFactory(),
            ColumnDTOFactory(task_template_stages=task_template_stages)
        ]

    @pytest.fixture
    def column_dtos_with_invalid_task_template_id(self):
        return ColumnDTOFactory.create_batch(3)

    def test_with_duplicate_board_ids_raise_exception(
            self, storage_mock, sequence_reset,
            board_dto_with_duplicate_ids, column_dtos):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import DuplicateBoardIds
        with pytest.raises(DuplicateBoardIds) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dto_with_duplicate_ids,
                column_dtos=column_dtos
            )

    def test_with_invalid_board_display_name_raise_exception(
            self, storage_mock, sequence_reset,
            board_dtos_with_no_display_name, column_dtos):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import InvalidBoardDisplayName
        with pytest.raises(InvalidBoardDisplayName) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos_with_no_display_name,
                column_dtos=column_dtos
            )

    def test_with_duplicate_column_ids_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_duplicate_ids, board_dtos):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            DuplicateColumnIds
        with pytest.raises(DuplicateColumnIds) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_duplicate_ids
            )

    def test_with_invalid_column_display_name_raise_exception(
            self, storage_mock, sequence_reset,
            column_dtos_with_no_display_name, board_dtos):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidColumnDisplayName
        with pytest.raises(InvalidColumnDisplayName) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_no_display_name
            )

    def test_with_invalid_task_template_stages_json_raises_exception(
            self,storage_mock, sequence_reset, board_dtos,
            column_dtos_with_invalid_task_template_stages):

        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidJsonForTaskTemplateStages
        with pytest.raises(InvalidJsonForTaskTemplateStages) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_stages
            )

    def test_with_invalid_task_template_id_in_stages_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id, mocker):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock

        adapter_mock = adapter_mock(mocker=mocker)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidTaskTemplateIdInStages
        with pytest.raises(InvalidTaskTemplateIdInStages) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )

    def test_with_invalid_task_template_fields_json_raises_exception(
            self,storage_mock, sequence_reset, board_dtos,
            column_dtos_with_invalid_task_template_summary_fields):

        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidJsonForTaskTemplateSummaryFields
        with pytest.raises(InvalidJsonForTaskTemplateSummaryFields) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_summary_fields
            )

    def test_with_invalid_task_template_id_in_fields_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_invalid_task_template_id, mocker):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock

        adapter_mock(mocker=mocker)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            InvalidTaskTemplateIdInStages
        with pytest.raises(InvalidTaskTemplateIdInStages) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_invalid_task_template_id
            )

    def test_with_empty_task_template_stages_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_empty_task_template_stages):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            EmptyValuesForTaskTemplateStages
        with pytest.raises(EmptyValuesForTaskTemplateStages) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_empty_task_template_stages
            )

    def test_with_duplicate_task_template_stages_raise_exception(
            self, storage_mock, board_dtos, sequence_reset,
            column_dtos_with_duplicate_task_template_stages, mocker):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )
        # Act
        from ib_boards.exceptions.custom_exceptions import \
            DuplicateStagesInTaskTemplateStages
        with pytest.raises(DuplicateStagesInTaskTemplateStages) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos,
                column_dtos=column_dtos_with_duplicate_task_template_stages
            )

    def test_with_task_template_stages_not_belongs_to_task_template_id(
            self, storage_mock, sequence_reset, board_dtos, column_dtos, mocker):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            adapter_mock_for_task_template_stages
        adapter_mock_for_task_template_stages(mocker)

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            TaskTemplateStagesNotBelongsToTastTemplateId
        with pytest.raises(TaskTemplateStagesNotBelongsToTastTemplateId) as error:
            assert interactor.populate_script_wrapper(
                board_dtos=board_dtos,
                column_dtos=column_dtos
            )

    def test_with_valid_data_creates_data(
            self, storage_mock, sequence_reset, board_dtos, column_dtos):
        # Arrange
        interactor = PopulateScriptInteractor(
            storage=storage_mock
        )

        # Act
        interactor.populate_script_wrapper(
            board_dtos=board_dtos,
            column_dtos=column_dtos
        )

        # Assert
        storage_mock.populate_data.assert_called_once_with(
            board_dtos=board_dtos,
            column_dtos=column_dtos
        )






