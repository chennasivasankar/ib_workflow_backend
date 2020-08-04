import pytest
from ib_iam.storages.user_storage_implementation import \
    UserStorageImplementation


@pytest.mark.django_db
class TestIsUserAdmin:
    def test_given_user_is_not_admin_returns_false(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id="user_id-2", is_admin=False)
        expected_response = False
        storage = UserStorageImplementation()

        actual_response = storage.is_user_admin(user_id="user_id-2")

        assert actual_response == expected_response

    def test_given_user_is_admin_returns_true(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id="user_id-2", is_admin=True)
        expected_response = True
        storage = UserStorageImplementation()

        actual_response = storage.is_user_admin(user_id="user_id-2")

        assert actual_response == expected_response