import pytest

from ib_tasks.tests.factories.interactor_dtos import (
    StageDisplayLogicDTOFactory, StatusOperandStageDTOFactory
)
from ib_tasks.tests.factories.storage_dtos import (
    StageDisplayValueDTOFactory, StatusVariableDTOFactory
)


class TestGetTaskStageLogicSatisfiedStages:

    @classmethod
    def setup_class(cls):
        StageDisplayValueDTOFactory.reset_sequence()
        StatusOperandStageDTOFactory.reset_sequence()
        StageDisplayLogicDTOFactory.reset_sequence()
        StatusVariableDTOFactory.reset_sequence()

    @staticmethod
    @pytest.fixture()
    def storage():
        from unittest.mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    def setup_storage(self, storage, operator, display_logic):
        self.setup_class()
        storage.validate_task_id.return_value = True
        status_variables_dtos = StatusVariableDTOFactory.create_batch(3)
        storage.get_status_variables_to_task.return_value = \
            status_variables_dtos
        stage_values = [
            StageDisplayValueDTOFactory(display_logic=display_logic)
        ]
        storage.get_task_template_stage_logic_to_task \
            .return_value = stage_values
        status_stage_dtos = [
            StageDisplayLogicDTOFactory(
                display_logic_dto=StatusOperandStageDTOFactory(operator=operator)
            )
        ]
        return status_stage_dtos

    @staticmethod
    @pytest.fixture()
    def stage_storage():
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
            StageStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(StageStorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def interactor(storage, stage_storage):
        task_id = 1

        from ib_tasks.interactors.get_task_stage_logic_satisfied_stages \
            import GetTaskStageLogicSatisfiedStagesInteractor
        interactor = GetTaskStageLogicSatisfiedStagesInteractor(
            task_id=task_id, storage=storage, stage_storage=stage_storage
        )
        return interactor

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
            StageDisplayValueDTOFactory(display_logic='value[variable_2]>=value[stage_2]'),
            StageDisplayValueDTOFactory(display_logic='value[variable_3]<=value[stage_1]')
        ]
        return stage_values

    @staticmethod
    @pytest.fixture()
    def stage_display_mock(mocker):

        path = 'ib_tasks.interactors.get_stage_display_logic_interactor.StageDisplayLogicInteractor' \
               '.get_stage_display_logic_condition'
        mock_obj = mocker.patch(path)
        return mock_obj

    def test_given_invalid_task_raises_exception(self, storage, interactor):

        # Arrange
        task_id = 1
        storage.validate_task_id.return_value = False
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskException

        # Act
        with pytest.raises(InvalidTaskException) as err:
            interactor.get_task_stage_logic_satisfied_stages()

        # Assert
        assert err.value.task_id == task_id

    def test_given_variable_stage_returns_all_stage_ids(
            self, storage, stage_display_value, interactor, stage_display_mock):

        # Arrange
        storage.get_task_template_stage_logic_to_task\
            .return_value = stage_display_value
        storage.validate_task_id.return_value = True
        status_stage_dtos = StageDisplayLogicDTOFactory.create_batch(3)
        stage_display_mock.return_value = status_stage_dtos
        status_variables_dtos = StatusVariableDTOFactory.create_batch(3)
        storage.get_status_variables_to_task.return_value = \
            status_variables_dtos

        # Act
        response = interactor.get_task_stage_logic_satisfied_stages()

        # Assert
        assert response == ['stage_1', 'stage_2', 'stage_3']

    def test_given_variable_stage_returns_empty_stages(
            self, storage, stage_display_mock, stage_display_value, interactor):

        # Arrange
        storage.get_task_template_stage_logic_to_task\
            .return_value = stage_display_value
        storage.validate_task_id.return_value = True
        status_stage_dtos = StageDisplayLogicDTOFactory.create_batch(3)
        stage_display_mock.return_value = status_stage_dtos
        status_variables_dtos = [
            StatusVariableDTOFactory(value='stage_2'),
            StatusVariableDTOFactory(value='stage_3'),
            StatusVariableDTOFactory(value='stage_1')
        ]
        storage.get_status_variables_to_task.return_value = \
            status_variables_dtos

        # Act
        response = interactor.get_task_stage_logic_satisfied_stages()

        # Assert
        assert response == []

    def test_given_variable_stage_returns_mixed_stages(
            self, storage, mocker, stage_mixed_value,
            interactor
    ):

        # Arrange
        storage.validate_task_id.return_value = True
        status_variables_dtos = StatusVariableDTOFactory.create_batch(3)
        storage.get_status_variables_to_task.return_value = \
            status_variables_dtos
        storage.get_task_template_stage_logic_to_task\
            .return_value = stage_mixed_value
        status_stage_dtos = [
            StageDisplayLogicDTOFactory(display_logic_dto=StatusOperandStageDTOFactory()),
            StageDisplayLogicDTOFactory(
                display_logic_dto=StatusOperandStageDTOFactory(operator=">=")),
            StageDisplayLogicDTOFactory(
                display_logic_dto=StatusOperandStageDTOFactory(operator="<=", stage='stage_1'))
        ]
        mock_obj = self.stage_display_mock(mocker)
        mock_obj.return_value = status_stage_dtos

        # Act
        response = interactor.get_task_stage_logic_satisfied_stages()

        # Assert
        assert response == ['stage_1', 'stage_2']

    @pytest.mark.parametrize(
        ("operator", "display_logic"),
        [
            ("==", "variable_1==stage_1"),
            (">=", "value[variable_1]>=value[stage_1]"),
            ("<=", "value[variable_1]<=value[stage_1]")
        ]
    )
    def test_given_variable_stage_returns_mixed_stages(
            self, operator, display_logic, storage,
            interactor, stage_display_mock
    ):

        # Arrange
        status_stage_dtos = self.setup_storage(storage, operator, display_logic)
        stage_display_mock.return_value = status_stage_dtos

        # Act
        response = interactor.get_task_stage_logic_satisfied_stages()

        # Assert
        assert response == ['stage_1']

    @pytest.mark.parametrize(
        ("operator", "display_logic"),
        [
            (">", "value[variable_1]>value[stage_1]"),
            ("<", "value[variable_1]<value[stage_1]")
        ]
    )
    def test_given_variable_stage_returns_mixed_stages(
            self, operator, display_logic, storage,
            interactor, stage_display_mock
    ):
        # Arrange
        status_stage_dtos = self.setup_storage(storage, operator, display_logic)
        stage_display_mock.return_value = status_stage_dtos

        # Act
        response = interactor.get_task_stage_logic_satisfied_stages()

        # Assert
        assert response == []