from unittest.mock import create_autospec

import pytest

from ib_tasks.interactors.get_task_related_rps_in_given_stage import GetTaskRPsInteractor


class TestGetTaskRelatedRps:

    @pytest.fixture
    def storage(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        return create_autospec(StorageInterface)

    @pytest.fixture
    def task_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        return create_autospec(TaskStorageInterface)

    @pytest.fixture
    def parameters(self):
        from ib_tasks.interactors.task_dtos import GetTaskRPsParametersDTO
        return GetTaskRPsParametersDTO(
            task_id="IBWF-1",
            stage_id=1,
            user_id="user_id_1"
        )

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.get_task_rps_presenter \
            import GetTaskRpsPresenterInterface
        return create_autospec(GetTaskRpsPresenterInterface)

    def test_given_invalid_task_id_raises_exception(self, storage, task_storage,
                                                    parameters, presenter_mock):
        # Arrange
        task_display_id = parameters.task_id
        task_storage.check_is_valid_task_display_id.return_value = False

        interactor = GetTaskRPsInteractor(storage=storage, task_storage=task_storage)

        # Act
        response = interactor.get_task_rps_wrapper(presenter_mock, parameters)

        # Assert
        task_storage.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id)
        presenter_mock.response_for_invalid_task_id.assert_called_once()

    def test_given_user_is_not_assigned_to_task_raises_exception(
            self, storage, task_storage,
            parameters, presenter_mock):
        # Arrange
        task_display_id = parameters.task_id
        task_id = 1
        stage_id = parameters.stage_id
        user_id = parameters.user_id
        storage.validate_stage_id.return_value = True
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user.return_value = False

        interactor = GetTaskRPsInteractor(storage=storage, task_storage=task_storage)

        # Act
        response = interactor.get_task_rps_wrapper(presenter_mock, parameters)

        # Assert
        task_storage.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id)
        storage.validate_if_task_is_assigned_to_user.assert_called_once_with(
            task_id, user_id
        )
        presenter_mock.response_for_user_is_not_assignee_for_task.assert_called_once()
