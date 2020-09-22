import pytest

from ib_tasks.tests.interactors.super_storage_mock_class import StorageMockClass


class TestGetUserPermittedStageIds(StorageMockClass):

    @pytest.fixture
    def interactor(self, stage_storage):
        from ib_tasks.interactors.get_user_permitted_stage_ids \
            import GetUserPermittedStageIds
        interactor = GetUserPermittedStageIds(stage_storage=stage_storage)
        return interactor

    @pytest.fixture()
    def roles_mock(self, mocker):
        path = 'ib_tasks.adapters.roles_service.RolesService.get_valid_role_ids_in_given_role_ids'
        return mocker.patch(path)

    def test_given_invalid_roles_raises_exception(
            self, interactor, roles_mock, stage_storage):
        # Arrange
        role_ids = ["role_1", "role_2", "role_3"]
        valid_role_ids = ["role_1", "role_2"]
        invalid_role_ids = ["role_3"]
        roles_mock.return_value = valid_role_ids
        from ib_tasks.exceptions.roles_custom_exceptions \
            import InvalidRoleIdsException

        # Act
        with pytest.raises(InvalidRoleIdsException) as err:
            interactor.get_permitted_stage_ids_to_user_role_ids(user_roles=role_ids)

        # Assert
        assert err.value.role_ids == invalid_role_ids

    def test_given_valid_returns_stage_ids(
            self, interactor, roles_mock, stage_storage
    ):
        # Arrange
        role_ids = ["role_1", "role_2", "role_3"]
        roles_mock.return_value = role_ids
        stage_ids = ["stage_1", "stage_2"]
        stage_storage.get_stage_ids_having_actions.return_value = stage_ids

        # Act
        response_stage_ids = interactor \
            .get_permitted_stage_ids_to_user_role_ids(user_roles=role_ids)

        # Assert
        assert response_stage_ids == stage_ids
