import pytest

from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
from ib_iam.storages.team_storage_implementation import \
    TeamStorageImplementation


@pytest.mark.django_db
class TestRaiseExceptionIfUserIsNotAdmin:
    def test_given_user_is_not_admin_raises_user_has_no_access_error(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id="user_id-2", is_admin=False)
        storage = TeamStorageImplementation()

        with pytest.raises(UserHasNoAccess):
            storage.validate_is_user_admin(user_id="user_id-2")

    def test_if_user_is_admin_returns_none(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id="user_id-1", is_admin=True)
        storage = TeamStorageImplementation()
        expected_result = None

        actual_result = storage.validate_is_user_admin(
            user_id="user_id-1"
        )

        assert actual_result == expected_result
