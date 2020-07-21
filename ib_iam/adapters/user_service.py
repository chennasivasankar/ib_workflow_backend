import dataclasses
from typing import List

from ib_iam.adapters.dtos import UserProfileDTO


class InvalidUserId(Exception):
    pass


class UserAccountDoesNotExist(Exception):
    pass


class UserService:
    @property
    def interface(self):
        from ib_users.interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    def get_user_profile_bulk(self, user_ids: List[int]) -> List[
        UserProfileDTO]:
        pass

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
                raise UserAccountDoesNotExist
        else:
            user_profile_dto = self._convert_to_user_profile_dto(
                user_profile_dto=user_profile_dto
            )
            return user_profile_dto

    @staticmethod
    def _convert_to_user_profile_dto(user_profile_dto):
        converted_user_profile_dto = UserProfileDTO(
            user_id=user_profile_dto.user_id,
            name=user_profile_dto.name,
            email=user_profile_dto.email,
            profile_pic_url=user_profile_dto.profile_pic_url
        )
        return converted_user_profile_dto
