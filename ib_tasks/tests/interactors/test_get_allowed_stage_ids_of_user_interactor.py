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

    def test_given_user_id_get_stage_ids(self, storage_mock, mocker):
        # Arrange
        user_id = "iB_01"
        stage_ids = ["stage_1"]
        from ib_tasks.tests.factories.storage_dtos import StageRolesDTOFactory
        StageRolesDTOFactory.reset_sequence(1)
        stages = StageRolesDTOFactory.create_batch(2)
        storage_mock.get_stages_roles.return_value = stages
        interactor = GetAllowedStageIdsOfUserInteractor(storage=storage_mock)
        path = "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids"
        mock_obj = mocker.patch(path)
        mock_obj.return_value = ['ROLE_1']
        # Act
        result = interactor.get_allowed_stage_ids_of_user(user_id=user_id)
        # Assert
        assert result == stage_ids
        mock_obj.called_once()

    def test_given_user_id_returns_stage_ids(self, storage_mock, mocker):
        # Arrange
        user_id = "iB_01"
        stage_ids = ["stage_1", "stage_2"]
        from ib_tasks.tests.factories.storage_dtos import StageRolesDTOFactory
        StageRolesDTOFactory.reset_sequence(1)
        stages = StageRolesDTOFactory.create_batch(2)
        storage_mock.get_stages_roles.return_value = stages
        interactor = GetAllowedStageIdsOfUserInteractor(storage=storage_mock)
        path = "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids"
        mock_obj = mocker.patch(path)
        mock_obj.return_value = ['ROLE_2']
        # Act
        result = interactor.get_allowed_stage_ids_of_user(user_id=user_id)
        # Assert
        assert result == stage_ids
        mock_obj.called_once()

    def test_given_user_id_returns_empty_stage_ids(self, storage_mock, mocker):
        # Arrange
        user_id = "iB_01"
        stage_ids = []
        from ib_tasks.tests.factories.storage_dtos import StageRolesDTOFactory
        StageRolesDTOFactory.reset_sequence(1)
        stages = StageRolesDTOFactory.create_batch(2)
        storage_mock.get_stages_roles.return_value = stages
        interactor = GetAllowedStageIdsOfUserInteractor(storage=storage_mock)
        path = "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids"
        mock_obj = mocker.patch(path)
        mock_obj.return_value = ['ROLE_4']
        # Act
        result = interactor.get_allowed_stage_ids_of_user(user_id=user_id)
        # Assert
        assert result == stage_ids
        mock_obj.called_once()

    def test_given_user_id_returns_one_stage_ids(self, storage_mock, mocker):
        # Arrange
        user_id = "iB_01"
        stage_ids = ['stage_1']
        from ib_tasks.tests.factories.storage_dtos import StageRolesDTOFactory
        StageRolesDTOFactory.reset_sequence(1)
        stages = StageRolesDTOFactory.create_batch(1, role_ids=['ALL_ROLES'])
        stages.append(StageRolesDTOFactory())
        storage_mock.get_stages_roles.return_value = stages
        interactor = GetAllowedStageIdsOfUserInteractor(storage=storage_mock)
        path = "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids"
        mock_obj = mocker.patch(path)
        mock_obj.return_value = ['ROLE_4']
        # Act
        result = interactor.get_allowed_stage_ids_of_user(user_id=user_id)
        # Assert
        assert result == stage_ids
        mock_obj.called_once()