import pytest
from mock import create_autospec

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.interactors.user_action_on_task. \
    call_action_logic_function_and_get_or_update_task_status_variables_interactor \
    import \
    CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor, \
    InvalidModulePathFound, InvalidMethodFound
from ib_tasks.tests.factories.storage_dtos import StatusVariableDTOFactory, \
    TaskDetailsDTOFactory, TaskGoFDTOFactory, \
    TaskGoFFieldDTOFactory, GOFMultipleStatusDTOFactory, FieldTypeDTOFactory, \
    StageDisplayValueDTOFactory, TaskBaseDetailsDTOFactory


class TestCallActionLogicFunctionAndGetTaskStatusVariablesInteractor:
    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskDetailsDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence(1)
        GOFMultipleStatusDTOFactory.reset_sequence()
        FieldTypeDTOFactory.reset_sequence(1)
        StatusVariableDTOFactory.reset_sequence()
        TaskGoFDTOFactory.reset_sequence()
        StageDisplayValueDTOFactory.reset_sequence(0)
        TaskBaseDetailsDTOFactory.reset_sequence()

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        storage = create_autospec(
            StorageInterface)
        return storage

    @pytest.fixture
    def create_task_storage(self):
        from ib_tasks.interactors.storage_interfaces.\
            create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        storage = create_autospec(CreateOrUpdateTaskStorageInterface)
        return storage

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        task_storage = create_autospec(
            TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.action_storage_interface \
            import ActionStorageInterface
        action_storage = create_autospec(
            ActionStorageInterface)
        return action_storage

    @pytest.fixture
    def field_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface \
            import FieldsStorageInterface
        field_storage = create_autospec(FieldsStorageInterface)
        return field_storage

    @pytest.fixture
    def gof_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import GoFStorageInterface
        gof_storage = create_autospec(GoFStorageInterface)
        return gof_storage

    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface \
            import StageStorageInterface
        stage_storage = create_autospec(StageStorageInterface)
        return stage_storage

    @staticmethod
    def stage_display_mock(mocker):
        path = \
            'ib_tasks.interactors.' \
            'get_stage_display_logic_interactor.StageDisplayLogicInteractor' \
            '.get_stage_display_logic_condition'
        mock_obj = mocker.patch(path)
        return mock_obj

    @pytest.fixture()
    def task_gof_dtos(self):
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

    def test_assert_called_with_expected_arguments(
            self, mocker, storage_mock, action_storage_mock, task_storage_mock,
            create_task_storage, task_gof_dtos, field_storage_mock,
            stage_storage_mock, gof_storage_mock):
        # Arrange
        template_id = "template_0"
        field_ids = ["field1", "field2", "field3"]
        mock_task_dict = {
            'gof2': [
                {'field2': 'field_response2'},
                {'field3': 'field_response3'}],
                'gof1': {'field1': 'field_response1'},
                'status_variables': {'variable_1': 'stage_1'}}
        action_id = 1
        task_id = 1
        path_name = \
            "ib_tasks.tests.populate.stage_actions_logic.stage_1_action_name_1"
        stage_action_logic_mock_obj = mocker.patch(path_name)

        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        multiple_gof = GOFMultipleStatusDTOFactory()
        gof_storage_mock.\
            get_enable_multiple_gofs_field_to_gof_ids.return_value = [
                single_gof, multiple_gof
            ]
        field_type_dtos = FieldTypeDTOFactory.create_batch(size=3)
        field_storage_mock.get_field_type_dtos.return_value = \
            field_type_dtos
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        get_task_mock_obj = self.gof_and_fields_mock(mocker, task_dto)

        action_storage_mock.get_action_logic_to_action.return_value = path_name
        statuses = [StatusVariableDTOFactory()]
        task_storage_mock.get_status_variables_to_task.return_value = statuses
        interactor = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                storage=storage_mock, create_task_storage=create_task_storage,
                action_id=action_id, task_id=task_id,
                task_storage=task_storage_mock,
                field_storage=field_storage_mock,
                action_storage=action_storage_mock,
                stage_storage=stage_storage_mock, gof_storage=gof_storage_mock
            )

        # Act
        interactor \
            .call_action_logic_function_and_get_status_variables_dtos_of_task()

        # Assert
        gof_storage_mock.get_enable_multiple_gofs_field_to_gof_ids. \
            assert_called_once_with(template_id=template_id)
        field_storage_mock.get_field_type_dtos.assert_called_once_with(
            field_ids=field_ids
        )
        get_task_mock_obj.assert_called_once_with(task_id=task_id)
        action_storage_mock.get_action_logic_to_action.assert_called_once_with(
            action_id=action_id)
        task_storage_mock.get_status_variables_to_task.assert_called_once_with(
            task_id=task_id)
        stage_action_logic_mock_obj.assert_called_once_with(
            task_dict=mock_task_dict,
            global_constants={}, stage_value_dict={})

    def test_given_invalid_path_raises_exception(
            self, mocker, storage_mock, action_storage_mock, task_storage_mock,
            create_task_storage, task_gof_dtos, field_storage_mock,
            stage_storage_mock, gof_storage_mock):
        # Arrange
        template_id = "template_0"
        field_ids = ["field1", "field2", "field3"]
        task_id = 1
        action_id = 1
        path_name = "ib_tasks.populate.stage_ac.stage_1_action_name_1"
        action_storage_mock.get_action_logic_to_action.return_value = path_name
        statuses = [StatusVariableDTOFactory()]

        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        multiple_gof = GOFMultipleStatusDTOFactory()
        gof_storage_mock.\
            get_enable_multiple_gofs_field_to_gof_ids.return_value = [
                single_gof, multiple_gof]
        field_type_dtos = FieldTypeDTOFactory.create_batch(
            size=3, field_type=FieldTypes.PLAIN_TEXT.value)
        field_storage_mock.get_field_type_dtos.return_value = \
            field_type_dtos
        task_storage_mock.get_status_variables_to_task.return_value = statuses

        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )

        self.gof_and_fields_mock(mocker, task_dto)
        interactor = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                storage=storage_mock, create_task_storage=create_task_storage,
                action_id=action_id, task_id=task_id,
                task_storage=task_storage_mock,
                field_storage=field_storage_mock,
                action_storage=action_storage_mock,
                stage_storage=stage_storage_mock, gof_storage=gof_storage_mock
            )

        # Assert
        with pytest.raises(InvalidModulePathFound) as error:
            interactor \
                .call_action_logic_function_and_get_status_variables_dtos_of_task()

        assert error.value.path_name == path_name
        action_storage_mock.get_action_logic_to_action.assert_called_once_with(
            action_id=action_id)
        gof_storage_mock.get_enable_multiple_gofs_field_to_gof_ids. \
            assert_called_once_with(template_id=template_id)
        field_storage_mock.get_field_type_dtos.assert_called_once_with(
            field_ids=field_ids
        )
        task_storage_mock.get_status_variables_to_task.assert_called_once_with(
            task_id=task_id)

    def test_given_invalid_method_name_raises_exception(
            self, mocker, storage_mock, action_storage_mock, task_storage_mock,
            create_task_storage, task_gof_dtos, field_storage_mock,
            stage_storage_mock, gof_storage_mock):
        # Arrange
        template_id = "template_0"
        field_ids = ["field1", "field2", "field3"]
        task_id = 1
        action_id = 1

        path_name = \
            "ib_tasks.tests.populate.stage_actions_logic.stage_1_action_name_1"
        mock_obj = mocker.patch("importlib.import_module")
        mock_obj.side_effect = InvalidMethodFound(
            method_name="stage_1_action_name_1")
        action_storage_mock.get_action_logic_to_action.return_value = path_name

        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage_mock.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]

        statuses = [StatusVariableDTOFactory()]

        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        task_storage_mock.get_status_variables_to_task.return_value = statuses
        field_type_dtos = FieldTypeDTOFactory.create_batch(
            size=3, field_type=FieldTypes.PLAIN_TEXT.value)
        field_storage_mock.get_field_type_dtos.return_value = \
            field_type_dtos

        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        self.gof_and_fields_mock(mocker, task_dto)

        interactor = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                storage=storage_mock, create_task_storage=create_task_storage,
                action_id=action_id, task_id=task_id,
                task_storage=task_storage_mock,
                field_storage=field_storage_mock,
                action_storage=action_storage_mock,
                stage_storage=stage_storage_mock, gof_storage=gof_storage_mock
            )

        # Assert
        with pytest.raises(InvalidMethodFound) as error:
            interactor \
                .call_action_logic_function_and_get_status_variables_dtos_of_task()

        assert error.value.method_name == "stage_1_action_name_1"
        action_storage_mock.get_action_logic_to_action.assert_called_once_with(
            action_id=action_id)

        gof_storage_mock.get_enable_multiple_gofs_field_to_gof_ids. \
            assert_called_once_with(template_id=template_id)
        field_storage_mock.get_field_type_dtos.assert_called_once_with(
            field_ids=field_ids
        )
        action_storage_mock.get_action_logic_to_action.assert_called_once_with(
            action_id=action_id)
        task_storage_mock.get_status_variables_to_task.assert_called_once_with(
            task_id=task_id)

    def test_access_invalid_key_raises_invalid_key_error(
            self, mocker, storage_mock, action_storage_mock, task_storage_mock,
            create_task_storage, task_gof_dtos, field_storage_mock,
            stage_storage_mock, gof_storage_mock):
        # Arrange
        template_id = "template_0"
        field_ids = ["field1", "field2", "field3"]
        action_id = 1
        task_id = 1

        path_name = \
            "ib_tasks.tests.interactors." \
            "call_action_logic_testing_file.stage_1_action_name_1"
        action_storage_mock.get_action_logic_to_action.return_value = path_name

        statuses = [StatusVariableDTOFactory(status_variable="variable0")]
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        multiple_gof = GOFMultipleStatusDTOFactory()
        gof_storage_mock.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        field_type_dtos = FieldTypeDTOFactory.create_batch(
            size=3, field_type=FieldTypes.PLAIN_TEXT.value)
        field_storage_mock.get_field_type_dtos.return_value = \
            field_type_dtos
        task_storage_mock.get_status_variables_to_task.return_value = statuses
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        self.gof_and_fields_mock(mocker, task_dto)
        interactor = \
            CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
                storage=storage_mock, create_task_storage=create_task_storage,
                action_id=action_id, task_id=task_id,
                task_storage=task_storage_mock,
                field_storage=field_storage_mock,
                action_storage=action_storage_mock,
                stage_storage=stage_storage_mock, gof_storage=gof_storage_mock
            )

        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidKeyError

        # Assert
        with pytest.raises(InvalidKeyError):
            interactor \
                .call_action_logic_function_and_get_status_variables_dtos_of_task()

        gof_storage_mock.get_enable_multiple_gofs_field_to_gof_ids. \
            assert_called_once_with(template_id=template_id)
        field_storage_mock.get_field_type_dtos.assert_called_once_with(
            field_ids=field_ids
        )
        action_storage_mock.get_action_logic_to_action.assert_called_once_with(
            action_id=action_id)
        task_storage_mock.get_status_variables_to_task.assert_called_once_with(
            task_id=task_id)
