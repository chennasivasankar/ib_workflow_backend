import pytest
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)


@pytest.mark.django_db
class TestGetValidMemberIdsAmongTheGivenMemberIds:
    def test_given_some_valid_members_it_returns_member_ids(
            self, create_users
    ):
        storage = TeamStorageImplementation()
        user_ids = ["user1", "user2", "user3"]
        expected_user_ids = ["user1", "user2"]

        actual_user_ids = \
            storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids
            )

        assert actual_user_ids == expected_user_ids

    def test_given_no_valid_members_it_returns_empty_list(
            self, create_users
    ):
        storage = TeamStorageImplementation()
        user_ids = ["user_id-3", "user_id-4"]
        expected_user_ids = []

        actual_user_ids = \
            storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids
            )

        assert actual_user_ids == expected_user_ids
