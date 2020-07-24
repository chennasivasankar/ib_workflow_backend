import pytest

from ib_iam.storages.delete_user_storage_implementation import \
    DeleteUserStorageImplementation


class TestDeleteUSerStorageImplementation:

    @pytest.mark.django_db
    def test_check_is_admin_user_given_user_is_admin_then_return_true(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        is_admin = True
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)
        expected_result = is_admin
        storage = DeleteUserStorageImplementation()

        actual_result = storage.check_is_admin_user(user_id=user_id)

        assert actual_result == expected_result

    @pytest.mark.django_db
    def test_check_is_admin_user_given_user_is_not_admin_then_return_false(
            self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        is_admin = False
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)
        expected_result = is_admin
        storage = DeleteUserStorageImplementation()

        actual_result = storage.check_is_admin_user(user_id=user_id)

        assert actual_result == expected_result

    @pytest.mark.django_db
    def test_delete_user_from_user_details_db(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        is_admin = False
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)
        expected_result = is_admin
        storage = DeleteUserStorageImplementation()

        actual_result = storage.check_is_admin_user(user_id=user_id)

        assert actual_result == expected_result
