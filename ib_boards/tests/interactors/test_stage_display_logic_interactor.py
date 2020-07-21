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

    @classmethod
    def setup_class(cls):
        from ib_boards.tests.factories.interactor_dtos import \
            TaskStatusDTOFactory
        TaskStatusDTOFactory.reset_sequence()

    def test_with_valid_stage_ids_return_task_status_dtos(
            self, presenter_mock, mocker):
        # Arrange
        from ib_boards.tests.factories.interactor_dtos import \
            TaskStatusDTOFactory
        task_status_dtos = TaskStatusDTOFactory.create_batch(2)
        stage_display_logics = [
            "STATUS_ID_1 == STAGE_ID_1",
            "STATUS_ID_2 == STAGE_ID_2"
        ]
        expected_response = Mock()
        interactor = StageDisplayLogicInteractor()
        presenter_mock.get_response_for_stage_display_logic.\
            return_value = expected_response



        # Act
        actual_response = interactor.get_stage_display_logic_condition_wrapper(
            stage_display_logics=stage_display_logics, presenter=presenter_mock
        )

        # Assert
        assert actual_response == expected_response
        print("task_status_dtos: ", task_status_dtos)
        presenter_mock.get_response_for_stage_display_logic.assert_called_once_with(
            task_status_dtos=task_status_dtos
        )