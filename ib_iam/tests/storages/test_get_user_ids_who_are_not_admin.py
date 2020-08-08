import pytest
from ib_iam.tests.common_fixtures.reset_fixture \
    import reset_sequence_company_factory, \
    reset_sequence_user_details_factory
from ib_iam.tests.factories.models import UserDetailsFactory, CompanyFactory


class TestGetUserIdsWhoAreNotAdmin:
    @pytest.mark.django_db
    def test_get_user_ids_who_are_not_admin(self):
        # Arrange
        users = [
            {
                "user_id": "3",
                "is_admin": True
            },
            {
                "user_id": "4",
                "is_admin": False
            },
            {
                "user_id": "5",
                "is_admin": False
            },
            {
                "user_id": "6",
                "is_admin": False
            }
        ]
        actual_user_ids = ["4", "5", "6"]
        reset_sequence_company_factory()
        reset_sequence_user_details_factory()
        for user in users:
            company = CompanyFactory.create()
            UserDetailsFactory.create(
                user_id=user["user_id"], is_admin=user["is_admin"],
                company=company)

        from ib_iam.storages.user_storage_implementation \
            import UserStorageImplementation
        storage = UserStorageImplementation()

        # Act
        expected_user_ids = storage.get_user_ids_who_are_not_admin()

        # Assert
        assert actual_user_ids == expected_user_ids
        assert len(actual_user_ids) == len(expected_user_ids)
