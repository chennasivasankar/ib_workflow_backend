"""
Created on: 17/07/20
Author: Pavankumar Pamuru

"""

from ib_tasks.interactors.user_action_on_task.get_stage_display_logic_interactor import \
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
        from ib_tasks.tests.factories.interactor_dtos \
            import StageDisplayLogicDTOFactory
        StageDisplayLogicDTOFactory.reset_sequence()
        expected_response = StageDisplayLogicDTOFactory.create_batch(3)
        from ib_tasks.tests.factories.storage_dtos import StageDisplayDTOFactory
        StageDisplayDTOFactory.reset_sequence()
        stage_display_dtos = StageDisplayDTOFactory.create_batch(3)
        interactor = StageDisplayLogicInteractor()

        # Act
        actual_response = interactor.get_stage_display_logic_condition(
            stage_display_dtos=stage_display_dtos
        )

        # Assert
        assert actual_response == expected_response

    def test_with_valid_stage_ids_return_all_indirect_task_status_dtos(
            self):
        # Arrange

        from ib_tasks.tests.factories.interactor_dtos \
            import StatusOperandStageDTOFactory
        StatusOperandStageDTOFactory.reset_sequence()

        from ib_tasks.tests.factories.interactor_dtos \
            import StageDisplayLogicDTOFactory
        StageDisplayLogicDTOFactory.reset_sequence()
        expected_response = [
            StageDisplayLogicDTOFactory(display_logic_dto=StatusOperandStageDTOFactory(operator='>=')),
            StageDisplayLogicDTOFactory(display_logic_dto=StatusOperandStageDTOFactory(operator='<=')),
            StageDisplayLogicDTOFactory(display_logic_dto=StatusOperandStageDTOFactory(operator='!='))
        ]
        from ib_tasks.tests.factories.storage_dtos import StageDisplayDTOFactory
        StageDisplayDTOFactory.reset_sequence()
        stage_display_logics = [
            StageDisplayDTOFactory(display_value="value[variable_1] >= value[stage_1]"),
            StageDisplayDTOFactory(display_value="value[variable_2] <= value[stage_2]"),
            StageDisplayDTOFactory(display_value="value[variable_3] != value[stage_3]")
        ]
        interactor = StageDisplayLogicInteractor()

        # Act
        actual_response = interactor.get_stage_display_logic_condition(
            stage_display_dtos=stage_display_logics
        )

        # Assert
        assert actual_response == expected_response

    def test_with_valid_stage_ids_return_mixed_task_status_dtos(
            self):
        # Arrange

        from ib_tasks.tests.factories.interactor_dtos \
            import StatusOperandStageDTOFactory
        StatusOperandStageDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos \
            import StageDisplayLogicDTOFactory
        StageDisplayLogicDTOFactory.reset_sequence()
        expected_response = [
            StageDisplayLogicDTOFactory(display_logic_dto=StatusOperandStageDTOFactory()),
            StageDisplayLogicDTOFactory(display_logic_dto=StatusOperandStageDTOFactory(operator='<=')),
            StageDisplayLogicDTOFactory(display_logic_dto=StatusOperandStageDTOFactory(operator='!='))
        ]
        from ib_tasks.tests.factories.storage_dtos import StageDisplayDTOFactory
        StageDisplayDTOFactory.reset_sequence()
        stage_display_logics = [
            StageDisplayDTOFactory(display_value="variable_1 == stage_1"),
            StageDisplayDTOFactory(display_value="value[variable_2] <= value[stage_2]"),
            StageDisplayDTOFactory(display_value="value[variable_3] != value[stage_3]")
        ]
        interactor = StageDisplayLogicInteractor()

        # Act
        actual_response = interactor.get_stage_display_logic_condition(
            stage_display_dtos=stage_display_logics
        )

        # Assert
        assert actual_response == expected_response
