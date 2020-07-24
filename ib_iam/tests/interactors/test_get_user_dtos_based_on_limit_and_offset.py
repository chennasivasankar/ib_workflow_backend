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
        from ib_iam.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    def test_invalid_offset_raise_exception(self, storage_mock):
        # Arrange
        offset = -1
        limit = 1
        search_query = ""

        from ib_iam.interactors.get_user_profile_interactor import \
            GetUserProfileInteractor
        interactor = GetUserProfileInteractor(
            storage=storage_mock
        )

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidOffsetValue
        with pytest.raises(InvalidOffsetValue):
            interactor.get_user_dtos_based_on_limit_and_offset(
                limit=limit, offset=offset, search_query=search_query
            )

    def test_invalid_limit_raise_exception(self, storage_mock):
        # Arrange
        offset = 1
        limit = -1
        search_query = ""

        from ib_iam.interactors.get_user_profile_interactor import \
            GetUserProfileInteractor
        interactor = GetUserProfileInteractor(
            storage=storage_mock
        )

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidLimitValue
        with pytest.raises(InvalidLimitValue):
            interactor.get_user_dtos_based_on_limit_and_offset(
                limit=limit, offset=offset, search_query=search_query
            )

    def test_with_valid_details_return_response(self, storage_mock):
        # Arrange
        offset = 1
        limit = -1
        search_query = ""
        expected_user_details_dtos = []

        from ib_iam.interactors.get_user_profile_interactor import \
            GetUserProfileInteractor
        interactor = GetUserProfileInteractor(
            storage=storage_mock
        )

        # Act
        user_details_dtos = interactor.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query
        )

        # Assert
        assert user_details_dtos == expected_user_details_dtos
