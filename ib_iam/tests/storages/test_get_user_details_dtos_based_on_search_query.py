import pytest


class TestGetUsersDTOSBasedOnSearchQuery:

    @pytest.mark.django_db
    def test_get_user_details_dtos_based_on_search_query_return_response(self):
        # Arrange
        search_query = "s"

        user_details_dict = [
            {
                "user_id": "2bdb417e-4632-419a-8ddd-085ea272c6eb",
                "name": "Samuel"
            },
            {
                "user_id": "548a803c-7b48-47ba-a700-24f2ea0d1280",
                "name": "Matthew"
            },
            {
                "user_id": "4b8fb6eb-fa7d-47c1-8726-cd917901104e",
                "name": "Anthony"
            },
            {
                "user_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
                "name": "Christopher"
            },
            {
                "user_id": "aa66c40f-6d93-484a-b418-984716514c7b",
                "name": "Thomas"
            },
            {
                "user_id": "c982032b-53a7-4dfa-a627-4701a5230765",
                "name": "Jonathan"
            }
        ]

        expected_user_details_dict = [
            {
                "user_id": '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                "name": 'Samuel'
            },
            {
                "user_id": 'f2c02d98-f311-4ab2-8673-3daa00757002',
                "name": 'Christopher'
            },
            {
                "user_id": 'aa66c40f-6d93-484a-b418-984716514c7b',
                "name": 'Thomas'
            }
        ]

        from ib_iam.tests.factories.storage_dtos import UserIdAndNameFactory
        expected_user_details_dtos = [
            UserIdAndNameFactory(
                user_id=user_details["user_id"],
                name=user_details["name"]
            )
            for user_details in expected_user_details_dict
        ]

        from ib_iam.tests.factories.models import UserDetailsFactory
        for user_details in user_details_dict:
            UserDetailsFactory(
                user_id=user_details["user_id"],
                name=user_details["name"]
            )

        from ib_iam.storages.get_users_list_storage_implementation import \
            GetUsersListStorageImplementation
        storage = GetUsersListStorageImplementation()

        # Act
        response = storage.get_user_details_dtos_based_on_search_query(
            search_query=search_query
        )

        # Assert
        assert response == expected_user_details_dtos
