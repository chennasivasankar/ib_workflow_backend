import pytest
from unittest.mock import create_autospec, patch, Mock
from ib_tasks.interactors.storage_interfaces.dtos import GOFMultipleStatusDTO
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.call_action_logic_function_and_update_task_status_variables_interactor \
    import (
    CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor,
    InvalidModulePathFound, InvalidMethodFound
)
from ib_tasks.tests.factories.storage_dtos import (
    FieldValueDTOFactory, StatusVariableDTOFactory,
    GroupOfFieldsDTOFactory, GOFMultipleStatusDTOFactory
)


class TestUpdateTaskStatusVariablesInteractor:

    @staticmethod
    def test_given_invalid_path_raises_exception():
        # Arrange
        action_id = "action_1"
        storage = create_autospec(StorageInterface)
        GOFMultipleStatusDTOFactory.reset_sequence()
        multiple_gof = GOFMultipleStatusDTOFactory()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        storage.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            multiple_gof, single_gof
        ]
        path_name = "ib_tasks.populate.stage_ac.stage_1_action_name_1"
        storage.get_path_name_to_action.return_value = path_name
        GroupOfFieldsDTOFactory.reset_sequence()
        FieldValueDTOFactory.reset_sequence()
        StatusVariableDTOFactory.reset_sequence()
        group_of_fields = GroupOfFieldsDTOFactory.create_batch(size=2)
        fields = FieldValueDTOFactory.create_batch(size=2)
        statuses = [StatusVariableDTOFactory()]
        from ib_tasks.interactors.dtos import TaskGofAndStatusesDTO
        task_dto = TaskGofAndStatusesDTO(
            task_id="task_1",
            group_of_fields_dto=group_of_fields,
            fields_dto=fields,
            statuses_dto=statuses
        )
        interactor = CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor(
            storage=storage, action_id=action_id
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
    def test_given_invalid_method_name_raises_exception(mocker):
        # Arrange
        action_id = "action_1"
        storage = create_autospec(StorageInterface)
        GOFMultipleStatusDTOFactory.reset_sequence()
        multiple_gof = GOFMultipleStatusDTOFactory()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        storage.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            multiple_gof, single_gof
        ]
        path_name = "ib_tasks.populate.stage_actions_logic.stage_1_action_name_1"
        mock_obj = mocker.patch("importlib.import_module")
        mock_obj.side_effect = InvalidMethodFound(method_name="stage_1_action_name_1")
        storage.get_path_name_to_action.return_value = path_name
        GroupOfFieldsDTOFactory.reset_sequence()
        FieldValueDTOFactory.reset_sequence()
        StatusVariableDTOFactory.reset_sequence()
        group_of_fields = GroupOfFieldsDTOFactory.create_batch(size=2)
        fields = FieldValueDTOFactory.create_batch(size=2)
        statuses = [StatusVariableDTOFactory()]
        from ib_tasks.interactors.dtos import TaskGofAndStatusesDTO
        task_dto = TaskGofAndStatusesDTO(
            task_id="task_1",
            group_of_fields_dto=group_of_fields,
            fields_dto=fields,
            statuses_dto=statuses
        )
        interactor = CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor(
            storage=storage, action_id=action_id
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
    def test_given_valid_details_updates_statuses(mocker):
        # Arrange
        mock_task_dict = {'group_of_field_1': [{'field_1': 'value_1'}],
                          'group_of_field_2': {'field_2': 'value_2'},
                          'statuses': {'status_variable_1': 'value_1'}}
        action_id = "action_1"
        stage_ids = ['value_1']
        storage = create_autospec(StorageInterface)
        GOFMultipleStatusDTOFactory.reset_sequence()
        multiple_gof = GOFMultipleStatusDTOFactory()
        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        storage.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            multiple_gof, single_gof
        ]
        path_name = "ib_tasks.populate.stage_actions_logic.stage_1_action_name_1"
        mock_obj = mocker.patch("importlib.import_module")
        mock_obj.stage_1_action_name_1.return_value = mock_task_dict
        storage.get_path_name_to_action.return_value = path_name
        GroupOfFieldsDTOFactory.reset_sequence()
        FieldValueDTOFactory.reset_sequence()
        StatusVariableDTOFactory.reset_sequence()
        group_of_fields = GroupOfFieldsDTOFactory.create_batch(size=2)
        fields = FieldValueDTOFactory.create_batch(size=2)
        statuses = [StatusVariableDTOFactory()]
        from ib_tasks.interactors.dtos import TaskGofAndStatusesDTO
        task_dto = TaskGofAndStatusesDTO(
            task_id="task_1",
            group_of_fields_dto=group_of_fields,
            fields_dto=fields,
            statuses_dto=statuses
        )
        interactor = CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor(
            storage=storage, action_id=action_id
        )

        # Act
        response = interactor.call_action_logic_function_and_update_task_status_variables(
            task_dto=task_dto
        )

        # Assert
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )
        mock_obj.called_once()
        storage.update_status_variables_to_task.assert_called_once_with(
            task_id="task_1", status_variables_dto=statuses
        )
        # assert response == stage_ids
