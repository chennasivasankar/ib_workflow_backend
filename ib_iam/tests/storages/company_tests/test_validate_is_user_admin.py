import pytest

from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
from ib_iam.storages.company_storage_implementation import CompanyStorageImplementation
from ib_iam.tests.factories.models import UserDetailsFactory


@pytest.mark.django_db
class TestValidateIsUserAdmin:
    def test_given_user_is_not_admin_raises_user_has_no_access_error(self):
        storage = CompanyStorageImplementation()
        UserDetailsFactory.create(user_id="1", is_admin=False)

        with pytest.raises(UserHasNoAccess):
            storage.validate_is_user_admin(user_id="1")

    def test_if_user_is_admin_returns_none(self):
        storage = CompanyStorageImplementation()
        UserDetailsFactory.create(user_id="1", is_admin=True)
        expected_result = None

        actual_result = storage.validate_is_user_admin(user_id="1")

        assert actual_result == expected_result
