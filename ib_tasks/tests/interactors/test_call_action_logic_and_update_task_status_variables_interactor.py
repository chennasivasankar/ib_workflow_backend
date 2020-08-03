import pytest
from unittest.mock import create_autospec, patch, Mock
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.call_action_logic_function_and_update_task_status_variables_interactor \
    import (
    CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor,
    InvalidModulePathFound, InvalidMethodFound
)
from ib_tasks.tests.factories.storage_dtos import (
    FieldValueDTOFactory, StatusVariableDTOFactory,
    GroupOfFieldsDTOFactory, GOFMultipleStatusDTOFactory,
    TaskGoFFieldDTOFactory, TaskGoFDTOFactory
)


class TestUpdateTaskStatusVariablesInteractor:

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
    def test_given_invalid_path_raises_exception(task_gof_dtos):
        # Arrange
        task_id = 1
        action_id = 1
        storage = create_autospec(StorageInterface)
        GOFMultipleStatusDTOFactory.reset_sequence()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        TaskGoFFieldDTOFactory.reset_sequence(1)
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        path_name = "ib_tasks.populate.stage_ac.stage_1_action_name_1"
        storage.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage.get_status_variables_to_task.return_value = statuses
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_dto = TaskDetailsDTO(
            template_id="template_1",
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        interactor = CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor(
            storage=storage, action_id=action_id, task_id=task_id
        )

        # Act
        with pytest.raises(InvalidModulePathFound) as error:
            interactor \
                .call_action_logic_function_and_update_task_status_variables(
                    task_dto=task_dto
                )

        # Assert
        assert error.value.path_name == path_name
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )

    @staticmethod
    def test_given_invalid_method_name_raises_exception(mocker, task_gof_dtos):
        # Arrange
        task_id = 1
        action_id = 1
        storage = create_autospec(StorageInterface)
        GOFMultipleStatusDTOFactory.reset_sequence()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        TaskGoFFieldDTOFactory.reset_sequence(1)
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        path_name = "ib_tasks.populate.stage_actions_logic.stage_1_action_name_1"
        mock_obj = mocker.patch("importlib.import_module")
        mock_obj.side_effect = InvalidMethodFound(method_name="stage_1_action_name_1")
        storage.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage.get_status_variables_to_task.return_value = statuses
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_dto = TaskDetailsDTO(
            template_id="template_1",
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        interactor = CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor(
            storage=storage, action_id=action_id, task_id=task_id
        )

        # Act
        with pytest.raises(InvalidMethodFound) as error:
            interactor \
                .call_action_logic_function_and_update_task_status_variables(
                    task_dto=task_dto
                )

        # Assert
        assert error.value.method_name == "stage_1_action_name_1"
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )

    @staticmethod
    def test_access_invalid_key_raises_invalid_key_error(mocker, task_gof_dtos):
        # Arrange
        mock_task_dict = {'gof2': [{'field2': 'field_response2'}, {'field3': 'field_response3'}],
                          'gof1': {'field1': 'field_response1'},
                          'status_variables': {'status_variable_1': 'value_1'}}
        action_id = 1
        task_id = 1
        storage = create_autospec(StorageInterface)
        GOFMultipleStatusDTOFactory.reset_sequence()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        TaskGoFFieldDTOFactory.reset_sequence(1)
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_1"
        mock_obj = mocker.patch(path_name)

        storage.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage.get_status_variables_to_task.return_value = statuses
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_dto = TaskDetailsDTO(
            template_id="template_1",
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        interactor = CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor(
            storage=storage, action_id=action_id, task_id=task_id
        )
        from ib_tasks.exceptions.action_custom_exceptions import InvalidKeyError

        # Act
        with pytest.raises(InvalidKeyError):
            interactor\
                .call_action_logic_function_and_update_task_status_variables(
                    task_dto=task_dto
                )

        # Assert
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )
        mock_obj.assert_called_once_with(
            task_dict=mock_task_dict, global_constants={},
            stage_value_dict={}
        )
        storage.update_status_variables_to_task.assert_called_once_with(
            task_id=1, status_variables_dto=statuses
        )
        storage.get_global_constants_to_task\
            .assert_called_once_with(task_id=task_id)
        storage.get_stage_dtos_to_task\
            .assert_called_once_with(task_id=task_id)

    @staticmethod
    def test_given_valid_details_updates_statuses(mocker, task_gof_dtos):
        # Arrange
        mock_task_dict = {'gof1': {'field1': 'field_response1'},
                          'group_of_field_2': [{'field2': 'field_response2'},
                                               {'field3': 'field_response3'}],
                          'statuses': {'status_variable_1': 'value_1'}}
        action_id = 1
        task_id = 1
        storage = create_autospec(StorageInterface)
        GOFMultipleStatusDTOFactory.reset_sequence()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        TaskGoFFieldDTOFactory.reset_sequence(1)
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        path_name = "ib_tasks.populate.stage_actions_logic.stage_1_action_name_1"
        mock_obj = mocker.patch("importlib.import_module")
        mock_obj.stage_1_action_name_1.return_value = mock_task_dict
        storage.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage.get_status_variables_to_task.return_value = statuses
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_dto = TaskDetailsDTO(
            template_id="template_1",
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        interactor = CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor(
            storage=storage, action_id=action_id, task_id=task_id
        )

        # Act
        interactor\
            .call_action_logic_function_and_update_task_status_variables(
                task_dto=task_dto
            )

        # Assert
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )
        mock_obj.called_once()
        storage.update_status_variables_to_task.assert_called_once_with(
            task_id=1, status_variables_dto=statuses
        )
        storage.get_global_constants_to_task\
            .assert_called_once_with(task_id=task_id)
        storage.get_stage_dtos_to_task\
            .assert_called_once_with(task_id=task_id)
