from unittest.mock import create_autospec

import pytest

from ib_tasks.interactors.get_task_details_interactor import \
    GetTaskDetailsInteractor
from ib_tasks.tests.factories.storage_dtos import TaskProjectDTOFactory, \
    TaskDisplayIdDTOFactory


class TestGetTaskProjectIds:

    @pytest.fixture
    def task_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import \
            TaskStorageInterface
        return create_autospec(TaskStorageInterface)

    @pytest.fixture
    def interactor_mock(self, task_storage):
        return GetTaskDetailsInteractor(task_storage)

    @pytest.fixture
    def expected_response(self):
        TaskProjectDTOFactory.reset_sequence()
        return TaskProjectDTOFactory.create_batch(4)

    def test_invalid_task_ids_raises_exception(self, task_storage,
                                               interactor_mock):
        # Arrange
        task_ids = [1, 2, 3, 4]
        valid_task_ids = []
        task_storage.get_valid_task_ids.return_value = valid_task_ids

        # Act
        from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
        with pytest.raises(InvalidTaskIds) as err:
            interactor_mock.get_task_project_ids(task_ids)

        # Assert
        assert err.value.invalid_task_ids == task_ids

    def test_with_valid_task_ids_return_task_project_ids(
            self, task_storage, expected_response, interactor_mock):
        # Arrange
        task_project_dtos = expected_response
        task_ids = [1, 2, 3, 4]
        valid_task_ids = task_ids
        task_storage.get_valid_task_ids.return_value = valid_task_ids
        task_storage.get_task_project_ids.return_value = task_project_dtos

        # Act
        response = interactor_mock.get_task_project_ids(task_ids)

        # Assert
        assert response == expected_response


class TestGetTaskIdsGivenTDisplayIds:
    @pytest.fixture
    def task_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import \
            TaskStorageInterface
        return create_autospec(TaskStorageInterface)

    @pytest.fixture
    def interactor_mock(self, task_storage):
        return GetTaskDetailsInteractor(task_storage)

    @pytest.fixture
    def expected_output(self):
        TaskDisplayIdDTOFactory.reset_sequence()
        return TaskDisplayIdDTOFactory.create_batch(3)

    def test_get_task_ids(self, interactor_mock, task_storage,
                          expected_output):
        # Arrange
        task_display_dtos = expected_output
        task_display_ids = ["IBWF-1", "IBWF-2", "IBWF-3"]
        task_storage.get_valid_task_display_ids.return_value = task_display_ids
        task_storage.get_task_ids_given_task_display_ids.return_value = \
            task_display_dtos

        # Act
        response = interactor_mock.get_task_ids_for_given_task_display_ids(
            task_display_ids)

        # Assert
        self._validate_output(expected_output, response)

    @staticmethod
    def _validate_output(expected_dtos, returned_dtos):
        for returned_dto, expected_dto in zip(returned_dtos,
                                              expected_dtos):
            assert returned_dto.task_id == expected_dto.task_id
            assert returned_dto.display_id == expected_dto.display_id

    def test_given_invalid_task_display_ids_rasise_exception(
            self, interactor_mock, task_storage):
        # Arrange
        task_display_ids = ["IBWF-1", "IBWF-2", "IBWF-3"]
        valid_display_ids = []
        task_storage.get_valid_task_display_ids.return_value = \
            valid_display_ids

        # Act
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayIds
        with pytest.raises(InvalidTaskDisplayIds) as err:
            interactor_mock.get_task_ids_for_given_task_display_ids(
                task_display_ids)

        # Assert
        assert err.value.invalid_task_display_ids == task_display_ids
