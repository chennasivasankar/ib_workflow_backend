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
        expected_user_details_dtos = []

        storage_mock.get_user_details_dtos_based_on_limit_offset_and_search_query.return_value \
            =

        # Act
        user_details_dtos = interactor.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query
        )

        # Assert
        assert user_details_dtos == expected_user_details_dtos
