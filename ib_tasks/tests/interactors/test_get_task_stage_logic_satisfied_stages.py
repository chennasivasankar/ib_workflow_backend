import pytest


class TestGetTaskStageLogicSatisfiedStages:

    @staticmethod
    @pytest.fixture()
    def storage():
        from unittest.mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def stage_display_value():
        from ib_tasks.tests.factories.storage_dtos \
            import StageDisplayValueDTOFactory
        StageDisplayValueDTOFactory.reset_sequence(0)
        stage_values = [
            StageDisplayValueDTOFactory(),
            StageDisplayValueDTOFactory(
                display_logic='value[variable_2]>=value[stage_2]'
            )
        ]
        return stage_values

    def test_given_invalid_task_raises_exception(self, storage):

        # Arrange

        from ib_tasks.interactors.get_task_stage_logic_satisfied_stages \
            import GetTaskStageLogicSatisfiedStages
        task_id = 1

        storage.validate_task_id.return_value = False

        interactor = GetTaskStageLogicSatisfiedStages(
            task_id=task_id, storage=storage
        )
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskException

        # Act
        with pytest.raises(InvalidTaskException) as err:
            interactor.get_task_stage_logic_satisfied_stages()

        # Assert
        assert err.value.task_id == task_id

    def test_given_variable_stage_returns_stage_ids(
            self, storage, stage_display_value):

        # Arrange

        from ib_tasks.interactors.get_task_stage_logic_satisfied_stages \
            import GetTaskStageLogicSatisfiedStages
        task_id = 1
        storage.get_task_template_stage_logic_to_task\
            .return_value = stage_display_value
        storage.validate_task_id.return_value = True
        from ib_tasks.interactors.storage_interfaces.status_dtos \
            import StatusVariableDTO
        storage.get_status_variables_to_task.return_value = [
            StatusVariableDTO(
                status_id="1",
                status_variable='variable_1',
                value='stage_1'
            ),
            StatusVariableDTO(
                status_id="2",
                status_variable='variable_2',
                value='stage_2'
            )

        ]
        interactor = GetTaskStageLogicSatisfiedStages(
            task_id=task_id, storage=storage
        )

        # Act
        response = interactor.get_task_stage_logic_satisfied_stages()

        # Assert
        assert response == ['stage_1', 'stage_2']
