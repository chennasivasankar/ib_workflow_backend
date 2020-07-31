import pytest

from ib_tasks.interactors.get_allowed_stage_ids_of_user_interactor import \
    GetAllowedStageIdsOfUserInteractor
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


class TestGetAllowedStageIdsOfUserInteractor:
    @pytest.fixture
    def storage_mock(self):
        from mock import create_autospec
        storage_mock = create_autospec(StageStorageInterface)
        return storage_mock

    def test_given_user_id_get_stage_ids(self, storage_mock):
        # Arrange
        user_id = "iB_01"
        stage_ids = ["stage_1", "stage_2"]
        storage_mock.get_allowed_stage_ids_of_user.return_value = stage_ids
        interactor = GetAllowedStageIdsOfUserInteractor(storage=storage_mock)
        # Act
        result = interactor.get_allowed_stage_ids_of_user(user_id=user_id)
        # Assert
        assert result == stage_ids
        storage_mock.get_allowed_stage_ids_of_user. \
            assert_called_once()
