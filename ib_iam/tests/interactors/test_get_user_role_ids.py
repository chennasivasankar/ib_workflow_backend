import pytest


class TestGetValidRoleIds:
    @pytest.fixture()
    def storage_mock(self):
        from ib_iam.interactors.storage_interfaces.roles_storage_interface import \
            RolesStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(RolesStorageInterface)
        return storage

    def test_get_user_role_ids(self, storage_mock):
        # Arrange
        role_ids = ["12233442", "12312323", "4141264557", "12312323"]
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        storage_mock.get_user_role_ids.return_value = role_ids

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage_mock)

        # Act
        response = interactor.get_user_role_ids(user_id=user_id)

        # Assert
        assert response == role_ids
        storage_mock.get_user_role_ids.assert_called_with(user_id=user_id)

    def test_invalid_user_id_raise_exception(self, storage_mock):
        # Arrange
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        storage_mock.validate_user_id.side_effect \
            = InvalidUserId

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage_mock)

        # Assert
        with pytest.raises(InvalidUserId):
            interactor.get_user_role_ids(user_id=user_id)

        storage_mock.validate_user_id.assert_called_once_with(user_id=user_id)
