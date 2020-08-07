from dataclasses import dataclass
from typing import List


@dataclass
class UserProfileDTO:
    user_id: str
    name: str
    profile_pic_url: str = None


class AuthService:
    @property
    def interface(self):
        from ib_users.interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    def get_user_profile_dtos(
            self, user_ids: List[str]) -> List[UserProfileDTO]:
        from ib_users.interactors.exceptions.user_profile import \
            InvalidUserException
        try:
            user_details_dtos = self.interface.get_user_profile_bulk(
                user_ids=user_ids
            )
        except InvalidUserException as err:
            from ib_discussions.exceptions.custom_exceptions import \
                InvalidUserId
            from ib_users.constants.user_profile.error_types import \
                INVALID_USER_ID_ERROR_TYPE
            if err.error_type == INVALID_USER_ID_ERROR_TYPE:
                raise InvalidUserId
            from ib_users.constants.user_profile.error_types import \
                EMPTY_USER_ID_ERROR_TYPE
            if err.error_type == EMPTY_USER_ID_ERROR_TYPE:
                raise InvalidUserId
        else:
            converted_user_dtos = self._convert_to_required_user_profile_dtos(
                user_details_dtos=user_details_dtos
            )
            return converted_user_dtos

    def _convert_to_required_user_profile_dtos(self, user_details_dtos):
        converted_user_profile_dtos = [
            self._convert_to_required_user_profile_dto(user_details_dto)
            for user_details_dto in user_details_dtos
        ]
        return converted_user_profile_dtos

    def _convert_to_required_user_profile_dto(self, user_details_dto):
        converted_user_profile_dto = UserProfileDTO(
            user_id=user_details_dto.user_id,
            name=user_details_dto.name,
            profile_pic_url=self._get_user_profile_pic_url(
                user_details_dto.profile_pic_url)
        )
        return converted_user_profile_dto

    @staticmethod
    def _get_user_profile_pic_url(profile_pic_url: str) -> str:
        if profile_pic_url is None:
            profile_pic_url = ""
        return profile_pic_url
