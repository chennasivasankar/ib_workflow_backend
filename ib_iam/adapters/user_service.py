from typing import List

from ib_users.validators.base_validator import CustomException

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.exceptions.custom_exceptions import InvalidUserId, InvalidEmail, \
    UserAccountDoesNotExist
from ib_iam.interactors.storage_interfaces.dtos import BasicUserDetailsDTO


class UserService:
    @property
    def interface(self):
        from ib_users.interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    def get_user_profile_bulk(
            self, user_ids: List[str]
    ) -> List[UserProfileDTO]:
        from ib_users.interactors.exceptions.user_profile \
            import InvalidUserException
        from ib_iam.exceptions.custom_exceptions import InvalidUserId

        try:
            user_profiles = self.interface.get_user_profile_bulk(
                user_ids=user_ids)
        except InvalidUserException:
            raise InvalidUserId()
        user_profile_dtos = [
            UserProfileDTO(
                user_id=str(user.user_id),
                name=user.name,
                email=user.email,
                is_email_verified=user.is_email_verified
            )
            for user in user_profiles
        ]
        return user_profile_dtos

    def create_user_account_with_email(
            self, email: str, password: str = None) -> str:
        from ib_iam.exceptions.custom_exceptions import \
            UserAccountAlreadyExistWithThisEmail
        from ib_users.exceptions.registration_exceptions \
            import AccountWithThisEmailAlreadyExistsException
        from ib_users.exceptions.custom_exception_constants import \
            INVALID_EMAIL
        try:
            user_id = self.interface.create_user_account_with_email(
                email=email, password=password)
            return user_id
        except AccountWithThisEmailAlreadyExistsException:
            raise UserAccountAlreadyExistWithThisEmail
        except CustomException as err:
            if err.error_type == INVALID_EMAIL.code:
                from ib_iam.exceptions.custom_exceptions import InvalidEmail
                raise InvalidEmail

    def create_user_profile(
            self, user_id: str, user_profile_dto: UserProfileDTO):
        from ib_users.exceptions.invalid_email_exception import \
            InvalidEmailException
        from ib_users.interactors.user_profile_interactor import \
            CreateUserProfileDTO
        try:
            create_user_profile_dto = CreateUserProfileDTO(
                name=user_profile_dto.name,
                email=user_profile_dto.email
            )
            self.interface.create_user_profile(
                user_id=user_id, user_profile=create_user_profile_dto)
        except InvalidEmailException:
            raise InvalidEmail

    def update_user_profile(
            self, user_id: str, user_profile_dto: UserProfileDTO):
        from ib_users.interactors.user_profile_interactor import UserProfileDTO
        from ib_users.exceptions.invalid_email_exception import \
            InvalidEmailException
        from ib_users.constants.custom_exception_messages import INVALID_EMAIL
        from ib_users.interactors.exceptions.user_profile import \
            EmailAlreadyLinkedException
        from ib_users.constants.user_profile.error_types import \
            EMAIL_ALREADY_LINKED_ERROR_TYPE
        user_profile = UserProfileDTO(
            name=user_profile_dto.name,
            email=user_profile_dto.email,
            profile_pic_url=user_profile_dto.profile_pic_url
        )
        try:
            self.interface.update_user_profile(
                user_id=user_id, user_profile=user_profile)
        except InvalidEmailException as exception:
            if exception.error_type == INVALID_EMAIL.code:
                from ib_iam.exceptions.custom_exceptions import InvalidEmail
                raise InvalidEmail
        except EmailAlreadyLinkedException as exception:
            if exception.error_type == EMAIL_ALREADY_LINKED_ERROR_TYPE:
                from ib_iam.exceptions.custom_exceptions import \
                    UserAccountAlreadyExistWithThisEmail
                raise UserAccountAlreadyExistWithThisEmail

    def get_user_profile_dto(self, user_id: str) -> UserProfileDTO:
        from ib_users.interactors.exceptions.user_profile import \
            InvalidUserException
        try:
            user_profile_dto = self.interface.get_user_profile(user_id=user_id)
        except InvalidUserException as err:
            from ib_users.constants.user_profile.error_types import \
                EMPTY_USER_ID_ERROR_TYPE
            from ib_users.constants.user_profile.error_types import \
                INVALID_USER_ID_ERROR_TYPE
            if err.error_type == EMPTY_USER_ID_ERROR_TYPE:
                raise InvalidUserId
            elif err.error_type == INVALID_USER_ID_ERROR_TYPE:
                raise UserAccountDoesNotExist
        else:
            user_profile_dto = self._convert_to_user_profile_dto(
                user_profile_dto=user_profile_dto)
            return user_profile_dto

    def deactivate_delete_user_id_in_ib_users(self, user_id: str):
        self.interface.deactivate_user(user_id=user_id)

    @staticmethod
    def _convert_to_user_profile_dto(user_profile_dto):
        converted_user_profile_dto = UserProfileDTO(
            user_id=user_profile_dto.user_id,
            name=user_profile_dto.name,
            email=user_profile_dto.email,
            profile_pic_url=user_profile_dto.profile_pic_url,
            is_email_verified=user_profile_dto.is_email_verified
        )
        return converted_user_profile_dto

    def get_basic_user_dtos(
            self, user_ids: List[str]
    ) -> List[BasicUserDetailsDTO]:
        user_dtos_from_service = self.interface.get_user_profile_bulk(
            user_ids=user_ids)
        basic_user_profile_dto = [
            BasicUserDetailsDTO(
                user_id=user_dto.user_id,
                name=user_dto.name,
                profile_pic_url=user_dto.profile_pic_url)
            for user_dto in user_dtos_from_service
        ]
        return basic_user_profile_dto

    def get_user_id_for_given_email(self, email: str) -> str:
        try:
            return self.interface.get_user_id_give_email(email=email)
        except CustomException as err:
            from ib_users.exceptions.custom_exception_constants import \
                NOT_REGISTERED_USER
            if err.error_type == NOT_REGISTERED_USER.code:
                raise UserAccountDoesNotExist

    def is_active_user_account(self, email: str) -> bool:
        pass

    def activate_user_account(self, user_id: str):
        pass
