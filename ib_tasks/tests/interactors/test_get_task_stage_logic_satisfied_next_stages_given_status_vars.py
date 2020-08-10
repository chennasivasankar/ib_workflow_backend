import pytest


class TestGetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor:

    @staticmethod
    @pytest.fixture()
    def storage_mock():
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
            StageDisplayValueDTOFactory(),
            StageDisplayValueDTOFactory()
        ]
        return stage_values

    @staticmethod
    @pytest.fixture()
    def stage_mixed_value():
        from ib_tasks.tests.factories.storage_dtos \
            import StageDisplayValueDTOFactory
        StageDisplayValueDTOFactory.reset_sequence(0)
        stage_values = [
            StageDisplayValueDTOFactory(),
            StageDisplayValueDTOFactory(
                display_logic='value[variable_2]>=value[stage_2]'),
            StageDisplayValueDTOFactory(
                display_logic='value[variable_3]<=value[stage_1]')
        ]
        return stage_values

    @staticmethod
    @pytest.fixture()
    def status_variable_dtos():
        from ib_tasks.tests.factories.storage_dtos import \
            StatusVariableDTOFactory

        StatusVariableDTOFactory.reset_sequence()
        status_variable_dtos = StatusVariableDTOFactory.create_batch(3)
        return status_variable_dtos

    @pytest.fixture
    def status_stage_dtos(self):
        from ib_tasks.tests.factories.interactor_dtos \
            import StatusOperandStageDTOFactory
        StatusOperandStageDTOFactory.reset_sequence()
        status_stage_dtos = StatusOperandStageDTOFactory.create_batch(3)
        return status_stage_dtos

    @staticmethod
    def stage_display_mock(mocker):
        path = 'ib_tasks.interactors.get_stage_display_logic_interactor.' \
               'StageDisplayLogicInteractor.get_stage_display_logic_condition'
        mock_obj = mocker.patch(path)
        return mock_obj

    def test_given_invalid_task_raises_exception(self, storage_mock,
                                                 status_variable_dtos):
        # Arrange

        task_id = 1

        storage_mock.validate_task_id.return_value = False

        from ib_tasks.interactors. \
            get_task_stage_logic_satisfied_next_stages_given_status_vars \
            import \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor

        interactor = \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor(
                storage=storage_mock)

        # Act
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskException
        with pytest.raises(InvalidTaskException) as err:
            interactor.get_task_stage_logic_satisfied_next_stages(
                task_id=task_id, status_variable_dtos=status_variable_dtos)

        # Assert
        assert err.value.task_id == task_id

    def test_given_variable_stage_returns_all_stage_ids(
            self, storage_mock, status_variable_dtos, mocker,
            stage_display_value, status_stage_dtos):
        # Arrange
        task_id = 1
        storage_mock.get_task_template_stage_logic_to_task \
            .return_value = stage_display_value
        storage_mock.validate_task_id.return_value = True

        mock_obj = self.stage_display_mock(mocker)
        mock_obj.return_value = status_stage_dtos

        from ib_tasks.interactors. \
            get_task_stage_logic_satisfied_next_stages_given_status_vars \
            import \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor

        interactor = \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor(
                storage=storage_mock)
        # Act
        response = interactor.get_task_stage_logic_satisfied_next_stages(
            task_id=task_id, status_variable_dtos=status_variable_dtos)

        # Assert
        assert response == ['stage_1', 'stage_2', 'stage_3']

    def test_given_variable_stage_returns_empty_stages(
            self, storage_mock, mocker, stage_display_value,
            status_stage_dtos):
        # Arrange

        task_id = 1
        storage_mock.get_task_template_stage_logic_to_task \
            .return_value = stage_display_value
        storage_mock.validate_task_id.return_value = True
        mock_obj = self.stage_display_mock(mocker)
        mock_obj.return_value = status_stage_dtos
        from ib_tasks.tests.factories.storage_dtos \
            import StatusVariableDTOFactory
        StatusVariableDTOFactory.reset_sequence()
        status_variable_dtos = [
            StatusVariableDTOFactory(value='stage_2'),
            StatusVariableDTOFactory(value='stage_3'),
            StatusVariableDTOFactory(value='stage_1')
        ]

        from ib_tasks.interactors. \
            get_task_stage_logic_satisfied_next_stages_given_status_vars \
            import \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor

        interactor = \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor(
                storage=storage_mock)

        # Act
        response = interactor.get_task_stage_logic_satisfied_next_stages(
            task_id=task_id, status_variable_dtos=status_variable_dtos)

        # Assert
        assert response == []

    def test_given_variable_stage_returns_mixed_stages(
            self, storage_mock, mocker, stage_mixed_value,
            status_variable_dtos):
        # Arrange
        task_id = 1
        storage_mock.get_task_template_stage_logic_to_task \
            .return_value = stage_mixed_value
        storage_mock.validate_task_id.return_value = True
        from ib_tasks.tests.factories.interactor_dtos \
            import StatusOperandStageDTOFactory
        StatusOperandStageDTOFactory.reset_sequence()
        status_stage_dtos = [
            StatusOperandStageDTOFactory(),
            StatusOperandStageDTOFactory(operator=">="),
            StatusOperandStageDTOFactory(operator="<=", stage='stage_1')
        ]
        mock_obj = self.stage_display_mock(mocker)
        mock_obj.return_value = status_stage_dtos
        from ib_tasks.interactors. \
            get_task_stage_logic_satisfied_next_stages_given_status_vars \
            import \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor

        interactor = \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor(
                storage=storage_mock)

        # Act
        response = interactor.get_task_stage_logic_satisfied_next_stages(
            task_id=task_id, status_variable_dtos=status_variable_dtos)

        # Assert
        assert response == ['stage_1', 'stage_2']
