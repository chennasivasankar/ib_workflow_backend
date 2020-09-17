import pytest
import mock
from ib_tasks.interactors.task_log_interactor import TaskLogInteractor
from ib_tasks.tests.factories.interactor_dtos import \
    CreateTaskLogDTOFactory
from ib_tasks.tests.interactors.super_storage_mock_class import StorageMockClass


class TestCreateTaskLogInteractor(StorageMockClass):
    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        task_storage = mock.create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        storage = mock.create_autospec(StorageInterface)
        return storage

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        CreateTaskLogDTOFactory.reset_sequence(1)

    def test_with_empty_task_json_string_raises_exception(
            self, task_storage_mock, storage_mock, action_storage_mock):
        # Arrange
        create_task_log_dto = CreateTaskLogDTOFactory(task_json="  ")
        interactor = TaskLogInteractor(
            task_storage=task_storage_mock, storage=storage_mock,
            action_storage=action_storage_mock
        )
        from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskJson
        from ib_tasks.constants.exception_messages import INVALID_TASK_JSON

        # Assert
        with pytest.raises(InvalidTaskJson) as err:
            interactor.create_task_log(
                create_task_log_dto=create_task_log_dto
            )
        assert err.value.args[0] == INVALID_TASK_JSON

    def test_with_invalid_task_id_raises_exception(
            self, task_storage_mock, storage_mock,
            action_storage_mock):
        # Arrange
        invalid_task_id = 1
        from ib_tasks.constants.exception_messages import INVALID_TASK_ID
        expected_err_msg = INVALID_TASK_ID[0].format(invalid_task_id)

        create_task_log_dto = CreateTaskLogDTOFactory()
        interactor = TaskLogInteractor(
            task_storage=task_storage_mock, storage=storage_mock,
            action_storage=action_storage_mock
        )
        task_storage_mock.check_is_task_exists.return_value = False
        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskDoesNotExists

        # Assert
        with pytest.raises(TaskDoesNotExists) as err:
            interactor.create_task_log(
                create_task_log_dto=create_task_log_dto
            )
        assert err.value.args[0] == expected_err_msg
        task_storage_mock.check_is_task_exists. \
            assert_called_once_with(task_id=invalid_task_id)

    def test_with_invalid_action_id_raises_exception(
            self, task_storage_mock, storage_mock, action_storage_mock):
        # Arrange
        task_id = 1
        action_id = 1
        from ib_tasks.constants.exception_messages import INVALID_ACTION_ID
        invalid_action_id = 1
        expected_err_msg = INVALID_ACTION_ID[0].format(invalid_action_id)

        create_task_log_dto = CreateTaskLogDTOFactory()
        interactor = TaskLogInteractor(
            task_storage=task_storage_mock, storage=storage_mock,
            action_storage=action_storage_mock
        )
        task_storage_mock.check_is_task_exists.return_value = True
        action_storage_mock.validate_action.return_value = False
        from ib_tasks.exceptions.action_custom_exceptions import \
            ActionDoesNotExists

        # Assert
        with pytest.raises(ActionDoesNotExists) as err:
            interactor.create_task_log(
                create_task_log_dto=create_task_log_dto
            )
        assert err.value.args[0] == expected_err_msg
        task_storage_mock.check_is_task_exists. \
            assert_called_once_with(task_id=task_id)
        action_storage_mock.validate_action. \
            assert_called_once_with(action_id=action_id)

    def test_with_valid_details(self, task_storage_mock, storage_mock, action_storage_mock):
        # Arrange
        task_id = 1
        action_id = 1
        create_task_log_dto = CreateTaskLogDTOFactory()
        interactor = TaskLogInteractor(
            task_storage=task_storage_mock, storage=storage_mock,
            action_storage=action_storage_mock
        )
        task_storage_mock.check_is_task_exists.return_value = True
        action_storage_mock.validate_action.return_value = True

        # Act
        interactor.create_task_log(create_task_log_dto=create_task_log_dto)

        # Assert
        task_storage_mock.check_is_task_exists. \
            assert_called_once_with(task_id=task_id)
        action_storage_mock.validate_action. \
            assert_called_once_with(action_id=action_id)
        task_storage_mock.create_task_log. \
            assert_called_once_with(create_task_log_dto=create_task_log_dto)
