import pytest


class TestGetValidRoleIds:

    @pytest.mark.django_db
    def test_with_role_ids_return_valid_role_ids(self, snapshot):
        # Arrange
        role_ids = ["12233442", "12312323", "4141264557", "12312323"]
        expected_valid_ids = ["12233442", "12312323"]
        from ib_iam.tests.factories.models import RoleFactory
        RoleFactory.create(role_id=expected_valid_ids[0])
        RoleFactory.create(role_id=expected_valid_ids[1])

        from ib_iam.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)

        # Act
        valid_role_ids = interactor.get_valid_role_ids(role_ids=role_ids)

        # Assert
        snapshot.assert_match(sorted(valid_role_ids), "valid_role_ids")
