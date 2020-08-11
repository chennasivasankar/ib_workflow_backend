import pytest

from ib_tasks.interactors.get_task_id_for_task_display_id import \
    GetTaskIdForTaskDisplayId


class TestGetTaskIdForTaskDisplayId:

    @pytest.fixture
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface

        storage = create_autospec(TaskStorageInterface)
        return storage

    def test_with_invalid_task_display_id_raises_exception(self, storage_mock):
        # Arrange
        task_display_id = "IBWF_001"
        storage_mock.check_is_valid_task_display_id.return_value = False
        interactor = GetTaskIdForTaskDisplayId(task_storage=storage_mock)
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId

        # Assert
        with pytest.raises(InvalidTaskDisplayId):
            interactor.get_task_id_for_task_display_id(
                task_display_id=task_display_id)

        storage_mock.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id=task_display_id
        )

    def test_with_valid_task_display_id_returns_task_id(self, storage_mock):
        # Arrange
        expected_task_id = 1
        task_display_id = "IBWF_001"
        storage_mock.check_is_valid_task_display_id.return_value = True
        storage_mock.get_task_id_for_task_display_id.return_value = \
            expected_task_id

        interactor = GetTaskIdForTaskDisplayId(task_storage=storage_mock)

        # Act
        task_id = interactor.get_task_id_for_task_display_id(
            task_display_id=task_display_id)

        # Assert
        assert task_id == expected_task_id
        storage_mock.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id=task_display_id
        )
        storage_mock.get_task_id_for_task_display_id.assert_called_once_with(
            task_display_id=task_display_id
        )
