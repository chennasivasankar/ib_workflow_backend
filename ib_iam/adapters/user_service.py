from typing import List
from ib_iam.adapters.dtos import UserProfileDTO


class UserService:

    @property
    def user_interface(self):
        from ib_users.interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_basic_user_dtos(self, user_ids: List[str]):
        user_dtos_from_service = self.user_interface.get_user_profile_bulk(
                                    user_ids=user_ids
                                )
        user_profile_dtos = [
            UserProfileDTO(
                user_id=user_dto.user_id,
                name=user_dto.name,
                profile_pic_url=user_dto.profile_pic_url,
            )
            for user_dto in user_dtos_from_service
        ]
        return user_profile_dtos
