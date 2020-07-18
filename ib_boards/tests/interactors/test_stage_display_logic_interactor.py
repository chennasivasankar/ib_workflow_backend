"""
Created on: 17/07/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock

import pytest

from ib_boards.interactors.get_stage_display_logic_interactor import \
    StageDisplayLogicInteractor


class TestStageDisplayLogic:

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_boards.interactors.presenter_interfaces.presenter_interface import \
            StageDisplayLogicPresenterInterface
        presenter = mock.create_autospec(StageDisplayLogicPresenterInterface)
        return presenter

    def test_with_invalid_stage_ids_return_error_message(
            self, presenter_mock, mocker):
        # Arrange

        stage_ids = ['STAGE_ID_1', 'STAGE_ID_1']
        expected_response = Mock()
        interactor = StageDisplayLogicInteractor()
        presenter_mock.get_response_for_invalid_stage_ids.\
            return_value = expected_response

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            validate_stage_ids_mock

        validate_stage_ids_mock = validate_stage_ids_mock(
            mocker=mocker, stage_ids=stage_ids
        )

        # Act
        actual_response = interactor.get_stage_display_logic_condition_wrapper(
            stage_display_logics=stage_display_logics, presenter=presenter_mock
        )

        # Assert
        assert actual_response == expected_response
        validate_stage_ids_mock.assert_called_once_with(
            stage_ids=stage_ids
        )
        call_args = presenter_mock.get_response_for_invalid_stage_ids.call_args

        assert call_args.kwargs['error'].stage_ids == stage_ids

    def test_with_valid_stage_ids_return_task_status_dtos(
            self, presenter_mock, mocker):
        # Arrange
        from ib_boards.tests.factories.interactor_dtos import \
            TaskStatusDTOFactory
        task_status_dtos = TaskStatusDTOFactory.create_batch(2)
        stage_display_logics = [
            "STATUS_ID_3 == STAGE_ID_3",
            "STATUS_ID_4 == STAGE_ID_4"
        ]
        expected_response = Mock()
        interactor = StageDisplayLogicInteractor()
        presenter_mock.get_response_for_stage_display_logic.\
            return_value = expected_response

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_stage_display_logics_mock

        stage_display_logic_mock = get_stage_display_logics_mock(
            mocker=mocker
        )

        # Act
        actual_response = interactor.get_stage_display_logic_condition_wrapper(
            stage_display_logics=stage_display_logics, presenter=presenter_mock
        )

        # Assert
        assert actual_response == expected_response
        stage_display_logic_mock.assert_called_once_with(
            stage_ids=stage_ids
        )
        presenter_mock.get_response_for_stage_display_logic.assert_called_once_with(
            task_status_dtos=task_status_dtos
        )