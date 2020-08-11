import pytest


class TestGetRoleIdsForEachUserId:

    @pytest.fixture()
    def storage_mock(self):
        from ib_iam.interactors.storage_interfaces.roles_storage_interface import \
            RolesStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(RolesStorageInterface)
        return storage

    def test_get_role_ids_for_each_user_id(self, storage_mock):
        # Arrange
        user_ids = [
            "eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "abc1a0c1-b9ef-4e59-b415-60a28ef17b10"
        ]

        from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO
        user_id_with_role_ids_dtos = [
            UserIdWithRoleIdsDTO(
                user_id="eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
                role_ids=["12233442", "12312323"]
            ),
            UserIdWithRoleIdsDTO(
                user_id="abc1a0c1-b9ef-4e59-b415-60a28ef17b10",
                role_ids=["4141264557", "12312323"]
            )
        ]

        storage_mock.get_user_id_with_role_ids_dtos.return_value \
            = user_id_with_role_ids_dtos

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage_mock)

        # Act
        response = interactor.get_role_ids_for_each_user_id(user_ids=user_ids)

        # Assert
        assert response == user_id_with_role_ids_dtos

    def test_invalid_user_id_raise_exception(self, storage_mock):
        # Arrange
        user_ids = [
            "eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "abc1a0c1-b9ef-4e59-b415-60a28ef17b10"
        ]
        invalid_user_ids = user_ids

        from ib_iam.exceptions.custom_exceptions import InvalidUserIds
        storage_mock.validate_user_ids.side_effect \
            = InvalidUserIds(user_ids=user_ids)

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage_mock)

        # Assert
        with pytest.raises(InvalidUserIds) as err:
            interactor.get_role_ids_for_each_user_id(user_ids=user_ids)

        assert invalid_user_ids == err.value.user_ids
