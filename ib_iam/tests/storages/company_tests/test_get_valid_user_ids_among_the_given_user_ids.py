import pytest
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation



@pytest.fixture
def create_users():
    from ib_iam.tests.factories.models import UserDetailsFactory
    user_ids = ["user 1", "user 2"]
    for user_id in user_ids:
        UserDetailsFactory.create(user_id=user_id)
    return user_ids

@pytest.mark.django_db
class TestGetValidUserIdsAmongTheGivenUserIds:
    def test_given_some_valid_users_it_returns_user_ids(
            self, create_users
    ):
        storage = CompanyStorageImplementation()
        user_ids = ["user 1", "user 2", "user 3"]
        expected_user_ids = create_users

        actual_user_ids = storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids)

        assert actual_user_ids == expected_user_ids

    def test_given_no_valid_members_it_returns_empty_list(
            self, create_users):
        storage = CompanyStorageImplementation()
        user_ids = ["user 3", "user 4"]
        expected_user_ids = []

        actual_user_ids = \
            storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids
            )

        assert actual_user_ids == expected_user_ids
