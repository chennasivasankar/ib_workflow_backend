import pytest
from mock import create_autospec

from ib_tasks.interactors.call_action_logic_function_and_get_or_update_task_status_variables_interactor import \
    CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor, \
    InvalidModulePathFound, InvalidMethodFound
from ib_tasks.tests.factories.storage_dtos import StatusVariableDTOFactory, \
    TaskDetailsDTOFactory, TaskGoFDTOFactory, \
    TaskGoFFieldDTOFactory, GOFMultipleStatusDTOFactory


class TestCallActionLogicFunctionAndGetTaskStatusVariablesInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        storage = create_autospec(
            StorageInterface)
        return storage

    @pytest.fixture
    def create_task_storage(self):
        from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        storage = create_autospec(CreateOrUpdateTaskStorageInterface)
        return storage

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
            TaskStorageInterface
        task_storage = create_autospec(
            TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
            ActionStorageInterface
        action_storage = create_autospec(
            ActionStorageInterface)
        return action_storage

    @staticmethod
    def stage_display_mock(mocker):
        path = 'ib_tasks.interactors.get_stage_display_logic_interactor.StageDisplayLogicInteractor' \
               '.get_stage_display_logic_condition'
        mock_obj = mocker.patch(path)
        return mock_obj

    @pytest.fixture()
    def task_gof_dtos(self):
        TaskGoFDTOFactory.reset_sequence()
        task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=1),
            TaskGoFDTOFactory(task_gof_id=2, gof_id="gof2", same_gof_order=1),
            TaskGoFDTOFactory(task_gof_id=3, gof_id="gof2", same_gof_order=2),
        ]
        return task_gof_dtos

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
    def gof_and_fields_mock(mocker, task_dto):
        path = 'ib_tasks.interactors.get_task_base_interactor' \
               '.GetTaskBaseInteractor.get_task'

        mock_obj = mocker.patch(path)
        mock_obj.return_value = task_dto
        return mock_obj

    def test_assert_called_with_expected_arguments(self, mocker, storage_mock,
                                                   action_storage_mock,
                                                   task_storage_mock,
                                                   create_task_storage,
                                                   task_gof_dtos):
        # Arrange
        mock_task_dict = {'gof2': [{'field2': 'field_response2'},
                                   {'field3': 'field_response3'}],
                          'gof1': {'field1': 'field_response1'},
                          'status_variables': {'variable_1': 'stage_1'}}
        action_id = 1
        task_id = 1
        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_1"
        mock_obj = mocker.patch(path_name)
        TaskDetailsDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence(1)
        GOFMultipleStatusDTOFactory.reset_sequence()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage_mock.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        self.gof_and_fields_mock(mocker, task_dto)

        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage_mock.get_status_variables_to_task.return_value = statuses
        interactor = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                storage=storage_mock, create_task_storage=create_task_storage,
                action_id=action_id, task_id=task_id)

        # Act
        interactor \
            .call_action_logic_function_and_get_status_variables_dtos_of_task()

        # Assert
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id)
        mock_obj.assert_called_once_with(
            task_dict=mock_task_dict, global_constants={},
            stage_value_dict={})
        storage_mock.get_global_constants_to_task \
            .assert_called_once_with(task_id=task_id)
        storage_mock.get_stage_dtos_to_task \
            .assert_called_once_with(task_id=task_id)

    def test_given_invalid_path_raises_exception(self, mocker, storage_mock,
                                                 task_storage_mock,
                                                 action_storage_mock,
                                                 create_task_storage,
                                                 task_gof_dtos):
        # Arrange
        task_id = 1
        action_id = 1
        path_name = "ib_tasks.populate.stage_ac.stage_1_action_name_1"
        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        GOFMultipleStatusDTOFactory.reset_sequence()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage_mock.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        storage_mock.get_status_variables_to_task.return_value = statuses
        TaskDetailsDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence(1)
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        self.gof_and_fields_mock(mocker, task_dto)
        interactor = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                storage=storage_mock, create_task_storage=create_task_storage,
                action_id=action_id, task_id=task_id)

        # Act
        with pytest.raises(InvalidModulePathFound) as error:
            interactor \
                .call_action_logic_function_and_get_status_variables_dtos_of_task()

        # Assert
        assert error.value.path_name == path_name
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id)

    def test_given_invalid_method_name_raises_exception(self, mocker,
                                                        storage_mock,
                                                        task_storage_mock,
                                                        action_storage_mock,
                                                        create_task_storage,
                                                        task_gof_dtos):
        # Arrange
        task_id = 1
        action_id = 1

        path_name = "ib_tasks.populate.stage_actions_logic.stage_1_action_name_1"
        mock_obj = mocker.patch("importlib.import_module")
        mock_obj.side_effect = InvalidMethodFound(
            method_name="stage_1_action_name_1")
        storage_mock.get_path_name_to_action.return_value = path_name
        GOFMultipleStatusDTOFactory.reset_sequence()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage_mock.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        TaskGoFFieldDTOFactory.reset_sequence(1)
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        storage_mock.get_status_variables_to_task.return_value = statuses
        TaskDetailsDTOFactory.reset_sequence()
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        self.gof_and_fields_mock(mocker, task_dto)

        interactor = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                storage=storage_mock, create_task_storage=create_task_storage,
                action_id=action_id, task_id=task_id)

        # Act
        with pytest.raises(InvalidMethodFound) as error:
            interactor \
                .call_action_logic_function_and_get_status_variables_dtos_of_task()

        # Assert
        assert error.value.method_name == "stage_1_action_name_1"
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id)

    def test_access_invalid_key_raises_invalid_key_error(self, mocker,
                                                         storage_mock,
                                                         action_storage_mock,
                                                         task_storage_mock,
                                                         create_task_storage,
                                                         task_gof_dtos):
        # Arrange
        action_id = 1
        task_id = 1

        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_1"

        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        GOFMultipleStatusDTOFactory.reset_sequence()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage_mock.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        storage_mock.get_status_variables_to_task.return_value = statuses
        TaskDetailsDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence(1)
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        self.gof_and_fields_mock(mocker, task_dto)
        interactor = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                storage=storage_mock, create_task_storage=create_task_storage,
                task_id=task_id, action_id=action_id)
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidKeyError

        # Act
        with pytest.raises(InvalidKeyError):
            interactor \
                .call_action_logic_function_and_get_status_variables_dtos_of_task()
        # Assert
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )
