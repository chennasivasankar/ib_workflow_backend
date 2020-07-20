import pytest

from ib_iam.exceptions import UserHasNoAccess
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation


@pytest.mark.django_db
class TestRaiseExceptionIfUserIsNotAdmin:
    def test_given_user_is_not_admin_raises_user_has_no_access_error(
            self, create_users
    ):
        storage = TeamStorageImplementation()

        with pytest.raises(UserHasNoAccess):
            storage.raise_exception_if_user_is_not_admin(user_id="user_id-2")

    def test_if_user_is_admin_returns_none(
            self, create_users
    ):
        storage = TeamStorageImplementation()
        expected_result = None

        actual_result = storage.raise_exception_if_user_is_not_admin(
            user_id="user_id-1"
        )

        assert actual_result == expected_result

