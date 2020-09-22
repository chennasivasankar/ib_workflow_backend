import pytest


class TestSubTasksInteractor:

    @staticmethod
    @pytest.fixture()
    def task_storage():
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(TaskStorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def interactor(task_storage):
        from ib_tasks.interactors.sub_tasks_interactor import SubTasksInteractor
        interactor = SubTasksInteractor(task_storage=task_storage)
        return interactor

    def test_given_invalid_task_ids_raises_exception(self, interactor, task_storage):
        # Arrange
        task_ids = [1, 2, 3]
        valid_task_ids = [1, 2]
        invalid_task_ids = [3]
        task_storage.get_valid_task_ids.return_value = valid_task_ids
        from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds

        # Act
        with pytest.raises(InvalidTaskIds) as err:
            interactor.get_sub_tasks_count_task_ids(task_ids=task_ids)

        # Assert
        assert err.value.invalid_task_ids == invalid_task_ids
        task_storage.get_valid_task_ids.assert_called_once_with(
            task_ids=task_ids
        )

    def set_up_storage_sub_tasks_count(self, task_storage):
        from ib_tasks.tests.factories.storage_dtos import SubTasksCountDTOFactory
        SubTasksCountDTOFactory.reset_sequence(1)
        expected = SubTasksCountDTOFactory.create_batch(2)
        task_storage.get_sub_tasks_count_to_tasks.return_value = expected
        return expected

    def test_given_valid_details_returns_sub_tasks_count(self, interactor, task_storage):
        # Arrange
        task_ids = [1, 2]
        task_storage.get_valid_task_ids.return_value = task_ids
        expected = self.set_up_storage_sub_tasks_count(task_storage)

        # Act
        response = interactor.get_sub_tasks_count_task_ids(task_ids=task_ids)

        # Assert
        assert response == expected

    def test_given_invalid_tasks_raises_exception(self, interactor, task_storage):
        # Arrange
        task_ids = [1, 2, 3]
        valid_task_ids = [1, 2]
        invalid_task_ids = [3]
        task_storage.get_valid_task_ids.return_value = valid_task_ids
        from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds

        # Act
        with pytest.raises(InvalidTaskIds) as err:
            interactor.get_sub_task_ids_to_task_ids(task_ids=task_ids)

        # Assert
        assert err.value.invalid_task_ids == invalid_task_ids
        task_storage.get_valid_task_ids.assert_called_once_with(
            task_ids=task_ids
        )

    def set_up_storage_sub_task_ids(self, task_storage):
        from ib_tasks.tests.factories.storage_dtos import SubTasksIdsDTOFactory
        SubTasksIdsDTOFactory.reset_sequence(1)
        expected = SubTasksIdsDTOFactory.create_batch(2)
        task_storage.get_sub_task_ids_to_tasks.return_value = expected
        return expected

    def test_given_valid_details_returns_sub_task_ids(self, interactor, task_storage):
        # Arrange
        task_ids = [1]
        task_storage.get_valid_task_ids.return_value = task_ids
        expected = self.set_up_storage_sub_task_ids(task_storage)

        # Act
        response = interactor.get_sub_task_ids_to_task_ids(task_ids=task_ids)

        # Assert
        assert response == expected
