'''
validate offset
validate limit
get user objects based on serch query
return user dtos
'''
import pytest


class TestGetUserDTOSBasedOnLimitAndOffset:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.get_users_list_storage_interface import \
            GetUsersListStorageInterface
        storage = create_autospec(GetUsersListStorageInterface)
        return storage

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_iam.interactors.get_users_list_interactor import \
            GetUsersDetailsInteractor
        interactor = GetUsersDetailsInteractor(storage=storage_mock)
        return interactor

    def test_invalid_offset_raise_exception(self, interactor):
        # Arrange
        offset = -1
        limit = 1
        search_query = ""

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidOffsetValue
        with pytest.raises(InvalidOffsetValue):
            interactor.get_user_dtos_based_on_limit_and_offset(
                limit=limit, offset=offset, search_query=search_query
            )

    def test_invalid_limit_raise_exception(self, interactor):
        # Arrange
        offset = 1
        limit = -1
        search_query = ""

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidLimitValue
        with pytest.raises(InvalidLimitValue):
            interactor.get_user_dtos_based_on_limit_and_offset(
                limit=limit, offset=offset, search_query=search_query
            )

    def test_with_valid_details_return_response(self, storage_mock, interactor):
        # Arrange
        offset = 1
        limit = 1
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

        storage_mock.get_user_details_dtos_based_on_limit_offset_and_search_query.return_value \
            = user_details_dtos

        # Act
        response_user_details_dtos = interactor.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query
        )

        # Assert
        assert response_user_details_dtos == expected_user_details_dtos
        storage_mock.get_user_details_dtos_based_on_limit_offset_and_search_query.assert_called_once()
