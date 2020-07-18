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

    def get_user_profile_dtos(self, user_ids: List[str]):
        user_details_dtos = self.interface.get_user_profile_bulk(
            user_ids=user_ids
        )
        converted_user_dtos = self._convert_to_required_user_profile_dtos(
            user_details_dtos=user_details_dtos
        )
        return converted_user_dtos

    def _convert_to_required_user_profile_dtos(self, user_details_dtos):
        user_profile_dtos = [
            self._convert_to_required_user_profile_dto(user_details_dto)
            for user_details_dto in user_details_dtos
        ]
        return user_profile_dtos

    @staticmethod
    def _convert_to_required_user_profile_dto(user_details_dto):
        user_profile_dto = UserProfileDTO(
            user_id=user_details_dto.user_id,
            name=user_details_dto.name,
            profile_pic_url=user_details_dto.profile_pic_url
        )
        return user_profile_dto
