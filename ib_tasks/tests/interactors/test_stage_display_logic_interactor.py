"""
Created on: 17/07/20
Author: Pavankumar Pamuru

"""

import pytest

from ib_tasks.interactors.get_stage_display_logic_interactor import \
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
            self):
        # Arrange

        from ib_tasks.interactors.task_dtos import StatusOperandStageDTO
        expected_response = [
            StatusOperandStageDTO(
                variable="STATUS_ID_1", operator="==", stage="STAGE_ID_1"
            )
        ]
        stage_display_logics = [
            "STATUS_ID_1 == STAGE_ID_1"
        ]
        interactor = StageDisplayLogicInteractor()

        # Act
        actual_response = interactor.get_stage_display_logic_condition(
            stage_display_logics=stage_display_logics
        )

        # Assert
        assert actual_response == expected_response
