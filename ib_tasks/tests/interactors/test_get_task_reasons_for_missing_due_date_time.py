from unittest.mock import create_autospec

from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface import \
    GetTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.

class TestGetTaskReasons:

    def test_given_invalid_task_id_raises_exception(self):
        # Arrange
        task_id = 1
        user_id = "user_id_1"
        storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(GetTaskPresenterInterface)
        interactor = GetTaskDueMissingReasonsInteractor(
            task_storage=storage
        )
        # Act
        # Assert
