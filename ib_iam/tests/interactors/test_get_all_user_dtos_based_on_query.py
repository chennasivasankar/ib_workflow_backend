import pytest


class TestGetAllUserDTOsBasedOnQuery:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_iam.interactors.users.get_users_list_interactor import \
            GetListOfUsersInteractor
        interactor = GetListOfUsersInteractor(user_storage=storage_mock)
        return interactor

    def test_get_all_user_dtos_based_on_query_return_response(
            self, storage_mock, interactor
    ):
        search_query = ""
        user_details_dict = [
            {
                "user_id": "eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
                "name": "test1"
            },
            {
                "user_id": "abc1a0c1-b9ef-4e59-b415-60a28ef17b10",
                "name": "test2"
            }
        ]

        from ib_iam.tests.factories.storage_dtos import UserIdAndNameFactory
        user_details_dtos = [
            UserIdAndNameFactory(
                user_id=user_details["user_id"],
                name=user_details["name"]
            )
            for user_details in user_details_dict
        ]

        expected_user_details_dtos = user_details_dtos

        storage_mock.get_user_details_dtos_based_on_search_query.return_value \
            = user_details_dtos

        # Act
        response_user_details_dtos = interactor.get_all_user_dtos_based_on_query(
            search_query=search_query
        )

        # Assert
        assert response_user_details_dtos == expected_user_details_dtos
        storage_mock.get_user_details_dtos_based_on_search_query. \
            assert_called_once_with(search_query=search_query)
