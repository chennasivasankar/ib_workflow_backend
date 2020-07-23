import pytest
from ib_tasks.interactors.get_task_interactor import GetTaskInteractor


class TestTaskInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface \
            import CreateOrUpdateTaskStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(CreateOrUpdateTaskStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface\
            import GetTaskPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(GetTaskPresenterInterface)
        return presenter

    @pytest.fixture
    def mock_object(self):
        from unittest.mock import Mock
        mock_object = Mock()
        return mock_object

    def test_given_invalid_task_id_raise_exception(
            self, storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskIdException
        user_id = 1
        task_id = "task0"
        interactor = GetTaskInteractor(storage=storage_mock)
        storage_mock.validate_task_id.side_effect = InvalidTaskIdException(task_id)
        presenter_mock.raise_exception_for_invalid_task_id.return_value = mock_object

        # Act
        with pytest.raises(InvalidTaskIdException) as err:
            interactor.get_task_wrapper(
                user_id=user_id, task_id=task_id, presenter=presenter_mock
            )

        # Assert
        storage_mock.validate_task_id.assert_called_once_with(task_id=task_id)
        presenter_mock.raise_exception_for_invalid_task_id.assert_called_once()
