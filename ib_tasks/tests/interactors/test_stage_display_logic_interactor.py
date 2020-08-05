"""
Created on: 17/07/20
Author: Pavankumar Pamuru

"""

import pytest

from ib_tasks.interactors.get_stage_display_logic_interactor import \
    StageDisplayLogicInteractor


class TestStageDisplayLogic:

    @classmethod
    def setup_class(cls):
        pass

    def test_with_valid_stage_ids_return_all_direct_task_status_dtos(
            self):
        # Arrange

        from ib_tasks.tests.factories.interactor_dtos \
            import StatusOperandStageDTOFactory
        StatusOperandStageDTOFactory.reset_sequence()

        expected_response = StatusOperandStageDTOFactory.create_batch(3)
        stage_display_logics = [
            "variable_1 == stage_1", "variable_2 == stage_2",
            "variable_3 == stage_3"
        ]
        interactor = StageDisplayLogicInteractor()

        # Act
        actual_response = interactor.get_stage_display_logic_condition(
            stage_display_logics=stage_display_logics
        )

        # Assert
        assert actual_response == expected_response

    def test_with_valid_stage_ids_return_all_indirect_task_status_dtos(
            self):
        # Arrange

        from ib_tasks.tests.factories.interactor_dtos \
            import StatusOperandStageDTOFactory
        StatusOperandStageDTOFactory.reset_sequence()

        expected_response = [
            StatusOperandStageDTOFactory(operator='>='),
            StatusOperandStageDTOFactory(operator='<='),
            StatusOperandStageDTOFactory(operator='!=')
        ]
        stage_display_logics = [
            "value[variable_1] >= value[stage_1]",
            "value[variable_2] <= value[stage_2]",
            "value[variable_3] != value[stage_3]"
        ]
        interactor = StageDisplayLogicInteractor()

        # Act
        actual_response = interactor.get_stage_display_logic_condition(
            stage_display_logics=stage_display_logics
        )

        # Assert
        assert actual_response == expected_response

    def test_with_valid_stage_ids_return_mixed_task_status_dtos(
            self):
        # Arrange

        from ib_tasks.tests.factories.interactor_dtos \
            import StatusOperandStageDTOFactory
        StatusOperandStageDTOFactory.reset_sequence()

        expected_response = [
            StatusOperandStageDTOFactory(),
            StatusOperandStageDTOFactory(operator='<='),
            StatusOperandStageDTOFactory(operator='!=')
        ]
        stage_display_logics = [
            "variable_1 == stage_1",
            "value[variable_2] <= value[stage_2]",
            "value[variable_3] != value[stage_3]"
        ]
        interactor = StageDisplayLogicInteractor()

        # Act
        actual_response = interactor.get_stage_display_logic_condition(
            stage_display_logics=stage_display_logics
        )

        # Assert
        assert actual_response == expected_response
