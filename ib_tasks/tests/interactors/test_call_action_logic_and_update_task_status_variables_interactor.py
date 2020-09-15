from unittest.mock import create_autospec

import pytest

from ib_tasks.interactors.user_action_on_task\
    .call_action_logic_function_and_get_or_update_task_status_variables_interactor \
    import (
    CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor,
    InvalidModulePathFound, InvalidMethodFound
)
from ib_tasks.tests.factories.storage_dtos import (
    StatusVariableDTOFactory, GOFMultipleStatusDTOFactory,
    TaskGoFFieldDTOFactory, TaskGoFDTOFactory, TaskDetailsDTOFactory, FieldTypeDTOFactory
)
from ib_tasks.tests.interactors.super_storage_mock_class import StorageMockClass


class TestUpdateTaskStatusVariablesInteractor(StorageMockClass):

    @pytest.fixture()
    def task_gof_dtos(self):
        TaskGoFDTOFactory.reset_sequence()
        task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=1),
            TaskGoFDTOFactory(task_gof_id=2, gof_id="gof2", same_gof_order=1),
            TaskGoFDTOFactory(task_gof_id=3, gof_id="gof2", same_gof_order=2),
        ]
        return task_gof_dtos

    @pytest.fixture()
    def task_dto_mock(self, mocker):
        path = "ib_tasks.interactors.get_task_base_interactor.GetTaskBaseInteractor.get_task"
        return mocker.patch(path)

    @pytest.fixture()
    def single_task_gof_dtos(self):
        TaskGoFDTOFactory.reset_sequence()
        task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=1),
            TaskGoFDTOFactory(task_gof_id=2, gof_id="gof2", same_gof_order=1),
            TaskGoFDTOFactory(task_gof_id=3, gof_id="gof3", same_gof_order=1),
        ]
        return task_gof_dtos

    @pytest.fixture()
    def create_task_storage(self):
        from ib_tasks.interactors.storage_interfaces. \
            create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        create_task_storage = create_autospec(
            CreateOrUpdateTaskStorageInterface)
        return create_task_storage

    @staticmethod
    @pytest.fixture()
    def interactor(storage, create_task_storage, field_storage, gof_storage):
        task_id = 1
        action_id = 1
        interactor = CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor(
            storage=storage, action_id=action_id, task_id=task_id, gof_storage=gof_storage,
            create_task_storage=create_task_storage, field_storage=field_storage
        )
        return interactor

    @classmethod
    def setup(cls):
        GOFMultipleStatusDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence(1)
        StatusVariableDTOFactory.reset_sequence()
        TaskDetailsDTOFactory.reset_sequence()
        StatusVariableDTOFactory.reset_sequence()
        FieldTypeDTOFactory.reset_sequence(1)

    @staticmethod
    @pytest.fixture()
    def set_up_storage(storage, field_storage):

        single_gof = GOFMultipleStatusDTOFactory(multiple_status=False)
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        statuses = [StatusVariableDTOFactory()]
        storage.get_status_variables_to_task.return_value = statuses
        from ib_tasks.constants.enum import FieldTypes
        field_type_dtos = FieldTypeDTOFactory.create_batch(
            3, field_type=FieldTypes.PLAIN_TEXT.value
        )
        field_storage.get_field_type_dtos.return_value = field_type_dtos

    @staticmethod
    @pytest.fixture()
    def task_dto(task_gof_dtos):
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        return task_dto

    @staticmethod
    def test_given_invalid_path_raises_exception(
            interactor, storage,
            task_dto_mock, task_dto,
            set_up_storage
    ):
        # Arrange
        action_id = 1
        path_name = "ib_tasks.tests.interactors.stage_ac.stage_1_action_name_1"
        storage.get_path_name_to_action.return_value = path_name
        task_dto_mock.return_value = task_dto

        # Act
        with pytest.raises(InvalidModulePathFound) as error:
            interactor.call_action_logic_function_and_update_task_status_variables()

        # Assert
        assert error.value.path_name == path_name
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )

    @staticmethod
    def test_given_invalid_method_name_raises_exception(
            interactor, storage, task_dto_mock,
            task_dto, mocker, set_up_storage
    ):
        # Arrange
        action_id = 1
        path_name = "ib_tasks.tests.interactors.call_action_logic_testing_file.stage_1_action_name_9"
        mock_obj = mocker.patch("importlib.import_module")
        mock_obj.side_effect = \
            InvalidMethodFound(method_name="stage_1_action_name_1")
        storage.get_path_name_to_action.return_value = path_name
        task_dto_mock.return_value = task_dto

        # Act
        with pytest.raises(InvalidMethodFound) as error:
            interactor.call_action_logic_function_and_update_task_status_variables()

        # Assert
        assert error.value.method_name == "stage_1_action_name_1"
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )

    @staticmethod
    def test_assert_called_with_expected_arguments(
            mocker, task_gof_dtos,
            create_task_storage,
            field_storage, interactor, storage,
            task_dto_mock, task_dto, set_up_storage
    ):
        # Arrange
        mock_task_dict = {'gof2': [{'field2': 'field_response2'},
                                   {'field3': 'field_response3'}],
                          'gof1': {'field1': 'field_response1'},
                          'status_variables': {'variable_1': 'stage_1'}}
        path_name = "ib_tasks.tests.interactors.call_action_logic_testing_file.stage_1_action_name_3"
        mock_obj = mocker.patch(path_name)
        storage.get_path_name_to_action.return_value = path_name
        task_dto_mock.return_value = task_dto
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]

        # Act
        interactor \
            .call_action_logic_function_and_update_task_status_variables()

        # Assert
        mock_obj.assert_called_once_with(
            task_dict=mock_task_dict, global_constants={},
            stage_value_dict={}
        )

    @pytest.fixture()
    def set_up_storage_for_all_multiple_gofs(self, storage, field_storage):
        self.setup()
        single_gof = GOFMultipleStatusDTOFactory()
        multiple_gof = GOFMultipleStatusDTOFactory()
        storage.get_enable_multiple_gofs_field_to_gof_ids.return_value = [
            single_gof, multiple_gof
        ]
        statuses = [StatusVariableDTOFactory()]
        storage.get_status_variables_to_task.return_value = statuses
        from ib_tasks.constants.enum import FieldTypes
        field_type_dtos = FieldTypeDTOFactory.create_batch(
            3, field_type=FieldTypes.PLAIN_TEXT.value
        )
        field_storage.get_field_type_dtos.return_value = field_type_dtos

    @staticmethod
    def test_given_all_multiple_gofs(
            mocker, task_gof_dtos, create_task_storage,
            field_storage, interactor, storage, task_dto_mock,
            set_up_storage_for_all_multiple_gofs, task_dto
    ):
        # Arrange
        mock_task_dict = {'gof2': [{'field2': 'field_response2'},
                                   {'field3': 'field_response3'}],
                          'gof1': [{'field1': 'field_response1'}],
                          'status_variables': {'variable_1': 'stage_1'}}
        path_name = "ib_tasks.tests.interactors.call_action_logic_testing_file.stage_1_action_name_3"
        mock_obj = mocker.patch(path_name)
        storage.get_path_name_to_action.return_value = path_name
        task_dto_mock.return_value = task_dto

        # Act
        interactor \
            .call_action_logic_function_and_update_task_status_variables()

        # Assert
        mock_obj.assert_called_once_with(
            task_dict=mock_task_dict, global_constants={},
            stage_value_dict={}
        )

    @staticmethod
    @pytest.fixture()
    def set_up_storage_for_all_single_gofs(
            storage, field_storage, single_task_gof_dtos):
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        multiple_gofs = \
            GOFMultipleStatusDTOFactory.create_batch(3, multiple_status=False)
        TaskGoFFieldDTOFactory.reset_sequence(1)
        storage.get_enable_multiple_gofs_field_to_gof_ids \
            .return_value = multiple_gofs
        statuses = [StatusVariableDTOFactory()]
        storage.get_status_variables_to_task.return_value = statuses
        from ib_tasks.constants.enum import FieldTypes
        field_type_dtos = FieldTypeDTOFactory.create_batch(
            3, field_type=FieldTypes.PLAIN_TEXT.value
        )
        field_storage.get_field_type_dtos.return_value = field_type_dtos
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=single_task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        return task_dto

    @staticmethod
    def test_given_all_single_gofs(
            mocker, single_task_gof_dtos,
            create_task_storage, field_storage,
            interactor, storage, task_dto_mock,
            set_up_storage_for_all_single_gofs
    ):
        # Arrange
        mock_task_dict = {'gof2': {'field2': 'field_response2'},
                          'gof3': {'field3': 'field_response3'},
                          'gof1': {'field1': 'field_response1'},
                          'status_variables': {'variable_1': 'stage_1'}}
        path_name = "ib_tasks.tests.interactors.call_action_logic_testing_file.stage_1_action_name_1"
        mock_obj = mocker.patch(path_name)
        storage.get_path_name_to_action.return_value = path_name
        task_dto_mock.return_value = set_up_storage_for_all_single_gofs

        # Act
        interactor \
            .call_action_logic_function_and_update_task_status_variables()

        # Assert
        mock_obj.assert_called_once_with(
            task_dict=mock_task_dict, global_constants={},
            stage_value_dict={}
        )

    @staticmethod
    def test_access_invalid_key_raises_invalid_key_error(
            task_gof_dtos, interactor, storage,
            create_task_storage, set_up_storage_for_all_multiple_gofs,
            field_storage, task_dto_mock, task_dto
    ):
        # Arrange
        action_id = 1
        path_name = "ib_tasks.tests.interactors.call_action_logic_testing_file.stage_1_action_name_1"
        storage.get_path_name_to_action.return_value = path_name
        task_dto_mock.return_value = task_dto
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidKeyError

        # Act
        with pytest.raises(InvalidKeyError):
            interactor.call_action_logic_function_and_update_task_status_variables()

        # Assert
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )

    @staticmethod
    def test_do_bad_function_invalid_custom_logic_exception(
            task_gof_dtos, create_task_storage,
            field_storage, interactor, storage,
            task_dto_mock, task_dto, set_up_storage_for_all_single_gofs
    ):
        # Arrange
        action_id = 1
        path_name = "ib_tasks.tests.interactors.call_action_logic_testing_file.stage_1_action_name_2"
        storage.get_path_name_to_action.return_value = path_name

        task_dto_mock.return_value = task_dto
        from ib_tasks.exceptions.action_custom_exceptions \
            import InvalidCustomLogicException

        # Act
        with pytest.raises(InvalidCustomLogicException):
            interactor.call_action_logic_function_and_update_task_status_variables()

        # Assert
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )

    @staticmethod
    def test_given_valid_details_updates_statuses(set_up_storage_for_all_single_gofs,
                                                  create_task_storage, field_storage,
                                                  interactor, storage, task_dto_mock):
        # Arrange
        action_id = 1
        path_name = "ib_tasks.tests.interactors.call_action_logic_testing_file.stage_1_action_name_3"
        storage.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        expected_status = [
            StatusVariableDTOFactory(value='stage_2')
        ]
        task_dto_mock.return_value = set_up_storage_for_all_single_gofs

        # Act
        interactor.call_action_logic_function_and_update_task_status_variables()

        # Assert
        storage.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )
        storage.update_status_variables_to_task.assert_called_once_with(
            task_id=1, status_variables_dto=expected_status
        )

    # TODO fields update test case
