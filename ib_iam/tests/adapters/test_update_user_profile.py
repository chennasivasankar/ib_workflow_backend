import pytest


class TestUpdateUserProfile:
    def update_user_profile_mock(self, mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.update_user_profile"
        )
        return mock

    def test_update_user_profile_updates_profile_of_user_in_ib_users(
            self, mocker):
        # Arrange
        name = 'parker'
        email = 'parker2020@gmail.com'
        user_id = 'e06b8a3b-94af-4d2e-ba14-bcec11140277'
        update_user_profile_with_valid_details_mock = \
            self.update_user_profile_mock(mocker=mocker)
        from ib_iam.adapters.dtos import UserProfileDTO
        profile_dto_from_interactor = UserProfileDTO(
            user_id=user_id,
            name=name,
            email=email
        )
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        from ib_users.interactors.user_profile_interactor \
            import UserProfileDTO
        user_profile = UserProfileDTO(
            name=profile_dto_from_interactor.name,
            email=profile_dto_from_interactor.email,
            profile_pic_url=profile_dto_from_interactor.profile_pic_url
        )
        # Act
        service_adapter.user_service.update_user_profile(
            user_id, profile_dto_from_interactor)

        # Assert
        update_user_profile_with_valid_details_mock.assert_called_once_with(
            user_id=user_id, user_profile=user_profile)

    def test_update_user_profile_raises_invalid_email_exception(
            self, mocker):
        # Arrange
        from ib_iam.adapters.dtos import UserProfileDTO
        update_user_profile_with_invalid_mail_mock = \
            self.update_user_profile_mock(mocker=mocker)
        name = 'parker'
        email = 'parkgmail.com'
        user_id = 'e06b8a3b-94af-4d2e-ba14-bcec11140277'
        profile_dto_from_interactor = UserProfileDTO(user_id=user_id,
                                                     name=name,
                                                     email=email)
        from ib_users.interactors.user_profile_interactor \
            import UserProfileDTO
        user_profile = UserProfileDTO(
            name=profile_dto_from_interactor.name,
            email=profile_dto_from_interactor.email,
            profile_pic_url=profile_dto_from_interactor.profile_pic_url
        )
        from ib_users.exceptions.invalid_email_exception import \
            InvalidEmailException
        from ib_users.constants.custom_exception_messages import INVALID_EMAIL
        update_user_profile_with_invalid_mail_mock.side_effect = \
            InvalidEmailException(message=INVALID_EMAIL.message,
                                  exception_type=INVALID_EMAIL.code)

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Act
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        with pytest.raises(InvalidEmail):
            service_adapter.user_service.update_user_profile(
                user_id, profile_dto_from_interactor)

        # Assert
        update_user_profile_with_invalid_mail_mock.assert_called_once_with(
            user_id=user_id, user_profile=user_profile)

    def test_update_user_profile_raises_email_already_linked_exception(
            self, mocker):
        # Arrange
        from ib_iam.adapters.dtos import UserProfileDTO
        update_user_profile_with_invalid_mail_mock = \
            self.update_user_profile_mock(mocker=mocker)
        name = 'parker'
        email = 'park@gmail.com'
        user_id = 'e06b8a3b-94af-4d2e-ba14-bcec11140277'
        profile_dto_from_interactor = UserProfileDTO(user_id=user_id,
                                                     name=name,
                                                     email=email)
        from ib_users.interactors.user_profile_interactor \
            import UserProfileDTO
        user_profile = UserProfileDTO(
            name=profile_dto_from_interactor.name,
            email=profile_dto_from_interactor.email,
            profile_pic_url=profile_dto_from_interactor.profile_pic_url
        )
        from ib_users.interactors.exceptions.user_profile import \
            EmailAlreadyLinkedException
        from ib_users.constants.user_profile.error_messages import \
            EMAIL_ALREADY_LINKED
        from ib_users.constants.user_profile.error_types import \
            EMAIL_ALREADY_LINKED_ERROR_TYPE
        update_user_profile_with_invalid_mail_mock.side_effect = \
            EmailAlreadyLinkedException(
                message=EMAIL_ALREADY_LINKED,
                exception_type=EMAIL_ALREADY_LINKED_ERROR_TYPE)

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Act
        from ib_iam.exceptions.custom_exceptions import \
            UserAccountAlreadyExistWithThisEmail
        with pytest.raises(UserAccountAlreadyExistWithThisEmail):
            service_adapter.user_service.update_user_profile(
                user_id, profile_dto_from_interactor)

        # Assert
        update_user_profile_with_invalid_mail_mock.assert_called_once_with(
            user_id=user_id, user_profile=user_profile)
