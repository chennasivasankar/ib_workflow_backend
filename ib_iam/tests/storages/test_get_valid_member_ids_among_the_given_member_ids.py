import pytest
from ib_iam.storages.team_storage_implementation import (
    TeamStorageImplementation
)


@pytest.mark.django_db
class TestGetValidMemberIdsAmongTheGivenMemberIds:
    def test_given_some_valid_members_it_returns_member_ids(
            self, create_users
    ):
        sql_storage = TeamStorageImplementation()
        print("*************************")
        from ib_iam.models import UserDetails
        print(UserDetails.objects.values())
        member_ids = ["user_id-1", "user_id-2", "user_id-3"]
        expected_member_ids = ["user_id-1", "user_id-2"]

        actual_member_ids = \
            sql_storage.get_valid_member_ids_among_the_given_member_ids(
                member_ids=member_ids
            )

        assert actual_member_ids == expected_member_ids

    def test_given_no_valid_members_it_returns_empty_list(
            self, create_users
    ):
        sql_storage = TeamStorageImplementation()
        member_ids = ["user_id-3", "user_id-4"]
        expected_member_ids = []

        actual_member_ids = \
            sql_storage.get_valid_member_ids_among_the_given_member_ids(
                member_ids=member_ids
            )

        assert actual_member_ids == expected_member_ids
