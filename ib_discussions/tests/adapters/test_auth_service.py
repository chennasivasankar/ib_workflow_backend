from unittest.mock import patch

import pytest


class TestAuthService:
    @pytest.fixture()
    def prepare_get_user_profile_dtos_mock(self, mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.get_user_profile_bulk"
        )
        return mock

    @patch(
        "ib_users.interfaces.service_interface.ServiceInterface.get_user_profile_bulk"
    )
    def test_with_empty_user_id_raise_exception(
            self, get_user_profile_dtos_mock
    ):
        # Arrange
        user_ids = ["1", "", "3"]
        from ib_users.interactors.exceptions.user_profile import \
            InvalidUserException
        from ib_users.constants.user_profile.error_types import \
            EMPTY_USER_ID_ERROR_TYPE
        from ib_users.constants.user_profile.error_messages import EMPTY_USER_ID
        get_user_profile_dtos_mock.side_effect = InvalidUserException(
            message=EMPTY_USER_ID, exception_type=EMPTY_USER_ID_ERROR_TYPE
        )

        from ib_discussions.adapters.service_adapter import ServiceAdapter
        serice_adapter = ServiceAdapter()
        auth_service = serice_adapter.auth_service

        # Assert
        from ib_discussions.interactors.discussion_interactor import \
            InvalidUserId

        with pytest.raises(InvalidUserId):
            auth_service.get_user_profile_dtos(user_ids=user_ids)

    @patch(
        "ib_users.interfaces.service_interface.ServiceInterface.get_user_profile_bulk"
    )
    def test_with_invalid_user_id_raise_exception(
            self, get_user_profile_dtos_mock
    ):
        # Arrange
        user_ids = ["1", "2", "3"]
        from ib_users.interactors.exceptions.user_profile import \
            InvalidUserException

        from ib_users.constants.user_profile.error_messages import \
            INVALID_USER_ID
        from ib_users.constants.user_profile.error_types import \
            INVALID_USER_ID_ERROR_TYPE
        get_user_profile_dtos_mock.side_effect = InvalidUserException(
            message=INVALID_USER_ID, exception_type=INVALID_USER_ID_ERROR_TYPE
        )

        from ib_discussions.adapters.service_adapter import ServiceAdapter
        serice_adapter = ServiceAdapter()
        auth_service = serice_adapter.auth_service

        # Assert
        from ib_discussions.interactors.discussion_interactor import \
            InvalidUserId

        with pytest.raises(InvalidUserId):
            auth_service.get_user_profile_dtos(user_ids=user_ids)
