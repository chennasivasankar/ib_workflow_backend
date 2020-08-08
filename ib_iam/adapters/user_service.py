from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.exceptions.custom_exceptions import InvalidUserId


class UserAccountDoesNotExist(Exception):
    pass


class UserService:
    @property
    def interface(self):
        from ib_users.interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    def get_user_profile_bulk(
            self, user_ids: List[str]) -> List[UserProfileDTO]:
        from ib_users.interactors.exceptions.user_profile \
            import InvalidUserException
        try:
            user_profiles = self.interface.get_user_profile_bulk(
                user_ids=user_ids)
        except InvalidUserException:
            from ib_iam.exceptions.custom_exceptions import InvalidUserId
            raise InvalidUserId()
        user_profile_dtos = []
        for user in user_profiles:
            user_profile_dtos.append(UserProfileDTO(
                user_id=user.user_id,
                name=user.name,
                email=user.email
            ))
        return user_profile_dtos

    def create_user_account_with_email(self, email: str) -> str:
        from ib_iam.exceptions.custom_exceptions \
            import UserAccountAlreadyExistWithThisEmail
        from ib_users.exceptions.registration_exceptions \
            import AccountWithThisEmailAlreadyExistsException

        try:
            user_id = self.interface.create_user_account_with_email(
                email=email)
            return user_id
        except AccountWithThisEmailAlreadyExistsException:
            raise UserAccountAlreadyExistWithThisEmail

    def create_user_profile(
            self, user_id: str, user_profile_dto: UserProfileDTO):
        from ib_users.interactors.user_profile_interactor import \
            CreateUserProfileDTO
        create_user_profile_dto = CreateUserProfileDTO(
            name=user_profile_dto.name,
            email=user_profile_dto.email
        )
        self.interface.create_user_profile(
            user_id=user_id, user_profile=create_user_profile_dto)

    def update_user_profile(
            self, user_id: str, user_profile_dto: UserProfileDTO):
        from ib_users.interactors.user_profile_interactor import UserProfileDTO
        from ib_users.interactors.exceptions.user_profile import \
            InvalidEmailException
        from ib_users.interactors.exceptions.user_profile import \
            EmailAlreadyLinkedException
        from ib_users.constants.user_profile.error_types import \
            INVALID_EMAIL_ERROR_TYPE, EMAIL_ALREADY_LINKED_ERROR_TYPE
        user_profile = UserProfileDTO(
            name=user_profile_dto.name,
            email=user_profile_dto.email,
            profile_pic_url=user_profile_dto.profile_pic_url
        )
        try:
            self.interface.update_user_profile(
                user_id=user_id, user_profile=user_profile)
        except InvalidEmailException as exception:
            if exception.error_type == INVALID_EMAIL_ERROR_TYPE:
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
            user_profile_dto = self.interface.get_user_profile(
                user_id=user_id
            )
        except InvalidUserException as err:
            from ib_users.constants.user_profile.error_types import \
                EMPTY_USER_ID_ERROR_TYPE
            from ib_users.constants.user_profile.error_types import \
                INVALID_USER_ID_ERROR_TYPE
            if err.error_type == EMPTY_USER_ID_ERROR_TYPE:
                raise InvalidUserId
            elif err.error_type == INVALID_USER_ID_ERROR_TYPE:
                raise UserAccountDoesNotExist()
        else:
            user_profile_dto = self._convert_to_user_profile_dto(
                user_profile_dto=user_profile_dto
            )
            return user_profile_dto

    def deactivate_delete_user_id_in_ib_users(self, user_id: str):
        self.interface.deactivate_user(user_id=user_id)

    @staticmethod
    def _convert_to_user_profile_dto(user_profile_dto):
        converted_user_profile_dto = UserProfileDTO(
            user_id=user_profile_dto.user_id,
            name=user_profile_dto.name,
            email=user_profile_dto.email,
            profile_pic_url=user_profile_dto.profile_pic_url
        )
        return converted_user_profile_dto

    def get_basic_user_dtos(self, user_ids: List[str]):
        user_dtos_from_service = self.interface.get_user_profile_bulk(
            user_ids=user_ids
        )
        basic_user_profile_dto = [
            UserProfileDTO(
                user_id=user_dto.user_id,
                name=user_dto.name,
                profile_pic_url=self._get_user_profile_pic_url(
                    user_dto.profile_pic_url),
            )
            for user_dto in user_dtos_from_service
        ]
        return basic_user_profile_dto

    @staticmethod
    def _get_user_profile_pic_url(profile_pic_url) -> str:
        if profile_pic_url is None:
            profile_pic_url = ""
        return profile_pic_url
