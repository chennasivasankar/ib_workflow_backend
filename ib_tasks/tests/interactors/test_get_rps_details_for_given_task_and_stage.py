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

    def test_given_invalid_task_id_raises_exception(self, storage, task_storage):
        # Arrange

        interactor = GetTaskRPsInteractor(storage=storage, task_storage=task_storage)
        # Act
        # Assert
