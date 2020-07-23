import pytest


class TestGetValidRoleIds:
    @pytest.fixture()
    def storage_mock(self):
        from ib_iam.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    def test_get_valid_role_ids_return_valid_ids(self, storage_mock):
        # Arrange
        role_ids = ["12233442", "12312323", "4141264557", "12312323"]
        expected_valid_ids = ["12233442", "12312323"]

        storage_mock.get_valid_role_ids.return_value = expected_valid_ids

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage_mock)

        # Act
        valid_ids = interactor.get_valid_role_ids(role_ids=role_ids)

        # Assert
        assert valid_ids == expected_valid_ids
